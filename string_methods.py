# String practice Questions

# 1). input user first name and print its length

firstName = input("Enter your first name: ")

print("Length of Firstname is:", len(firstName))

# 2). find the occurence of "$" in the given string

givenString = "i am a $developer working in $google"

print("Occurrence of $ is at index:", givenString.find("$"))



# String Methods
whoIam = "I am Flutter Developer until now"

print("Ends With:", whoIam.endswith("now"))
# Return new string
print("Capitalize:", whoIam.capitalize())
# tell start index of substring
print("Find:", whoIam.find("Developer"))

# replace substring with new substring
# case sensitive as well
updaetdString= whoIam.replace("until ", "")
print("Replace:", updaetdString.replace("Flutter", "Python"))

# split string into list
print("Split:", whoIam.split(" "))

# repeat string
print("Repeat:", whoIam * 2)

# count substring occurrences
print("Count:", whoIam.count("f"))

# concatenation of strings
str1 = "ahsan"
str2 = "ali"
finalString = str1+str2

# negative slicing
print(str2[-2:])


len1 = len(finalString)

print(len1)

print(finalString)