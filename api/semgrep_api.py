import subprocess

def ejecutar_semgrep(ruta):
    try:
        print("inicializando semgrep")
        result = subprocess.run(["semgrep", "--config", "p/security-audit", ".", "--verbose"], cwd=ruta, capture_output=True, text=True)
        print(result)
        return result.stdout or result.stderr
    except Exception as e:
        return f"Error ejecutando Semgrep: {str(e)}"
