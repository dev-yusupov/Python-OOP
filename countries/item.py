from country import Country

class Russia(Country):
    def __init__(self, name, capital):
        super().__init__(name, capital)
    
    def __str__(self):
        return f"The capital city of {self.name} is {self.capital}"

russia = Russia("Russia", "Moscow")
print(russia)