def suma_lista(l):
    if len(l)==1:
        return l[0]
    else:
        actual=l.pop()
        return actual + suma_lista(l)

def main():
    lista=[2,5,9,1,3]
    print(suma_lista(lista))

main()
