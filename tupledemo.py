ir=(0.10,0.44,0.80)
for data in ir:
    print(data)

#ir.append(0.90)
for data in ir:
    print(data)

#combination
customer=[48548,"Anoop",("3/4/1980","5/6/2001")]
customer.append(4386584326)
for cust in customer:
    #print(type(cust))

    if (type(cust) is tuple):
        print(cust)
