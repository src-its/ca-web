

## Installing the Django [web framework](https://github.com/src-its/ca-web/blob/master/content/web-framework_definition.md)

Django is a full-featured Python web framework for developing dynamic websites and applications. [ref: Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-14-04)



There are a number of different ways in which you can install Django depending upon your needs and how you want to configure your development environment. These have different advantages and one method may lend itself better to your specific situation than others.

Some of the different methods are below:

* **Global Install from Packages**: The official Ubuntu repositories contain Django packages that can be installed easily with the conventional apt package manager. This is very simple, but not as flexible as some other methods. Also, the version contained in the repositories may lag behind the official versions available from the project.

* **Global Install through pip**: The pip tool is a package manager for Python packages. If you install pip, you can easily install Django on the system level for use by any user. This should always contain the latest stable release. Even so, global installations are inherently less flexible.

* **Install through pip in a Virtualenv**: The Python virtualenv package allows you to create self-contained environments for various projects. Using this technology, you can install Django in a project directory without affecting the greater system. This allows you to provide per-project customizations and packages easily. Virtual environments add some slight mental and process overhead in comparison to globally accessible installation, but provide the most flexibility. **This is the installation method that we use (detailed below).**

* **Development Version Install through git**: If you wish to install the latest development version instead of the stable release, you will have to acquire the code from the git repo. This is necessary to get the latest features/fixes and can be done globally or locally. Development versions do not have the same stability guarantees, however.

----

## System Prep

1. Enable the [universe repository](https://help.ubuntu.com/community/Repositories/CommandLine).



1. Install the following packages:

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

1. Install geospatial libraries <!--We should note why we're asking users to do this-->

        sudo apt-get install binutils libproj-dev gdal-bin libgeo-proj4-perl libjson0-dev

1. Install [PostGIS](http://trac.osgeo.org/postgis/wiki/UsersWikiPostGIS20Ubuntu1204)
   * For Ubuntu 14.04*: 
    ````
        sudo apt-get install postgresql-9.3-postgis-2.1
        sudo apt-get install postgresql-server-dev-9.3
    ````
   * For Ubuntu 12.04*: 
    ````
        sudo apt-add-repository ppa:ubuntugis/ppa
        sudo apt-get update
        sudo apt-get install postgres9.1-postgis
        sudo apt-get install postgresql-server-dev-9.1
    ````


1. [Install Git](http://git-scm.com/book/en/Getting-Started-Installing-Git):

        ~ $ apt-get install libcurl4-gnutls-dev libexpat1-dev gettext libz-dev libssl-dev
        ~ $ sudo apt-get install git 
        
        
1. Install pip

    **NOTE:** PIP is used to conveniently install Python modules needed for the project. If 'which pip' returns a path to pip, it is already installed. If it is not installed, you can install pip by typing:

        sudo apt-get install python-pip

If, instead, you plan on using version 3 of Python, you can install pip by typing:

        sudo apt-get install python3-pip

Once pip is installed, you can use it to install the virtualenv package. If you installed the Python 2 pip, you can type:

        sudo pip install virtualenv

If you installed the Python 3 version of pip, you should type this instead:

        sudo pip3 install virtualenv

               
   verify `pip`:

        ~ $ which pip
        >> /usr/local/bin/pip

1. [Install virtualenwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/install.html)
Install `virtualenvwrapper` with `sudo`.



## Django Install


1. Create a new virtual environment and work within it

        mkvirtualenv ca-web

This will install a standalone version of Python, as well as pip, into an isolated directory structure within your project directory. We chose to call our virtual environment newenv, but you should name it something descriptive. A directory will be created with the name you select, which will hold the file hierarchy where your packages will be installed.

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


### references:


Justin Ellingwood. 2015-Mar-05. "How To Install the Django Web Framework on Ubuntu 14.04" https://www.digitalocean.com/community/tutorials/how-to-install-the-django-web-framework-on-ubuntu-14-04

Kenneth Reitz Project. 2016. "Virtual Environments" **Python Guide.** http://docs.python-guide.org/en/latest/dev/virtualenvs/

