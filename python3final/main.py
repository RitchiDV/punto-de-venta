clients = "ricardo, \npablo, \nlalo, "
#________________________________________________________________________________
def _print_welcome():
    print(''' WELCOME TO PUNTO DE VENTAS IN MEXICO''')
    print("*"*50)
    print ("what would you like to do today")
    print("(L) list clients")
    print("(c) create client")
    print("(D) delete client")
    print("(U) update client")
    print("(S) search client")

#________________________________________________________________________________
def list_clients():
    global clients
    print(clients)
    

#________________________________________________________________________________

def add_comma():
    global clients
    clients += ",\n"

#_______________________________________________________________________________
def create_client(client_name):#creacion de nuevo cliente
    global clients
    if client_name not in clients:
        #si cliente no esta en clients entonces se agrega client_name a clients
        clients += client_name
        add_comma()
    else:
        print("client already is in  the clients list")

#_____________________________________________________________________________________
def update_client(client_name,new_update):
    global clients
    
    if client_name in clients:
        #si cliente esta en clients entonces se remplasa client_name por el segundo parametro new_update
        clients = clients.replace(client_name + ",", new_update+",")
        #y su no esta en client 
    else:
        print("client is not in clients list")
#______________________________________________________________________________
def delete_client(client_name):
    global clients
    if client_name in clients:# si client name esta en client entonces
        clients = clients.replace(client_name +",","")#clients remplasa (clients_name por, "" un string vasio)
    else:
        print("client is not in clients list")
#_________________________________________________________
def search_clients(client_name): 
    global clients
    list_clients = clients.split(",")

    for clients in list_clients: # no me imprime los siogientes nombres solo el primero        
                   #error aqui ... falta solucionar....
        if clients != client_name:
            continue
        else:
            return True
#_________________________________________________________________________--


def pidiendo_datos():

    opcion =input()
    opcion = opcion.upper()#por si el usuario escribe un string miniscula el upper lo hace mayuscula (evitando error)

#_____________________________________________________________________________
    if opcion == "C":
        client_name = (input("what is the client name?:  "))#primer parametro de la funcion create_client
        create_client(client_name)#funcion

#_____________________________________________________________________________
    elif opcion == "L":
        list_clients()
        
#_____________________________________________________________________________
    elif opcion == "D":
        client_name =input("whats is client delete?:  ")#parametro de delete_client 
        delete_client(client_name)#funcion con el parametro 

#_____________________________________________________________________________
    elif opcion == "U":#actualiza y borra nombre anterior.
        client_name = (input("what is the client name?:   "))#primer parametro  de la funcion update_client
        new_update = input("what is the update client name?:   ")#segundo parametro de la funcion update_client
        update_client(client_name,new_update)#funcion y sus parametros 1 y 2
        # list_clients()#lista de clientes
#______________________________________________________________________________
    elif opcion == "S":
        client_name=input("what is search name?:   ")
        result =search_clients(client_name)
        if result:
            print("the clients is in  the clients list")
        else:
            print("the client: {} is not in  our clients list".format(client_name))   


#______________________________________________________________________________

    else:
        print("opcion incorrecta")
#_______________________________________________________________________________




#*************************************************************  
def run():


    _print_welcome()#bienvenida a la app con sus opciones de menu


    pidiendo_datos() #se pide al usuario  el nombre del cliente  segun la opcion C or D and U.


    print("*"*50)# un plus


    print("**lista actualizada**")
    list_clients()



if __name__=="__main__":
    run()
#******************************************************************