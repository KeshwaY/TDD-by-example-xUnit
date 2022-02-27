from WasRun import WasRun
from WasRunBrokenSetUp import WasRunBrokenSetUp
from TestCase import TestCase
from TestResult import TestResult
from TestSuite import TestSuite


class TestCaseTest(TestCase):

    def setUp(self):
        self.result = TestResult()

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert("setUp testMethod tearDown" == test.log)

    def testResult(self):
        test = WasRun("testMethod")
        test.run(self.result)
        assert("1 run, 0 failed" == self.result.summary())

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        test.run(self.result)
        assert("1 run, 1 failed" == self.result.summary())

    def testFailedSetUp(self):
        test = WasRunBrokenSetUp("testMethod")
        test.run(self.result)
        assert("0 run, 1 failed" == self.result.summary())

    def testSuite(self):
        localSuite = TestSuite("Local suite")
        localSuite.add(WasRun("testMethod"))
        localSuite.add(WasRun("testBrokenMethod"))
        localSuite.run(self.result)
        assert("2 run, 1 failed" == self.result.summary())

    def testLogFailedSetUp(self):
        test = WasRunBrokenSetUp("testMethod")
        test.run(self.result)
        assert("Error setting up: \n" == self.result.log)

    def testLogBrokenMethod(self):
        test = WasRun("testBrokenMethod")
        test.run(self.result)
        assert("Error running testBrokenMethod: \n" == self.result.log)


if __name__ == '__main__':
    suite = TestSuite("Main")
    suite.add(TestCaseTest("testTemplateMethod"))
    suite.add(TestCaseTest("testResult"))
    suite.add(TestCaseTest("testFailedResult"))
    suite.add(TestCaseTest("testFailedSetUp"))
    suite.add(TestCaseTest("testSuite"))
    suite.add(TestCaseTest("testLogFailedSetUp"))
    suite.add(TestCaseTest("testLogBrokenMethod"))
    result = TestResult()
    suite.run(result)
    print(result.log)
    print(result.summary())
