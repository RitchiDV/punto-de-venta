from http import client


CLIENTS = "pablo,\nricardo,\n"

def _print_welcome():
    print(''' WELCOME TO PUNTO DE VENTAS IN MEXICO''')
    print("*"*50)
    print ("what would you like to do today")
    print("(c) create client")
    print("(D) delete client")


def list_clients():
    global CLIENTS
    print(CLIENTS)
    



def add_comma():
    global CLIENTS
    CLIENTS += ",\n"


def create_client(client_name):
    global CLIENTS
    if client_name not in CLIENTS:
        CLIENTS += client_name
        add_comma()
    else:
        print("client already is in  the clients list")



def pidiendo_datos():
    opcion =input()
    if opcion == "C":
        client_name = (input("what is the client name?:  "))
        create_client(client_name)
    elif opcion == "D":
        pass
    else:
        print("opcion incorrecta")





#*************************************************************  
def run():


    _print_welcome()#bienvenida a la app con sus opciones de menu

    print("lista antigua: ")
    list_clients()


    pidiendo_datos() #se pide al usuario  el nombre del cliente  segun la opcion C or D.


    print("*"*50)# un plus


    print("**lista actualizada**")
    list_clients()



if __name__=="__main__":
    run()
#******************************************************************