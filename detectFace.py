from __future__ import print_function
import cv2 as cv
import argparse
from gpiozero import AngularServo


# ~ pan = AngularServo(12, min_angle=-90, max_angle=90)
# ~ tilt = AngularServo(13, min_angle=-90, max_angle=90)

def detectAndDisplay(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)
    #-- Detect faces
    faces = face_cascade.detectMultiScale(frame_gray)
    # ~ for (x,y,w,h) in faces:
        # ~ center = (x + w//2, y + h//2)
        # ~ frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
        # ~ faceROI = frame_gray[y:y+h,x:x+w]
        
        #-- In each face, detect eyes
        # ~ eyes = eyes_cascade.detectMultiScale(faceROI)
        # ~ for (x2,y2,w2,h2) in eyes:
            # ~ eye_center = (x + x2 + w2//2, y + y2 + h2//2)
            # ~ radius = int(round((w2 + h2)*0.25))
            # ~ frame = cv.circle(frame, eye_center, radius, (255, 0, 0 ), 4)
    
    profiles = profile_cascade.detectMultiScale(frame_gray)
    (FRAME_W, FRAME_H) = frame_gray.shape[:2] #w:image-width and h:image-height
    for (x,y,w,h) in profiles:
        center = (x + w//2, y + h//2)
        frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
        
        # ~ if center[0] <  FRAME_W:
            # ~ print("left")
        # ~ else: 
            # ~ print("right")
        
        # ~ if center[1] <  FRAME_H:
            # ~ print(center[1])
            # ~ print("down")
        # ~ else: 
            # ~ print("up")
            
            
        # Correct relative to centre of image
        turn_x  = float(x - (FRAME_W/2))
        turn_y  = float(y - (FRAME_H/2))

        # Convert to percentage offset
        turn_x  /= float(FRAME_W/2)
        turn_y  /= float(FRAME_H/2)

        # Scale offset to degrees (that 2.5 value below acts like the Proportional factor in PID)
        turn_x   *= 10 # VFOV
        turn_y   *= 2.5 # HFOV
        cam_pan   = -turn_x
        cam_tilt  = turn_y

        print(cam_pan, cam_tilt)

        # Clamp Pan/Tilt to 0 to 180 degrees
        # ~ cam_pan = max(0,min(180,cam_pan))
        # ~ cam_tilt = max(0,min(180,cam_tilt))

        # Update the servos
        # ~ pan.angle = int(cam_pan)
        # ~ tilt.angle = int(cam_tilt)
        
    cv.imshow('Capture - Face detection', frame)
parser = argparse.ArgumentParser(description='Code for Cascade Classifier tutorial.')
parser.add_argument('--face_cascade', help='Path to face cascade.', default='data/haarcascades/haarcascade_frontalface_alt.xml')
parser.add_argument('--profile_cascade', help='Path to face cascade.', default='data/haarcascades/haarcascade_profileface.xml')
parser.add_argument('--eyes_cascade', help='Path to eyes cascade.', default='data/haarcascades/haarcascade_eye_tree_eyeglasses.xml')
parser.add_argument('--camera', help='Camera divide number.', type=int, default=0)
args = parser.parse_args()
face_cascade_name = args.face_cascade
profile_cascade_name = args.face_cascade
eyes_cascade_name = args.eyes_cascade

face_cascade = cv.CascadeClassifier()
profile_cascade = cv.CascadeClassifier()
eyes_cascade = cv.CascadeClassifier()
#-- 1. Load the cascades
if not face_cascade.load(cv.samples.findFile(face_cascade_name)):
    print('--(!)Error loading face cascade')
    exit(0)
if not eyes_cascade.load(cv.samples.findFile(eyes_cascade_name)):
    print('--(!)Error loading eyes cascade')
    exit(0)
if not profile_cascade.load(cv.samples.findFile(profile_cascade_name)):
    print('--(!)Error loading profile cascade')
    exit(0)
camera_device = args.camera
#-- 2. Read the video stream
cap = cv.VideoCapture(camera_device)
if not cap.isOpened:
    print('--(!)Error opening video capture')
    exit(0)
while True:
    ret, frame = cap.read()
    if frame is None:
        print('--(!) No captured frame -- Break!')
        break
    detectAndDisplay(frame)
    if cv.waitKey(10) == 27:
        break
