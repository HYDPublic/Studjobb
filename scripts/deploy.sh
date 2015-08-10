ssh -o "StrictHostKeyChecking no" -i scripts/id_rsa michael@studjobb.no "ifconfig > ~/hey.txt"
scp -o StrictHostKeyChecking=no -i scripts/id_rsa -r ./ michael@studjobb.no:/~
