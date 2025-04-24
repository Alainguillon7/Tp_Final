from utils import get_indice


def porcentaje (filas):
    values_region = {}

    region = get_indice(filas[0],"REGION")
    ii7 = get_indice(filas[0],"II7")

    for fila in filas[1:]:

        clave = fila[region]
        if clave not in values_region:
            values_region[clave] = {"total": 0, "inquilinos": 0}

        if fila[ii7] == "3":
            values_region[clave]["inquilinos"] += 1
            values_region[clave]["total"] += 1
        else:
            values_region[clave]["total"] += 1

    porcentaje_region = {}

    for region, datos in values_region.items():
        total = datos['total']
        inquilinos = datos['inquilinos']        
        porcentaje_region[region] = (inquilinos / total) * 100 

    return porcentaje_region