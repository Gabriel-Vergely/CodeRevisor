import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from servicios.revisar_codigo_srvc import procesar_webhook
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuración de CORS para permitir todos los orígenes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todos los orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos
    allow_headers=["*"],  # Permitir todos los encabezados
)

class WebhookPayload(BaseModel):
    repository: dict

@app.post("/webhook")
async def webhook(payload: WebhookPayload):
    try:
        print(payload)
        salida = procesar_webhook(payload)
        return {"status": "ok", "detalles": salida}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

