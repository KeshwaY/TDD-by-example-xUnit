from WasRun import WasRun
from TestCase import TestCase


class TestCaseTest(TestCase):

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert "setUp testMethod tearDown" == test.log


if __name__ == '__main__':
    TestCaseTest("testTemplateMethod").run()
