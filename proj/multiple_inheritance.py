class A(object):
    def f1(self):
        print "From A"

class B(A):
    def f1(self):
        print "From B"

class C(A):
    def f1(self):
        print "From C"

class D(C,B):
    pass

# Linearization of Multi derived classes
objd = D()
objd.f1()
#method resolution order
print D.__mro__
