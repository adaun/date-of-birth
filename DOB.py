#CALCULATING THE DAY ONE'S BORN
import datetime
Age = int(input("Age: "))
MonthOfBirth = int(input("Month Of Birth: "))
DateOfBirth = int(input("Date Of Birth: "))
DateNow = datetime.datetime.now()
DaysPerYear = 365
DaysLived = Age*DaysPerYear
RealDateOfBirthTimeDelta = datetime.timedelta(days=DaysLived)
RealDateOfBirth = DateNow-RealDateOfBirthTimeDelta
YearOfBirth = int(RealDateOfBirth.strftime("%Y"))
ActualDateOfBirth = datetime.date(YearOfBirth,MonthOfBirth,DateOfBirth)
print("You Were Born On",ActualDateOfBirth.strftime("%A"))
