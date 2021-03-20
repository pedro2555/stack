class DictRepo():
    def __init__(self):
        self._stacks = dict()

    def save(self, s):
        self._stacks[str(s.id)] = s

    def get_by_id(self, stack_id):
        return self._stacks[stack_id]

class MongoRepo():
    @classmethod
    def create_stack(cls, mongo_uri, cache_dao, google_dao):
        import .mapper import Mapper
        return cls(mongo_uri, Mapper(), 'stacks')

    @classmethod
    def create_outra_coisa(cls, mongo_uri):
        import .mapper import Mapper
        return cls(mongo_uri, Mapper(), 'outra_coisa')

    def __init__(self, conn_string, mapper, collection):
        self._m = mapper
        self._c = collection

    def save(self, s):
        json = self._m.to_json(s)
        mongo.insert(self._c, json)

    def get_by_id(self, stack_id):
        json = mongo.get({'id': stack_id})
        return self._m.to_entity(json)
