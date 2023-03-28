from fastapi import FastAPI
from api.users import user_router

app = FastAPI(
    debug=True,
    title="Fintech Portfolio API",
    description="A webserver with a REST API for keeping track of your different financial assets,"
    " stocks and crypto, and see/compare their evolution",
    version="0.2.0",
)
app.include_router(user_router)

if __name__ =="__main__":
    import subprocess
    subprocess.run(["uvicorn", "main:app", "--reload"])