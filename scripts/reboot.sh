kill -9 $(pidof python) || true; nohup python /srv/studjobb.no/src/webserver/webserver.py > /dev/null 2>&1 &
