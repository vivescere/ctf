import socket

def menu():
	print("______________________")
	print("|       MENU         |")
	print("| 1) see option      |")
	print("| 2) edit option     |")
	print("| 3) connect         |")
	print("______________________")
	
print("""

  ______             __                  __                                             ______  
 /      \           /  |                /  |                                           /      \ 
/$$$$$$  | ________ $$ |   __   ______  $$ |____    ______   _______          _______ /$$$$$$  |
$$ |__$$ |/        |$$ |  /  | /      \ $$      \  /      \ /       \        /       |$$____$$ |
$$    $$ |$$$$$$$$/ $$ |_/$$/  $$$$$$  |$$$$$$$  | $$$$$$  |$$$$$$$  |      /$$$$$$$/  /    $$/ 
$$$$$$$$ |  /  $$/  $$   $$<   /    $$ |$$ |  $$ | /    $$ |$$ |  $$ |      $$ |      /$$$$$$/  
$$ |  $$ | /$$$$/__ $$$$$$  \ /$$$$$$$ |$$ |__$$ |/$$$$$$$ |$$ |  $$ |      $$ \_____ $$ |_____ 
$$ |  $$ |/$$      |$$ | $$  |$$    $$ |$$    $$/ $$    $$ |$$ |  $$ |      $$       |$$       |
$$/   $$/ $$$$$$$$/ $$/   $$/  $$$$$$$/ $$$$$$$/   $$$$$$$/ $$/   $$/        $$$$$$$/ $$$$$$$$/ 
                                                                                                
-----=[Azkaban C2 v.0.0.1 alpha]
""")

def see_option():
	print("_________________________________")
	print("| PIN CODE : " + pin_code + "               |")
	print("| Team Serveur IP : " + teamserver_ip + "|")
	print("| Team Serveur Port : " + teamserver_port + "      |")
	print("_________________________________")
		
def edit_option():
	print("Current option :")
	see_option()
	print("Where option you want to edit ?")
	
	print(" 1) PIN_CODE\n2) TeamServer IP \n3) TeamServer Port ")
	choix = input("Azk-c2 > ")
	choix = str(choix)
	while (True):
		if choix == "1":
			pin_code = input("Azk-c2 | Edit PIN_CODE > ")
			pin_code = str(pin_code)
			print("[+]PIN_CODE : " + pin_code)
			break
			
		elif choix == "2":
			teamserver_ip  = input("Azk-c2 | Edit TeamServer IP > ")
			teamserver_ip = str(teamserver_ip)
			print("[+]TeamServer IP : " + teamserver_ip)
			break
			
		elif choix == "3":
			teamserver_port  = input("Azk-c2 | Edit TeamServer Port > ")
			teamserver_port = str(teamserver_port)
			print("[+]TeamServer Port : " + teamserver_port)
			break
		else:
			print("Error")
	
def connect(pin_code, teamserver_ip, teamserver_port):

	teamserver_port = int(teamserver_port)
	
	clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
	clientSocket.connect((teamserver_ip,teamserver_port));
	clientSocket.send(pin_code.encode());
	dataFromServer = clientSocket.recv(1024);
	print(dataFromServer.decode());
	
	res = input("Azk-c2 > ")
	res = str(res)
	clientSocket.send(res.encode());
	dataFromServer = clientSocket.recv(1024);
	print(dataFromServer.decode());
	
	

while (True):
	menu()
	pin_code = "4785"
	teamserver_ip = "192.168.1.19"
	teamserver_port = "9050"
	teamserver_ip = "144.217.73.235"
	teamserver_port = "26007"
	
	
	choix = input("Azk-c2 > ")
	choix = str(choix)
	if choix == "1":
		see_option()
	elif choix == "2":
		edit_option()
	elif choix == "3":
		connect(pin_code, teamserver_ip, teamserver_port)
	else:
		print("Bad choice, try again")
