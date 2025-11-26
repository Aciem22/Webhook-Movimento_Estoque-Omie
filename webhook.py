from fastapi import FastAPI, Request
import httpx

app = FastAPI()

GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbxlUDRnfbeey_yQ75SjsXP0pkA1rx56QeHmucA0i4_Jef3Hheh-3HpJzb-vXb28EV9K/exec"

@app.post("/webhook")
async def receber_webhook(request: Request):
    body = await request.json()
    
    print("📦 Webhook recebido:")
    print(body)  # Vai aparecer nos logs do Render


    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                GOOGLE_SCRIPT_URL,
                json=body,
                timeout = 10
            )

        print("📤 Resposta do Google Script:")
        print(response.text)
    
    except Exception as e:
        print("❌ Erro ao enviar para o Google Script:", e)

    return {"status": "ok"}
