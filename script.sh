sudo apt-get build-dep python-mysqldb
mysql -u root -p < bd.sql
python setup.py install