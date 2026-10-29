name=input("enter thr student name:")
n=int(input("enter number of subjects:"))
tot=0
for i in range(1,n+1):
    mark=float(input(f"enter mark for subject {i}:"))
    tot=tot+mark
percentage=tot/n
if(percentage>=90):
    grade="A+"
    performance="outstanding"
elif(percentage>=80):
    grade="A"
    performance="excellent"
elif(percentage>=70):
    grade="B"
    performance="very good"
elif(percentage>=60):
    grade="C"
    performance="good"
elif(percentage>=50):
    grade="D"
    performance="average"
else:
    grade="F"
    performance="needs improvement"
print("\n --- academic performance---")
print("student name:",name)
print("total marks:",tot)
print("percentage:",round(percentage,2),"%")
print("grade:",grade)
print("performance:",performance)
