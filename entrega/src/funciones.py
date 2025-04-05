def calcular_puntos(kills, assists, deaths, puntos):
    return kills * puntos['kill'] + assists * puntos['assist'] + deaths * puntos['death']# calculo los puntos utilizando los valores que le pase en el main

def procesar_ronda(round_data, players, puntos):
    round_scores = {} #creo un diccionario para guardar las estadisticas
    
    for player, stats in round_data.items():
        kills = stats['kills']
        assists = stats['assists']
        deaths = 1 if stats['deaths'] else 0
        
        points = calcular_puntos(kills, assists, deaths, puntos)
        
        if player not in players:
            players[player] = {'kills': 0, 'assists': 0, 'deaths': 0, 'mvps': 0, 'points': 0}#si el jugador no esta lo inicializo
       #si eljugador no existe lo inicializo
        players[player]['kills'] += kills
        players[player]['assists'] += assists
        players[player]['deaths'] += deaths
        players[player]['points'] += points
        round_scores[player] = points #le guardo el puntaje
    
    mvp = max(round_scores, key=round_scores.get)#me  fijo si es MVP y , si lo es, le incremento esa categoria
    players[mvp]['mvps'] += 1

def mostrar_ranking(titulo, ranking):#imprimo la ronda
    print(titulo)
    print("Jugador   Kills  Asistencias  Muertes  MVPs  Puntos")
    print("-"*55)
    for player, stats in ranking:
        print(f"{player:<11} {stats['kills']:<9} {stats['assists']:<10} {stats['deaths']:<6} {stats['mvps']:<6} {stats['points']:<6}")
    print("-"*55)
    print()