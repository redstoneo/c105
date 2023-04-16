import cv2

#vid=cv2.VideoCapture("AnthonyShkraba.mp4")
vid=cv2.VideoCapture(0)
if(vid.isOpened()==False):
    print("unable to read the feed")

h=int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
w=int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
fps=int(vid.get(cv2.CAP_PROP_FPS))
print(h)
print(w)
print(fps)
cv2.VideoWriter_fourcc(*'mp4v')
out=cv2.VideoWriter("punch.mp4",cv2.VideoWriter_fourcc(*'DIVX'),30,(w,h))

while(True):
    ret,frame=vid.read()
    cv2.imshow("vid",frame)
    out.write(frame)
    if cv2.waitKey(1)==32:
        break
vid.release()
out.release()