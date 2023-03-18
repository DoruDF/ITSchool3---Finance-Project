from fastapi import FastAPI

app = FastAPI(
    debug=True,
    title="Fintech Portofolio API",
    description="A webserver with a REST API for keeping track of your different financial assets,"
    " stocks & crypto, and see/compare their evolution",
    version="0.1.0",
)

if __name__ == "__main__":
    import subprocess

    subprocess.run(["uvicorn", "finance-project.main:app", "--reload"])
