#FUNCIONES
#---------------------------------------------------------

# def greeting(nombre:str) -> None:
#     print(f"Hola, {nombre} 😎")
#     return None #si no retorna nada es un procedimiento

# #asigno input a variabkle
# nombre= input("Ingresa tu nombre:\n")

# #llamar a la funcion
# greeting(nombre)
# #greeting(nombre:= input("Ingresa tu nombre: \n")) #operador wallroute o algo asi

#CRUD, create, read, upload, delete
# """
# database (crear un usuario | muchos usuarios)
# - ingreso la operacion del crud
# - controllers: logica del negocio
# - que paso hacer despues
# """
 
from database.generador_users import create_database

db_user:list[dict] = create_database()

print(db_user)