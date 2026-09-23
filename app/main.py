from fastapi import FastAPI

app = FastAPI(
    title="DevOps Demo Application",
    description="Demo application for Kubernetes, CI/CD and GitOps",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "DevOps Demo Application",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/api/info")
def info():
    return {
        "application": "devops-demo",
        "version": "1.0.0",
        "environment": "local"
    }