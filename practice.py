# Basics practice

#print("+++++ Are 2 numbers equal? +++++")
#
#num1 = int(input("Enter a number . . . "))
#num2 = int(input("Enter another number . . . "))
#print("[", num1, "+", num2, "]", "=", num1 + num2)
#
#if num1 == num2: print(num1, " and ", num2, " are equal!")
#else: print(num1, "and", num2, " are not equal!")

#print("+++++ Is an integer divisible by 5? +++++")
#
#number = int(input("Enter a number . . . "))
#original_number = number 
#number = number % 5
#if (number % 5) == 0: print(original_number, " is divisible by 5!")
#else: print(original_number, " is not divisible by 5!")

#print("+++++ Sum of all list elements +++++")
#list = [563.66, 33, 5000]
#print("List length:", len(list))
#def sum_of_all_list_items(): 
#    print(list[0] + list[1] + list[2])
#sum_of_all_list_items()

#print("+++++ Sum of all list elements v2 +++++")
#list = []
#max_length = 4
#while len(list) < max_length:
#    item = int(input("Enter a number . . . "))
#    list.append(item)
#    print(list)
#sum_of_list = sum(list)
#sum_of_list = str(sum_of_list)
#list = str(list)
#print(list.replace(',', ' +').replace('[', '').replace(']', ''), "=", sum_of_list)

#print("+++++ 2 makes 10 +++++")
## take 2 arguments and return True if one is 10 or if both are a sum of 10
#a = input("Enter a number . . .")
#b = input("Enter a second number . . .")
#c = a+b
#if (a, b == 10) or (c == 10): print("True")

#print("+++++ Check if 2 strings are of equal length +++++")
#list = []
#max_len = 2
#while len(list) < max_len: 
#    item = input("Enter a string . . . ")
#    list.append(item)
#    print(list)
#if len(list[0]) == len(list[1]): print(list[0], "and", list[1], "are of equal length!")
#else: print(list[0], "and", list[1], "are not of equal length!")

#print("+++++ Random Int Gen +++++")
#import random 
#random_int = random.randint(1, 1000)
#print(random_int)
#restart = input("Print another random number? [Y/N]")
#print("Restart[Y/N] =", restart)
#while restart == "Y":
#    random_int = random.randint(1, 1000)
#    print(random_int)
#    restart = input("Print another random number? [Y/N]")
#    if restart == "N":
#        print("Restart[Y/N] =", restart)
#        break
#print("Random num gen end")

#print("+++++ Random Int Gen v2 +++++")
#import random 
#random_int = random.randint(1, 1000)
#print(random_int)
#print("[+] Yes, Generate another random number please [Y]")
#print("[-] No, Please do not generate another random number, please! [N]")
#restart = input(". . . ")
#print("Restart[Y/N] =", restart)
#while restart == "Y":
#    random_int = random.randint(1, 1000)
#    print(random_int)
#    print("[+] Yes, Generate another random number please [Y]")
#    print("[-] No, Please do not generate another random number, please! [N]")
#    restart = input(". . . ")
#    if restart == "N":
#        print("Restart[Y/N] =", restart)
#        break
#print("=====END OF RINTGEN=====")

#print("+++++ Basic User input + while loop +++++")
#a = input("Enter a Y or N...")
#print(a)
#
#while a == "Y":
#    print("YES")
#    a = input("Enter a Y or N...")
#    print(a)
#else:
#    print("idk")

#print("+++++ Age to Years ++++++")
#age = int(input("Enter your age . . . "))
#days_in_one_year = 365
#age_to_years = age * days_in_one_year
#print(age, "years =", age_to_years, "Days")

#print("+++++ Print - Pattern * +++++")
#number_of_rows = int(input("Enter  number of rows . . . "))
#number_of_columns = int(input("Enter numer of columns . . . "))
#for i in range(number_of_rows):
#    for j in range(number_of_columns):
#        print("* ",end="")
#    print()
#    number_of_columns -= 1

#>> 
#***
#**
#*
