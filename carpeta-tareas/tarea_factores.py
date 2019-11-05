
def valor_factor(x):
    if x==0:
        return x
    else:
        v=1
        return valor_factor(x)*valor_factor(x-1)


def main():
    n=5
    #valor_factor(5)
    print("el factor es:",valor_factor(n))


main()
    
    
