from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

archivo = open("data/datos_clubs.txt")
registros =  archivo.readlines()

clubs = []

for r in registros:
        lista = r.split(';')
        club = Club(nombre= lista[0], deporte=lista[1], \
        fundacion=int(lista[2].replace('\n','')))
        session.add(club)
        clubs.append(club)

session.commit()

archivo = open("data/datos_jugadores.txt")
registrosJugadores = archivo.readlines()

for c in clubs:
        for r in registrosJugadores:
                lista = r.split(';')
                if (c.nombre == lista[0]):
                        jugador = Jugador(nombre = lista[3].replace('\n',''),\
                        dorsal=lista[2], posicion= lista[1], \
                        club=c)
                        session.add(jugador)

# se agrega los objetos
# a la sesión

# se confirma las transacciones
session.commit()
