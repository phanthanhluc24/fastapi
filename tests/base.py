import uuid
from fastapi.testclient import TestClient
from db.session import Base
from tests.conftest import engine
from main import app
from middlewares import db_middleware
from sqlalchemy.orm import Session, scoped_session, sessionmaker, close_all_sessions

class BaseTestCase:
    client: TestClient
    db: Session

    def setup_method(self, method) -> None:
        # Create all tables
        Base.metadata.create_all(engine)
        
        # Create a new session for this test
        session_factory = sessionmaker(bind=engine)
        self.db = scoped_session(session_factory)
        
        # Set the session in middleware
        db_middleware.get_db_session = lambda: self.db
        
        # Create test client
        self.client = TestClient(app)

    def teardown_method(self, method) -> None:
        # Close the session
        self.db.remove()
        close_all_sessions()
        
        # Drop all tables
        Base.metadata.drop_all(engine)
