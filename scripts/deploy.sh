echo "changing permission"
ls
chmod 600 scripts/id_rsa
ssh -o "StrictHostKeyChecking no" -i scripts/id_rsa michael@studjobb.no echo "lol" > hey
