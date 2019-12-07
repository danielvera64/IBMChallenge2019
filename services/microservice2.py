
from flask import request, jsonify
from flask_restful import Resource
from werkzeug.exceptions import BadRequest
from services.utility import Utility
import pandas as pd


class Microservice2(Resource):

    def __init__(self, **kwargs):
        self.add_discarded = kwargs['add_discarded']

    def post(self):
        try:
            elements = Utility.get_array_from('elements', request)
        except BadRequest as e:
            return Utility.bad_request(e.description)

        number_elements = list(filter(Utility.is_numeric, elements))

        discarded_elements = list(set(elements) - set(number_elements))
        discarded_elements.sort()

        size = len(number_elements)
        sr = pd.Series(number_elements)
        mode = sr.mode()
        result_mode = 0
        if len(mode) > 0:
            result_mode = float(mode[0].astype('float'))

        data_dict = {
            "count": size,
            "average": sr.mean(),
            "median": sr.median(),
            "mode": result_mode,
            "max": float(sr.max().astype('float')),
            "min": float(sr.min().astype('float')),
            "stdev": float(sr.std().astype('float'))
        }
        if self.add_discarded:
            data_dict['discardedElements'] = discarded_elements

        return jsonify({
            "status": "success",
            "message": "ok",
            "data": data_dict
        })
