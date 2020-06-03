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

## Systemd service

* see gunicorn-systemd.template.service
* replace SITENAME with, eg. staging.2ndlvldomain.topllvldomain (staging.webstie.com)

## Folder structure:

/home/user
- /sites
    - /SITENAME
        - /database
        - /source
        - /static
        - /virtualenv