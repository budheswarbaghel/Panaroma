# Panaroma

Panaroma is a django based web application to upload and view the articles.
View the original repository in my gitlab profile -> [Panaroma] (https://gitlab.com/budheswarbaghel/panaroma)
___

### Preview

![alt text](https://i.imgur.com/alKJllA.png "Preview of the home page")
___

### Installation

* Setup the python virtual environment (_for example:_)
    ```bash
    pip install virtualenv
    mkdir ~/.virtualenv && cd ~/.virtualenv
    virtualenv django-panaroma
    ```

* Clone the repository
    ```bash
    git clone https://gitlab.com/budheswarbaghel/panaroma.git
    ```
* Activate the virtualenv
    ```bash
    #To activate the virtualenv
    source ~/.virtualenv/django-panaroma/bin/activate
    ```
* pip install the requirement packages
    ```bash
    pip install -r requirements.txt
    ```
* Essential commands to load the database and staticfiles
    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py collectstatic
    python3 manage.py createsuperuser
    python3 manage.py runserver
    ```
___

### Features

* User profile
* Login & logout from account
* Create new account
* Post new article
* Update and delete your article
* View articles in detail

```bash
___________.__             ___________           .___
\__    ___/|  |__   ____   \_   _____/ ____    __| _/
  |    |   |  |  \_/ __ \   |    __)_ /    \  / __ | 
  |    |   |   Y  \  ___/   |        \   |  \/ /_/ | 
  |____|   |___|  /\___  > /_______  /___|  /\____ | 
                \/     \/          \/     \/      \/ 
```
