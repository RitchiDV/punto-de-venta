from http import client
from re import U


clients = "pablo,\nricardo,\n"

def _print_welcome():
    print(''' WELCOME TO PUNTO DE VENTAS IN MEXICO''')
    print("*"*50)
    print ("what would you like to do today")
    print("(c) create client")
    print("(D) delete client")
    print("(U) update client")


def list_clients():
    global clients
    print(clients)
    



def add_comma():
    global clients
    clients += ",\n"


def create_client(client_name):#creacion de nuevo cliente
    global clients
    if client_name not in clients:
        #si cliente no esta en clients entonces se agrega client_name a clients
        clients += client_name
        add_comma()
    else:
        print("client already is in  the clients list")

 
def update_client(client_name,new_update):
    global clients
    
    if client_name in clients:
        #si cliente esta en clients entonces se remplasa client_name por el segundo parametro new_update
        clients = clients.replace(client_name + ",", new_update+",")
        #y su no esta en client 
    else:
        print("client is not in clients list")



def pidiendo_datos():

    opcion =input()
    opcion = opcion.upper()#por si el usuario escribe un string miniscula el upper lo hace mayuscula (evitando error)

#-------------------------------------------------------------------
    if opcion == "C":
        client_name = (input("what is the client name?:  "))#primer parametro de la funcion create_client
        create_client(client_name)#funcion

#-------------------------------------------------------------------
    elif opcion == "D":
        pass

#---------------------------------------------------------------------
    elif opcion == "U":#actualiza y borra nombre anterior.
        client_name = (input("what is the client name?:   "))#primer parametro  de la funcion update_client
        new_update = input("what is the update client name?:   ")#segundo parametro de la funcion update_client
        update_client(client_name,new_update)#funcion y sus parametros 1 y 2
        # list_clients()#lista de clientes
#---------------------------------------------------------------------

    else:
        print("opcion incorrecta")
#----------------------------------------------------------------------




#*************************************************************  
def run():


    _print_welcome()#bienvenida a la app con sus opciones de menu

    print("lista antigua: ")
    list_clients()


    pidiendo_datos() #se pide al usuario  el nombre del cliente  segun la opcion C or D and U.


    print("*"*50)# un plus


    print("**lista actualizada**")
    list_clients()



if __name__=="__main__":
    run()
#******************************************************************