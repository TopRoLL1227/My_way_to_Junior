class Example:

    def hello():
        print('Hello')

    def instance_hello(self):
        print(f'instance_hello')

    @staticmethod
    def static_hello():
        print('static_hello')

    @classmethod
    def class_hello(cls):
        print(f'instance_hello {cls}')


a = Example()

a.instance_hello()
Example.instance_hello(a)

s = Example()

s.static_hello()
Example.static_hello()

z = Example()
a.class_hello()
Example.class_hello()