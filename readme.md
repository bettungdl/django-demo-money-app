albmtz@gmail.com
Pass.W0rd$ <- el pass del admin
 
ip 192.168.146.131
cd /var/www/html/proyecto_nuevo/server/
source ./envs/paypal/bin/activate
cd paypal
python3 manage.py runserver 192.168.146.131:8000

cd /var/www/html/proyecto_nuevo/app/
npx expo start
