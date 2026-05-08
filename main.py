# OpenDrop-AGPL - A Simple File Sharing System
# Copyright (C) 2024 [Your Name/Organization]
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
import shutil
import zipfile

app = FastAPI()
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# 1. ファイルアップロード機能
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"message": "Upload successful", "filename": file.filename}

# 2. ファイルリスト取得
@app.get("/files")
async def list_files():
    return os.listdir(UPLOAD_DIR)

# 3. ファイルダウンロード
@app.get("/download/{filename}")
async def download_file(filename: str):
    return FileResponse(os.path.join(UPLOAD_DIR, filename))

# 4. 【重要】AGPL要件：自分自身のソースコードを配布する機能
# サーバーが稼働している現在のコードをzipに固めて提供
@app.get("/source-code")
async def get_source():
    source_zip = "source.zip"
    with zipfile.ZipFile(source_zip, 'w') as z:
        z.write("main.py")
        z.write("static/index.html")
        z.write("LICENSE")
    return FileResponse(source_zip, media_type="application/zip", filename="opendrop-source.zip")

app.mount("/", StaticFiles(directory="static", html=True), name="static")
