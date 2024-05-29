from fastapi import FastAPI

# สร้าง FastAPI instance
app = FastAPI()

# สร้าง endpoint สำหรับ path "/"
@app.get("/")
def read_root():
    return {"Hello": "World"}

# สร้าง endpoint สำหรับ path "/{name}"
@app.get("/{name}")
def read_item(name: str):
    return {"Hello": name}

# รันเซิร์ฟเวอร์ด้วย uvicorn
# uvicorn main:app --reload