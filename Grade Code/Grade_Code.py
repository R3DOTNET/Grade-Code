#input english marks, 2 tests
print("Please input your marks for your two english tests.")
eng1 = int(input(""))
eng2 = int(input(""))

#input maths marks, 3 tests
print("Same for all three maths")
math1 = int(input(""))
math2 = int(input(""))
math3 = int(input(""))

#input science marks, 3 tests
print("Same for Science.")
sci1 = int(input(""))
sci2 = int(input(""))
sci3 = int(input(""))

#work out averages
#english average
engav = eng1 + eng1
engav = engav / 2
#maths average
mathav = math1 + math2 + math3
mathav = mathav / 3
#science average
sciav = sci1 + sci2 + sci3
sciav = sciav / 3

#less then, grade boundaries
#english
if engav >= 104:
    EngGrade = "A"
elif engav >= 84:
    EngGrade = "B"
elif engav >= 64:
    EngGrade = "C"
else:
    EngGrade = "FAIL"
#math
if mathav >= 78:
    MathGrade = "A"
elif mathav >= 64:
    MathGrade = "B"
elif mathav >= 56:
    MathGrade = "C"
else:
    MathGrade = "FAIL"
#science
if sciav >= 128:
    SciGrade = "A"
elif sciav >= 113:
    SciGrade = "B"
elif sciav >= 96:
    SciGrade = "C"
else:
    SciGrade = "FAIL"

#tell grade
print("Here are your final Grades.")

print(f"English: {EngGrade}")
print(f"Maths: {MathGrade}")
print(f"Science: {SciGrade}")

#total marks of all subjects
def totalmarks():    #see i used a function <----
    print("Your total marks across all subjects:")
    totalmarks = engav + mathav + sciav
    print(totalmarks)
    totalmarks()