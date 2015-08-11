scp -o "StrictHostKeyChecking no" -i scripts/id_rsa --exclude .git --exclude config -r . michael@studjobb.no:/srv/studjobb.no
