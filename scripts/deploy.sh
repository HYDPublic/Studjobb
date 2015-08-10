ssh -o "StrictHostKeyChecking no" -i scripts/id_rsa michael@studjobb.no "ifconfig > ~/hey.txt"
scp -o "StrictHostKeyChecking no" -i scripts/id_rsa -r scripts/deploy.sh michael@studjobb.no:/home/michael/
