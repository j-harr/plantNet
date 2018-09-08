import picamera

with picamera.PiCamera() as cam:
	cam.resolution = (1280, 720)
	cam.capture("imageJJ.jpg")
print("Pic was taken")
