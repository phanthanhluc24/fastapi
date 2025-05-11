from typing import Annotated
from pydantic import BaseModel, constr, AfterValidator

from validates.main import validate_year


class BookRequest(BaseModel):
    title: Annotated[str, constr(max_length=150)]
    author_id: int
    published_year: Annotated[int, AfterValidator(validate_year)]
