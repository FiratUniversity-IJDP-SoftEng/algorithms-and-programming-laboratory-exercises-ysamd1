# Your Student ID:220543009
# Your Name and Surname:Yaşam Doğa Çevik
numbers = list(range(1, 11))
print("Original list:", numbers)

reversed_numbers = numbers[::-1]
print("Reversed list:", reversed_numbers)

numbers.extend([11, 12, 13])
print("List after adding 11, 12, 13:", numbers)
print("List length:", len(numbers))

numbers.pop(0)  
numbers.pop(-1) 
print("List after removing first and last elements:", numbers)

even_numbers = sorted([num for num in numbers if num % 2 == 0])
print("Sorted list with only even numbers:", even_numbers)
