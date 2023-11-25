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

while (fn >= 2):
    print(f"{fn}! ". format(fn), end='')
    fn = fn-1
    fat = fat*fn
print(f" = {fat}")
print("-----------------------")

while (fatnp>=2):
    print(f"{fatnp}! ". format(fatnp), end='')
    fatnp = fatnp-1
    fanp = fanp*fatnp
print(f" = {fanp}")
print("\n")
div = round(fat/fanp)
print(fat)
print(f"----------------------- = {div}")
print(fanp)

