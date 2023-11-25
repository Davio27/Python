# f = open("demofile.txt", "x")

# f = open("demofile.txt", "a")
# f.write("Agora o arquivo tem conteudo.\n")
# f.close()

f = open("demofile.txt", "w", encoding="UTF-8")
f.write("Opa! Sobrescrevi o conteúdo.\n")
f.close()

f = open("demofile.txt", "r", encoding="UTF-8")
print(f.read())
f.close()
