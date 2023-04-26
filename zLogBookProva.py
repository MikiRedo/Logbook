
import json

#funcio per inicialitzar el logbook

def load_logbook(logBook):
    with open("LB.json", "r") as f:
        logBook = json.load(f)
    return logBook


#funcio per guardar cada encadene al logbook

def save_logbook(logBook):
    with open("LB.json", "w") as f:
        json.dump(logBook, f, indent=2)
        f.write("\n")


#funcio per demanar les dades del encadene i afegirles al logbook

def add_encadene(logBook):
    encadene = {}
    encadene["Nom"] = input("Afegeix el nom de la via: ")
    encadene["Grau"] = input("Afegeix el grau de la via: ")
    if encadene["Grau"] == "7c":
        print("SUUUU per fi!!")
    encadene["Lloc"] = input("Afegeix la localització: ")
    encadene["Data"] = input(str("Afegeix la data (format 00/00/0000): "))

    logBook.append(encadene)


#funcions per filtrar en cas que es vulgui

def filtrarGrau(logBook):
    grade = input("Quin grau busques?: ")
    grauFiltrat = [entry for entry in logBook if entry.get("Grau") == grade]
    if grauFiltrat:
        for entry in grauFiltrat:
            print(entry)
    else:
        print("No hi ha res aquí")

def filtrarNom(logBook):
    nom = input("Quin nom busques?: ")
    nomFiltrat = [entry for entry in logBook if entry.get("Nom") == nom]
    if nomFiltrat:
        for entry in nomFiltrat:
            print(entry)
    else:
        print("No hi ha res aquí")


#funcio main

def main():
    print("You man, has encadenat eh! Afegeix la teva medalla Pokemon :)")
    logBook = load_logbook("LB.json")
    linies = int(input("Quants encadenes avui tet?: "))
    if linies == 0:
        print("Bajonazo :(")
    else:
        for i in range(int(linies)):
            add_encadene(logBook)
    save_logbook(logBook)

    filtrar = input("Vols buscar algo? Grau / Nom / res: ")
    if filtrar == "Grau":
        filtrarGrau(logBook)
    elif filtrar == "Nom":
        filtrarNom(logBook)
    else:
        print("weke")

if __name__ == '__main__':
    main()



#com puc explicar que 7c va primer que 7b+, 7b...

