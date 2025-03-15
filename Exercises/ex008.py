# Your Student ID:220543009
# Your Name and Surname:Yaşam Doğa Çevik

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    spaces = " " * (n - i)  
    stars = "*" * (2 * i - 1)  
    print(spaces + stars) 
