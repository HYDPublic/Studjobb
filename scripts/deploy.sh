rsync --exclude='.git/' --exclude='config'  -Pav -e 'ssh -o StrictHostKeyChecking=no -i scripts/id_rsa -C -c blowfish' . michael@studjobb.no:/srv/studjobb.no
