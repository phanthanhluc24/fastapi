import pytest
import logging
from sqlalchemy import create_engine, text
from sqlalchemy_utils import database_exists, create_database
from core.config import settings  # 

databaseURI = settings.database_test_url 

# Create test database if it doesn't exist
if not database_exists(databaseURI):
    create_database(databaseURI)

engine = create_engine(databaseURI, echo=False)

@pytest.fixture(autouse=True, scope="function")
def reset_database():
    # Drop all tables and recreate them
    with engine.connect() as connection:
        # Disable foreign key checks
        connection.execute(text("SET FOREIGN_KEY_CHECKS = 0;"))

        # Get all table names
        result = connection.execute(text(
            "SELECT table_name FROM information_schema.tables WHERE table_schema = DATABASE();"
        ))
        tables = result.fetchall()

        # Drop all tables
        for table in tables:
            connection.execute(text(f"DROP TABLE IF EXISTS `{table[0]}`;"))

        # Re-enable foreign key checks
        connection.execute(text("SET FOREIGN_KEY_CHECKS = 1;"))

        # Commit the changes
        connection.commit()

@pytest.fixture(autouse=True)
def suppress_sqlalchemy_logs():
    """Suppress SQLAlchemy logs by setting the log level to ERROR or higher."""
    logging.getLogger("sqlalchemy.engine").setLevel(logging.ERROR)
    logging.getLogger("sqlalchemy.pool").setLevel(logging.ERROR)
    logging.getLogger("sqlalchemy.dialects").setLevel(logging.ERROR)
