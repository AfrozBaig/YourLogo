import unittest
import os
import HTMLTestRunner

import POM.Tests.login


direct = os.getcwd()


class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(POM.Tests.login.LoginTest)
            # unittest.defaultTestLoader.loadTestsFromTestCase(GoogleTest.MyGoogleTest),
        ])

        outfile = open("C:/Users/Karan Singh Bais/PycharmProjects/YourLogo/Reports/ExecutionReport.html", "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title='Test Report',
            description='Smoke Tests'
        )

        runner1.run(smoke_test)



