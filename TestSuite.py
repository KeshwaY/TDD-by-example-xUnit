from TestCase import TestCase


class TestSuite(TestCase):
    def __init__(self, name):
        super().__init__(name)
        self.tests = []

    def add(self, test):
        self.tests.append(test)

    def run(self, result):
        result.log += f'{self.name}:\n'
        for test in self.tests:
            test.run(result)
