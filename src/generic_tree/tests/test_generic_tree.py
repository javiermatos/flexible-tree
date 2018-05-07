import unittest

from .. import GenericTree
from .. import GenericTreeError
from .. import GenericTreeKey


class TestGenericTree(unittest.TestCase):

    def setUp(self):
        self.gt = GenericTree(GenericTreeKey(''))

    def test_add_get(self):
        k1 = GenericTreeKey('1')
        v1 = 1
        k12 = GenericTreeKey('12')
        v12 = 12
        k2 = GenericTreeKey('2')
        v2 = 2

        self.gt.add(k1, v1)
        self.gt.add(k12, v12)
        self.gt.add(k2, v2)

        self.assertEqual(self.gt.get(k1), v1)
        self.assertEqual(self.gt.get(k12), v12)
        self.assertEqual(self.gt.get(k2), v2)

    def test_add_get_error(self):
        k1 = GenericTreeKey('1')
        v1 = 1
        k2 = GenericTreeKey('2')
        v2 = 2

        generic_tree = GenericTree(k1, v1)
        with self.assertRaises(GenericTreeError):
            generic_tree.add(k2, v2)

    def test_add_count_count_all_depth(self):
        k1 = GenericTreeKey('1')
        v1 = 1
        k123 = GenericTreeKey('123')
        v123 = 123

        self.gt.add(k1, v1)
        self.gt.add(k123, v123)

        self.assertEqual(self.gt.count(), 2)
        self.assertEqual(self.gt.count_all(), 4)
        self.assertEqual(len(self.gt), 2)
        self.assertEqual(self.gt.depth(), 3)

    def test_contains(self):
        k1 = GenericTreeKey('1')
        k123 = GenericTreeKey('123')
        v123 = 123

        self.assertFalse(k123 in self.gt)

        self.gt.add(k123, v123)

        self.assertTrue(k123 in self.gt)
        self.assertFalse(k1 in self.gt)

    def test_iter_from_key(self):
        k1 = GenericTreeKey('1')
        v1 = 1
        k123 = GenericTreeKey('123')
        v123 = 123
        k2 = GenericTreeKey('2')
        v2 = 2

        self.gt.add(k1, v1)
        self.gt.add(k123, v123)
        self.gt.add(k2, v2)

        self.assertEqual(
            [
                (generic_tree.key, generic_tree.value)
                for generic_tree in self.gt.iter_from_key(k1)
                if generic_tree.value is not None
            ],
            [
                (k1, v1),
                (k123, v123),
            ],
        )

        self.assertEqual(
            [
                (generic_tree.key, generic_tree.value)
                for generic_tree in self.gt.iter_from_key(k2)
                if generic_tree.value is not None
            ],
            [
                (k2, v2),
            ],
        )

    def test_iter_until_key(self):
        k1 = GenericTreeKey('1')
        v1 = 1
        k123 = GenericTreeKey('123')
        v123 = 123
        k2 = GenericTreeKey('2')
        v2 = 2

        self.gt.add(k1, v1)
        self.gt.add(k123, v123)
        self.gt.add(k2, v2)

        self.assertEqual(
            [
                (generic_tree.key, generic_tree.value)
                for generic_tree in self.gt.iter_until_key(k123)
                if generic_tree.value is not None
            ],
            [
                (k1, v1),
                (k123, v123),
            ],
        )

        self.assertEqual(
            [
                (generic_tree.key, generic_tree.value)
                for generic_tree in self.gt.iter_from_key(k2)
                if generic_tree.value is not None
            ],
            [
                (k2, v2),
            ],
        )
