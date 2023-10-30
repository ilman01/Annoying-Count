import random

def generate_random_numbers_sum_to_integer(n, max_attempts):
    result = []
    attempts = 0

    while n != 0 and attempts < max_attempts:
        # Generate a random decimal number between -n and n
        rand_num = random.uniform(-1000, 1000)

        # Round it to two decimal places
        rand_num = round(rand_num, 2)

        # Append it to the result
        result.append(rand_num)

        # Update the remaining sum
        n -= rand_num

        attempts += 1

    return result

# Input: An integer
user_input = int(input("Enter an integer: "))
length_input = input("Enter length (How many + and -, default 100 if empty): ")
if length_input == "":
    length_input = 100
else:
    length_input = int(length_input)


def repeat():

    random_numbers = generate_random_numbers_sum_to_integer(user_input, max_attempts=length_input)


    fix = round(user_input - sum(random_numbers),3)

    temp = ""
    i = 0
    for number in random_numbers:
        if str(number)[0] == "-":
            temp = temp + str(number)
        elif i == 0:
            temp = temp + str(number)[0:]
        else:
            temp = temp + "+" + str(number)
        i = i + 1
    if str(fix)[0] == "-":
        temp = temp + str(fix)
    else:
        temp = temp + "+" + str(fix)

    #print(temp)
    return fix,temp


repeatt = repeat()
nice_number = repeatt[0]
res = repeatt[1]

count = 0

while nice_number > 1000 or nice_number < -1000:
    if count > 1000:
        break
    
    repeatt = repeat()
    nice_number = repeatt[0]
    res = repeatt[1]
    count = count + 1
    print(f"Finding nice number... x{count}", end="\r")

count = 0

print(res)


