Months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
Rainfall = []

def GetRainfallData():
    MonthIndex = 0
    while MonthIndex < 12:  
        Rain = input("Enter the rainfall for " + Months[MonthIndex] + " (in inches): ")
        if Rain != '':
            try:
                Rain = float(Rain)
                if Rain >= 0:
                    Rainfall.append(Rain)
                    MonthIndex = MonthIndex + 1
                else:
                    print("Rainfall cannot be negative.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        else:
            print("Input cannot be blank.")

GetRainfallData()

HighestRainfall = Rainfall[0]
LowestRainfall = Rainfall[0]
HighestMonth = Months[0]
LowestMonth = Months[0]
MonthIndex = 1

while MonthIndex < 12:
    if Rainfall[MonthIndex] > HighestRainfall:
        HighestRainfall = Rainfall[MonthIndex]
        HighestMonth = Months[MonthIndex]
    if Rainfall[MonthIndex] < LowestRainfall:
        LowestRainfall = Rainfall[MonthIndex]
        LowestMonth = Months[MonthIndex]
    MonthIndex = MonthIndex + 1

TotalRainfall = sum(Rainfall)
AverageRainfall = TotalRainfall / len(Rainfall)

print("Data list:", Rainfall)
print("Highest:", HighestMonth, HighestRainfall)
print("Lowest:", LowestMonth, LowestRainfall)
print("Total:", TotalRainfall)
print("Average:", AverageRainfall)
