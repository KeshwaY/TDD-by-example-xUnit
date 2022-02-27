class TestResult:
    def __init__(self):
        self.runCount = 0
        self.errorCount = 0
        self.log = ""

    def testStarted(self):
        self.runCount += 1

    def testFailed(self, message):
        self.log += f'{message}'
        self.errorCount += 1

    def summary(self):
        return f'{self.runCount} run, {self.errorCount} failed'
