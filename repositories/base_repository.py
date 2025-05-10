from sqlalchemy.orm import Session
from typing import Any, Generic, Type, Union, Sequence, List
from db.session import ModelType
from exceptions.app_exception import NotFoundException


class BaseRepository(Generic[ModelType]):
    model: Type[ModelType]

    def __init__(self, db: Session):
        if self.model is None:
            raise ValueError("Must define model name")
        self.db = db
    
    def create(self, obj_data: dict) -> ModelType:
        obj = self.model(**obj_data)
        self.db.add(obj)
        self.db.flush() 
        self.db.commit()

        return obj

    def create_all(self, obj_data_list: list[dict]) -> list[ModelType]:
        obj = [self.model(**obj_data) for obj_data in obj_data_list]
        self.db.add_all(obj)
        self.db.flush()
        self.db.commit()

        return obj
    
    def get_by_id(self, id: int):
        query = self.db.query(self.model).filter(self.model.id == id)

        # Chỉ filter nếu model có trường is_deleted
        if hasattr(self.model, "is_deleted"):
            query = query.filter(self.model.is_deleted == False)

        instance = query.first()

        if not instance:
            raise NotFoundException(f"{self.model.__name__} with ID {id} not found or deleted")

        return instance



    def get_all(self):
        return self.db.query(self.model).filter_by(is_deleted=False).all()
    
    def update_by_id(self, id_: int, update_data: dict):
        instance = self.get_by_id(id_)  
        for key, value in update_data.items():
            setattr(instance, key, value)
        self.db.flush()
        self.db.commit()

        return instance

    def delete_by_id(self, id_: int):
        instance = self.get_by_id(id_) 
        self.db.delete(instance)
        self.db.flush()
        self.db.commit()

        return True

    def delete_by_columns(self, **conditions):
        count = self.db.query(self.model).filter_by(**conditions).delete()
        self.db.flush()
        self.db.commit()

        return count
