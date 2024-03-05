import redis

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

def agregar_puntos():
    redis_client.zadd('ranking_juego', {'player1': 100, 'player2': 150, 'player3': 75})

def obtener_rango(id_jugador):
    rango = redis_client.zrevrank('ranking_juego', id_jugador)
    return rango + 1  if rango is not None else None

agregar_puntos()
print("Ranking de player1:", obtener_rango('player1'))