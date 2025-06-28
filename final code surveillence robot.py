import RPi.GPIO as GPIO
from time import sleep
from threading import Thread
import cv2
import numpy

class WebcamVideoStream:
    def __init__(self, src =0):
        self.stream = cv2.VideoCapture(src)
        (self.grabbed,self.frame) = self.stream.read()

        self.stopped = False

    def start (self):
        Thread(target = self.update,args = ()).start()
        return self

    def update(self):
        while True:
            if self.stopped:
                return

            (self.grabbed, self.frame) = self.stream.read()

    def read(self):
        return self.frame

    def stop(self):
        self.stopped = True

GPIO.setmode(GPIO.BOARD)

lm_ena = 33
lm_pos = 35
lm_neg = 37

rm_ena = 40
rm_pos = 36
rm_neg = 38

GPIO.setup(lm_ena,GPIO.OUT)
GPIO.setup(lm_pos,GPIO.OUT)
GPIO.setup(lm_neg,GPIO.OUT)z

GPIO.setup(rm_ena,GPIO.OUT)
GPIO.setup(rm_pos,GPIO.OUT)
GPIO.setup(rm_neg,GPIO.OUT)

def moveRobot(direction):
    if(direction=='f'):
        print("FORWARD")
        GPIO.output(lm_ena,GPIO.HIGH)
        GPIO.output(lm_pos,GPIO.HIGH)
        GPIO.output(lm_neg,GPIO.LOW)

        GPIO.output(rm_ena,GPIO.HIGH)
        GPIO.output(rm_pos,GPIO.HIGH)
        GPIO.output(rm_neg,GPIO.LOW)

    if(direction=='b'):
        print("BACKWARD")
        GPIO.output(lm_ena,GPIO.HIGH)
        GPIO.output(lm_pos,GPIO.LOW)
        GPIO.output(lm_neg,GPIO.HIGH)

        GPIO.output(rm_ena,GPIO.HIGH)
        GPIO.output(rm_pos,GPIO.LOW)
        GPIO.output(rm_neg,GPIO.HIGH)

    if(direction=='r'):
        print("RIGHT")
        GPIO.output(lm_ena,GPIO.HIGH)
        GPIO.output(lm_pos,GPIO.HIGH)
        GPIO.output(lm_neg,GPIO.LOW)

        GPIO.output(rm_ena,GPIO.HIGH)
        GPIO.output(rm_pos,GPIO.LOW)
        GPIO.output(rm_neg,GPIO.HIGH)

    if(direction=='l'):
        print("LEFT")
        GPIO.output(lm_ena,GPIO.HIGH)
        GPIO.output(lm_pos,GPIO.LOW)
        GPIO.output(lm_neg,GPIO.HIGH)

        GPIO.output(rm_ena,GPIO.HIGH)
        GPIO.output(rm_pos,GPIO.HIGH)
        GPIO.output(rm_neg,GPIO.LOW)

    if(direction=='s'):
        print("STOP")
        GPIO.output(lm_ena,GPIO.HIGH)
        GPIO.output(lm_pos,GPIO.LOW)
        GPIO.output(lm_neg,GPIO.LOW)

        GPIO.output(rm_ena,GPIO.HIGH)
        GPIO.output(rm_pos,GPIO.LOW)
        GPIO.output(rm_neg,GPIO.LOW)

cam = WebcamVideoStream(src=0).start()

while(True):
    frame = cam.read()
    key = cv2.waitKey(10)

    if key == ord('w'):
        moveRobot('f')

    if key == ord('a'):
        moveRobot('l')

    if key == ord('s'):
        moveRobot('b')

    if key == ord('d'):
        moveRobot('r')

    if key == 32:
        moveRobot('s')

    if key == 27:
        break

    cv2.imshow("frame",frame)


img_RGB = cv2.cv2tColor(frame,cv2.COLOR_BGR2RGB)
plt.imshow(img_RGB)
plt.show()    
cam.stop()
cv2.destroyAllWindows()
GPIO.cleanup()
