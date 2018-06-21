import core.bank as cb
# ac1 = core.bank.Account('Aditya')
#
# print type(ac1)
# print ac1.n, ac1.b, ac1.t
#
# ac1.credit(1000000)
# print ac1.n, ac1.b, ac1.t
#
# ac1.debit(200)
# print ac1.n, ac1.b, ac1.t
#
# #Accessing documentation
# print core.bank.__doc__
# print core.bank.Account.__doc__
# print ac1.__doc__
# print ac1.credit.__doc__

acc_sa = cb.SA('Aditya')
print acc_sa.n, acc_sa.b, acc_sa.t
try:
    acc_sa.debit(2000)
except cb.InsufficientBlanceError as err:
    print "Please check your balance and try again!"
except Exception as err:
    print "Wasnt expecting this!: ", err

#ac = core.bank.Account('A', 100,'S')