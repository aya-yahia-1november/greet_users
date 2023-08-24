import  json
file_name="numbers.json"
with open(file_name,'r') as file :
    numbers=json.load(file)
print(numbers)