import cv2 
from video import results
from PIL import Image
from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
import uvicorn
from main import updatedValues,deploy


app = FastAPI()
templates = Jinja2Templates(directory="templates")
@app.get('/')
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/video_feed")
def video_feed():
    return StreamingResponse(deploy(), media_type="multipart/x-mixed-replace;boundary=frame")

@app.get('/value')
def values():
    print(updatedValues())
    data = {"value":updatedValues()}
    return JSONResponse(content=data)

if __name__ == '__main__':
   uvicorn.run(app, host='0.0.0.0', port=8000)
