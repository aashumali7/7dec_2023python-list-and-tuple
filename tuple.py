fruits = ('apple',"banana",'''mango''','orange') #this is tuple to store multiple students in one variable


print('Before change')
for fruit in fruits:
    print(f'i like {fruit}')

print("After change") 
fruits[0] = "Grapes" # we can not change the items in tuple
for fruit in fruits: 
    print(f'i like {fruit}')

    