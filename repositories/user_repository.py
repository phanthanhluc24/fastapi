from models.user import UserModel
from repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):
    model = UserModel
    