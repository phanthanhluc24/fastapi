from tests.dummys.author_dummy import create_author
from schemas.req.BookRequest import BookRequest
from tests.base import BaseTestCase
from tests.dummys.book_dummy import create_book


class TestBookController(BaseTestCase):
    def test_create_author_success(self):
        create_author(self.db)
        data_dict = BookRequest(title="Anh yêu em 9", author_id=8, published_year=2024).model_dump()

        response = self.client.post(
            "api/books",
            json=data_dict
        )
        print("AAAAA",response.json())
        assert response.status_code == 201
        response_data = response.json()
        assert response_data["created"] is True
        assert response_data["data"] == "Add new book successfully"
        assert response_data["error"] is None

    def test_create_author_fail(self):
        create_author(self.db)
        data_dict = BookRequest(title="Anh yêu em 9", author_id=2, published_year=2024).model_dump()

        response = self.client.post(
            "api/books",
            json=data_dict
        )
        assert response.status_code == 404
        response_data = response.json()
        assert response_data["data"] is None

    def test_get_all_books_success(self):
        create_author(self.db)
        create_book(self.db)
        response = self.client.get(
            "api/books"
        )
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["data"] is not None
        assert response_data["error"] is None


    def test_get_book_by_id_success(self):
        create_author(self.db)
        create_book(self.db)
        response = self.client.get(
            "api/books/3"
        )
        assert response.status_code == 200  
        response_data = response.json()
        assert response_data["data"] is not None
        assert response_data["error"] is None

    def test_get_book_by_id_fail(self):
        response = self.client.get(
            "api/books/1"
        )
        assert response.status_code == 404
        response_data = response.json()
        assert response_data["data"] is None

    def test_update_book_success(self): 
        create_author(self.db)
        create_book(self.db)
        data_dict = BookRequest(title="Anh yêu em 9", author_id=8, published_year=2024).model_dump()

        response = self.client.put(
            "api/books/4",
            json=data_dict
        )
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["data"] is not None
        assert response_data["error"] is None   

    def test_update_book_fail(self):
        create_author(self.db)
        create_book(self.db)
        data_dict = BookRequest(title="Anh yêu em 9", author_id=8, published_year=2024).model_dump()

        response = self.client.put(
            "api/books/1",
            json=data_dict
        )
        assert response.status_code == 404
        response_data = response.json()
        assert response_data["data"] is None

    # def test_delete_book_success(self):
    #     create_author(self.db)
    #     create_book(self.db)
    #     response = self.client.delete(
    #         "api/books/7"
    #     )
    #     assert response.status_code == 200
    #     response_data = response.json()
    #     assert response_data["data"] is not None
    #     assert response_data["error"] is None           

    def test_delete_book_fail(self):
        response = self.client.delete(
            "api/books/5"
        )   
        assert response.status_code == 404
        response_data = response.json()
        assert response_data["data"] is None 

    def test_get_book_by_author_id_success(self):
        create_author(self.db)
        create_book(self.db)
        response = self.client.get(
            "api/books/6"
        )
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["data"] is not None
        assert response_data["error"] is None

    def test_get_book_by_author_id_fail(self):
        response = self.client.get(
            "api/books/1"
        )
        assert response.status_code == 404
        response_data = response.json()


    def test_get_book_and_author_success(self):
        create_author(self.db)
        create_book(self.db)
        response = self.client.get(
            "api/books"
        )
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["data"] is not None
        assert response_data["error"] is None
