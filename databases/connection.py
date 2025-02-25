import psycopg2

#diccionario con la conexion a postgreSQL
postgres_config = {
    'host':'localhost',
    'port':'5432',
    'user':'tubarao',
    'database':'Lol',
    'password':'123456'
}
# a diferencia de mysql en postgres no es necesario usar 'auth_plugin':'mysql_native_password' 

conn = psycopg2.connect(**postgres_config)
#para no tener que describir todas las propiedades de postgres_config se le pone 
# los dos **, para que la funcion misma lo descomponga

#funcion para regresar la conexion
def get_connection():
    return conn