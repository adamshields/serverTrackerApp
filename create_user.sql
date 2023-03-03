create user serverdbadmin identified BY '12345';
grant all on serverdb.* to 'serverdbadmin'@'%';
flush privileges;