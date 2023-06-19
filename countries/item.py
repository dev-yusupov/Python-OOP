from country import Country

class Russia(Country):
    def __str__(self):
        return f"The capital city of {self.name} is {self.capital}"

country = Country("Russia", "Moscow")
russia = Russia("Russia", "Moscow")
print(russia)
