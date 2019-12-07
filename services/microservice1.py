
from flask import request, jsonify
from flask_restful import Resource
from werkzeug.exceptions import BadRequest
from services.utility import Utility


class Microservice1(Resource):

    def __init__(self, **kwargs):
        self.split_results = kwargs['split_results']

    def post(self):
        try:
            elements = Utility.get_array_from('elements', request)
        except BadRequest as e:
            return Utility.bad_request(e.description)

        if not self.split_results:
            elements_shorted = list(map(str, elements))
            elements_shorted.sort()
            data_response = {"sorted": elements_shorted}
        else:
            number_elements = list(filter(Utility.is_numeric, elements))
            other_elements = list(set(elements) - set(number_elements))
            number_elements.sort()
            other_elements.sort()
            data_response = {
                "numbers": number_elements,
                "others": other_elements
            }

        return jsonify({
            "status": "success",
            "message": "ok",
            "data": data_response
        })
