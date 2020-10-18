import unittest


from login_files.login_invalid import TestAutomationPracticeLoginInvalid
from login_files.login_new_user import TestAutomationPracticeLoginNewUser
from login_files.login_valid import TestAutomationPracticeLoginValid

from cart_order_files.search_addtocart import TestAutomationPracticeSearchAddtocart
from cart_order_files.orderconfirmation import TestAutomationPracticeOrderConmpletion

#Retreive all unit tests
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestAutomationPracticeLoginInvalid)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestAutomationPracticeLoginNewUser)
tc3 = unittest.TestLoader().loadTestsFromTestCase(TestAutomationPracticeLoginValid)
tc4 = unittest.TestLoader().loadTestsFromTestCase(TestAutomationPracticeSearchAddtocart)
tc5 = unittest.TestLoader().loadTestsFromTestCase(TestAutomationPracticeOrderConmpletion)

alltestsuite = unittest.TestSuite([tc1,tc2,tc3,tc4,tc5])

unittest.TextTestRunner().run(alltestsuite)






