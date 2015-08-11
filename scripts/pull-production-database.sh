ssh michael@studjobb.no "mysqldump --single-transaction studjobb_rewrite | gzip -c" | gunzip -c | mysql -u root studjobb_rewrite
