# ---------------------Learn Loop --------------------
for i in range(5):
    env = input("Enter the Envrionment: ")
    print("You enter the Envrionment", env)
    if env == "prod":
        print("Don't Deploy on friday")
    elif env == "stg":
        print("take backup & test well")
    else:
        print("safe to deploy any day")

