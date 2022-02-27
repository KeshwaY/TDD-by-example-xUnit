from TestCase import TestCase


class WasRun(TestCase):
    def __init__(self, name) -> None:
        super(WasRun, self).__init__(name)
        self.wasRun = None

    def testMethod(self):
        self.wasRun = 1
