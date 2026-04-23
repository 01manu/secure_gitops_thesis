from fastapi import FastAPI

app = FastAPI(
    title="Secure GitOps App",
    Version="1.0.0"
)

@app.get("/health")
def health_check():
    return{"status": "healthy"}

