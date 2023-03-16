from fastapi import FastAPI
from api.users import user_router


app = FastAPI(
    debug=True,
    title="Fintech Portfolio API",
    description="A webserver with a REST API for keeping track of your different financial assets, stocks & crypto, and see/compare their evolution",
    version="0.0.1",
)
app.include_router(user_router)

if __name__ == '__main__':
    import subprocess
    subprocess.run(["uvicorn","finance-project.main:app","--reload"])