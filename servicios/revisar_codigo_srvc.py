import os
import subprocess
from api.semgrep_api import ejecutar_semgrep

def obtener_repo_url(usuario_organizacion, nombre_repositorio):
    """Generar la URL de clonación del repositorio GitHub."""
    return f"git@github.com:{usuario_organizacion}/{nombre_repositorio}.git"

def obtener_ruta_local(nombre_repositorio):
    """Generar una ruta local única para el repositorio clonado."""
    return f"/tmp/{nombre_repositorio}"

def clonar_o_actualizar_repo(usuario_organizacion, nombre_repositorio):
    """Clonar o actualizar el repositorio en la ruta local."""
    repo_url = obtener_repo_url(usuario_organizacion, nombre_repositorio)
    ruta_local = obtener_ruta_local(nombre_repositorio)
    print(ruta_local)
    print(repo_url)

    if not os.path.exists(ruta_local):
        resultado = subprocess.run(["git", "clone", repo_url, ruta_local], capture_output=True, text=True)
        return f"Clonado: {resultado.stdout}"
        print(resultado)
    else:
        resultado = subprocess.run(["git", "pull"], cwd=ruta_local, capture_output=True, text=True)
        return f"Actualizado: {resultado.stdout}"

def procesar_webhook(payload):
    """Procesar el webhook y ejecutar el análisis de seguridad con Semgrep."""
    # Extraemos la información del repositorio y propietario del payload
    usuario_organizacion = payload.repository['owner']['login']
    print(usuario_organizacion)
    nombre_repositorio = payload.repository['name']
    print(nombre_repositorio)

    salida = {}

    # Clonamos o actualizamos el repositorio
    salida["git"] = clonar_o_actualizar_repo(usuario_organizacion, nombre_repositorio)

    # Ejecutamos Semgrep
    ruta_local = obtener_ruta_local(nombre_repositorio)
    print("ejecutando semgrep...")
    salida["semgrep"] = ejecutar_semgrep(ruta_local)
    print(salida["semgrep"])

    return salida
