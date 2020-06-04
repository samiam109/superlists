Provisioning a new site
=======================
## Required packages:

* nginx
* Python3.6
* virtualenv + pip
* Git

eg, on Ubuntu:

    sudo add-apt-repository ppa:fkrull/deadsnakes
    sudo apt install nginx git python36 python3.6-venv
    
## Nginx Virutal Host Config

* see nginx.template.conf
* replace SITENAME with, eg. staging.2ndlvldomain.topllvldomain (staging.webstie.com)
* sudo sed "s/SITENAME/SITENAME/g" \
 source/deploy_tools/nginx.template.conf \
 | sudo tee /etc/nginx/sites-available/SITENAME
* sudo ln -s /etc/nginx/sites-available/SITENAME \
 /etc/nginx/sites-enabled/SITENAME

## Systemd service

* see gunicorn-systemd.template.service
* replace SITENAME with, eg. staging.2ndlvldomain.topllvldomain (staging.webstie.com)
* sudo sed "s/SITENAME/SITENAME/g" \
 source/deploy_tools/gunicorn-systemd.template.service \
 | sudo tee /etc/systemd/system/gunicorn-SITENAME.service

## Folder structure:

/home/user
- /sites
    - /SITENAME
        - /database
        - /source
        - /static
        - /virtualenv