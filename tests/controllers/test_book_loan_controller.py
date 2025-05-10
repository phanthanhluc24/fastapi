from tests.dummys.author_dummy  import create_author
from dto.req.BookLoanRequest import BookLoanRequest
from tests.base import BaseTestCase
from tests.dummys.book_dummy import create_book


class TestBookLoanController(BaseTestCase):
    def test_create_book_loan_success(self):
        create_book(self.db)
        create_author(self.db)
        data_dict = BookLoanRequest(book_id=4, author_id=3, loan_date="2024-01-01").model_dump()
        response = self.client.post(
            "api/book-loans",
            json=data_dict
        )
        assert response.status_code == 201
        response_data = response.json()
        assert response_data["data"] is not None
        assert response_data["error"] is None

    def test_create_book_loan_fail(self):   
        create_book(self.db)
        create_author(self.db)
        data_dict = BookLoanRequest(book_id=1, author_id=1, loan_date="2024-01-01").model_dump()
        response = self.client.post(
            "api/book-loans",
            json=data_dict
        )
        assert response.status_code == 404
        response_data = response.json()

    def test_get_book_loan_by_id_success(self):
        create_book(self.db)
        create_author(self.db)
        data_dict = BookLoanRequest(book_id=4, author_id=3, loan_date="2024-02-01").model_dump()
        response = self.client.post(
            "api/book-loans",
            json=data_dict
        )   
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["data"] is not None
        assert response_data["error"] is None

    def test_get_book_loan_by_id_fail(self):
        response = self.client.get(
            "api/book-loans/1"
        )
        assert response.status_code == 404
        response_data = response.json()
        assert response_data["data"] is None
    
    def test_get_all_book_loans_success(self):
        create_book(self.db)
        create_author(self.db)
        response = self.client.post(
            "api/book-loans"        
            )   
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["data"] is not None
        assert response_data["error"] is None

    def test_get_all_book_loans_fail(self):
        response = self.client.get(
            "api/book-loans"
        )
        assert response.status_code == 404
        response_data = response.json()

    def test_get_book_loan_by_book_id_success(self):
        create_book(self.db)
        create_author(self.db)
        response = self.client.post(
            "api/book-loans",
        )   
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["data"] is not None
        assert response_data["error"] is None

    def test_get_book_loan_by_book_id_fail(self):
        response = self.client.get(
            "api/book-loans/1"
        )
        assert response.status_code == 404
        response_data = response.json()
        assert response_data["data"] is None    

    def test_get_book_loan_by_author_id_success(self):
        create_book(self.db)
        create_author(self.db)
        response = self.client.post(
            "api/book-loans",
        )   
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["data"] is not None
        assert response_data["error"] is None

    def test_get_book_loan_by_author_id_fail(self):
        response = self.client.get(
            "api/book-loans/1"
        )
        assert response.status_code == 404

    
    
