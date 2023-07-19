import cv2 
from video import results
from PIL import Image
cap = cv2.VideoCapture('video.mp4')
d = {}
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frame_rate = cap.get(cv2.CAP_PROP_FPS)
# Calculate the duration of the video in seconds
video_duration = total_frames / frame_rate

for i in range(int(video_duration)+1):
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    success, img = cap.read()
    if success==False:
        break
    timestamp = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    im_pil = Image.fromarray(img)
    a,b = results(im_pil)
    d[int(cap.get(cv2.CAP_PROP_POS_FRAMES))] = a
    print(d)
print(d)
