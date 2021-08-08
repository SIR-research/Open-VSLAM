import signal
import subprocess
import time
import os
import sys
# devnull = open('/dev/null', 'w')
# p = subprocess.Popen(['gnome-terminal','--',"ls","-lh"])
# print(p.communicate())
# time.sleep(1)
# # Get the process id
# pid = p.pid
# os.kill(pid, signal.SIGINT)
# if not p.poll():
#     print ("Process correctly halted")
def show_setting_prgrp():
    print('Calling os.setpgrp() from {}'.format(os.getpid()))
    os.setpgrp()
    print('Process group is now {}'.format(os.getpgrp()))
    sys.stdout.flush()

# def kill(proc_pid):
#     process = psutil.Process(proc_pid)
#     for proc in process.children(recursive=True):
#         proc.kill()
#     process.kill()


c = subprocess.Popen(['rosrun openvslam node-python.py -nome'], \
 shell=True, preexec_fn= os.setsid)

# d = subprocess.Popen(['rosrun turtlesim turtlesim_node'], \
# shell=True, preexec_fn= os.setsid)

# e = subprocess.Popen(['rosrun turtlesim turtle_teleop_key'], \
# shell=True, preexec_fn= os.setsid)

# e = subprocess.Popen(['killall','-9','rosmaster'], \
# shell=True, preexec_fn= os.setsid)

time.sleep(8)
os.killpg(os.getpgid(p.pid), signal.SIGTERM)  # Send the signal to all the process groups
os.killpg(os.getpgid(c.pid), signal.SIGTERM)  # Send the signal to all the process groups
#os.killpg(os.getpgid(d.pid), signal.SIGTERM)  # Send the signal to all the process groups

#p.send_signal(signal.SIGINT)   # send Ctrl-C signal

#e = subprocess.Popen(['killall -9 rosmaster'], \
#shell=True, preexec_fn= os.setsid)

if not p.poll():
    print("Process halted")
pid = p.pid
os.kill(pid, signal.SIGINT)

#Ideia: matar todos os terminais do ros... pelo ros msm.