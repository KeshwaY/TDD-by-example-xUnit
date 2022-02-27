class TestCase:
    def __init__(self, name) -> None:
        self.name = name

    def setUp(self):
        ...

    def tearDown(self):
        ...

    def run(self, result):
        try:
            self.setUp()
        except Exception as e:
            self.tearDown()
            result.testFailed(f"Error setting up: {e.__str__()}\n")
            return result

        try:
            result.testStarted()
            method = getattr(self, self.name)
            method()
        except Exception as e:
            result.testFailed(f"Error running {self.name}: {e.__str__()}\n")

        self.tearDown()
        return result
