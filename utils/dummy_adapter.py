from random import randint
class DummyAdapter(object):

    def __init__(self, *args):
        pass

    def read_int(self):
        return randint(0, 100)