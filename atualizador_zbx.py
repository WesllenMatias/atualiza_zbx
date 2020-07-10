import os
import subprocess
import datetime
from time import sleep
import platform
from pathlib import Path

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

print ("\n -> Arquivos a Serem Backupeados:\n")
arquivo1 = "/usr/zabbix/zabbix_server.conf"
arquivo2 = "/usr/zabbix/zabbix_agentd.conf"
obj1 = Path(arquivo1)
server_conf = obj1.is_file()
obj2 = Path(arquivo2)
agent_conf = obj2.is_file()

if server_conf == False:
    print("\n* zabbix_server.conf    \033[05;31mNão Encontrado\033[00;37m")
else:
    print("\n* zabbix_server.conf    \033[01;32mOK\033[00;37m")

if agent_conf == False:
    print("* zabbix_agentd.conf    \033[05;31mNão Encontrado\033[00;37m ")
else:
    print("* zabbix_agentd.conf    \033[01;32mOK\033[00;37m")


diretorio1 = "/usr/sbin/zabbix_server"
diretorio2 = "/usr/share/zabbix/"
obj3 = Path(diretorio1)
zbx_srv = obj3.is_file()
obj4 = Path(diretorio2)
zbx_share = obj4.is_file()
if zbx_srv == False:
    print("* /usr/sbin/zabbix_server    \033[05;31mNão Encontrado\033[00;37m")
else:
    print("* /usr/sbin/zabbix_server    \033[01;32mOK\033[00;37m")

if zbx_share == False:
    print("* /usr/share/zabbix    \033[05;31mNão Encontrado\033[00;37m")
else:
    print("* /usr/share/zabbix    \033[01;32mOK\033[00;37m")





print ("\033[41;1;37m"+"                                                                                                 "+"\033[0;0m")

