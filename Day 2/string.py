# To check if a certain phrase or character is present in a string, we can use the keyword in.


x = "Gadha"

for i in x:
    print(i)

# Check if "free" is present in the following text:

txt = "The best things in life are free!"
print("free" in txt)

# txt = "The best things in life are free!"

if "free" in txt:
    print("yes")

# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

print("free" not in txt)

if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
