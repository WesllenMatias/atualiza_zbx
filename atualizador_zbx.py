import os
import subprocess
import datetime
from time import sleep
import platform
from pathlib import Path
from shutil import copy
import config

print ("\033[41;1;37m"+"                                      Atualização do Zabbix                                      "+"\033[0;0m")
print ("\n -> Resumo de Informações Sobre o Sistema Operacional:\n")
sistema = platform.system()
if sistema == 'Linux':
    so = os.system('lsb_release -a')
    print(so)
else:
    so = platform.system()
    versao = platform.version().split()
    print ("Sistema Operacional: " + so)
    print ("Versão: "+ versao[0])

# Testando se existe o a Pasta de backup
pasta = Path("./backup_zbx/")
exist_pasta = pasta.exists()

if exist_pasta == True:
    print ("\n -> Diretório de Backup Criado    \033[01;32mOK\033[00;37m\n")
else:
    os.mkdir("backup_zbx")
    print ("\n -> Criando diretório de Backup...\n")
    sleep(3)
    print (" -> Diretório de Backup Criado    \033[01;32mOK\033[00;37m\n")

print ("\n -> Arquivos a Serem Backupeados:")
arquivo1 = "/etc/zabbix/zabbix_server.conf"
arquivo2 = "/etc/zabbix/zabbix_agentd.conf"
obj1 = Path(arquivo1)
server_conf = obj1.is_file()
obj2 = Path(arquivo2)
agent_conf = obj2.is_file()

if server_conf == False:
    print("\n* zabbix_server.conf....\033[05;31mNão Encontrado\033[00;37m")
else:
    print("\n* zabbix_server.conf....\033[01;32mOK\033[00;37m")

if agent_conf == False:
    print("* zabbix_agentd.conf....\033[05;31mNão Encontrado\033[00;37m ")
else:
    print("* zabbix_agentd.conf....\033[01;32mOK\033[00;37m")


diretorio1 = "/usr/sbin/zabbix_server"
diretorio2 = "/usr/share/zabbix/"
obj3 = Path(diretorio1)
zbx_srv = obj3.is_file()
obj4 = Path(diretorio2)
zbx_share = obj4.exists()
if zbx_srv == False:
    print("* /usr/sbin/zabbix_server....\033[05;31mNão Encontrado\033[00;37m")
else:
    print("* /usr/sbin/zabbix_server....\033[01;32mOK\033[00;37m")

if zbx_share == False:
    print("* /usr/share/zabbix....\033[05;31mNão Encontrado\033[00;37m")
else:
    print("* /usr/share/zabbix....\033[01;32mOK\033[00;37m")


print ("\n -> Backup dos Arquivos: \n")
sleep(3)
print (" -> Copiando Arquivos...\n")
sleep(1)
try:
    orig_srv = "/etc/zabbix/zabbix_server.conf"
    destino = "./backup_zbx/"
    orig_agent = "/etc/zabbix/zabbix_agentd.conf"
    copy(orig_srv, destino)
    copy(orig_agent, destino)
    print(" -> Backup de Arquivos Finalizado....\033[01;32mOK\033[00;37m \n")
except Exception as erro:
    print("Não Foi possivel copiar os Arquivos\nErro: {}".format(erro.__class__))


    #mysqldump -u root -p Z@bb1x > /root/backup-zabbix/bkpzabbix.sql
    print("\n -> Realizando Dump do Banco dentro da Pasta de Backup\n")
    sleep(5)
    dump_db = "mysqldump -u" + config.usr_db + " -p " + config.host_db + " > "+ destino
try:
    bkp = os.system(dump_db)
    if bkp == True:
        print("\n -> Dump do Banco de dados....\033[01;32mOK\033[00;37m")
    else:
        pass
except Exception as erro:
    
    print ("\n -> Dump do Banco de dados....\033[05;31m Falhou!!!\033[00;37m")
    print ("\nProblemas ao se conectar ao Banco de dados para realizar o Backup, verifique se este é o servidor onde se encontra o banco do zabbix")
    
print ("\033[41;1;37m"+"                                                                                                 "+"\033[0;0m")

