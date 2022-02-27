from WasRun import WasRun
from TestCase import TestCase


class TestCaseTest(TestCase):
    def testRunning(self):
        test = WasRun("testMethod")
        assert not test.wasRun
        test.run()
        assert test.wasRun


if __name__ == '__main__':
    TestCaseTest("testRunning").run()