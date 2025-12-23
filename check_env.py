env = input("Enter the Envrionment : ") #input user info.
print ("your envrionment is :", env) 

# Conditional statement
if env == "prod":
    print("Don`t Deploy on friday")
elif env == "stg":
    print("take  backup & Test well")

else:
    print("Safe to deploy any day")
