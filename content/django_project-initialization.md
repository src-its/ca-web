## Initializing the *ca-web* Django Application

1. Clone the repository and install the requirements

         workon ca-web
         (ca-web)~ $ git clone git@github.com:src-its/django-ca ca-web
         (ca-web)~ $ cd ca-web
         (ca-web)~/ca-web$ pip install -r requirements.txt

This installs Django, Mezzanine and the other required Python modules.

1. Configure the virtual environment to work with the application without needing to directly invoke 'manage.py':

   - ensure that you're in your project working directory (we're using ca-web as our example).

   - Switch to the virtual environment.

                 workon newenv

   - in the root directory (the working copy clone target), set up the project and add the folder to the path.

                 cd ca-web
                 add2virtualenv .
                 setvirtualenvproject

   - ... this will move you into this directory when you 'workon' the virtualenv in future and it will ensure that python searches for modules in this directory.

1. Generate a `secrets.py` file from the template `secrets.example.py` under `core` > `settings`. :

         (ca-web)~/ca-web$ cd core/settings/
         (ca-web)~/ca-web/core/settings$ cp secrets.py.example secrets.py

1. Generate a `settings.py` file based on any of the examples under `core` > `settings`. :

         (ca-web)~/django-ca/core/settings$ cp aaron.py ca.py

    - Set its values appropriately for the database you are working with.

1. Define your settings as the default:

        (src-its) ~/django-ca $ echo 'export DJANGO_SETTINGS_MODULE=core.settings.ca' >> ~/.virtualenvs/ca-web/bin/postactivate
   **NOTE:** This command may need editing for your particular set-up. It adds the assignment of the DJANGO_SETTINGS_MODULE to the python module responsible for supplying the django settings.

1. alias django into your `~/.bashrc` (`alias django='django-admin.py'`), then log out and log back in to ensure that the alias takes effect.

#### Set up postgresql

   **NOTE** The psql database user (e.g. its) must use `md5` rather than peer access for postgres. To enable this, you will likely need to edit `/etc/postgresql/9.3/main/pg_hba.conf`.  Add add a line for `username` and specify md5 access:

     # TYPE  DATABASE        USER            ADDRESS                 METHOD
      local   all            its                                     md5

   Postgres can be fiddly to set up. Google is your friend.

1. Switch to postgres and add yourself as a super user:

        ~ $ sudo -iu postgres
        ~ $ psql -c 'CREATE USER <username> WITH SUPERUSER;'

1. Add the `src-its` database and user.

         ~ $ psql -c "CREATE USER its WITH PASSWORD 'password';"

2. *When creating a database from scratch* (for a 'vanilla' copy of this work environment):

         (src-its)~ $ django createdb
   Then postgis enable the result:

         (src-its)~ $ psql django-ca
         django-ca=# CREATE EXTENSION postgis;
         django-ca=# CREATE EXTENSION postgis_topology;

2. *To restore a dump it on the target system*:

        ~ $ pg_restore -d postgres -C django-ca.pg_dump
   **NOTE:** The procss for making the database dump is to use `pg_dump` thus:

            ~ $ pg_dump -o -Fc django-ca >> django-ca.pg_dump

1. Ensure that the user has full access:

        ~ $ psql -c "GRANT ALL PRIVILEGES ON DATABASE django-ca TO its;"

6. Sync the database:

        (src-its)~ $ django syncdb

**NOTE**: You may encounter some errors here; especially if you are installing with Ubuntu 14.04. Common ones:
   * `django.core.exceptions.ImproperlyConfigured: Cannot determine PostGIS version`

   You need to explicitly define your`POSTGIS_VERSION`. If this is the case, and if you are using a `dev.py` or `production.py`, it's recommended that you `cp` your `*.py` module to a new local version for your and keep it out of git.  

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

#### Start your test local test site!

    django runserver

#### The User Interface

##### Setting up the CSS build

In order to get Sass and Compass working we need to have their Ruby gems installed.

1. Make sure you've got Ruby 1.9.3+

2. In the `cccs_web/theme/scss/` add a file named `Gemfile` pasting this content in:
````
      source "https://rubygems.org
      gem "sass
      gem "compass
````
Save the file and run `gem install bundler` (you might need sudo).
Now, from `scss/` folder (the one where Gemfile lives) you can do `bundle install` which will install the gems listed in the `Gemfile` and their dependencies. This will also create a Gemfile.lock file which is the result of installed gems.

3. In the same `cccs_web/theme/scss/` create a new file named `config.rb` with this content:
````
      # Get the directory that this configuration file exists in
      dir = File.dirname(__FILE__)

      # The output style // :expanded or :nested or :compact or :compressed
      output_style = :compressed

      # Set this to the root of your project when deployed:
      # http_path = "/"
      css_dir = "../static/css"
      sass_dir = ""
      images_dir = "../static/imgs"
      javascripts_dir = "../static/js"
      relative_assets = true

      # Compass configurations
      sass_path = dir
      css_path = File.join(dir, "../../static_collected/", "css")
````
This will setup the necessary Compass information to compile and build Sass to CSS.

Now we can:
````
      compass compile # compiles the scss/ folder into the destination file based on the settings provided in config.rb
      compass watch # watches any changes in the Sass files during the development and automatically overrides the destination files (eg. our app.css)
      compass clean # removes the destination files and .sass-cache/ folder placed in the Sass folder (eg. cccs_web/theme/scss)
````
At the moment, in config.rb, I've chosen that the Compass compiles the CSS into the `static_collected/` folder because this way I don't have to `django collectstatic` everytime I change something in the Sass files.

In the HTML template `<header>` a simple `<link>` to the build is enough, loading a single minified css file.
( there'll be four different css builds: app.css for modern broswers, ie78.css for old Exploders, text.css for text browsers and jsoff.css for the cases when javascript is off )

##### Javascript

The javascript layer is built using a `Require.js` AMD style.

In the `<head>` section of our template we load the first necessary two files. We do this in the `<head>` for two reasons:
- Modernizr is a library that likes to be loaded in the head. It detects the browsers capabilities and add a list of classes in the `<html>` tag that tells everything about the client, eg. `js, xhr2, rgba` etc
- we pull from CDN therefore we don't have to wait for those requests until the DOM is loaded. However with require.js we can control when the javascript are loaded.

`<script data-main="{% static "js/app/config/init" %}" src="{% static "js/libs/require.js" %}" type="text/javascript"></script>`

First we need `require.js` and then we provide a configuration file (eg. `init.js`)

In the init.js we have the global configuration file which maps and shims all the AMD modules. It will also call app.js as first dependency.

App.js will first require the first and most important libraries as AMD modules and then once they're loaded, in the callback we can start doing our first checkings and logic.

An example: say we now found with modernizr.js IE8 - we will then provide async js polyfills as AMD modules one by one to make it understand media queries, svg, rgba all we need depending on the page we're on. These are cachable.

Then we coud also make REST operations and various DOM manipulation organised on AMD modules called when needed etc.


--


```
git clone git@github.com:src-its/django-ca ca-web
cd ca-web;
mkvirtualenv ca-web
add2virtualenv .
setvirtualenvproject
deactivate
workon ca-web
cd core/settings/
cp secrets.py.example secrets.py
cp aaron.py.example ca.py
vim ca.py
## ENTER YOUR SETTINGS here
echo 'export DJANGO_SETTINGS_MODULE=core.settings.ca' >> ~/.virtualenvs/ca-web/bin/postactivate
deactivate
sudo service postgres restart
## MAKE YOUR configurations
sudo /etc/init.d/postgresql restart
workon ca-web
django createdb
```





----


1. Set the default settings module

        (newenv) ~/ca-web $ echo 'export DJANGO_SETTINGS_MODULE=core.settings' >> ~/.virtualenvs/newenv/bin/postactivate
   **NOTE:** This command may need editing for your particular set-up. It adds the assignment of the DJANGO_SETTINGS_MODULE to the python module responsible for supplying the django settings.  For the mapping app, use:

        (newenv) ~/ca-web $ echo 'export DJANGO_SETTINGS_MODULE=core.settings.local' >> ~/.virtualenvs/newenv/bin/postactivate

1. alias django into your `~/.bashrc` (`alias django='django-admin.py'`)


---
To install packages into the isolated environment, you must activate it by typing:

        source newenv/bin/activate

Your prompt should change to reflect that you are now in your virtual environment. It will look something like (newenv)username@hostname:~/newproject$.

In your new environment, you can use pip to install Django. Regardless of whether you are using version 2 or 3 of Python, it should be called just pip when you are in your virtual environment. Also note that you do not need to use sudo since you are installing locally:

        pip install django

You can verify the installation by typing:

        django-admin --version

To leave your virtual environment, you need to issue the deactivate command from anywhere on the system:

        deactivate

Your prompt should revert to the conventional display. When you wish to work on your project again, you should re-activate your virtual environment by moving back into your project directory and activating:

        cd ~/newproject
        source newenv/bin/activate
