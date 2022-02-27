from WasRun import WasRun
from WasRunBrokenSetUp import WasRunBrokenSetUp
from TestCase import TestCase


class TestCaseTest(TestCase):

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert("setUp testMethod tearDown" == test.log)

    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert("1 run, 0 failed" == result.summary())

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert("1 run, 1 failed" == result.summary())

    def testFailedSetUp(self):
        test = WasRunBrokenSetUp("testMethod")
        result = test.run()
        assert("0 run, 1 failed" == result.summary())


if __name__ == '__main__':
    TestCaseTest("testTemplateMethod").run()
    TestCaseTest("testResult").run()
    TestCaseTest("testFailedResult").run()
    TestCaseTest("testFailedSetUp").run()
