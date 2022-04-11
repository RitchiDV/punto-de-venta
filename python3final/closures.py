from timeit import repeat


def make_repeater_of(n):
    def repeater (string):
        assert type(string) == str ,"solo puedes ultilizar cadenas"
        #assert type(string) == str,
        #afirmamos que lo que llege a string tiene que ser str o si no 
        #te devuelve error  " solo puedes ultilisar cadena de tipo string"
        return string * n
    return repeater

def run():
    repeat_5 = make_repeater_of (5)
    print (repeat_5(input("escriba una cadena de tipo string:  "))) 
    repeat_10 = make_repeater_of(10)
    print(repeat_10("ricardo"))

if __name__=="__main__":
    run()