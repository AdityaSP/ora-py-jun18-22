import unittest
import core.bank as cb
import sys
import HtmlTestRunner

class TestBank(unittest.TestCase):
    def test_sa_default(self):
        sa = cb.SA('Aditya')
        assert sa.b == 1000, 'US102'
    def test_ca_default(self):
        sa = cb.CA('A')
        assert sa.b == 0, 'US102'
    def test_sa_credit(self):
        sa = cb.SA('A')
        sa.credit(100)
        assert sa.b == 1100, 'US103'
    def test_ca_credit(self):
        sa = cb.CA('A')
        sa.credit(100)
        assert sa.b == 100, 'US103'

#unittest.main(verbosity = 3)
ts = unittest.TestSuite()

# if sys.argv[1] == 'SA':
#     ts.addTest(TestBank('test_sa_default'))
#     ts.addTest(TestBank('test_sa_credit'))
# elif sys.argv[1] == 'CA':
#     ts.addTest(TestBank('test_ca_default'))
#     ts.addTest(TestBank('test_ca_credit'))
# else:
#     print "I do not know this", sys.argv[1]

with open(sys.argv[1]) as fh:
    for line in fh:
        tc, flag = line.split(',')
        if flag.strip() == 'y':
            ts.addTest(eval(tc))

#r = unittest.TextTestRunner(verbosity=3)
r = HtmlTestRunner.HTMLTestRunner(output='reports')
r.run(ts)
