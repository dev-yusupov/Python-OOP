class Math:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b

    @property
    def addition(self):
        print(f"Here is the result {self.add()}")
    
    @staticmethod
    def return_value():
        return print(f"This class helps you to solve simple mathematical problems!!!")
    

Math(3,4).addition