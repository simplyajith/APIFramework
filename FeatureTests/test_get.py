import allure

from core.logdecorator import log_request
from core.logger import get_logger
from validators.response_validator import ResponseValidator

logger = get_logger("TestGetAPI")

@allure.title("Verify GET API")
@allure.description("Validate status code for GET request")
def test_get(api_client):
    logger.info("Getting a user")
    response = api_client.get("get")
    ResponseValidator.validate_status_code(response,200)
