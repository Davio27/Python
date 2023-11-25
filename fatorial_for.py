print("\n")
print("     N !")
print("----------=")
print(" ( N - P ) !")

print("\n")

fn = int(input("Digite o valor de N: \n"))
fp = int(input("Digite o valor de P: \n"))

fat  = fn
fatnp = (fn - fp)
fanp = fatnp

print(f"     {fn} ! ")
print("--------------- = ")
print(f" ( {fn} - {fp} ) !\n")

for n in range(fn, 1, -1):
    print(f"{fat}! ", end='')
    fat -= 1


print("\n---------------------")

for p in range(fatnp, 1, -1):
    print(f"{fatnp}! ", end="")
    fatnp=fatnp-1
print("\n")



# while (fatnp>=2):
#     print(f"{fatnp} !")
#     fatnp = fatnp-1
#     fanp = fanp*fatnp
# print(f" = {fanp}")
# print("\n")
# div = fat/fanp
# print(fat)
# print(f"----------------------- ={div}")
# print(fanp)



# print('=-=-=Factorial in python=-=-=')
# num1 = int(input('Input a Number: '))
# factorial = num1
# sumfactor = 1
# print(f'O cálculo do fatorial é {num1}! = ', end= " ")
# for count in range(num1, 0, -1):
#     print(f'{factorial}', end= " ")
#     sumfactor = sumfactor * factorial
#     factorial -= 1
#     if factorial >= 1:
#         print(' X ',end= " ")
#     else:
#         print('=', end= " ")
# print(sumfactor)