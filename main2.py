import redis

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

def guardar_valor(llave, valor):
    redis_client.set(llave, valor)

def obtener_valor(llave):
    return redis_client.get(llave)

def editar_valor(llave, valor):
    redis_client.set(llave, valor)

def eliminar_valor(llave):
    redis_client.delete(llave)

guardar_valor('nombre', 'Petra')

nombre = obtener_valor('nombre')
print("Nombre:", nombre.decode('utf-8'))

editar_valor('nombre', 'Toribia')

nombre = obtener_valor('nombre')
print("Nombre Actualizado:", nombre.decode('utf-8'))

eliminar_valor('nombre')

nombre = obtener_valor('nombre')
if nombre is None:
    print("Nombre eliminado correctamente...")
else:
    print("Nombre todavia existe:", nombre)