kilometers = 1
miles = 1

choice = input('What would you like to convert (Miles or Kilometers) ')

if choice.upper() == 'MILES':
    miles = float(input('How many miles? '))
    miles_to_kilometers = miles*1.609344
    print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
elif choice.upper() == 'KILOMETERS':
    kilometers = float(input('How many kilometers? '))
    kilometers_to_miles = kilometers/1.609344
    print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")