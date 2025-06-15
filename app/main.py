from fastapi import FastAPI

app = FastAPI(title="ResumeRevamp AI – Smoke Test")

@app.get("/healthz")
async def ping():
    return {"status": "ok"}
