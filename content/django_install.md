* [Configuration Options](#configuration-cptions)
* [System Prep](#system-prep)
* [Django Install](#django-install)

## Installing the Django [web framework](https://github.com/src-its/ca-web/blob/master/content/web-framework_definition.md)

Django is a full-featured Python web framework for developing dynamic websites and applications. [ref: Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-14-04)

<a href="#configuration-cptions"></a>
## Be Aware of Configuration Options:

There are a number of different ways in which you can install Django depending upon your needs and how you want to configure your development environment. These have different advantages and one method may lend itself better to your specific situation than others.

Some of the different methods are:

* **Global Install from Packages**: The official Ubuntu repositories contain Django packages that can be installed easily with the conventional apt package manager. This is very simple, but not as flexible as some other methods. Also, the version contained in the repositories may lag behind the official versions available from the project.

* **Global Install through pip**: The pip tool is a package manager for Python packages. If you install pip, you can easily install Django on the system level for use by any user. This should always contain the latest stable release. Even so, global installations are inherently less flexible.

* **Install through pip in a Virtualenv**: The Python virtualenv package allows you to create self-contained environments for various projects. Using this technology, you can install Django in a project directory without affecting the greater system. This allows you to provide per-project customizations and packages easily. Virtual environments add some slight mental and process overhead in comparison to globally accessible installation, but provide the most flexibility. **This is the installation method that we use (detailed below).**

* **Development Version Install through git**: If you wish to install the latest development version instead of the stable release, you will have to acquire the code from the git repo. This is necessary to get the latest features/fixes and can be done globally or locally. Development versions do not have the same stability guarantees, however.

----
<a href="#system-prep"></a>
## System Prep

1. Enable the [universe repository](https://help.ubuntu.com/community/Repositories/CommandLine).

1. Install the following packages (N.B. the libxml2-dev package does **NOT** have a one before the two; that is a lower case L):

        sudo apt-get install libblas3gf libc6 libamd2.3.1 libumfpack5.6.2 \
        libgcc1 libgfortran3 liblapack3gf libstdc++6 \
        build-essential gfortran libatlas-dev libjpeg-dev libfreetype6-dev \
        python python-all-dev gcc g++ libblas-dev liblapack-dev libevent-dev \
        libxml2-dev libxslt1-dev

<!--
elaborate here about the purpose and function of each pakage:

 libblas3gf
 libc6
 libamd2.3.1
 libumfpack5.6.2
 libgcc1
 libgfortran3
 liblapack3gf
 libstdc++6

 build-essential

 gfortran

 libatlas-dev
 libjpeg-dev
 libfreetype6-dev

 python
 python-all-dev

 gcc
 g++

 libblas-dev
 liblapack-dev
 libevent-dev
 libxml2-dev
 libxslt1-dev
-->

3. Link image libraries to standard Debian locations

   Ubuntu has these in an 'unusual' location for debian, so the following links ensure that things like Pillow find them.

        sudo ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib
        sudo ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib
        sudo ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib
> **Note:** Make sure these links are valid if you are installing into a new version of Ubuntu (other than 14.04)

1. Install geospatial libraries

<!--We should note why we're asking users to do this-->

        sudo apt-get install binutils libproj-dev gdal-bin libgeo-proj4-perl libjson0-dev

1. Install [PostGIS](http://trac.osgeo.org/postgis/wiki/UsersWikiPostGIS20Ubuntu1204)

        sudo apt-get install postgresql-9.3-postgis-2.1
        sudo apt-get install postgresql-server-dev-9.3

1. [Install Git](http://git-scm.com/book/en/Getting-Started-Installing-Git):

        sudo apt-get install libcurl4-gnutls-dev libexpat1-dev gettext libz-dev libssl-dev
        sudo apt-get install git

1. [Install pip](https://pip.pypa.io/en/stable/installing/)

    **[pip](https://pip.pypa.io)** is used to conveniently install Python modules needed for the project.

    pip is already installed if you're using Python 2 >=2.7.9 or Python 3 >=3.4 downloaded from python.org. Verify this by entering `which pip` into the terminal. You should get an output like this:

            >> /usr/local/bin/pip

    If pip is not installed, first download [get-pip.py](https://bootstrap.pypa.io/get-pip.py)

        wget https://bootstrap.pypa.io/get-pip.py

    Then run the following:

        sudo python get-pip.py

    Alternatively, you can use the Ubuntu package manager to install pip for you:

        sudo apt-get install python-pip

    If you plan on using version 3 of Python, you can install pip and virtualenv by typing:

        sudo apt-get install python3-pip

1. Install virtualenv

   Once pip is installed, you can use it to install the virtualenv package. If you installed the Python 2 pip, you can type:

        sudo pip install virtualenv

   For Python 3, you can install virtualenv by typing:

        sudo pip3 install virtualenv

1. [Install virtualenwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/install.html)

        sudo apt-get install virtualenvwrapper

1. Create a file directory for your project:

        mkdir ca-web

1. Create a new virtual environment for your project

        mkvirtualenv ca-web

   **NOTE:** IThis will install a standalone version of Python, as well as pip, into an isolated directory structure within your project directory. We chose to call our virtual environment `newenv` but you should name it something descriptive. A directory will be created with the name you select, which will hold the file hierarchy where your packages will be installed.

---

   **NOTE:** If the `mkvirtualenv` returns a "command not found" error, follow these steps:

   - check that `virtualenvwrapper.sh` is in `/usr/local/bin`; if not, use `locate virtualenvwrapper.sh` and then `ln -s` to the install location
   - use the `source` command to pass the contents of 'virtualenvwrapper.sh'to the Tcl interpreter:

         `~ $ source /usr/local/bin/virtualenvwrapper.sh`

   - verify that this works by re-running the virtualenv command:

         `~ $ mkvirtualenv ca-web`

   - exit virtualenv and `echo` the `source` command into the local user's `.bashrc`:

         `~ $ deactivate`
         `~ $ echo 'source /usr/local/bin/virtualenvwrapper.sh' >> .bashrc`

   - verify contents of `.bashrc`

         `~ $ tail .bashrc`

1. Configure the virtual environment to work with the application without needing to directly invoke 'manage.py':

   - ensure that you're in your project working directory (we're using ca-web as our example).

   - Switch to the virtual environment.

                 workon newenv

   - in the root directory (the working copy clone target), set up the project and add the folder to the path.

                 cd ca-web
                 add2virtualenv .
                 setvirtualenvproject

   - ... this will move you into this directory when you 'workon' the virtualenv in future and it will ensure that python searches for modules in this directory.

---

** For a one-off system prep and environment build on Ubuntu 14.04, you can use to following code (which basically re-produces all the steps given above):

```
sudo apt-get update;
sudo apt-get upgrade;
sudo apt-get install libblas3gf libc6 libamd2.3.1 libumfpack5.6.2 libgcc1 libgfortran3 liblapack3gf libstdc++6 build-essential gfortran libatlas-dev libjpeg-dev libfreetype6-dev python python-all-dev gcc g++ libblas-dev liblapack-dev libevent-dev libxml2-dev libxslt1-dev;
sudo ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib;
sudo ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib;
sudo ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib;
sudo apt-get install binutils libproj-dev gdal-bin libgeo-proj4-perl libjson0-dev;
sudo apt-get install postgresql-9.3-postgis-2.1;
sudo apt-get install postgresql-server-dev-9.3;
sudo apt-get install libcurl4-gnutls-dev libexpat1-dev gettext libz-dev libssl-dev;
sudo apt-get install git;
wget https://bootstrap.pypa.io/get-pip.py;
sudo python get-pip.py;
sudo pip install virtualenv;
sudo pip install pyopenssl ndg-httpsclient pyasn1;
sudo apt-get install virtualenvwrapper;
sudo ln -s /usr/share/virtualenvwrapper/virtualenvwrapper.sh /usr/local/bin/;
source /usr/local/bin/virtualenvwrapper.sh;
cd;
echo 'source /usr/local/bin/virtualenvwrapper.sh' >> .bashrc;
mkdir ca-web;
cd ca-web;
mkvirtualenv ca-web
add2virtualenv .
setvirtualenvproject
deactivate
```

<a href="#django-install"></a>
## Django Install

1. After you’ve created and activated a virtual environment, use pip to install Django

        pip install Django

    - After running this command, you should receive a confirmation message that Django is installed.  At this point, however, you will not have any files or folders within your `ca-web` directory. You can tell Django is installed and which version by running the following command:

        python -c "import django; print(django.get_version())"

    - Next, we need to establish a Django 'project'&mdash;a collection of settings for an instance of Django, including database configuration, Django-specific options and application-specific settings.

---

<!-- NOTE: The installation instructions given below need to be updated -->


1. Clone our mezzanine fork

We are using a fork of mezzanine which currently needs to be cloned alongside the project.

```
git clone https://github.com:src-its/mezzanine.git
```

1. Clone the repository and install the requirements

         workon ca-web
         (ca-web)~ $ git clone git@github.com:src-its/django-ca
         (ca-web)~ $ cd django-ca
         (ca-web)~/django-ca$ pip install -r requirements.txt

This installs Django, Mezzanine and the other required Python modules.

1. Generate your local copy of `secrets.py` from `cccs.settings.secrets.example.py` and place it in `~/django-ca/core/settings`:

         (src-its)~/django-ca$ cd core/settings/
         (src-its)~/django-ca/core/settings$ cp secrets.py.example secrets.py

Set its values appropriately for the database you are working with. If creating a local test database where security it not an issue, the values in the  example file may be fine.

1. Set the default settings module

        (src-its) ~/django-ca $ echo 'export DJANGO_SETTINGS_MODULE=core.settings' >> ~/.virtualenvs/src-its/bin/postactivate
   **NOTE:** This command may need editing for your particular set-up. It adds the assignment of the DJANGO_SETTINGS_MODULE to the python module responsible for supplying the django settings.  For the mapping app, use:

        (src-its) ~/django-ca $ echo 'export DJANGO_SETTINGS_MODULE=core.settings.local' >> ~/.virtualenvs/src-its/bin/postactivate

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


### references:


Justin Ellingwood. 2015-Mar-05. "How To Install the Django Web Framework on Ubuntu 14.04" https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-14-04

Kenneth Reitz Project. 2016. "Virtual Environments" **Python Guide.** http://docs.python-guide.org/en/latest/dev/virtualenvs/
