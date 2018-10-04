class TestClass:

    @staticmethod
    def sample_staticmethod(x, y):
        return x + y


print(TestClass.sample_staticmethod(10, 100))


test_class = TestClass()
print(test_class.sample_staticmethod(100, 100))
