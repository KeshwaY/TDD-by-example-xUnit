from WasRun import WasRun
from TestCase import TestCase


class TestCaseTest(TestCase):

    def setUp(self):
        self.test = WasRun("testMethod")

    def testTemplateMethod(self):
        self.test.run()
        assert "setUp testMethod tearDown" == self.test.log

    def testResult(self):
        result = self.test.run()
        assert "1 run, 0 failed" == result.summary()

    def testFailedResult(self):
        result = self.test.run()
        assert "1 run, 1 failed" == result.summary()

if __name__ == '__main__':
    TestCaseTest("testTemplateMethod").run()
    TestCaseTest("testResult").run()
    TestCaseTest("testFailedResult").run()
