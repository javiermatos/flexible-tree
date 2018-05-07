
class GenericTreeKey(object):

    def __init__(self, key=''):
        self._key = key
        self._key_parts = None

    @property
    def key(self):
        return self._key

    @property
    def key_parts(self):
        if self._key_parts is None:
            self._key_parts = self.get_key_parts_from_key(self.key)
        return self._key_parts

    @staticmethod
    def get_key_parts_from_key(key):
        return list(key)

    @staticmethod
    def get_key_from_key_parts(key_parts):
        return ''.join(key_parts)

    def is_ascendent(self, tree_key):
        len_self = len(self)
        return len_self < len(tree_key) and self.key_parts == tree_key.key_parts[:len_self]

    def is_descendent(self, tree_key):
        len_tree_key = len(tree_key)
        return len_tree_key < len(self) and tree_key.key_parts == self.key_parts[:len_tree_key]

    def __str__(self):
        return self.key

    def __len__(self):
        return len(self.key_parts)

    def __eq__(self, tree_key):
        return isinstance(tree_key, self.__class__) and self.key == tree_key.key

    def __lt__(self, tree_key):
        return self.is_ascendent(tree_key)

    def __gt__(self, tree_key):
        return self.is_descendent(tree_key)
