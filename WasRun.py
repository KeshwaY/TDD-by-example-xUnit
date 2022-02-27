from TestCase import TestCase


class WasRun(TestCase):
    def __init__(self, name) -> None:
        super(WasRun, self).__init__(name)
        self.wasRun = None
        self.wasSetUp = None

    def testMethod(self):
        self.wasRun = 1

    def setUp(self):
        self.wasSetUp = 1
