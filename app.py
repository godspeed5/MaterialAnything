from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse, FileResponse
import subprocess
from pathlib import Path
import shutil
import uuid

app = FastAPI()

UPLOAD_DIR = Path("./uploads")
OUTPUT_DIR = Path("./outputs")
UPLOAD_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI application!"}

@app.post("/render/")
async def render_material(file: UploadFile = File(...)):
    try:
        unique_id = uuid.uuid4().hex
        input_path = UPLOAD_DIR / f"{unique_id}_{file.filename}"
        with input_path.open("wb") as buffer:
            buffer.write(await file.read())

        render_output_dir = OUTPUT_DIR / unique_id
        render_output_dir.mkdir(exist_ok=True)

        command = [
            "blender", "-b",
            "-P", "./rendering_scripts/blender_script_material.py", "--",
            "--object_path", str(input_path),
            "--output_dir", str(render_output_dir),
            "--render_space", "VIEW"
        ]
        subprocess.run(command, check=True)

        zip_path = OUTPUT_DIR / f"{unique_id}.zip"
        shutil.make_archive(str(zip_path).replace('.zip', ''), 'zip', render_output_dir)

        return {"output_link": f"/download/{unique_id}"}
    except subprocess.CalledProcessError as e:
        return JSONResponse(status_code=500, content={"error": f"Blender command failed: {e}"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/download/{unique_id}")
def download_zip(unique_id: str):
    zip_path = OUTPUT_DIR / f"{unique_id}.zip"
    if zip_path.exists():
        return FileResponse(zip_path, media_type="application/zip", filename=f"{unique_id}.zip")
    return JSONResponse(status_code=404, content={"error": "File not found."})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=22, reload=True)
