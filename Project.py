


monthList = ["january","february","mearch","april","may","june","july","august","september","october","november","december"]
userExpenses = []
userExpensesOne = []
userInput = ""
userInputOne = ""
restOfYear = 0
print("Welcome to your Budget Helper!")
currentMonth = input("Enter the month: ").lower()
if currentMonth in monthList:
    totalMoney = input("Enter your expected earnings for this month: ")
    userInput = ""
    while True:
        userInput = input("Name a reocurring monthly expense or type 'next' to move on: ")
        if userInput == "next":
            break
        userInput2 = float(input("How much is the expense? "))
        userExpenses.append((userInput,userInput2))
    while True:
        userInputOne = input("Name a one time expense or type 'exit' to finish: ")
        if userInputOne == "exit":
            break
        userInputOne2 = float(input("How much is the one time expense? "))
        userExpensesOne.append((userInput,userInputOne2))
else:
    print("You may have miss typed the month")
monthlyReExpTotal = 0
monthlyOTETotal = 0
for netTotal in userExpenses:
    #print(netTotal[0] + ": " + str(netTotal[1]))
    monthlyReExpTotal += netTotal[1]
for netTotalOne in userExpensesOne:
    #print(netTotal[0] + ": " + str(netTotal[1]))
    monthlyOTETotal += netTotalOne[1]
if currentMonth == "january":
    restOfYear = 12
elif currentMonth == "february":
    restOfYear = 11
elif currentMonth == "march":
    restOfYear = 10
elif currentMonth == "april":
    restOfYear = 9
elif currentMonth == "may":
    restOfYear = 8
elif currentMonth == "june":
    restOfYear = 7
elif currentMonth == "july":
    restOfYear = 6
elif currentMonth == "august":
    restOfYear = 5
elif currentMonth == "september":
    restOfYear = 4
elif currentMonth == "october":
    restOfYear = 3
elif currentMonth == "november":
    restOfYear = 2
elif currentMonth == "december":
    restOfYear = 1
else:
    print("invalid")
 
netMonthTotal = int(totalMoney) - int(monthlyReExpTotal) - int(monthlyOTETotal)
netMonthWOOT = int(totalMoney) - int(monthlyReExpTotal)
yearNetTotal = int(netMonthTotal) * int(restOfYear)
yearNetTotalWOOT = int(netMonthWOOT) * int(restOfYear)
print("Your net total for the month is: " + str(netMonthTotal))
print("Your net total for the month without one time purchases is: " + str(netMonthWOOT))
print("Your net total for the year is: " + str(yearNetTotal))
print("Your net total for the year without one time purchases is: " + str(yearNetTotalWOOT))
