# 🛡️ Análisis de Código Seguro con Semgrep + Webhook + Serveo

Esta aplicación realiza un análisis estático de seguridad sobre repositorios utilizando [Semgrep](https://semgrep.dev), y recibe notificaciones a través de un webhook configurado en GitHub.

---

## 📁 Estructura del Proyecto

      .  
      ├── api/ # Lógica principal (incluye integración con semgrep)
      ├── servicios/ # Módulos de servicio (por ejemplo, procesamiento del webhook)
      ├── main.py # Punto de entrada
      ├── requirements.txt # Dependencias del proyecto
      ├── README.md # Esta guía
      ├── venv/ # Entorno virtual (opcional)


---

## ⚙️ Requisitos

- Python 3.8 o superior
- [Semgrep CLI](https://semgrep.dev/docs/installation/)
- Cuenta en GitHub
- Acceso SSH configurado

---

## 🔐 Paso 1: Configurar Claves SSH

1. Genera un par de claves SSH:
   ```bash
   ssh-keygen -t rsa -b 4096 -C "tu-correo@example.com"

Acepta los valores por defecto (~/.ssh/id_rsa y id_rsa.pub).

    Agrega la clave privada a tu agente local:

eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa

Copia la clave pública y añádela a tu cuenta de GitHub:

    cat ~/.ssh/id_rsa.pub

        Ve a GitHub > Settings > SSH and GPG keys > New SSH key y pégala.

🌐 Paso 2: Exponer tu servidor local con Serveo

Para recibir webhooks desde GitHub, necesitas una URL pública. Usa Serveo:

ssh -R 80:localhost:8000 serveo.net

Esto expondrá tu servidor local en una URL como:

https://yourname.serveo.net

Nota: No cierres esta terminal mientras el túnel esté activo.
🔁 Paso 3: Crear Webhook en GitHub

    Ve al repositorio en GitHub donde quieras activar el análisis.

    Entra en Settings > Webhooks > Add webhook

    En "Payload URL" pon tu URL de Serveo, por ejemplo:

https://yourname.serveo.net/webhook

    En "Content type" selecciona: application/json

    En "Events" selecciona: Just the push event

    Haz clic en Add webhook

🕵️ Paso 4: Análisis de Código con Semgrep

Esta app usa Semgrep para hacer un análisis estático del repositorio.

Instalación:

pip install semgrep

Uso básico:

semgrep --config auto .

En el código ya se incluye una función que ejecuta Semgrep automáticamente sobre el repositorio clonado desde el webhook.

--

## ▶️ Ejecutar la Aplicación

    Instala las dependencias:

pip install -r requirements.txt

Ejecuta el servidor:

python main.py

Mantén abierto el túnel de Serveo:

    ssh -R 80:localhost:8000 serveo.net

    Espera los push a tu repositorio, y revisa los análisis en consola o donde los tengas configurados.

---

## 📌 Notas

    Puedes usar otras herramientas además de Semgrep (como Bandit, Trivy, Gitleaks, etc.).

    Serveo es útil para pruebas locales, pero considera usar servicios como Ngrok si necesitas más fiabilidad o autenticación.

---

## 🧑‍💻 Autor

Desarrollado por [Gabriel Vergely Fernandez].
