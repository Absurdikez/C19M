from operator import lt
from pathlib import Path
import uvicorn

from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse
import shutil
from fastapi.staticfiles import StaticFiles
import os
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/files", StaticFiles(directory="files"), name="files") #to make a file static
app.mount('/static',StaticFiles(directory=os.pardir+'/static'),name='static')

templates = Jinja2Templates(directory="art-museum-master")


@app.post("/uploadfile")
async def upload_file(file: UploadFile = File(...,description="Upload file"), author_name: str = Form(...,max_length=50,description="Author name"),
 keywords: str = Form(...,description="Enter keywords")):
	print(author_name)
	file_location = f"files/{file.filename}"
	with open(file_location, "wb+") as buffer:
		shutil.copyfileobj(file.file, buffer)
	return {"info": f"file '{file.filename}' saved at '{file_location}'"}

# author_name: str = Form(...), keywords: str = Form(...)

@app.get("/")
async def main():
	content = """
<body>
	<form action="/uploadfile" enctype="multipart/form-data" method="post">
		<input name="file" type="file">
		<input name="author_name">
		<input name="keywords">
		<input type="submit">
	</form>
</body>
"""
	return HTMLResponse(content=content)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
