## Initializing the [ca-web](https://github.com/src-its/django-ca) Django Application

1. Ensure that your [ssh keys are entered into your profile](/content/git_ssh-setup.md).

1. Clone the repository and install the requirements

         workon ca-web
         (ca-web)~ $ git clone git@github.com:src-its/django-ca ca-web
         (ca-web)~ $ cd ca-web
         (ca-web)~/ca-web$ pip install -r requirements.txt

    - This installs Django, Mezzanine and the other required Python modules.

1. Configure the virtual environment to work with the application without needing to directly invoke 'manage.py':

   - ensure that you're in your project working directory (we're using ca-web as our example).

   - Switch into the virtual environment.

                 workon ca-web

   - set up the project and add the folder to the path.

                 add2virtualenv .
                 setvirtualenvproject

   - ... this will move you into this directory when you 'workon' the virtualenv in future and it will ensure that python searches for modules in this directory.

1. Generate a `secrets.py` file from the template `secrets.example.py` under `core` > `settings`. :

         (ca-web)~/ca-web$ cd core/settings/
         (ca-web)~/ca-web/core/settings$ cp secrets.py.example secrets.py

    - NOTE: The `secrets.py` file contains your credentials for connecting to your database.  Be sure to change the salt values in this file and enter the user name and password that you will use when establishing your database connection.

1. Generate a `settings.py` file based on any of the examples under `core` > `settings`. :

         (ca-web)~/ca-web$ cd core/settings/
         (ca-web)~/django-ca/core/settings$ cp aaron.py ca.py

    - Set its values appropriately for the database you are working with.

1. Define your settings as the default:

        (src-its) ~/django-ca $ echo 'export DJANGO_SETTINGS_MODULE=core.settings.ca' >> ~/.virtualenvs/ca-web/bin/postactivate
        
   **NOTE:** This command may need editing for your particular set-up. It adds the assignment of the DJANGO_SETTINGS_MODULE to the python module responsible for supplying the django settings.

1. alias django into your `~/.bashrc`

        `alias django='django-admin.py'`)

1. log out and back into your virtual environment in order to ensure that the alias takes effect:

        deactivate
        workon ca-web

    - Your prompt should change to reflect that you are now in your virtual environment. It will look something like this
    
```
     (ca-web)src-its@ubuntu:~/ca-web$.

```


#### Set up postgresql

1. Adjust your settings for postgres. The psql database user (e.g. caweb) must use `md5` rather than peer access. To enable this, edit `/etc/postgresql/9.3/main/pg_hba.conf`.  Add add a line for `username` and specify md5 access:

```
     # TYPE  DATABASE        USER            ADDRESS                 METHOD
      local   all            its                                     md5
```

   - Postgres can be fiddly to set up. Google is your friend.

1. Switch to postgres and add yourself as a super user:

        ~ $ sudo -iu postgres
        ~ $ psql -c 'CREATE USER <username> WITH SUPERUSER;'


*When creating a database from scratch* (for a 'vanilla' copy of this work environment):

1. Add the `caweb` user.

         ~ $ psql -c "CREATE USER caweb WITH PASSWORD 'password';"

1. Create the `caweb` database.

         ~ $ psql -c "CREATE DATABASE caweb;"
         
1. Change ownership of the `caweb` database to the `caweb` user.

         ~ $ psql -c "ALTER DATABASE caweb OWNER TO caweb;"

1. Now drop directly into psql as the `caweb` user:

         psql caweb
         
1. Your terminal should change to something like this:

         caweb=#

1. Enable your empty database for post-GIS:

         caweb=# CREATE EXTENSION postgis;
         caweb=# CREATE EXTENSION postgis_topology;


1. Ensure that the `caweb` user has full access:

        ~ $ psql -c "GRANT ALL PRIVILEGES ON DATABASE django-ca TO its;"

1. Log out of the postgres user with `CTRL + D`

1. Once you're back in your virtual environment, create the database:

        (ca-web)~ $ django createdb


**NOTE**: You may encounter some errors here; especially if you are installing with Ubuntu 14.04. Common ones:
   * `django.core.exceptions.ImproperlyConfigured: Cannot determine PostGIS version`

   You need to explicitly define your`POSTGIS_VERSION`. If this is the case, and if you are using a `dev.py` or `production.py`, it's recommended that you `cp` your `*.py` module to a new local version for your and keep it out of git.  


---

1. *To restore a dump it on the target system*:

        ~ $ pg_restore -d postgres -C django-ca.pg_dump
   **NOTE:** The procss for making the database dump is to use `pg_dump` thus:

            ~ $ pg_dump -o -Fc django-ca >> django-ca.pg_dump

1. Sync the database:

        (ca-web)~ $ django syncdb
---



##### Dealing with locale issues

Postgres is very fussy about database locales. If the database you attempt to restore was created in a different locale, you may find that it will fail with an "Invalid locale name: <locale_name>". If this happens, add the locale and restart the postgres service:

    ~ $ sudo locale-gen en_AU.UTF-8
    Generating locales...
      en_AU.UTF-8... done
    Generation complete.
    ~ $ sudo service postgresql restart
     * Restarting PostgreSQL 9.3 database server     [ OK ]

#### Install Nginx and upstart job

This is for public facing servers only.

         ~ $ sudo apt-get install nginx
         ~ $ sudo ln -s /home/<user>/production/_deploy/production_nginx /etc/nginx/sites-available/production
         ~ $ sudo ln -s /etc/nginx/sites-available/production /etc/nginx/sites-enabled/production
         ~ $ sudo service nginx restart
         ~ $ sudo cp production/_deploy/production_upstart.conf /etc/init/webcore_production.conf
         ~ $ sudo service webcore_production start

#### Start your local test site!

    django runserver

--

It is not possible to provide a on-off deployment script for this process due to the need to edit configuration files, as provided above.  The following code block consolidates the steps defined above.  Use it for references purposes only.

```
git clone git@github.com:src-its/django-ca ca-web;
cd ca-web;
mkvirtualenv ca-web;
add2virtualenv .;
setvirtualenvproject;
deactivate;
workon ca-web;
pip install -r requirements.txt
cd core/settings/;
cp secrets.py.example secrets.py;
cp aaron.py.example ca.py;
vim ca.py;
## ENTER YOUR SETTINGS HERE
echo 'export DJANGO_SETTINGS_MODULE=core.settings.ca' >> ~/.virtualenvs/ca-web/bin/postactivate;
deactivate;
sudo service postgres restart;
## MAKE YOUR CONFIGURATIONS
sudo /etc/init.d/postgresql restart;
workon ca-web;
django createdb;
```
