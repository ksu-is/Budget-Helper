


monthList = ["january","february","mearch","april","may","june","july","august","september","october","november","december"]
userexpenses = []
userInput = ""
print("Welcome to your Budget Helper!")
currentMonth = input("Enter the month: ").lower()
if currentMonth in monthList:
    totalMoney = input("Enter your expected earnings for this month: ")
    userInput = ""
    while True:
        userInput = input("Name a reocurring monthly expense or type 'exit' to move on: ")
        if userInput == "exit":
            break
        userInput2 = float(input("How much is the expense? "))
        userexpenses.append((userInput,userInput2))
else:
    print("You may have miss typed the month")
grandTotal = 0
for netTotal in userexpenses:
    print(netTotal[0] + ": " + str(netTotal[1]))
    grandTotal += netTotal[1]
print("reoccrTotal: " + str(grandTotal))