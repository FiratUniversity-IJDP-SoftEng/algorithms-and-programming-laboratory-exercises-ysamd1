# Your Student ID:220543009
# Your Name and Surname:Yaşam Doğa Çevik

conversion_type = input("Choose conversion (C to F / F to C): ").strip().upper()

temperature = float(input("Enter the temperature value: "))

if conversion_type == "C TO F":
    converted = (temperature * 9/5) + 32
    print(f"{temperature}°C is equal to {converted:.2f}°F")

elif conversion_type == "F TO C":
    converted = (temperature - 32) * 5/9
    print(f"{temperature}°F is equal to {converted:.2f}°C")

else:
    print("Invalid conversion type! Please enter 'C to F' or 'F to C'.")
