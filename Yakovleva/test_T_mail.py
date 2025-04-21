import unittest
import re
import myform
import mails

class test_T_mail(unittest.TestCase):
    def test_T(self):
        for mail in mails.correct_mails:
            self.assertTrue(re.match(myform.reg, mail))


if __name__ == '__main__':
    unittest.main()