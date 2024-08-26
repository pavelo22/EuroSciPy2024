class Number:
    def __new__(cls, value):
        instance = super().__new__(cls)
        ... # <---- put your code here  
        instance.value = value
        return instance

    def __init__(self, value):
        ... # <---- put your code here  

    def __del__(self):
        ... # <---- put your code here  


n = Number(5)
print(n.value)
