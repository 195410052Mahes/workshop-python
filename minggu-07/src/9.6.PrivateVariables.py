class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # salinan pribadi dari metode pembaruan () asli

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # memberikan tanda tangan baru untuk pembaruan ()
        # tetapi tidak merusak __init__()
        for item in zip(keys, values):
            self.items_list.append(item)