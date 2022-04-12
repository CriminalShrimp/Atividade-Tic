import os 
import datetime
import stat
#Faz a verificação se arquivo ja existe 
if os.path.isfile("permissao.txt"):
  print("Este arquivo ja foi criando")
  os.chmod("permissao.txt", stat.S_IRWXU)#Leitura, escrita e execução pelo proprietário caso o aruqivo ja exista 
#adiquiri a data atual 
datetime.datetime.now()
datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)

texto = ("Data:" + str(datetime.datetime.now()))
arquivo = open('permissao.txt','a') #stat.S_IWUSR talvez pra linux 
os.chmod("permissao.txt",stat.S_IWUSR)
arquivo.seek(0)
arquivo.write(texto + '\n')
os.chmod("permissao.txt", stat.S_IRUSR)
arquivo.close()