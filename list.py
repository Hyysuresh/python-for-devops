#_______________________________________________
            # LIST METHODS 1
a =[ 200, 400, "hello", "world", 300.0, True]
# print type of a
print(type(a))
# print all elements
print(a)
# index 3th element
print(a[3])
# starting from the end, 2nd element
print(a[-2])
# elements from index 1 to 3
print(a[1:4])
# elements from start to index with step 3
print(a[::3])
# elements from index 4 to end
print(a[4::])
# elements from start to index 4 with step 2
print(a[::-5])
# elements from index -4 to end
print(a[-4::])
# length of the list
print(len(a))

# add elements 500, 600 at the end of the list
print(a + [500, 600])
# remove "hello", 1st index element
a.remove("hello")
a.pop(1)
# add "java", "python" at index 2 and 3
a.insert(2, "java")
a[3] = "python"
# delete all elements from the list
a.clear()
print(a)
#_______________________________________________
             # USE OF SORT FUNCTION IN LIST

# create  a list of numbers
numbers = [5, 2, 9, 1, 4, 6, 3]
# sort the list in ascending order
numbers.sort()
print(numbers)
# sort the list in descending order
numbers.sort(reverse=True)
print(numbers)
# sort the list in ascending order again
numbers.sort(reverse=False)
print(numbers)

Name = ["suresh", "anil", "ravi", "kumar", "zara"]
# sort the list based on length of each name
Name.sort(key=len)
print(Name)
# sort the list based on length of each name in descending order
Name.sort(key=len, reverse=True)
print(Name)

words = [{"name": "suresh", "age": 25}, {"name": "anil", "age": 20}, {"name":"ravi", "age": 30}]
# sort the list based on age
words.sort(key=lambda x: x["age"], reverse=True)
print(words)

#_______________________________________________
            # LIST METHODS 2                    

cloud = list()
# add elements to the list
cloud.append("AWS")
cloud.append("Azure")
cloud.append("GCP")
cloud.append("Oracle Cloud")
cloud.append("IBM Cloud")
cloud.append("Alibaba Cloud")
cloud.append("utto Cloud")
# print all elements
print(cloud)
# length of the list
print("NUMBER OF CLOUD PROVIDERS:", len(cloud))
# index 2nd element
print("WORLD NUMBER 1 CLOUD PROVIDER:", cloud[0])
# last element
print("INDIAN CLOUD PROVIDER:", cloud[-1])
# elements from index 1 to 3
print((cloud)[1:4])
# count occurrences of "AWS"
print("AWS COUNT:", cloud.count("AWS"))

# _____________________________________________________
#      USE FOR AND IF IN LISTS

cloud = ["AWS", "Azure", "GCP", "Oracle Cloud", "IBM Cloud", "Alibaba Cloud", "utto Cloud"]

for i in cloud:
    if i == "AWS":
        print("WORLD NUMBER 1 CLOUD PROVIDER:", i)
    elif i == "utto Cloud":
        print("INDIAN CLOUD PROVIDER:", i)


# _______________________________________________

sweets = ["Gulab Jamun", "Rasgulla", "Jalebi", "Barfi", "Ladoo", "Kheer"]
for i in sweets:
    print(f"Adding {i} to the list of favorite sweets.")
print("\nFinished adding sweets to the list!")

#________________________________________________________

numbers = [2, 3, 5, 6, 8, 12, 15, 24, 54, 76, 67, 45, 34]

even_number = []
old_number = []
print("-" * 20)

for i in numbers:
    if i % 2 == 0:
        print(f"{i} is enven number, adding the even list")
        even_number.append(i)

    else:
        print(f"{i} is old number, adding the old list")
        old_number.append(i)
print("-" * 20)
print("finshing your even and old numbers...")
print("Even Numbers = ",even_number)
print("Old Numbers = ",old_number)

print("🤫" * 20)