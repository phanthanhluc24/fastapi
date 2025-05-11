from typing import Annotated
from pydantic import BaseModel, constr, AfterValidator
from validates.main import validate_year

class AuthorRequest(BaseModel):
    name: Annotated[str, constr(max_length=50)]
    birth_year: Annotated[int, AfterValidator(validate_year)]
