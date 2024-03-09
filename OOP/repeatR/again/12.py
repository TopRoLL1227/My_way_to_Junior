class Example:

    def hello():
        print('hello')

    def instance_hello(self):
        print(f'hello {self}')

    @staticmethod
    def static_hello():
        print('static hello')

    @classmethod
    def class_hello(cls):
        print(f'class_hello {cls}')


Example.hello()

a = Example()
Example.instance_hello(a)

Example.static_hello()
a.static_hello()

Example.class_hello()
a.class_hello()