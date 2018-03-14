#multiple assignments

basicData=Summary=357867
print(basicData)
print(Summary)

#for loop
import random
for num in range(1,10):
    genData=random.randint(1,100)
    if(genData>50):
        print(genData,end="\t")

#conversions
#binary number
print("\n",bin(17))
#decimal number
print(int('1010',2))
#octal number
print(oct(59))
#hex format
print(hex(255))
#complex Number
print(complex(67,78))
