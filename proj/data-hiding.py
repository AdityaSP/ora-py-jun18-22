class Shape(object):
    def __init__(self):
        self.__name = 'Square'
    def get_name(self):
        print "In getter"
        return self.__name
    def set_name(self, value):
        print "In the setter"
        raise NameError('Cannot change the value')
    name = property(fget = get_name, fset = set_name)

sh = Shape()
# print sh.get_name()
# sh.set_name('Circle')
# print sh.get_name()
# print dir(sh)
print sh.name
sh.name = 'Circle'