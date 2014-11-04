ssh michael@146.185.190.144 'cd /var/www/studjobb; git fetch --all; git reset --hard origin/development';
scp -r crawler/ michael@146.185.190.144:/var/www/studjobb/
