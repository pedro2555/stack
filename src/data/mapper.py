class ToJson:
    def to_json(self, entity):
        pass

class ToEntity:
    def to_entity(self, json):
        pass

class Mapper1(ToJson, ToEntity):
    def to_json(self, entity):
        pass

    def to_entity(self, json):
        pass

class Mapper2:
    def to_json(self, entity):
        pass

    def to_entity(self, json):
        pass
