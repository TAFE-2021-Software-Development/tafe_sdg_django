echo Script started
apt update && apt upgrade
echo Installing pip
apt install python3-pip
echo Installing MySQL
apt install mysql-server
echo Setting up MySQL
mysql_secure_installation
echo Creating table
mysql
cd Djano2/app
echo installing dependencies
apt install python3-dev build-essential
apt install libssl1.1
apt install libssl1.1=1.1.1f-1ubuntu2
apt install libssl-dev
apt install libmysqlclient-dev
pip3 install mysqlclient
pip3 install -r ./app/reqs.txt
echo Script complete now edit settings.py and run setup-server.sh
