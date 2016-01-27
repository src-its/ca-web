
## installing a LAMP server

A common web server software stack is Linux, Apache, MySQL, and PHP (LAMP).

We're using Ubuntu 14.04 for the Linux (L) component, so next is to install Apache, MySQL, and PHP:

First, ensure that Ubuntu is up-to-date:

    sudo apt-get update && sudo apt-get upgrade


### Apache

    sudo apt-get install apache2

### MySQL

    sudo apt-get mysql-server

### PHP

    sudo apt-get install php5 php5-mysql

If you want to run PHP commands from the command line which is useful for debugging and running maintenance scripts, install PHP-cli like this:

    sudo apt-get install php5-cli

---

NOTE: In Linux, you can install several software packages at the same time by listing them all together:

    sudo apt-get install apache2 mysql-server php5 php5-mysql php5-cli




## installating alternative server bundles: Linux, nginx, postgres and python



### configuring your server

### routing HTTP requsts in Apache

### routing HTTP requsts in nginx


---



Configuration steps to increase the server security and usability:

1. set up user accounts (and use them!)

Once you are logged in as root, we're prepared to add the new user account that we will use to log in from now on.

This example creates a new user called "demo", but you should replace it with a user name that you like:

    adduser demo

You will be asked a few questions, starting with the account password.

Enter a strong password and, optionally, fill in any of the additional information if you would like. This is not required and you can just hit "ENTER" in any field you wish to skip. [1]

1. add public key authentication 

1. disable passwords

1. disable root login

The root user is the administrative user in a Linux environment that has very broad privileges. Because of the heightened privileges of the root account, you are actually discouraged from using it on a regular basis. This is because part of the power inherent with the root account is the ability to make very destructive changes, even by accident. [1]



### References

[1][2] Justin Ellingwood. 2014, April 17. "Initial Server Setup with Ubuntu 14.04" *Digital Ocean* https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-14-04 [Accessed 27 January 2016]

One practice for enhancing the security of your server is to disable the ability to log into your machine as the root user.  [**elaborate how**]