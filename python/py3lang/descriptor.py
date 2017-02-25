import unittest


class DataDescriptor(object):
    """A data descriptor that sets and returns values
       normally and prints a message logging their access.
    """

    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print('Retrieving', self.name)
        return self.val

    def __set__(self, obj, val):
        print('Updating', self.name)
        self.val = val


class NonDataDescriptor(object):
    """A data descriptor that sets and returns values
       normally and prints a message logging their access.
    """

    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print('Retrieving', self.name)
        return self.val


class MyClass:
    d = DataDescriptor(10, 'data descriptor')
    n = NonDataDescriptor([1, 2], 'non-data descriptor')


class DescriptorTest(unittest.TestCase):
    def setUp(self):
        self.instance = MyClass()
        self.instance.__dict__['d'] = 'd in instance dictionary'
        self.instance.__dict__['n'] = 'n in instance dictionary'

    def test_descriptor(self):
        self.assertEqual(self.instance.d, 10)
        self.assertEqual(self.instance.n, 'n in instance dictionary')
        self.assertEqual(type(self.instance).n, [1, 2])


if __name__ == '__main__':
    unittest.main()