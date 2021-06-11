# postgresql 

* sudo apt-get update
* sudo apt-get install postgresql-12
* sudo nano /etc/postgresql/12/main/pg_hba.conf

1. sudo service postgresql start
2. sudo passwd postgres
3. su postgres
4. create database test_db;
5. create user "test_user" with encrypted password 'securep@ss_here';
6. grant all privileges on database test_db to test_user;
7. sudo service postgresql restart

## any peer issue pops up then :-

1. edit :-  /etc/postgresql/12/main/pg_hba.conf*
2. change peer to md5 of unix