print("Welcome to the GPA calculator")
print("Please enter all your letter grades, one per line.")
print("Enter a blank line to designate the end.")

# map from letter grade to point value
points = {
    'A+': 4.0,
    'A': 3.8,
    'A-': 3.67,
    'B+': 3.33,
    'B': 3.0,
    'B-': 2.67,
    'C+': 2.33,
    'C': 2.0,
    'C-': 1.67,
    'D': 1.0,
    'F': 0.0,
}
num_courses = 0
total_points = 0
done = False

while not done:
    # readline from user input
    grade = input()
    if grade == '': # empty line was entered
        done = True
    elif grade not in points:
        print("Unknow grade '{0}' being ignored".format(grade))
    else:
        num_courses += 1
        total_points += points[grade]

if num_courses > 0: # avoid division by zero
    print("Your GPA is {0:.3}".format(total_points / num_courses))