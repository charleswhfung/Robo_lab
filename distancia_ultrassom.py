import RPi.GPIO as GPIO
import time
import rospy
from sensor_msgs.msg import Range

TRIG = 22
ECHO = 27

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(TRIG,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(ECHO,GPIO.IN)

rospy.init_node('ultrassom')

def dist():
        GPIO.output(TRIG,GPIO.HIGH)
        time.sleep(0.000015)
        GPIO.output(TRIG,GPIO.LOW)
        while not GPIO.input(ECHO):
                pass
        t1 = time.time()
        while GPIO.input(ECHO):
                pass
        t2 = time.time()
        return (t2-t1)*34000/2

def publica_dist():
        pub = rospy.Publisher('/distancia',Range,queue_size=10)
        ranges = [float('NaN'),1.0,-float('Inf'),3.0,float('Inf')]
        min_range = 2.0
        max_range = 2.0

        r = Range()
        r.header.stamp = rospy.Time.now()
        r.header.frame_id = "/base_link"
        r.radiation_type = 0
        r.field_of_view = 0.1
        r.min_range = min_range
        r.max_range = max_range
        rg = dist()
        r.range = rg
        pub.publish(r)

            
try:
        while True:
                print "Distance:%0.2f cm" % dist()
                publica_dist()
                time.sleep(1)
except KeyboardInterrupt:
        GPIO.cleanup()

