import allure
import json
from core.logger import get_logger

logger = get_logger("API_TRACE")

def log_request(func):
    def wrapper(self, method, endpoint, **kwargs):
        # Log the outgoing request
        payload = json.dumps(kwargs.get('json', {}), indent=2)
        message = f"Request: {method} {endpoint} | Payload: {payload}"
        logger.info(message)

        with allure.step(f"API {method} {endpoint}"):
            allure.attach(payload, "Request Body", allure.attachment_type.JSON)
            response = func(self, method, endpoint, **kwargs)

            # Attach response to Allure
            try:
                res_body = json.dumps(response.json(), indent=2)
                allure.attach(res_body, "Response Body", allure.attachment_type.JSON)
                logger.info(f"Response Status: {response.status_code}")
            except:
                allure.attach(response.text, "Response Text", allure.attachment_type.TEXT)

            return response

    return wrapper
