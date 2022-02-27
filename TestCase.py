class TestCase:
    def __init__(self, name) -> None:
        self.name = name

    def setUp(self):
        ...

    def tearDown(self):
        ...

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()
