# import libs
import time
import os
import subprocess
import RPi.GPIO as GPIO
# text to speech
from gtts import gTTS


GPIO.setmode(GPIO.BCM)

# setup vars
start_time = time.time()
end_time = time.time()
time_difference = 0
distance2 = 0.0
audio_playing = False

# setup sensors
front_left_trigger = 4
front_left_echo = 18

front_right_trigger = 17
front_right_echo = 27

back_left_trigger = 22
back_left_echo = 23

back_right_trigger = 24
back_right_echo = 25

GPIO.setup(front_left_trigger, GPIO.OUT)
GPIO.setup(front_left_echo, GPIO.IN)

GPIO.setup(front_right_trigger, GPIO.OUT)
GPIO.setup(front_right_echo, GPIO.IN)

GPIO.setup(back_left_trigger, GPIO.OUT)
GPIO.setup(back_left_echo, GPIO.IN)

GPIO.setup(back_right_trigger, GPIO.OUT)
GPIO.setup(back_right_echo, GPIO.IN)

# functions
def distance(trigger_pin, echo_pin):
    # set Trigger on HIGH
    GPIO.output(trigger_pin, True)

    # after 1ms set the trigger on low
    time.sleep(0.00001)
    GPIO.output(trigger_pin, False)

    # store the start time
    while GPIO.input(echo_pin) == 0:
        start_time = time.time()
    
    while GPIO.input(echo_pin) == 1:
        end_time = time.time()
    
    # time difference
    time_difference = end_time - start_time
    distance2 = (time_difference * 34300) / 2

    return distance2


while True:
    front_left_distance = round(distance(front_left_trigger, front_left_echo), 2)
    front_right_distance = round(distance(front_right_trigger, front_right_echo), 2)
    back_left_distance = round(distance(back_left_trigger, back_left_echo), 2)
    back_right_distance = round(distance(back_right_trigger, back_right_echo), 2)

    if front_left_distance < 1.00 and audio_playing == False:
        # play Sound
        audio_playing = True
        tts_frontLeft = gTTs("Vorne Links: " + front_left_distance, lang="de")
        tts_frontLeft.save('frontleft.mp3')
        os.system("mpg123 frontleft.mp3")
        time.sleep(3)
        audio_playing = False
    
    if front_right_distance < 1.00 and audio_playing == False:
        # play Sound
        audio_playing = True
        tts_frontRight = gTTs("Vorne Rechts: " + front_right_distance, lang="de")
        tts_frontRight.save('frontRight.mp3')
        os.system("mpg123 frontleft.mp3")
        time.sleep(3)
        audio_playing = False

    if back_left_distance < 1.00 and audio_playing == False:
        # play Sound
        audio_playing = True
        tts_backLeft = gTTs("Hinten Links: " + back_left_distance, lang="de")
        tts_backLeft.save('backLeft.mp3')
        os.system("mpg123 frontleft.mp3")
        time.sleep(3)
        audio_playing = False

    if back_right_distance < 1.00 and audio_playing == False:
        # play Sound
        audio_playing = True
        tts_backRight = gTTs("Hinten Rechts: " + back_right_distance, lang="de")
        tts_backRight.save('tts_backRight.mp3')
        os.system("mpg123 frontleft.mp3")
        time.sleep(3)
        audio_playing = False






# on script ending remove file with: os.remove('filename'), alla udio files
# while running it just replaces the new file
# sudo apt-get install mpg123 to play audio files?