from flask import Flask
from datetime import datetime

import requests

app = Flask(__name__)

@app.route('/')
def home():

    url = "https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/872172ebb60e22e95baf8f50e2472551f49311ff/gistfile1.txt"
    response =  requests.get(url) #hacer solicitud get al servidor para leer el archivo

    if response.status_code !=200:
        return "No se puede acceder al archivo"
    
    info = response.text #si la conexion fue exitosa, vamos a ver el contenido del archivo txt
    lineas = info.splitlines()

    personas_seleccionadas = []

    for linea in lineas: #recorrer linea por linea del archivo
        separar = linea.split("|") #separar las partes con la coma
        if len(separar) >=2: #verificar que se haya separado
            id_persona = separar[0].strip() #tomar solo la parte de id de las partes
            if id_persona[0] in ['3', '4', '5', '7']:
                personas_seleccionadas.append(separar)#añade las personas encontradas a la lista

    #tabla_html = "<table border='1'><tr><th>ID</th><th>Nombre</th><th>Apellido</th><th>País</th><th>Dirección</th></tr>"
    tabla_html = """
    <style>
        table { border-collapse: collapse; width: 100%; font-family: Arial; }
        th, td { border: 1px solid #333; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
    </style>
    <table>
        <tr><th>ID</th><th>Nombre</th><th>Apellido</th><th>País</th><th>Dirección</th></tr>
    """

    for persona in personas_seleccionadas:
        id_p = persona[0]
        nombre = persona[1]
        apellido = persona[2]
        pais = persona[3]
        direccion = persona[4]  # Aquí sí está completa
        tabla_html += f"<tr><td>{id_p}</td><td>{nombre}</td><td>{apellido}</td><td>{pais}</td><td>{direccion}</td></tr>"

    tabla_html += "</table>"
    
    
    actual = datetime.now()
    fecha_formateada = actual.strftime("%d, %B, %Y, %M, %H, %S")
    #return f'¡Hola, Loja! <b>{fecha_formateada}</b><br><br>{tabla_html}'
    return f'<h2>¡Hola, Loja!</h2><p><b>{fecha_formateada}</b></p><br>{tabla_html}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)