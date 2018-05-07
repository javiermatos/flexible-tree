
# GenericTree

This is a simple implementation of a generic tree similar to a Python dictionary but extended with some extra features
to work with special cases like phone numbers and SNMP MIBs.


## Usage

```
from generic_tree import GenericTree
from generic_tree import GenericTreeKey

root = GenericTree(key=GenericTreeKey(''))
root.add(GenericTreeKey('0034'), value='Spain')
root.add(GenericTreeKey('0033'), value='France')

contry, closest_key = root.get_closest(GenericTreeKey('0034951'))
```
