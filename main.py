print("Student Study Tracker")

name=input("Enter your name:")
subject=input("what subject did you study?")
hour=float(input("HOW many hour did you study?"))
print("\n---Study Summary---")
print("Student:",name)
print("Subject:",subject)

if hour >=2:
  print("Great job!")
else:
  print("Keep going!")
