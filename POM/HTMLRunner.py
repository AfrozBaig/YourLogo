from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
import POM.Tests.login

example_tests = TestLoader().loadTestsFromTestCase(POM.Tests.login.LoginTest)


suite = TestSuite([example_tests])

runner = HTMLTestRunner(output='C:/Users/Karan Singh Bais/PycharmProjects/YourLogo/Reports/ExecutionReport.html')

runner.run(suite)
