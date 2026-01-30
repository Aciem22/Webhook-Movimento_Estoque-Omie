from fastapi import FastAPI, Request
import httpx

app = FastAPI()

GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbyS_uIEfmE3a2u9LuxePn3T4Zc3dthpHuyAB88lukx7yu6Ml_qWvwDBfjrw8rBxhxDP/exec"

@app.post("/webhook")
async def receber_webhook(request: Request):
    body = await request.json()
    
    print("📦 Webhook recebido:")
    print(body)  # Vai aparecer nos logs do Render


    '''try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                GOOGLE_SCRIPT_URL,
                json=body,
                timeout = 10
            )

        print("📤 Resposta do Google Script:")
        print(response.text)
    
    except Exception as e:
        print("❌ Erro ao enviar para o Google Script:", e)'''

    return {"status": "ok"}
