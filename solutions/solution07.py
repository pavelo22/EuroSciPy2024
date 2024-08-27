class Number:
    def __new__(cls, value):
        instance = super().__new__(cls)
        print('__new__')
        instance.value = value
        return instance

    def __init__(self, value):
        print('__init__')

    def __del__(self):
        print('__del__')


n = Number(5)
print(n.value)
del n
