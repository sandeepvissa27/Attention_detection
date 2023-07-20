import cv2 
from video import results
from PIL import Image



x,y = 0,0
def updatedValues():
    global x,y
    print(x,y)
    return x


def deploy():
    global x,y
    cap = cv2.VideoCapture('static/video.mp4')
    d = {}
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    # Calculate the duration of the video in seconds
    video_duration = total_frames / frame_rate
    f = True
    while True:

        if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        success, img = cap.read()
        if not success:
            break
        timestamp = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        im_pil = Image.fromarray(img)
        a,b = results(im_pil)
        x = a
        y = b      
        if f:
            k = b 
            f = False
        cv2.putText(img, str(a)+"/"+str(k), (250, 250), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 255, 0), 4)
        ret, buffer = cv2.imencode('.jpg', img)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
