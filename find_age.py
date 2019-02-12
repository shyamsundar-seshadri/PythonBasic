'''
    finds your age
'''
import datetime

def find_age(yob, year):
    return year - yob

def get_year_of_birth():
    return input("Enter your year of birth: ")
def main():
    current_year = int(datetime.datetime.now().year)
    yob =  int(get_year_of_birth())
    current_age = find_age(yob, current_year)
    age_in_10_years =  current_age + 10
    print("You current age is:",current_age, "and in 10 years you will be:",age_in_10_years)

main()
