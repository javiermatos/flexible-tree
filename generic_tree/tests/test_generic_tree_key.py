import unittest

from .. import GenericTreeKey


class TestGenericTreeKey(unittest.TestCase):

    def test_create_instance(self):
        GenericTreeKey('')

    def test_key(self):
        key = '1'
        k = GenericTreeKey(key)
        self.assertEqual(k.key, key)

    def test_key_parts(self):
        key = '123'
        key_parts = ['1', '2', '3']
        k = GenericTreeKey(key)
        self.assertEqual(k.key_parts, key_parts)

    def test_get_key_parts_from_key(self):
        self.assertEqual(GenericTreeKey.get_key_parts_from_key(''), [])
        self.assertEqual(GenericTreeKey.get_key_parts_from_key('123'), ['1', '2', '3'])

    def test_get_key_from_key_parts(self):
        self.assertEqual(GenericTreeKey.get_key_from_key_parts([]), '')
        self.assertEqual(GenericTreeKey.get_key_from_key_parts(['1', '2', '3']), '123')

    def test_is_ascendent(self):
        k0 = GenericTreeKey('')
        k1 = GenericTreeKey('1')
        k2 = GenericTreeKey('123')

        self.assertFalse(k0.is_ascendent(k0))
        self.assertTrue(k0.is_ascendent(k1))
        self.assertTrue(k0.is_ascendent(k2))

        self.assertFalse(k1.is_ascendent(k0))
        self.assertFalse(k1.is_ascendent(k1))
        self.assertTrue(k1.is_ascendent(k2))

        self.assertFalse(k2.is_ascendent(k0))
        self.assertFalse(k2.is_ascendent(k1))
        self.assertFalse(k2.is_ascendent(k2))

    def test_is_ascendent__lt__(self):
        k0 = GenericTreeKey('')
        k1 = GenericTreeKey('1')

        self.assertFalse(k0 < k0)
        self.assertTrue(k0 < k1)

        self.assertFalse(k1 < k0)
        self.assertFalse(k1 < k1)

    def test_is_descendent(self):
        k0 = GenericTreeKey('')
        k1 = GenericTreeKey('1')
        k2 = GenericTreeKey('123')

        self.assertFalse(k0.is_descendent(k0))
        self.assertFalse(k0.is_descendent(k1))
        self.assertFalse(k0.is_descendent(k2))

        self.assertTrue(k1.is_descendent(k0))
        self.assertFalse(k1.is_descendent(k1))
        self.assertFalse(k1.is_descendent(k2))

        self.assertTrue(k2.is_descendent(k0))
        self.assertTrue(k2.is_descendent(k1))
        self.assertFalse(k2.is_descendent(k2))

    def test_is_descendent__gt__(self):
        k0 = GenericTreeKey('')
        k1 = GenericTreeKey('1')

        self.assertFalse(k0 > k0)
        self.assertFalse(k0 > k1)

        self.assertTrue(k1 > k0)
        self.assertFalse(k1 > k1)
