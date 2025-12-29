info = {
    "name" : "Suresh",
    "age" : 20,
    "city" : "Ajmer",
    "qualification": "BSc",
    "salary" : 50000,
    "married" : False,
    "favourites" : ["cricket", "tennis", "listening music"]
}
print(type(info))
# print all key-value pairs
print(info)
# print value of key 'city'
print("i live in", info["city"])
# print value of key 'favourites'
print("my favourites", info["favourites"])
# print 2nd element from favourites
print("my 2nd favourites is", info["favourites"][1])
# add new key-value pair 'hobbies'
info["hobbies"] = ["reading", "traveling"]
print("my hobbies are", info["hobbies"])
# update value of key 'salary'
info["salary"] = 60000
print(info)
# remove key 'married'
info.pop("married")
print(info)
# length of the dictionary
print("length of dictionary is", len(info))
# print all keys
print("all keys are", info.keys())
# print all values
print("all values are", info.values())
# print all key-value pairs
print("all key-value pairs are", info.items())
# delete all elements from the dictionary
info.clear()
print(info)
# setdefault example
info.setdefault("name", "Suresh")
info.setdefault("age", 20)
print(info)
# get example
print("i am", info.get("age"), "years old")
print("i love", info.get("favourites"))
print(info)
# update example
info.update({"city": "jaipur"})
print(info)