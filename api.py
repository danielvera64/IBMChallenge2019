
from flask import Flask
from flask_restful import Api
from os import environ

from services.microservice1 import Microservice1
from services.microservice2 import Microservice2

app = Flask(__name__)
api = Api(app)

api.add_resource(Microservice1,
                 '/ibmchallengemic1/element_sorter1_0',
                 endpoint='element_sorter1_0',
                 resource_class_kwargs={'split_results': False})

api.add_resource(Microservice1,
                 '/ibmchallengemic1/element_sorter1_1',
                 endpoint='element_sorter1_1',
                 resource_class_kwargs={'split_results': True})

api.add_resource(Microservice2,
                 '/ibmchallengemic2/statistics1_0',
                 endpoint='statistics1_0',
                 resource_class_kwargs={'add_discarded': False})

api.add_resource(Microservice2,
                 '/ibmchallengemic2/statistics1_1',
                 endpoint='statistics1_1',
                 resource_class_kwargs={'add_discarded': True})

if __name__ == '__main__':
    if environ.get('SERVER_NAME') is not None:
        app.config['SERVER_NAME'] = environ.get('SERVER_NAME')
    app.config['SERVER_NAME'] = '0.0.0.0:5000'
    app.run(debug=True)
