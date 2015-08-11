rsync -Pav -e 'ssh -o StrictHostKeyChecking=no -i scripts/id_rsa -C -c blowfish' . michael@studjobb.no:/srv/studjobb.no

#scp -o "StrictHostKeyChecking no" -i scripts/id_rsa --exclude .git --exclude config -r . michael@studjobb.no:/srv/studjobb.no
