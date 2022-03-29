class Person:
    '''This is a person class
       this is the second line
    '''
    def __init__(self, default_sex):
        self.age = 10
        self.default_sex =default_sex

        print(f'Aget is {self.age} - Sex {self.default_sex}')

    def greet(self):
        print('Hello')


class Man(Person):
    def __init__(self, default_sex):
        self.name = "Input Name"
        super().__init__(default_sex)

Bren = Man('Male')

# Output: 10
print(Bren.age)

# Output: <function Person.greet>
print(Bren.greet)

# Output: "This is a person class"
print(Person.__doc__)
