from TestCase import TestCase


class WasRun(TestCase):
    def __init__(self, name) -> None:
        super(WasRun, self).__init__(name)
        self.log = None

    def setUp(self):
        self.log = "setUp"

    def tearDown(self):
        self.log = f'{self.log} tearDown'

    def testMethod(self):
        self.log = f'{self.log} testMethod'

    def testBrokenMethod(self):
        raise Exception
