from fastapi import FastAPI 
from router import disk, aws


app = FastAPI(
    title = "PYTHON FOR DEVOPS",
    description = "This is APi Use for :- CPU Percent Check And High CPU Alert, Memory Percent Check And Low Space Alert, Disk Space Check and ALert, AWS Instance Health show, AWS S3 bucket show ",
    version = '1.0.0.0',
    docs_url = '/doc',
    redoc_url="/redoc"
)
@app.get("/")
def Hello():
    """
    this doc use for testing
    """
    return {"massage": "hello Dosto Kaise hai app sbhi"}
app.include_router(disk.router)
app.include_router(aws.router, prefix="/aws")