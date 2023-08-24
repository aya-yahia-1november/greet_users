import  json
user_name=input("What is the user_name\n")
file_name="user_name.json"
with open(file_name,'r+') as file:
    json.dump(user_name,file)
    print("we will remeber you when you come back "+user_name+"!")