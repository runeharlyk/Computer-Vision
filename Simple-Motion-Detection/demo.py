import MD
import picamera
from time import sleep
import datetime as dt

camera = picamera.PiCamera(resolution=(300, 400))
M = MD.Motion()

camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
camera.start_preview(resolution=(300, 400))
SurOnGoing = True
recording = False
filePlacement = ""

#Warm up time
sleep(2)
print("Starting surveillance")

while SurOnGoing:
	camera.capture(filePlacement + "baseStatus.jpg", resize=(320, 240))
	sleep(3)
	camera.capture(filePlacement + "newstatus.jpg", resize=(320, 240))
	#camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

	thereIsMotion = M.Check(filePlacement + "baseStatus.jpg", filePlacement + "newstatus.jpg", 10, False)

	if thereIsMotion:
		if not recording:
			print("Motion started")
			#camera.stop_recording(filePlacement + "video.h264")
			recording = True
	else:
		if recording:
			print("Motion stopped")
			#camera.stop_recording()
			#await client.send_file(filePlacement + "video.h264")
			recording = False
	sleep(1)
