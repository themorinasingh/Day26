list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
#converting list of strings to list of numbers via list comprehension
numbers = [int(num) for num  in  list_of_strings]
#print(numbers)
#adding even numbers to result using list comprehension
result = [num for num in numbers if num %2 == 0 and num > 0]
print(result)

#Note they want 0 to be in the list of numbers