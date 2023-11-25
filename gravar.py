arquivo=open("arqtext.text", 'w')

arquivo.write('curso python, essa função e para escrever\n')
arquivo.write('voce pode pular linha para escrever tambem, mas tem que repetir a função')
arquivo.close()

# leitura do arquivo de texto

leitura=open("arqtext.text", 'r')
print(leitura.read())
leitura.close()