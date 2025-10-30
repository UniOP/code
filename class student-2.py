class student:
    grade = 11
    name = "shashwata"

    def introduction(self):
        print("hi i am a student")

    def details(self):
        print("my name is", self.name)
        print("I study in grade", self.grade)
ob = student()
ob.introduction()
ob.details()