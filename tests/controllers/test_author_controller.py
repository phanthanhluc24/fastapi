from tests.base import BaseTestCase
from schemas.req.AuthorRequest import AuthorRequest
from tests.dummys.author_dummy import create_author
from tests.dummys.book_dummy import create_book


class TestAuthorController(BaseTestCase):
    def test_create_author_success(self):
        data_dict = AuthorRequest(name="John Doe", birth_year=1990).model_dump()

        response = self.client.post(
            "api/authors",
            json=data_dict
        )
        assert response.status_code == 201
        response_data = response.json()
        assert response_data["created"] is True
        assert response_data["data"] == "Create author successfully"
        assert response_data["error"] is None

    def test_create_author_fail(self):
        data_dict = AuthorRequest(name="John Doe", birth_date=2019).model_dump()

        response = self.client.post(
            "api/authors",
            json=data_dict
        )
        assert response.status_code == 422 
        response_data = response.json()
        assert response_data["data"] is None

    def test_get_all_authors_success(self):
        create_author(self.db)
        response = self.client.get(
            "api/authors"
        )
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["data"] is not None
        assert response_data["error"] is None   

    def test_get_author_by_id_success(self):
        create_author(self.db)
        response = self.client.get(
            "api/authors/3"
        )   
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["data"] is not None
        assert response_data["error"] is None

    def test_get_author_by_id_fail(self):
        response = self.client.get(
            "api/authors/1"
        )
        assert response.status_code == 404
        response_data = response.json()
        assert response_data["data"] is None    

    def test_update_author_success(self):
        create_author(self.db)
        data_dict = AuthorRequest(name="John Doe", birth_year=1930).model_dump()

        response = self.client.put(
            "api/authors/3",
            json=data_dict
        )
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["data"] is not None
        assert response_data["error"] is None   

    def test_update_author_fail(self):
        create_author(self.db)
        data_dict = AuthorRequest(name="John Doe", birth_year=1930).model_dump()

        response = self.client.put(
            "api/authors/1",
            json=data_dict
        )
        assert response.status_code == 404
        response_data = response.json()
        assert response_data["data"] is None

    # def test_delete_author_success(self):   
    #     create_author(self.db)
    #     response = self.client.delete(
    #         "api/authors/7"
    #     )
    #     assert response.status_code == 200
    #     response_data = response.json()
    #     assert response_data["data"] is not None
    #     assert response_data["error"] is None

    def test_delete_author_fail(self):
        response = self.client.delete(
            "api/authors/1"
        )   
        assert response.status_code == 404
        response_data = response.json()
        assert response_data["data"] is None
