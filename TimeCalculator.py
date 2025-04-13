def add_time(start, duration, day = "none"):
    day = day.lower()
    dayInMins = 1440 # 1440 minutes in a day.
    
    startInfo = start.split()
    startInfo[0] = startInfo[0].split(":")
    startHours = int(startInfo[0][0])
    startMins = int(startInfo[0][1])
    startHalfOfDay = startInfo[1]
    if startHours == 12:
        startHours = 0 # The hour calculation being 12 would cause an error and is taken care of by AM/PM notation.
    if startHalfOfDay == "AM":
        startTotalMins = (startHours * 60) + startMins
    else:
        startTotalMins = (startHours * 60) + startMins + (12 * 60)
    
    durationInfo = duration.split(":")
    durationHours = int(durationInfo[0])
    durationMins = int(durationInfo[1])
    durationTotalMins = (durationHours * 60) + durationMins
    
    totalMins = durationTotalMins + startTotalMins
    daysAfter = totalMins // dayInMins
    totalMinsForCalc = totalMins % dayInMins
    
    if day != "none":
        match day:
            case "monday":
                weekday = 1
            case "tuesday":
                weekday = 2
            case "wednesday":
                weekday = 3
            case "thursday":
                weekday = 4
            case "friday":
                weekday = 5
            case "saturday":
                weekday = 6
            case "sunday":
                weekday = 7
        dayAfterNum = weekday + daysAfter
        if dayAfterNum > 7:
            dayAfterNum = ((dayAfterNum - 1) % 7) + 1
        match dayAfterNum:
            case 1:
                dayAfter = "Monday"
            case 2:
                dayAfter = "Tuesday"
            case 3:
                dayAfter = "Wednesday"
            case 4:
                dayAfter = "Thursday"
            case 5:
                dayAfter = "Friday"
            case 6:
                dayAfter = "Saturday"
            case 7:
                dayAfter = "Sunday"
    
            
    
    hoursAfter = totalMinsForCalc // 60
    minsAfter = totalMinsForCalc % 60
    
    if day == "none":
        if daysAfter == 0:
            if hoursAfter < 12:
                if hoursAfter == 0:
                    hoursAfter = 12
                return "{}:{:02} AM".format(hoursAfter, minsAfter)
            else:
                if hoursAfter == 12:
                    return "{}:{:02} PM".format(hoursAfter, minsAfter)
                else:
                    hoursAfter -= 12
                    return "{}:{:02} PM".format(hoursAfter, minsAfter)
        elif daysAfter == 1:
            if hoursAfter < 12:
                if hoursAfter == 0:
                    hoursAfter = 12
                return "{}:{:02} AM (next day)".format(hoursAfter, minsAfter)
            else:
                if hoursAfter == 12:
                    return "{}:{:02} PM (next day)".format(hoursAfter, minsAfter)
                else:
                    hoursAfter -= 12
                    return "{}:{:02} PM (next day)".format(hoursAfter, minsAfter)
        else:
            if hoursAfter < 12:
                if hoursAfter == 0:
                    hoursAfter = 12
                return "{}:{:02} AM ({} days later)".format(hoursAfter, minsAfter, daysAfter)
            else:
                if hoursAfter == 12:
                    return "{}:{:02} PM ({} days later)".format(hoursAfter, minsAfter, daysAfter)
                else:
                    hoursAfter -= 12
                    return "{}:{:02} PM ({} days later)".format(hoursAfter, minsAfter, daysAfter)
    else:
        if daysAfter == 0:
            if hoursAfter < 12:
                if hoursAfter == 0:
                    hoursAfter = 12
                return "{}:{:02} AM, {}".format(hoursAfter, minsAfter, dayAfter)
            else:
                if hoursAfter == 12:
                    return "{}:{:02} PM, {}".format(hoursAfter, minsAfter, dayAfter)
                else:
                    hoursAfter -= 12
                    return "{}:{:02} PM, {}".format(hoursAfter, minsAfter, dayAfter)
        elif daysAfter == 1:
            if hoursAfter < 12:
                if hoursAfter == 0:
                    hoursAfter = 12
                return "{}:{:02} AM, {} (next day)".format(hoursAfter, minsAfter, dayAfter)
            else:
                if hoursAfter == 12:
                    return "{}:{:02} PM, {} (next day)".format(hoursAfter, minsAfter, dayAfter)
                else:
                    hoursAfter -= 12
                    return "{}:{:02} PM, {} (next day)".format(hoursAfter, minsAfter, dayAfter)
        else:
            if hoursAfter < 12:
                if hoursAfter == 0:
                    hoursAfter = 12
                return "{}:{:02} AM, {} ({} days later)".format(hoursAfter, minsAfter, dayAfter, daysAfter)
            else:
                if hoursAfter == 12:
                    return "{}:{:02} PM, {} ({} days later)".format(hoursAfter, minsAfter, dayAfter, daysAfter)
                else:
                    hoursAfter -= 12
                    return "{}:{:02} PM, {} ({} days later)".format(hoursAfter, minsAfter, dayAfter, daysAfter)
    
    
print(add_time("3:00 PM", "24:20", "Friday")) # "3:20 PM, Saturday (next day)"
print(add_time("3:00 PM", "24:20")) # "3:20 PM (next day)"
print(add_time('8:16 PM', '466:02', 'tuesday')) # "6:18 AM, Monday (20 days later)"