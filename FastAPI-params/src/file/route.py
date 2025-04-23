import fastapi
import chardet
from fastapi import File , UploadFile 
from pathlib import Path
import os

router = fastapi.APIRouter()
UPLOAD_DIR_BIN = "uploads-Binary"
UPLOAD_DIR_TXT = "uploads-Text"


os.makedirs(UPLOAD_DIR_BIN , exist_ok=True)
os.makedirs(UPLOAD_DIR_TXT , exist_ok=True)


@router.post("/file/")
def postFile (file: UploadFile  = File(...)):
    return {
        "filename": file.filename,
        "filename Header": file.headers,
        "content_type": file.content_type,
        "fileBody": file
    }
    
    
# conversion and writing to server 
@router.post("/upload/")
async def uploadFile(file: UploadFile = File(...)):
    content = await file.read()
    filename = file.filename or "default.txt"
    safe_name = Path(filename).name

    binaryPath = os.path.join(UPLOAD_DIR_BIN, f"Binary-uploaded-{safe_name}")
    textPath = os.path.join(UPLOAD_DIR_TXT, f"Text-uploaded-{safe_name}")

    with open(binaryPath, "wb") as binary_file:
        binary_file.write(content)

    try:
        detection = chardet.detect(content)
        encoding = detection.get("encoding", "utf-8") or "utf-8"
        confidence = detection.get("confidence", 0)
        text_content = content.decode(encoding)

        with open(textPath, "w", encoding=encoding) as f:
            f.write(text_content)
    except Exception as e:
        text_content = f"❌ Could not decode file: {str(e)}"

    return {
        "filename": file.filename,
        "headers": dict(file.headers),
        "content_type": file.content_type,
        "file_size_bytes": len(content),
        "text_saved": os.path.exists(textPath),
        "binary_saved": os.path.exists(binaryPath),
        "text_preview": text_content[:200] if isinstance(text_content, str) else None,
    }
