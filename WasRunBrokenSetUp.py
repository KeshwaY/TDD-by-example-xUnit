from WasRun import WasRun


class WasRunBrokenSetUp(WasRun):

    def setUp(self):
        raise Exception
