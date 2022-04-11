from http import client


clients = "pablo,\nricardo,\n"


def create_client(client_name):
    global clients
    clients += client_name
    add_comma()


def list_clients():
    global clients
    print(clients)
    



def add_comma():
    global clients
    clients += ",\n"

    
def run ():
    list_clients()
    create_client(input("nombre del cliente nuevo:  "))
    list_clients()



if __name__=="__main__":
    run()