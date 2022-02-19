install vitualbox
install vagrant


<!-- vagrant commands -->
vagrant init hashicorp/bionic64
vagrant up
vagrant ssh
<!-- once it's setup it will be faster to suspend and resume the vm -->
vagrant suspend
vagrant resume

configure apache: 
https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-18-04

python3.10 -m venv ./venv
pip install flask
pip install mod-wsgi

mod_wsgi-express module-config
take the output of that and put it in the .conf file
