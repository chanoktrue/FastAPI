import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=4040,
        reload=True,
        reload_dirs=["."],  # ตรวจสอบเฉพาะไดเรกทอรีปัจจุบัน
        reload_excludes=["*.venv/*"],  # เพิกเฉยต่อการเปลี่ยนแปลงใน .venv
    )
