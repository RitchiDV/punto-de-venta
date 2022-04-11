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

    
def run():
    print("lista antigua: ")
    list_clients()
    create_client(input("nombre del cliente nuevo:  "))
    print("**lista actualizada**")
    list_clients()



if __name__=="__main__":
    run()