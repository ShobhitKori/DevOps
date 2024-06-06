from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
	return {"Hello": "World"}

@app.get("/About")
def about():
	return {"msg": "About msg"}
