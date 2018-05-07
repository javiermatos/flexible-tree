
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
        return self.key == tree_key.key

    def __lt__(self, tree_key):
        return self.is_ascendent(tree_key)

    def __gt__(self, tree_key):
        return self.is_descendent(tree_key)


class GenericTreeError(Exception):
    pass


class GenericTree(object):

    def __init__(self, key, value=None):
        if not isinstance(key, GenericTreeKey):
            raise ValueError('First argument key must be a {}'.format(str(GenericTreeKey)))
        self.key = key
        self.value = value
        self.children = {}

    def add(self, key, value):
        if self.key == key:
            self.value = value
        elif self.key.is_ascendent(key):
            n = len(self.key)
            symbol = key.key_parts[n]
            if symbol not in self.children:
                klass = key.__class__
                generic_tree = GenericTree(klass(klass.get_key_from_key_parts(key.key_parts[:n+1])))
                self.children[symbol] = generic_tree
            self.children[symbol].add(key, value)
        else:
            raise GenericTreeError('Non valid key {} for generic tree with key {}'.format(key, self.key))

    def get(self, key, value=None):
        if self.key == key:
            return self.value
        elif self.key.is_ascendent(key):
            n = len(self.key)
            symbol = key.key_parts[n]
            if symbol in self.children:
                return self.children[symbol].get(key, value)
        return value

    def __contains__(self, key):
        if self.key == key:
            return self.value is not None
        elif self.key.is_ascendent(key):
            n = len(self.key)
            symbol = key.key_parts[n]
            return False if symbol not in self.children else (key in self.children[symbol])
        return False

    def count(self):
        return (1 if self.value is not None else 0) + sum([child.count() for child in self.children.values()])

    def count_all(self):
        return 1 + sum([child.count_all() for child in self.children.values()])

    def depth(self, depth=0):
        return depth if not self.children else max(map(lambda child: child.depth(depth+1), self.children.values()))

    def __len__(self):
        return self.count()

    def __eq__(self, generic_tree):
        return self.key == generic_tree.key

    def __lt__(self, generic_tree):
        return self.key < generic_tree.key

    def __gt__(self, generic_tree):
        return self.key > generic_tree.key

    def __iter__(self):
        yield self
        for symbol, child in self.children.items():
            yield from child

    def iter_from_key(self, key):
        if self.key.is_ascendent(key):
            n = len(self.key)
            symbol = key.key_parts[n]
            if symbol in self.children:
                yield from self.children[symbol].iter_from_key(key)
        elif self.key == key:
            yield from self

    def iter_until_key(self, key):
        if self.key.is_ascendent(key):
            yield self
            n = len(self.key)
            symbol = key.key_parts[n]
            if symbol in self.children:
                yield from self.children[symbol].iter_until_key(key)
        elif self.key == key:
            yield self

    def __str__(self):
        return self.key

    def print(self, padding=None):
        if self.value is not None:
            print('{}{} {}'.format('' if padding is None else ' ' * padding, self.key, self.value))
        for symbol in sorted(self.children.keys()):
            self.children[symbol].to_stdout(None if padding is None else padding + 1)
