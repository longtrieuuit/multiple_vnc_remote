
docker run -p 7005:5901 --restart always --shm-size=512m -e VNC_RESOLUTION=1920x1080 -e VNC_PW=vnc_password --user $(id -u):$(id -g) -v /home/dev_coin/autoremote/:/home/autoremote/ --name AIR_REMOTE -it longtrieuuit/chrome-debian11-xfce-vnc:suiwallet /bin/bash
