import pyodbc

# Configuración de la conexión (considerando que la DB uso 'Windows Authentication')
servidor = 'ANDRESSON\\SQLEXPRESS'  # Cambia por el nombre de tu servidor
base_datos = 'MusicGUIProject'     # Cambia por el nombre de tu base de datos
songs_list = []
global conexion
try:
    # Crear la conexión
    conexion = pyodbc.connect(
        f"DRIVER={{ODBC Driver 18 for SQL Server}};"
        f"SERVER={servidor};"
        f"DATABASE={base_datos};"
        f"Trusted_Connection=yes;"
        f"TrustServerCertificate=yes;"
    )

    print("Conexión exitosa a la base de datos")

    # Crear un cursor para realizar consultas
    cursor = conexion.cursor()

    # Consulta a una tabla existente
    consulta = "SELECT * FROM Music"  # Cambia 'mi_tabla' por el nombre de tu tabla
    cursor.execute(consulta)

    # Recuperar los resultados
    resultados = cursor.fetchall()
    for fila in resultados:
        #print(fila)  # Cada fila es una tupla
        songs_list.append(fila)  # Concatenar fila de datos en una lista

except pyodbc.Error as e:
    print(f"Error al conectar a SQL Server: {e}")

finally:
    # Cerrar la conexión
    if 'conexion' in locals():
        conexion.close()
        #print("Conexión cerrada")

def get_songs():
    return songs_list