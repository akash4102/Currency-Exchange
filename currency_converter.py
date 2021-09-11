with open("currencydata.txt") as f:
    lines=f.readlines()

Currencydict={}
for line in lines:
    parsed = line.split("\t")
    Currencydict[parsed[0]]=parsed[1]
amount=int(input("enter the amount:\n"))
print("enter the name of the currency you want to convert this amount to? available options:\n")
[print(item) for item in Currencydict.keys()]
currency=input("please enter one of the values\n")
print(f"{amount} INR is equal to {amount *float(Currencydict[currency])} {currency}")