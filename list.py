fruits = ['apple',"pineapple",'''mango''','strawberry',]#this is list


print('Before change')
for fruit in fruits:
    print(f'i like {fruit}')
    
print("After change") 
fruits[0] = "Watermelon" # the list is changeable 
for fruit in fruits: 
    print(f'i like {fruit}')