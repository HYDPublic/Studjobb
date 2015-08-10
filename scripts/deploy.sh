chmod 600 id_rsa
ssh -o "StrictHostKeyChecking no" -i id_rsa michael@studjobb.no echo "lol" > hey
