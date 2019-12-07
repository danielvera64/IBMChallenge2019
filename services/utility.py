
from flask import jsonify
from werkzeug.exceptions import BadRequest


class Utility:

    @staticmethod
    def get_array_from(tag, request):
        if not request.is_json:
            raise BadRequest('Required json data')

        try:
            json_data = request.get_json(force=True)
        except BadRequest as e:
            raise e

        if tag not in json_data:
            raise BadRequest('Missing array field called: ' + tag)

        elements = json_data['elements']

        if elements is None or not isinstance(elements, list):
            raise BadRequest('Invalid elements field, elements must be an array')

        return list(filter(lambda x: x or x == 0, elements))

    @staticmethod
    def bad_request(reason):
        error_response = jsonify({"status": "error", "message": reason})
        error_response.status_code = 400
        return error_response

    @staticmethod
    def is_numeric(x):
        try:
            if isinstance(x, str):
                return False
            float(x)
            return True
        except ValueError:
            return False
