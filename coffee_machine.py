menu={
    "cappuccino":{
    "ingredients":{
        "water":60,
        "milk":30,
        "coffee":20,

    },
    "cost":120
    },
    "choclate":{
        "ingredients":{
            "water":50,
            "coffee":20,        
            },
        "cost":100
    },
    "espreso":{
        "ingredients":{
            "water":55,
            "coffee":25,        
            },
        "cost":70
    }
    
}
profit=0
resources={
    "water":500,
    "milk":300,
    "coffee":200,
}
def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print(f"sorry...!! there is no {item}")
            return False
        return True
def process_coins():
    print("please insert coins (only Rs 5, RS 10, Rs 20 are accepted)")
    total=0
    coins_five=int(input("how many 5 rs coins"))
    coins_ten=int(input("how many 10 rs coins"))
    coins_twenty=int(input("how many 20 rs coins"))
    total=coins_five*5+coins_ten*10+coins_twenty*20
    return total
def is_payment(money_received,coffee_cost):
    if money_received>=coffee_cost:
        global profit
        profit+=coffee_cost
        change=money_received-coffee_cost
        print(f"here is your change{change}.")
        return True
    else:
        print("sorry thats not enough money. money refunded")
        return False
def make_coffe(coffe_name,coffee_ingredients):
    for item in coffee_ingredients:
        resources[item]-=coffee_ingredients[item]
    print(f"Here is your {coffe_name}  thank you....")
is_on=True
while is_on:
    choice=input("what would you like to have (espreso/cappuccino/chocolate)")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"water = {resources['water']} ml")
        print(f"milk = {resources['milk']} ml")
        print(f"coffee = {resources['coffee']} g")
        print(f"money = Rs {profit}")
    else:
        coffe_type=menu[choice]
        print(coffe_type)
        if check_resources(coffe_type['ingredients']):
            payment=process_coins()
            if is_payment(payment,coffe_type['cost']):
                make_coffe(choice,coffe_type['ingredients'])

