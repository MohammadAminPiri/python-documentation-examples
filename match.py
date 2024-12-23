# Write a function that takes a string representing a day of the week and uses a match statement to return whether it is a weekday or the weekend.


def day_type(day):
    match day:
        case "sunday" | "saturday":
            print("weekend")
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            print("Weekday")


day_type("monday")
