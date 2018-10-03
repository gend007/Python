class NewStyleClassBase(object):

    def test_method(self, msg):
        print('NewStyleClassBase: {}'.format(msg))


class NewStyleClassBase(NewStyleClassBase):

    def test_method(self, msg):
        print('NewStyleClass: {}'.format(msg))
        super().test_method(msg)


new = NewStyleClassBase()
new.test_method('method call')