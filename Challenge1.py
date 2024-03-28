import random


class Student:
    educational_platform = 'udemy'

    def __init__(self, name, age=30):
        self.name = name
        self.age = age

    def greet(self):
        greetingsList = ["Hi, I'm {}", "Hey there, my name is {}", "Hi. Oh, my name is {}"]
        print(random.choices(greetingsList)[0].format(self.name))


def class_create(student_names):
    return [Student(name) for name in student_names]


studentsList = ["Lara", "sandra", "Carl", "john", "krasinksi"]

for student in class_create(studentsList):
    student.greet()
