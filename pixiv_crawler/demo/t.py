class foo(object):
    def __init__(self):
        self.x = []
    def a(self):
        def b():
            self.x.append('1')
            print(self.x)
        b()


foo().a()