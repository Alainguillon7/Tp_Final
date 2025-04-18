def ranking (rows):
    if rows:
        last_row=rows[-1]
        anio=last_row[1]
        trimestre=last_row[2]
        filtradas = list(filter(lambda row: row[1] == anio and row[2] == trimestre, rows))
        ordenadas = sorted(filtradas, key=lambda row: (row[8], row[0]))
        i = 0
        n = len(ordenadas)
        resultados = {}  # aglomerado -> [hogares_con_2_o_mas, total_hogares]
        while i < n:
            fila = ordenadas[i]
            aglomerado = fila[8]    
            hogares_con_2_o_mas = 0
            total_hogares = 0
            while i < n and ordenadas[i][8] == aglomerado:
                codusu = ordenadas[i][0]
                personas_con_estudios = 0
                pondera = 0
                primer_persona = True
                while i < n and ordenadas[i][8] == aglomerado and ordenadas[i][0] == codusu:
                    if ordenadas[i][29] == 'Superior o universitario':        #poner bien la columna
                        personas_con_estudios += 1
                    if primer_persona:
                        pondera = int(ordenadas[i][9])  # tomamos el pondera una sola vez por hogar
                        primer_persona = False
                    i += 1
                if personas_con_estudios >= 2:
                    hogares_con_2_o_mas += pondera
                total_hogares += pondera
            resultados[aglomerado] = (hogares_con_2_o_mas, total_hogares)
        # Ahora hacemos el ranking
        ranking = []
        for aglo, (con_estudios, total) in resultados.items():
            porcentaje = (con_estudios / total) * 100 if total > 0 else 0
            ranking.append((aglo, porcentaje))
        ranking.sort(key=lambda x: x[1], reverse=True)
        ranking = ranking[:5]
    return ranking
       
    