def recongnize_od_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    


number = recongnize_od_even(3)
print(number)


def nameOfFunction(n):
    if(n <=0):
        return 0
    else:
        return n + nameOfFunction(n-1)
result = nameOfFunction(5)
print(result)






names = ["ahsan", "ali", "hassan", "umer"]

def fun1(var1):
    if(var1 == len(names)):
        return
    print("var1 in fun1:", names[var1])
    fun1(var1 + 1)


fun1(0)

    

print("Before adding name:", names)
def add_name(lst, name):
    new_list = lst.copy()    
    new_list.append(name)
    return new_list
new_names = add_name(names, "zain")
print("After adding name Old List:", names)
print("After adding name New List:", new_names)


def len_of_list(lst):
    print(len(lst))

len_of_list(names)


def print_elements(lst):
    for el in lst:
        print(el,end=" ")


def factorial(n):
    total = 1
    for i in range(1,n+1):
        total *= i
    return total

fac =  factorial(3)
print(fac)  # Output: 6

#recursive factorial
def factorial_by_while(n):
    total = n
    if(n <= 1 ):
        return 1
    total = total * factorial_by_while(n-1)
    return total

fac2 = factorial_by_while(5)
print(fac2)  # Output: 120


def convert_inr_to_usd(inr):
    usd = inr / 82.0
    return usd

inr_amount = 8200
usd_amount = convert_inr_to_usd(inr_amount)
print(f"{inr_amount} INR is equal to {usd_amount} USD")