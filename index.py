from datetime import datetime

def get_day_of_week(year, month, day):
    date = datetime(year, month, day)
    return date.strftime("%A")

def main():
    year = int(input("Enter the year: "))
    month = int(input("Enter the month: "))
    day = int(input("Enter the day: "))
    
    print(f"The day of the week for {year}-{month}-{day} is:")
    print(get_day_of_week(year, month, day))
main()
