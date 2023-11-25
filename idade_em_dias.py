idade = int(input())

anos = idade // 365
idade %= 365

meses = idade // 30
idade %= 30

dias = idade

# print(f"""      {anos} ano(s)
#       {meses} mes(es)
#       {dias} dia(s)""")

if anos:
    print(f"{anos} ano(s)")
    
if meses:
    print(f"{meses} mes(es)")
    
if dias:
    print(f"{dias} dia(a)")