from TestResult import TestResult


class TestCase:
    def __init__(self, name) -> None:
        self.name = name

    def setUp(self):
        ...

    def tearDown(self):
        ...

    def run(self):
        result = TestResult()
        try:
            self.setUp()
            result.testStarted()
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()
        self.tearDown()
        return result
