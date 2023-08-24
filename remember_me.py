import  json



def get_stroed_user_name():
    file_name="user_name.json"
    try:
        with open(file_name) as  file:
            user_name=json.load(file)

   except FileNotFoundError:
        return None

  else:
      return user_name




def greet_users():
    user_name=get_stroed_user_name()
    if user_name:
        print("welcome back , "+user_name+' !')


    else:
        user_name=input("What is your name ?")
        file_name='user_name.json'
        with open(file_name,'w')as file :
            json.dump(user_name,file)
            print("we will remember you when you came back" + user_name + " !")
greet_users()