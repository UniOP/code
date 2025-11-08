class cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old")

    def make_sound(self):
        print("Meow")

class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old")

    def make_sound(self):
        print("Bark")

cat1 = cat("dodo", 25)
dog1 = dog("tyson", 16)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()