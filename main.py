import time
import csv


fizz = "Fizz"
buzz = "Buzz"

max_iterations = 5000
time_score = [[
    'Method 1',
    'Method 2',
    'Method 3',
    'Method 4',
    'Method 5',
    'Method 6'
    ]]

for iteration in range(max_iterations):
    numbers_1 = []
    numbers_2 = []
    numbers_3 = []
    numbers_4 = []
    numbers_5 = []
    numbers_6 = []

    time_method_1 = 0
    time_method_2 = 0
    time_method_3 = 0
    time_method_4 = 0
    time_method_5 = 0
    time_method_6 = 0

    # Method 1:
    # Start at 0 (fizzbuzz), and repeat in steps of 15
    # n is always fizzbuzz
    # Insert into a list: n + 1 to n + 14
    # After the loop, remove the overflow numbers
    # Touches numbers n + (2 x overflow)

    t0 = time.time()
    for n in range(0, iteration, 15):
        numbers_1.append(fizz + buzz)
        numbers_1.append(n + 1)
        numbers_1.append(n + 2)
        numbers_1.append(fizz)
        numbers_1.append(n + 4)
        numbers_1.append(buzz)
        numbers_1.append(fizz)
        numbers_1.append(n + 7)
        numbers_1.append(n + 8)
        numbers_1.append(fizz)
        numbers_1.append(buzz)
        numbers_1.append(n + 11)
        numbers_1.append(fizz)
        numbers_1.append(n + 13)
        numbers_1.append(n + 14)

    for overflow in range(len(numbers_1) - 1, iteration - 1, -1):
        numbers_1.pop(overflow)

    t1 = time.time()
    time_method_1 = t1 - t0
    # print(time_method_1)
    # print(numbers_1)

    # Method 2:
    # Create a list 0-n
    # Loop through list in counts of  3 and replace with fizz
    # Loop through list in counts of  5 and replace with buzz
    # Loop through list in counts of 15 and replace with fizzbuzz
    # Touches numbers n + ((9/15) * n) times < 2n

    t0 = time.time()
    for i in range(iteration):
        numbers_2.append(i)

    for n in range(0, len(numbers_2), 3):
        numbers_2[n] = fizz
        # only 1/3 numbers

    for n in range(0, len(numbers_2), 5):
        numbers_2[n] = buzz
        # only 1/5 numbers

    for n in range(0, len(numbers_2), 15):
        numbers_2[n] = fizz + buzz
        # only 1/15 numbers

    t1 = time.time()
    time_method_2 = t1 - t0
    # print(time_method_2)
    # print(numbers_2)

    # Method 3:
    # Create a list 0-n
    # Loop through list and check each number
    # if n % 15 then fizzbuzz
    # otherwise... 3/5 then fizz/buzz respectively
    # Touches numbers 2n times, but performs at most 3 tests each time

    t0 = time.time()
    for i in range(iteration):
        numbers_3.append(i)

    for n in numbers_3:
        if n % 3 == 0:
            numbers_3[n] = fizz
        elif n % 5 == 0:
            numbers_3[n] = buzz
        if n % 3 == 0 and n % 5 == 0:
            numbers_3[n] = fizz + buzz
    t1 = time.time()
    time_method_3 = t1 - t0
    # print(time_method_3)

    # Method 4:
    # Loop through and check each number
    # if n % 15 then append to list fizzbuzz
    # otherwise... 3/5 then fizz/buzz respectively
    # Touches numbers n times, but performs at most 3 tests each time

    t0 = time.time()
    for n in range(iteration):
        if n % 3 == 0 and n % 5 == 0:
            numbers_4.append(fizz + buzz)
        elif n % 3 == 0:
            numbers_4.append(fizz)
        elif n % 5 == 0:
            numbers_4.append(buzz)
        else:
            numbers_4.append(n)

    t1 = time.time()
    time_method_4 = t1 - t0
    # print(time_method_4)

    t0 = time.time()
    for n in range(iteration):
        value = n
        if n % 3 == 0:
            value = fizz
        if n % 5 == 0:
            if isinstance(value, int):
                numbers_5.append(buzz)
            else:
                numbers_5.append(fizz + buzz)
            continue
        numbers_5.append(value)

    t1 = time.time()
    time_method_5 = t1 - t0
    # print(numbers_5)
    # print(time_method_5)

    t0 = time.time()
    for n in range(iteration):
        value = n
        match n % 15:
            case 0:
                numbers_6.append(fizz + buzz)
            case 3:
                numbers_6.append(fizz)
            case 5:
                numbers_6.append(buzz)
            case 6:
                numbers_6.append(fizz)
            case 9:
                numbers_6.append(fizz)
            case 10:
                numbers_6.append(buzz)
            case 12:
                numbers_6.append(fizz)
            case _:
                numbers_6.append(n)

    t1 = time.time()
    time_method_6 = t1 - t0
    # print(numbers_6)
    # print(time_method_6)

    # if numbers_1 == numbers_2 == numbers_3 == numbers_4 == numbers_5 == numbers_6:
    #     print("All the same")
    # De-allocate
    numbers_1 = None
    numbers_2 = None
    numbers_3 = None
    numbers_4 = None
    numbers_5 = None
    numbers_6 = None
    time_score.append([time_method_1, time_method_2, time_method_3, time_method_4, time_method_5, time_method_6])

# quickest = [time_method_1, time_method_2, time_method_3, time_method_4, time_method_5, time_method_6]
# quickest_time = quickest.index(min(quickest)) + 1
# print(f"Method {quickest_time} is the quickest")
with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(time_score)
print(time_score)
