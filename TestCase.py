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
        self.setUp()
        result.testStarted()
        method = getattr(self, self.name)
        method()
        self.tearDown()
        return result
