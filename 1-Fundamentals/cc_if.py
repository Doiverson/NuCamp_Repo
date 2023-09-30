"""
  Students  |  Grades  |  Letters
------------|----------|----------
  George    |  46      |  F
  Michell   |  80      |  B
  Josh      |  12      |  F
  Chloe     |  68      |  D
  Stanley   |  99      |  A
  Annie     |  100     |  A+
"""
students = [
    {"George": 46},
    {"Michell": 80},
    {"Josh": 12},
    {"Chloe": 68},
    {"Stanley": 99},
    {"Annie": 100},
]

for dic in students:
    for name in dic:
        gradeToTest = dic[name]
        if gradeToTest == 100:
            print(name + " is A+")
        elif gradeToTest >= 90:
            print(name + " is A")
        elif gradeToTest >= 80:
            print(name + " is B")
        elif gradeToTest >= 70:
            print(name + " is C")
        elif gradeToTest >= 50:
            print(name + " is D")
        else:
            print(name + " is F")
