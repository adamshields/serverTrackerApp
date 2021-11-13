create user dbadmin identified BY '12345';
grant all on mothership.* to 'dbadmin'@'%';
flush privileges;