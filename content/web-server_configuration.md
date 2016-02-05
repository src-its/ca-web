## What is needed to set up a web server for hosting a website?

A server is a computer program or a machine accepts and supervises the HTTP requests. [^wikipedia]

## Server Harware
   - Read our article about [self-hosting versus hosted servers!](https://github.com/src-its/ca-web/blob/master/content/server-hosting.md)

### Server Software

Two popular web server software are Apache and nginx.

1. [Apache HTTP server](http://httpd.apache.org/) - 
    The Apache HTTP Server Project is an effort to develop and maintain an open-source HTTP server for modern operating systems including UNIX and Windows. The goal of this project is to provide a secure, efficient and extensible server that provides HTTP services in sync with the current HTTP standards.[^apache] <br />
    The Apache HTTP Server ("httpd") was launched in 1995 and it has been the most popular web server on the Internet since April 1996. It has celebrated its 20th birthday as a project in February 2015.

2. [nginx](http://nginx.org/en/) -
    nginx [engine x] is an HTTP and reverse proxy server, a mail proxy server, and a generic TCP proxy server, originally written by Igor Sysoev. For a long time, it has been running on many heavily loaded Russian sites including Yandex, Mail.Ru, VK, and Rambler. According to Netcraft, nginx served or proxied 24.33% busiest sites in January 2016. Here are some of the success stories: Netflix, Wordpress.com, FastMail.FM.[^nginx]<br />
    The sources and documentation are distributed under the 2-clause BSD-like license.
### Apache configuration

### Nginx configuration

Install Nginx and upstart job:

         ~ $ sudo apt-get install nginx
         ~ $ sudo ln -s /home/<user>/production/_deploy/production_nginx /etc/nginx/sites-available/production
         ~ $ sudo ln -s /etc/nginx/sites-available/production /etc/nginx/sites-enabled/production
         ~ $ sudo service nginx restart
         ~ $ sudo cp production/_deploy/production_upstart.conf /etc/init/webcore_production.conf
         ~ $ sudo service webcore_production start


## References:

[^wikipedia]: https://en.wikipedia.org/wiki/Server_(computing) Wikipedia. "Server (computing)." Wikimedia Foundation, Inc. https://en.wikipedia.org/wiki/Server_(computing)
[^apache]: http://httpd.apache.org/
[^nginx]: http://nginx.org/en/
