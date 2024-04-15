from pydantic import ValidationError
import json


class Validate:

    @staticmethod
    def get_model_response(model, response):
        try:
            response_model = model.model_validate({
                **response.json(),
                "status_code": response.status_code
            })
        except ValidationError as e:
            response_model = model(success=False,
                                   message=f'Validation Error: {str(e)}',
                                   status_code=response.status_code)
        except json.JSONDecodeError:
            response_model = model(success=False,
                                   message=f'Not a valid JSON: {response.text}',
                                   status_code=response.status_code)

        return response_model
