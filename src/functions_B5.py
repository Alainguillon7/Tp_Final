from utils import traducir


def get_porcentaje(registro):
    total = 0
    for i in range(1, 8):
        total += registro[str(i)]
    propietarios = registro["1"] + registro["2"]
    return (propietarios * 100) / total


def imprimir_resultado(actual, registro):
    p = get_porcentaje(registro)
    aglomerado = traducir(actual)
    print(f"{aglomerado} : {p:.2f} %")
