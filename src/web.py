from uuid import uuid4
from flask import Flask
from flask_restful import Resource, Api
from os import environ

from .domain import Stack
from .data import DictRepo, MongoRepo
from .data.mapper import Mapper

app = Flask(__name__)
api = Api(app)

# repo = DictRepo()
mapper = Mapper()
uri = environ.get('MONGO_DB', 'mongodb://admin:jsdofdf@10.154.54.23:27017/db')
stack_repo = MongoRepo.create_stack(uri)
outra_coisa_qql_repo = MongoRepo.create_outra_coisa(uri)

class UUIDResource(Resource):
    def get(self):
        return {'str': str(uuid4())}

class StackResource(Resource):
    def post(self, auth_token):
        s = {'_id': uuid4()}
        repo.save(s)
        return {
                 '_id': str(s.id),
            'is_empty': s.is_empty(),
        }

class ItemPushResource(Resource):
    def post(self, stack_id, item):
        item = item
        s = repo.get_by_id(stack_id)
        s.push(item)
        repo.save(s)
        return {'_id': str(item)}

class ItemPopResource(Resource):
    def post(self, stack_id):
        s = repo.get_by_id(stack_id)
        if s.is_empty():
            return 'stack is empty', 403
        item = s.pop()
        repo.save(s)
        return {'_id': str(item)}

api.add_resource(UUIDResource, '/uuid')
api.add_resource(StackResource, '/stack')
api.add_resource(ItemPushResource, '/stack/<stack_id>/push/<item>')
api.add_resource(ItemPopResource, '/stack/<stack_id>/pop')
