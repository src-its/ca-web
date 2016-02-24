
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
