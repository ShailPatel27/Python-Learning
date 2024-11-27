def printDay(day):
    match day:
        case "Monday":
            return "Today is Monday"
        
        case "Tuesday":
            return "Today is Tuesday"
        
        case "Wednesday":
            return "Today is Wednesday"
        
        case "Thursday":
            return "Today is Thursday"
        
        case "Friday":
            return "Today is Friday"
        
        case "Saturday":
            return "Today is Saturday"
        
        case "Sunday":
            return "Today is Sunday"
        
day = input("Enter a day: ")
print(printDay(day))