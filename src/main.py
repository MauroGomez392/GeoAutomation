import subprocess
from packages.paths_handler import *

paths = PathHandler()

try:
    # Ejecutar MCDA Carga de Datos
    subprocess.run(["python", paths.mcda]) 
    #TODO FALTARÍA AGREGARLE EL RESTO DE RUTA HACIA EJECUTABLES

    # Ejecutar GeoProcess
    subprocess.run(["python", paths.geoprocess])

    # Ejecutar GeoNormalize
    subprocess.run(["python", paths.gronormalize])

    print("Los programas se ejecutaron exitosamente de manera secuencial.")
except Exception as e:
    print(f"Ocurrió un error: {str(e)}")


