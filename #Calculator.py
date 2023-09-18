#Calculator
import array
import math
def Check_Numbers(number=str):
    Is_Forbidden = bool
    chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in number: 
        if i in chars:
            Is_Forbidden = False
        else:
            Is_Forbidden = True
            break
    return Is_Forbidden
def Initialize_numbers(Numbers_amount, numbers_array):
    if Numbers_amount == 2:
        print('Input any two numbers')
        for i in range(2):
            number = input()
            if (Check_Numbers(number) == False):
                numbers_array[i] = int(number)
            else:
                while(Check_Numbers(number) == True):
                    print('comrade, You inputted something wrong. Check if there is no literals in your number next time.')
                    number = input()
                numbers_array[i] = int(number)
    elif Numbers_amount == 1:
        print('Input any number')
        number = input()
        if (Check_Numbers(number) == False):
                numbers_array[0] = int(numbers)
        else:
            while(Check_Numbers(number) == False):
                print('comrade, You inputted something wrong. Check if there is no literals in your number next time.')
                number = input()
            numbers_array[0] = int(number)
numbers = [1,1]
while (True):
    print('=============================Our social calculator=============================\nWelcome comrade to our social calculator, which can help you to count how many capitalists have you captured.\nWell, here are all the functions we can do:\r\n1. Find summ of two your numbers two \r\n2. Subtract the first from the second\r\n3. Multiply two numbers\r\n4. Divide the first by the second\r\n5. Raise first number to the N power, where N is second number\r\n6. Find square root of a number\r\n7. Find factorial of your number\r\n8. Find sin of your number\r\n9. Find cos of your number\r\n10. Find tg of your number \r\n11. Exit the programm')
    print('===============================================================================\nNow choose operation to do: ')
    answer = input()
    if(Check_Numbers(answer) == False):
        answerInt = int(answer)
    else:
        print('You inputted wrong value. Comrade, check if there is no literals in your answer\n Press any key to continue')
        input()
        continue
    if answerInt < 6:
        Initialize_numbers(2, numbers)
    elif (answerInt >= 6)and (answerInt <11):
        Initialize_numbers(1, numbers)
    if answerInt == 1:
        print('Here is the sum you wanted to see: ')
        print(numbers[0] + numbers[1])
    elif answerInt == 2:
        print('Here is the substrction you wanted to see: ')
        print(numbers[0] - numbers[1])
    elif answerInt == 3:
        print('Here is the result you wanted to see: ')
        print(numbers[0] * numbers[1])
    elif answerInt == 4:
        if numbers[1] == 0:
            print("You cant actualy divide any number by zero. So try again next time comrade")
            input()
            break
        print('Here is the result you wanted to see: ')
        print(numbers[0] / numbers[1])
    elif answerInt == 5:
        result = 1
        for i in range(1, numbers[1]+1):
            result *=numbers[0]
        print('Here is the your first number power you wanted to see: ')
        print(result)
    elif answerInt == 6:
        print("Comrade, here you can see the square root of your number")
        print(math.sqrt(numbers[0]))
    elif answerInt == 7:
        if numbers[0] >0:
            math.factorial(numbers[0])
        else:
            print("You cant find factorial of negative numbers")
            input()
            break
    elif answerInt == 8:
        print("Comrade, here you can see sin of your number")
        print(math.sin(numbers[0]))
    elif answerInt == 9:
        print("Comrade, here you can see cos of your number")
        print(math.cos(numbers[0]))
    elif answerInt == 10:
        print("Comrade, here you can see tg of your number")
        print(math.tg(numbers[0]))
    elif answerInt == 11:
        print("Good Luck comrade. Go and lead our party to success. Let's build beautiful future together.")
        break
    else:
        print("We cant defintely say what you wanted for real. So at least we an sent you out of here to think and understand what you want. Good Luck comrade. Go and lead our party to success. Let's build beautiful future together.")
        break
    print("Do you want to continue, comrade? (Y/N)")
    continuation = input()
    if continuation == "Y":
        continue
    elif continuation == "N":
        print("Good Luck comrade. Go and lead our party to success. Let's build beautiful future together.")
        break
    else:
        print("We cant defintely say what you wanted for real. So at least we an sent you out of here to think and understand what you want. Good Luck comrade. Go and lead our party to success. Let's build beautiful future together.")
        break