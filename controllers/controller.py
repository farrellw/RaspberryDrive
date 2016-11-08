import os
import sys
from time import sleep
sys.path.insert(0, os.getcwd())
# import models.analyze
from models.analyze import check_blob_in_direct_path
from get_images_from_pi import get_image, valid_image
from connect import new_connection, send_command, receive_confirmation
from start_camera import start_camera
from start_server import start_server
import threading

#Start-all
  #start the camera taking pictures on camera pi
  #start the server listening on contr pi
  #start the server connection on this current server
threads = []
server_thread = threading.Thread(target=start_server)
threads.append(server_thread)
server_thread.start()
#Sleep for testing
sleep(2)
camera_thread = threading.Thread(target=start_camera)
threads.append(camera_thread)
camera_thread.start()
# Sleep to make sure server connects
sleep(5)
s = new_connection()

#Run-All.  X times do
    #retrieve image.  #Blog Detection
    #send instruction over server
count = 0
while (count < 20):
  get_image()
  if valid_image(os.getcwd() + "/images/gregTest.jpg"):
    instruction = check_blob_in_direct_path(os.getcwd() + "/images/gregTest.jpg")
    send_command(s, instruction, "0.5")
    count += 1
    receive_confirmation(s)
    count += 1

# #End-all
#   #Stop the camera taking pictures on the camera pi -- still needs to be implemented
#   #close the server connection
s.send("quit")
#   #Kill the server listening process
s.close()
exit()
