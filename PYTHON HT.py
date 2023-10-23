ht=float(input("entrer le prix ht:"))
c=str(input("entrer sa catégorie:"))
match c:
    case"a":
        print("le prix TTC est:",ht+ht*0.07)
    case"b":
        print("le prix TTC est:",ht+ht*0.2)
    case"c":
        print("le prix TTC est:",ht+ht*0.25)
        