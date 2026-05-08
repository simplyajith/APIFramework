
class ResponseValidator:

    @staticmethod
    def validate_status_code(response,expected_status_code):
        assert response.status_code == expected_status_code
