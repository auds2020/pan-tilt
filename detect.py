from multiprocessing import Process, Queue
import time
import cv2
import imutils

camera = cv2.VideoCapture(0)
cv2.namedWindow("original", cv2.WINDOW_NORMAL)
cv2.namedWindow("mask", cv2.WINDOW_NORMAL)

frontalface = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")		# frontal face pattern detection
profileface = cv2.CascadeClassifier("haarcascade_profileface.xml")		# side face pattern detection

while(True):
	ret, image = camera.read()
	cv2.imshow("original", image)
	cv2.imshow("mask", mask)
	if cv2.waitKey(1) & 0xFF is ord('q'):
		break
	
# ~ webcam = cv2.VideoCapture(0)				# Get ready to start getting images from the webcam
# ~ webcam.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 320)		# I have found this to be about the highest-
# ~ webcam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 240)	# 	resolution you'll want to attempt on the pi

# ~ frontalface = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")		# frontal face pattern detection
# ~ profileface = cv2.CascadeClassifier("haarcascade_profileface.xml")		# side face pattern detection

# ~ face = [0,0,0,0]	# This will hold the array that OpenCV returns when it finds a face: (makes a rectangle)
# ~ Cface = [0,0]		# Center of the face: a point calculated from the above variable
# ~ lastface = 0		# int 1-3 used to speed up detection. The script is looking for a right profile face,-
			# ~ # 	a left profile face, or a frontal face; rather than searching for all three every time,-
			# ~ # 	it uses this variable to remember which is last saw: and looks for that again. If it-
			# ~ # 	doesn't find it, it's set back to zero and on the next loop it will search for all three.-
			# ~ # 	This basically tripples the detect time so long as the face hasn't moved much.
