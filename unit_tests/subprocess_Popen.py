import subprocess
import time
import os
import signal
import glob

for i in range(2):
    try:
        time.sleep(3)
        p_core = subprocess.Popen('roscore')

        p_transport = subprocess.Popen(['rosrun', 'image_transport',
                                        'republish',
                                        'raw', 'in:=/video/image_raw',
                                        'raw', 'out:=/camera/image_raw', ],
                                       preexec_fn=os.setpgrp)

        p_pkl = subprocess.Popen(['rosrun', 'openvslam',
                                  'cam_pose2pkl.py',
                                  'map_name_debug'],
                                 preexec_fn=os.setpgrp)

        base_path = '/home/paulo/openvslam/openvslam/build'
        test = 'test-debug'

        video_names = glob.glob(base_path+'/{}/videos/*.MP4'.format(test))
        print("Detected videos: {}".format(video_names[0]))

        vocab_path = base_path+'/orb_vocab/orb_vocab.dbow2'
        config_path = base_path+'/{}/videos/gopro.yaml'.format(test)
        print("Config path : \n{}".format(config_path))
        map_path = base_path+'/{}/maps/{}.msg'.format(test, "mapa_teste")

        # Call video publisher node
        p_video = subprocess.Popen(['rosrun', 'publisher',
                                    'video', '-m',
                                    '{}'.format(video_names[0])],
                                   preexec_fn=os.setpgrp)
        time.sleep(2)
        p_slam = subprocess.Popen(['rosrun', 'openvslam',
                                   'run_slam',
                                   '-v', '{}'.format(vocab_path),
                                   '-c', '{}'.format(config_path),
                                   '--map-db', '{}'.format(map_path),
                                   'frame-skip {}'.format(0),
                                   '--no-sleep',
                                   '--auto-term'],
                                  preexec_fn=os.setpgrp)
        p_slam.wait()
        p_core.terminate()
        time.sleep(10)
    # p_slam.send_signal(signal.SIGINT)
    # p_transport.send_signal(signal.SIGINT)
    # time.sleep(3)

    # p_video.send_signal(signal.SIGINT)
# #    p.terminate()
#     time.sleep(5)
#     # It will create process group with id same as p1.pid
#     os.setpgrp(p_transport.pid, 0)/id))
#     os.setpgrp(p_video.pid, os.getpgid(p_transport.pid))
#     os.setpgrp(p_pkl.pid, os.getpgid(p_transport.pid))

#     os.killpg(os.getpgid(p_transport.pid), signal.SIGTERM)
# \
#     time.sleep(10)
#     os.killpg(os.getpgid(p_transport.pid), signal.SIGTERM)
#     os.killpg(os.getpgid(p_slam.pid), signal.SIGINT)
#     os.killpg(os.getpgid(p_pkl.pid), signal.SIGTERM)
#     #os.killpg(os.getpgid(p_transport.pid), signal.SIGTERM)

    # os.kill(pid, signal.SIGINT)
    except KeyboardInterrupt:
        p_transport.send_signal(signal.SIGINT)
        p_transport.wait()
    time.sleep(2)
