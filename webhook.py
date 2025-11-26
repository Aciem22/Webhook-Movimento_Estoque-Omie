from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/webhook")
async def receber_webhook(request: Request):
    body = await request.json()
    
    print("📦 Webhook recebido:")
    print(body)  # Vai aparecer nos logs do Render

    return {"status": "ok"}
