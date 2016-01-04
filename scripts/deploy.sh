rsync --exclude='.git/' -Pav -e 'ssh -o StrictHostKeyChecking=no -i scripts/id_rsa -C -c blowfish' . michael@studjobb.no:/srv/studjobb.no
ssh -o StrictHostKeyChecking=no -i scripts/id_rsa michael@studjobb.no '/srv/studjobb.no/scripts/reboot.sh' 
