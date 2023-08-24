import  json
file_name='user_name.json'
with open(file_name,'r')as file :
    user_name=json.load(file)
    print("Welcome back, "+user_name+"!")