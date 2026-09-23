# Highest
numbers = [15, 42, 7, 89, 31, 56]

def find_highest(numbers):
    return max(numbers)
result = find_highest(numbers)
print("Highest:", result)

# Average Marks
students = [
    {"name": "Abhinav", "marks": 80},
    {"name": "Rahul", "marks": 70},
    {"name": "Aman", "marks": 90}
]

def calculate_average(students):
    total = 0
    for student in students:
        total += student["marks"]
        average = total / len(students)
    return average
result = calculate_average(students)
print("Average:", result)

# Function + List + Dictionary
students = [
    {"name": "Abhinav", "marks": 85},
    {"name": "Rahul", "marks": 32},
    {"name": "Aman", "marks": 76},
    {"name": "Karan", "marks": 28}
]

def count_failed_students(students):
    failed_students = 0
    for student in students:
        if student["marks"] < 33:
            failed_students += 1
    return failed_students

result = count_failed_students(students)

print("Failed students:", result)

# Pyhton Skills Search
students = [
    {"name": "Abhinav", "skills": {"Python", "HTML", "CSS"}},
    {"name": "Rahul", "skills": {"Java", "HTML"}},
    {"name": "Aman", "skills": {"Python", "JavaScript"}}
]

def find_python_students(students):
    python_students = []
    for student in students:
        if "Python" in student["skills"]:
            python_students.append(student["name"]) 
    return python_students

result = find_python_students(students)

print(result)

# Common Skills
student1 = {"Python", "HTML", "CSS"}
student2 = {"Python", "Java", "HTML"}

def find_common_skills(student1, student2):
    common = student1 & student2
    return common
result = find_common_skills(student1, student2)

print(result)

# Unique Skills
student1 = {"Python", "HTML", "CSS"}
student2 = {"Python", "Java", "HTML"}

def find_all_skills(student1, student2):
    unique = student1 | student2
    return unique

result = find_all_skills(student1, student2)

print(result)

# Top Student
students = [
    {"name": "Abhinav", "marks": 85},
    {"name": "Rahul", "marks": 92},
    {"name": "Aman", "marks": 78},
    {"name": "Karan", "marks": 88}
]
def find_top_student(students):
    top_student = students[0]
    for student in students:
        if student["marks"] > top_student["marks"]:
            top_student = student
    return top_student
result = find_top_student(students)
print(result)


students = [
    {"name": "Abhinav", "marks": 80},
    {"name": "Rahul", "marks": 60},
    {"name": "Aman", "marks": 90},
    {"name": "Karan", "marks": 70}
]

def find_above_average(students):

    total = 0

    for student in students:
        total += student["marks"]

    average = total / len(students)

    above_average = []

    for student in students:
        if student["marks"] > average:
            above_average.append(student["name"])

    return above_average


result = find_above_average(students)

print(result)

# Question3
numbers = [25, 60, 45, 80, 32, 75, 10]
def count_greater_than_50(numbers):
    count = 0
    for number in numbers:
        if number > 50:
            count += 1
    return count
result = count_greater_than_50(numbers)
print("Count:", result)


# FIND EVEN NUMBERS
numbers = [12, 7, 20, 15, 8, 3, 10]
def get_even_numbers(numbers):
    even = []
    for number in numbers:
        if number % 2 == 0:
            even.append(number)
    return even
result = get_even_numbers(numbers)
print(result)

# Count Unique Numbers
numbers = [10, 20, 10, 30, 20, 40, 30, 50]
def count_unique_numbers(numbers):
    unique_numbers = set(numbers)
    return len(unique_numbers)
result = count_unique_numbers(numbers)
print("Unique numbers:", result)

# Find a Specific Number
numbers = [15, 22, 8, 41, 30, 17]
def find_number(numbers, target):
    for number in numbers:
        if number == target:
            return True
    return False
result = find_number(numbers, 41)
print(result)


# Count a Specific Number
numbers = [10, 20, 10, 30, 10, 40, 20]
def count_number(numbers, target):
    count = 0
    for number in numbers:
        if number == target:
            count += 1
    return count
result = count_number(numbers, 10)
print("Count:", result)


students = [
    {"name": "Abhinav", "marks": 80},
    {"name": "Rahul", "marks": 65},
    {"name": "Aman", "marks": 90},
    {"name": "Karan", "marks": 70}
]

def get_high_scorers(students):

    high_scorers = []

    for student in students:
        if student["marks"] >= 75:
            high_scorers.append(student["name"])

    return high_scorers


result = get_high_scorers(students)

print(result)


# Q.18
numbers = [15, 42, 8, 31, 22, 50, 12]
def get_below_30(numbers):
    num = []
    for number in numbers:
        if number < 30:
            num.append(number)
    return num
result = get_below_30(numbers)
print(result)



# Q.19
numbers = [15, 42, 8, 31, 22, 50, 12]  
def count_below_30(numbers):
    count = 0
    for number in numbers:
        if number < 30:
            count += 1
    return count
result = count_below_30(numbers)
print(result)

# Q.20
numbers = [45, 12, 78, 5, 34, 20]
def find_smallest(numbers):
    for number in numbers:
        small = min(numbers)
    return small
result = find_smallest(numbers)
print(result)


# Q.21
numbers = [45, 12, 78, 5, 34, 20]
def find_smallest(numbers):
    small = numbers[0]
    for number in numbers:
        if number < small:
            small = number
    return small
result = find_smallest(numbers)
print(result)


# Q.22
numbers = [25, 60, 15, 90, 42, 30]
def find_largest(numbers):
    large = numbers[0]
    for number in numbers:
        if number > large:
            large = number
    return large        
result = find_largest(numbers)
print(result)

# Q.23
numbers = [25, 60, 15, 90, 42, 70, 30, 85]
def count_greater_than_50(numbers):
    count= 0 
    for number in numbers:
        if number > 50:
            count += 1
    return count
result = count_greater_than_50(numbers)
print(result)


# Q.24
numbers = [25, 60, 15, 90, 42, 70, 30, 85]
def get_greater_than_50(numbers):
    num = []
    for number in numbers:
        
        if number > 50:
            num.append(number)
            
    return num
result = get_greater_than_50(numbers)
print(result)

# Q.25
numbers = [12, 7, 20, 15, 8, 3, 10, 21]
def count_even(numbers):
    even_count = 0
    for number in numbers:
        if number % 2 == 0:
            even_count += 1
    return even_count
result = count_even(numbers)
print(result)


# Q.26
numbers = [12, 7, 20, 15, 8, 3, 10, 21]
def get_even_numbers(numbers):
    num = []
    for number in numbers:
        if number % 2 == 0:
            num.append(number)
    return num
result = get_even_numbers(numbers)
print(result)

# Q.27
numbers = [12, 7, 20, 15, 8, 3, 10, 21]
def count_odd(numbers):
    count = 0
    for number in numbers:
        if number % 2 != 0:
            count += 1
    return count
result = count_odd(numbers)
print(result)


# Q.28
numbers = [12, 7, 20, 15, 8, 3, 10, 21]

def get_odd_numbers(numbers):
    num = []
    for number in numbers:
        if number % 2 != 0:
            num.append(number)
    return num
result = get_odd_numbers(numbers)
print(result)


# Q.29
numbers = [12, 7, 20, 15, 8, 3, 10, 21]
def sum_even(numbers):
    total = 0
  
    for number in numbers:
        if number % 2 == 0:
            total += number 
    return total
result = sum_even(numbers)
print(result)


# Q.30
numbers = [12, 7, 20, 15, 8, 3, 10, 21]
def sum_odd(numbers):
    total = 0
    for number in numbers:
        if number % 2 != 0:
            total += number
    return total
result = sum_odd(numbers)
print(result)


# Q.31
numbers = [10, 23, 35, 42, 50, 17, 60, 71]
def count_divisible_by_5(numbers):
    count = 0
    for number in numbers:
        if number % 5 == 0:
            count += 1
    return count
result = count_divisible_by_5(numbers)
print(result)


# Q.32
numbers = [10, 23, 35, 42, 50, 17, 60, 71]
def get_divisible_by_5(numbers):
    num = []
    for number in numbers:
        if number % 5 == 0:
            num.append(number)
    return num
result = get_divisible_by_5(numbers)
print(result)


# Q.33
numbers = [12, 7, 15, 22, 30, 41, 18, 25]
def count_divisible_by_3(numbers):
    count = 0
    for number in numbers:
        if number % 3 == 0:
            count += 1
    return count
result = count_divisible_by_3(numbers)
print(result)


# Q.34
numbers = [12, 7, 15, 22, 30, 41, 18, 25]
def get_divisible_by_3(numbers):
    num = []
    for number in numbers:
        if number % 3 == 0:
            num.append(number)
    return num
result = get_divisible_by_3(numbers)
print(result)

# Q.35
numbers = [12, 7, 15, 22, 30, 41, 18, 25]
def sum_divisible_by_3(numbers):
    total = 0
    for number in numbers:
        if number % 3 == 0:
            total += number
    return total
result = sum_divisible_by_3(numbers)
print(result)


# Q.36
numbers = [10, 25, 30, 44, 50, 63, 70, 81]
def count_divisible_by_10(numbers):
    count = 0
    for number in numbers:
        if number % 10 == 0:
            count += 1
    return count
result = count_divisible_by_10(numbers)
print(result)

# Q.37
numbers = [10, 25, 30, 44, 50, 63, 70, 81]
def get_divisible_by_10(numbers):
    num = []
    for number in numbers:
        if number % 10 == 0:
            num.append(number)
    return num
result = get_divisible_by_10(numbers)
print(result)


# Q.38
numbers = [10, 25, 30, 44, 50, 63, 70, 81]
def sum_divisible_by_10(numbers):
    total = 0
    for number in numbers:
        if number % 10 == 0:
            total += number

    return total
result = sum_divisible_by_10(numbers)
print(result)


# Q.39
numbers = [-5, 10, -2, 8, 0, 15, -7, 20]
def count_positive(numbers):
    count = 0
    for number in numbers:
        if number > 0:
            count += 1
    return count
result = count_positive(numbers)
print(result)


# Q.40
numbers = [-5, 10, -2, 8, 0, 15, -7, 20]
def get_positive_numbers(numbers):
    num = []
    for number in numbers:
        if number > 0:
            num.append(number)
    return num
result = get_positive_numbers(numbers)
print(result)


# Q.41
numbers = [-5, 10, -2, 8, 0, 15, -7, 20]
def count_negative(numbers):
    count = 0
    for number in numbers:
        if number < 0:
            count += 1
    return count
result = count_negative(numbers)
print(result)


# Q.42
numbers = [-5, 10, -2, 8, 0, 15, -7, 20]
def get_negative_numbers(numbers):
    num = []
    for number in numbers:
        if number < 0:
            num.append(number)
    return num
result = get_negative_numbers(numbers)
print(result)


# Q.43
numbers = [-5, 10, -2, 8, 0, 15, -7, 20]
def sum_positive(numbers):
    total = 0
    for number in numbers:
        if number > 0:
            total += number
    return total
result = sum_positive(numbers)
print(result)


# Q.44
numbers = [-5, 10, -2, 8, 0, 15, -7, 20]
def sum_negative(numbers):
    total = 0
    for number in numbers:
        if number < 0:
            total += number
    return total
result = sum_negative(numbers)
print(result)


# Q.45
numbers = [-5, 10, -2, 8, 0, 15, -7, 20]
def average_positive(numbers):
    total = 0
    count = 0
    for number in numbers:
        if number > 0:
            total += number
            count += 1
            avg = total / count
    return avg
result = average_positive(numbers)
print(result)

# Q.46
numbers = [10, 15, 20, 7, 8, 25, 12]
def average_even(numbers):
    total = 0
    count = 0
    for number in numbers:
        if number % 2 == 0:
            total += number
            count += 1
    avg  = total / count
    return avg
result= average_even(numbers)
print(result)


# Q.47
numbers = [25, 60, 80, 40, 70, 30, 90]
def average_greater_than_50(numbers):
    total = 0
    count = 0
    for number in numbers:
        if number > 50:
            total += number
            count += 1
    avg = total + count
    return avg
result = average_greater_than_50(numbers)
print(result)


# Q.48
numbers = [15, 42, 18, 75, 60, 33, 90, 27]
def find_largest_even(numbers):
    large = 0
    
    for number in numbers:
        if number % 2 == 0 and number > large:
            large = number
    return large
result = find_largest_even(numbers)
print(result)

# Q.49
numbers = [15, 42, 18, 75, 60, 33, 8, 27]

def find_smallest_even(numbers):
    small = None
    for number in numbers:
        if number % 2 == 0:
            if small is None or number < small:
                small = number
    return small
result = find_smallest_even(numbers)
print(result)


# Q.50
numbers = [12, 35, 18, 47, 60, 21, 55, 8]
def find_largest_odd(numbers):
    large = 0
    for number in numbers:
        if number % 2 != 0:
            large  = number
    return large
result = find_largest_odd(numbers)
print(result)


# Q.51
numbers = [12, 35, 18, 47, 60, 21, 55, 8]
def find_smallest_odd(numbers):
    small  = None
    for number in numbers:
        if number % 2 != 0:
            if small is None or number < small:
                small =  number
    return  small
result = find_smallest_odd(numbers)
print(result)

# Q.52
numbers = [10, 20, 30, 40, 50]
def count_above_average(numbers):
    total = 0
    for number in numbers:
        total += number
    avg = total / len(numbers)
    count = 0
    for number in numbers:
        if number > avg:
            count += 1
    return count
result = count_above_average(numbers)
print(result)

# Q.53
numbers = [10, 20, 30, 40, 50]

def get_above_average(numbers):
    total = 0
    for number in numbers:
        total += number
    avg = total / len(numbers)
    num = []
    for number in numbers:
        if number > avg:
            num.append(number)
    return num
result = get_above_average(numbers)
print(result)


# Q.54
numbers = [10, 20, 30, 40, 50]

def get_below_average(numbers):
    total = 0
    for number in numbers:
        total += number
    avg = total / len(numbers)
    num = []
    for number in numbers:
        if number < avg:
            num.append(number)
    return num
result = get_below_average(numbers)
print(result)


# Q.55
numbers = [10, 20, 30, 40, 50]

def count_below_average(numbers):
    total = 0
    for number in numbers:
        total += number
    avg = total / len(numbers)
    count = 0
    for number in numbers:
        if number < avg:
            count += 1
    return count
result = count_below_average(numbers)
print(result)

# Q.56
numbers = [10, 20, 30, 40, 50]

def sum_above_average(numbers):
    total = 0
    for number in numbers:
        total += number
    avg = total / len(numbers)
    
    total2 = 0
    for number in numbers:
            if number > avg:
                total2 += number
    return total2
result  = sum_above_average(numbers)
print(result)


# Q.57
numbers = [10, 20, 30, 40, 50]

def sum_below_average(numbers):
    total = 0
    for number in numbers:
        total += number
    avg = total / len(numbers)
    total2 = 0
    for number in numbers:
        if number < avg:
            total2 += number
    return total2
result = sum_below_average(numbers)
print(result)

# Q.58
numbers = [10, 20, 30, 40, 50]

def average_above_average(numbers):
    total = 0
    for number in numbers:
        total += number
    avg = total / len(numbers)
    total2 = 0
    count = 0
    for number in numbers:
        if number > avg:
            total2 += number
            count += 1
    return total2 / count
result = average_above_average(numbers)
print(result)


# Q.59
numbers = [10, 20, 30, 40, 50]

def average_below_average(numbers):
    total = 0
    for number in numbers:
        total += number
    avg = total / len(numbers)
    total2 = 0
    count = 0
    for number in numbers:
        if number < avg:
            total2 += number
            count += 1
    return total2 / count
result = average_below_average(numbers)
print(result)

# Q.60
numbers = [10, 20, 30, 40, 50]

def count_equal_average(numbers):
    total = 0
    for number in numbers:
        total += number
    avg = total / len(numbers)
    count = 0
    for number in numbers:
        if number == avg:
            count += 1
    return count
result = count_equal_average(numbers)
print(result)


# Q.61
numbers = [10, 20, 30, 40, 50]

def get_equal_average(numbers):
    total = 0
    for number in numbers:
        total += number
    avg = total / len(numbers)
    num = []
    for number in numbers:
        if number == avg:
            num.append(number)
    return num
result = get_equal_average(numbers)
print(result)

# Q.62
numbers = [10, 20, 30, 40, 50]

def count_not_equal_average(numbers):
    total = 0
    for number in numbers:
        total += number
    avg = total / len(numbers)
    count = 0
    for number in numbers:
        if number != avg:
            count += 1
    return count
result = count_not_equal_average(numbers)
print(result)


# Q 63
numbers = [10, 20, 30, 40, 50]

def get_not_equal_average(numbers):
    total = 0
    for number in numbers:
        total += number
    avg = total / len(numbers)
    num = []
    for number in numbers:
        if number != avg:
            num.append(number)
    return num
result = get_not_equal_average(numbers)
print(result)

# Q.64
numbers = [10, 25, 32, 40, 55, 60, 71, 80]

def count_greater_than_30_even(numbers):
    count = 0
    for number in numbers:
        if number > 30 and number  % 2 == 0:
            count += 1
    return count
result = count_greater_than_30_even(numbers)
print(result)

# Q.65
numbers = [10, 25, 32, 40, 55, 60, 71, 80]

def get_greater_than_30_even(numbers):
    num = []
    for number in numbers:
        if number > 30 and number % 2 == 0:
            num.append(number)
    return num
result = get_greater_than_30_even(numbers)
print(result)

# Q.66
numbers = [10, 25, 33, 42, 47, 55, 61, 19]

def count_less_than_50_odd(numbers):
    count = 0
    for number in numbers:
        if number < 50 and number % 2 != 0 :
            count += 1
    return count
result = count_less_than_50_odd(numbers)
print(result)


# Q.67
numbers = [10, 25, 33, 42, 47, 55, 61, 19]

def get_less_than_50_odd(numbers):
    num = []
    for number in numbers:
        if number < 50 and number % 2 != 0:
            num.append(number)
    return num
result = get_less_than_50_odd(numbers)
print(result)


# Q.68
numbers = [10, 25, 33, 42, 47, 55, 61, 19]

def sum_less_than_50_odd(numbers):
    total = 0 
    for number in numbers:
        if number < 50 and number % 2 != 0:
            total += number
    return total
result = sum_less_than_50_odd(numbers)
print(result)

# Q.69
numbers = [10, 15, 22, 25, 30, 33, 40, 42, 55]

def count_greater_than_20_divisible_by_5(numbers):
    count= 0 
    for number in numbers:
        if number > 20 and number % 5 == 0:
            count += 1
    return count
result = count_greater_than_20_divisible_by_5(numbers)
print(result)


# Q.70
numbers = [10, 15, 22, 25, 30, 33, 40, 42, 55]

def get_greater_than_20_divisible_by_5(numbers):
    num = []
    for number in numbers:
        if number > 20 and number % 5 == 0:
            num.append(number)
    return num
result = get_greater_than_20_divisible_by_5(numbers)
print(result)

# Q.71
numbers = [10, 15, 22, 25, 30, 33, 40, 42, 55]

def sum_greater_than_20_divisible_by_5(numbers):
    total = 0
    for number in numbers:
        if number > 20 and number % 5 == 0:
            total += number
    return total
result = sum_greater_than_20_divisible_by_5(numbers)
print(result)


# Q.72
numbers = [10, 25, 40, 55, 70, 85, 100, 120, 30]

def count_less_than_100_divisible_by_10(numbers):
    count = 0
    for number in numbers:
        if number < 100 and number % 10 == 0:
            count += 1
    return count
result = count_less_than_100_divisible_by_10(numbers)
print(result)


# Q.73
numbers = [10, 25, 40, 55, 70, 85, 100, 120, 30]

def get_less_than_100_divisible_by_10(numbers):
    num = []
    for number in numbers:
        if number < 100 and number % 10 == 0:
            num.append(number)
    return num
result = get_less_than_100_divisible_by_10(numbers)
print(result)


# Q.74
numbers = [10, 25, 40, 55, 70, 85, 100, 120, 30]

def sum_less_than_100_divisible_by_10(numbers):
    total = 0
    for number in numbers:
        if number < 100 and number % 10 == 0:
            total += number
    return total
result = sum_less_than_100_divisible_by_10(numbers)
print(result)


# Q.75
numbers = [12, 55, 63, 40, 71, 80, 95, 22, 33]
def function(numbers):
    count = 0
    for number in numbers:
        if number > 50 and number % 2 != 0:
            count += 1
    return count
result = function(numbers)
print(result)


# Q.76
numbers = [12, 55, 63, 40, 71, 80, 95, 22, 33]
def function(numbers):
    num = []
    for number in numbers:
        if number > 50 and number % 2 != 0:
            num.append(number)
    return num
result= function(numbers)
print(result)

# Q.77
numbers = [12, 55, 63, 40, 71, 80, 95, 22, 33]
def function(numbers):
    total = 0
    for number in numbers:
        if number > 50 and number % 2 != 0:
            total += number
    return total
result = function(numbers)
print(result)

# Q.78
numbers = [12, 25, 34, 47, 50, 62, 18, 71, 40]
count = 0
for number in numbers:
    if number < 50 and number % 2 == 0:
        count += 1
print(count)

# Q.79
numbers = [12, 25, 34, 47, 50, 62, 18, 71, 40]
def function(numbers):
    num = []
    for number in numbers:
        if number < 50 and number % 2 == 0:
            num.append(number)
    return num
result = function(numbers)
print(result)


# Q.80
numbers = [12, 25, 34, 47, 50, 62, 18, 71, 40]
def function(numbers):
    total = 0
    for number in numbers:
        if number < 50 and number % 2 == 0:
            total += number
    return total
result = function(numbers)
print(result)


# Q.81
numbers = [12, 31, 36, 45, 50, 63, 22, 72, 25]
def function(numbers):
    count = 0
    for number in numbers:
        if number > 30 and number % 3 == 0:
            count += 1
    return count
result = function(numbers)
print(result)


# Q.82
numbers = [12, 31, 36, 45, 50, 63, 22, 72, 25]
def function(numbers):
    num = []
    for number in numbers:
        if number > 30 and number % 3 == 0:
            num.append(number)
    return num
result = function(numbers)
print(result)


# Q.83
numbers = [12, 31, 36, 45, 50, 63, 22, 72, 25]
def function(numbers):
    total = 0
    for number in numbers:
        if number > 30 and number  % 3 == 0:
            total += number
    return total
result = function(numbers)
print(result)


# Q.84
numbers = [10, 22, 35, 48, 50, 63, 75, 40, 55]
def function(numbers):
    count = 0
    for number in numbers:
        if number < 60 and number % 5 == 0:
            count += 1
    return count
result = function(numbers)
print(result)


# Q.85
numbers = [10, 22, 35, 48, 50, 63, 75, 40, 55]
def function(numbers):
    num = []
    for number in numbers:
        if number < 60 and number % 5 == 0:
            num.append(number)
    return num
result= function(numbers)
print(result)


# Q.86
numbers = [10, 22, 35, 48, 50, 63, 75, 40, 55]
def function(numbers):
    total = 0
    for number in numbers:
        if number < 60 and number % 5 == 0:
            total += number
    return total
result = function(numbers)
print(result)

# Q.87
numbers = [12, 42, 55, 64, 71, 80, 33, 92, 25]
def function(numbers):
    count = 0
    for number in numbers:
        if number > 40 and number % 2 == 0:
            count += 1
    return count
result = function(numbers)
print(result)

# Q.88
numbers = [12, 42, 55, 64, 71, 80, 33, 92, 25]
def function(numbers):
    num = []
    for number in numbers:
        if number > 40 and number % 2 == 0:
            num.append(number)
    return num
result = function(numbers)
print(result)

# Q.89
numbers = [12, 42, 55, 64, 71, 80, 33, 92, 25]
def function(numbers):
    total = 0
    for number in numbers:
        if number > 40 and number % 2 == 0:
            total += number
    return total
result = function(numbers)
print(result)


# Q.90
numbers = [12, 25, 33, 48, 41, 55, 17, 62, 39]
def function(numbers):
    count = 0
    for number in numbers:
        if number < 50 and number % 2 != 0:
            count += 1
    return count
result = function(numbers)
print(result)


# Q.91
numbers = [12, 25, 33, 48, 41, 55, 17, 62, 39]
def function(numbers):
    num = []
    for number in numbers:
        if number < 50 and number % 2 != 0:
            num.append(number)
    return num
result = function(numbers)
print(result)


# Q.92
numbers = [12, 25, 33, 48, 41, 55, 17, 62, 39]
def function(numbers):
    total= 0
    for number in numbers:
        if number < 50 and number % 2 != 0:
            total += number
    return total
result = function(numbers)
print(result)


# Q.93
numbers = [12, 24, 31, 40, 45, 52, 18, 64, 70]
def function(numbers):
    count = 0
    for number in numbers:
        if number > 20 and number % 4 == 0:
            count += 1
    return count
result = function(numbers)
print(result)


# Q.94
numbers = [12, 24, 31, 40, 45, 52, 18, 64, 70]
def function(numbers):
    num = []
    for number in numbers:
        if number > 20 and number % 4 == 0:
            num.append(number)
    return num
result = function(numbers)
print(result)

# Q.95
numbers = [12, 24, 31, 40, 45, 52, 18, 64, 70]
def function(numbers):
    total = 0
    for number in numbers:
        if number > 20 and number % 4 == 0:
            total += number
    return total
result = function(numbers)
print(result)

# Q.96
numbers = [14, 22, 28, 35, 41, 49, 56, 70, 63]
def function(numbers):
    count = 0
    for number in numbers:
        if number < 70 and number % 7 == 0:
            count += 1
    return count
result = function(numbers)
print(result)

# Q.97
numbers = [14, 22, 28, 35, 41, 49, 56, 70, 63]
def function(numbers):
    num = []
    for number in numbers:
        if number < 70 and number % 7 == 0:
            num.append(number)
    return num
result = function(numbers)
print(result)

# Q.98
numbers = [14, 22, 28, 35, 41, 49, 56, 70, 63]
def function(numbers):
    total = 0
    for number in numbers:
        if number < 70 and number % 7 == 0:
            total += number
    return total
result = function(numbers)
print(result)

# Q.99
numbers = [12, 18, 25, 36, 42, 50, 54, 61, 72]
def function(numbers):
    count = 0
    for number in numbers:
        if number > 30 and number % 6 == 0:
            count += 1
    return count
result = function(numbers)
print(result)

# Q.100
numbers = [12, 18, 25, 36, 42, 50, 54, 61, 72]
def function(numbers):
    num = []
    for number in numbers:
        if number > 30 and number % 6 == 0:
            num.append(number)
    return num
result = function(numbers)
print(result)

