#monthList = ["january"==1,"february"==2,"march"==3,"april"==4,"may"==5,"june"==6,"july"==7,"august"==8,"september"==9,"october"==10,"november"==11,"december"==12]
monthList = ["january","february","march","april","may","june","july","august","september","october","november","december"]
userexpenses = []
userInput = ""
print("Welcome to your Budget Helper!")
currentMonth = input("Enter the month: ").lower()
if currentMonth in monthList:
    totalMoney = input("Enter your expected earnings for this month")
    while userInput != "exit":
        userInput == input("Name a reocurring monthly expense or type 'exit' to move on")
else:
    print("You may have miss typed the month")

#newMonths = ['jan']