from models.user import UserModel
from repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):
    model = UserModel
    
    def get_by_email(self, email: str):  
        return self.db.query(self.model).filter(self.model.email == email).first()
    