import pandas as pd 


# Alias import pandas as pd 

# Series 

a = [1, 2, 3, 4]

myvar = pd.Series(a)
print(myvar)


# Labels

print(myvar[0])
print(myvar[2])
print("###############")

# create labels

myvar = pd.Series(a, index = ["a", "b", "c", "d"])
print(myvar)

print(myvar["c"])
print("##################")


# Key/value objects in series

food = {"protein": "Meat", "vegetables": "spinach"}

calories = {"day1": 230, "day2": 400, "day3": 630}

calories_converted = pd.Series(calories)
print(calories_converted)

print(calories_converted["day1"])
print("############################")


# Dataframes

data = {
    "calories":[100, 200, 300], 
    "duration": [5, 10, 15]
}

myvar = pd.DataFrame(data)

print(myvar)