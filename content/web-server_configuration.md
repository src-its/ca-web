## What is needed to set up a web server for hosting a website?

A server is a computer program or a machine that waits for requests from other machines or software (clients) and responds to them. [1]



### self-hosting vs hosted servers

Almost any computer with an active Internet connection can be configured to operate as a web server--so it is possible to host a web site or web application right from your home and have it available to anyone on the World Wide Web.

While typically the most economical option, there are numerous potential challenges in setting up a home server [2]:

1. reliability of Internet delivery
   addressing the need to keep your site online all the time
2. security
   separting your computer from your server. being able to identify attacks and break-ins
3. IP addressing and domain routing
   getting a fixed IP address or setting up a dynamic DNS
4. upload (outbound) speeds
    the upload speed of most typical home broadband connections is significantly slower than the download speeds that one experiences when browsing the web, meaning that the pages you are serving out are likely to load very slowly for anyone attempting to view them (especially viewers in geographically distant areas).
5. packet filtering - Not every Internet Service Provider allows users to host a public web site from computers on their network. Many ISPs do port filtering that will prevent email sent to your home-located server. They may also prevent access of a home web server or filter out other protocols.


Most people wishing to host a website opt for third-party hosting.  Advantages of hosted servers are that they are fast, always-on, powerful machines with access to lots of bandwidth.

There's a plethora of companies offering to host your web server. Big names include:

* Amazon
* Google

There are even a few companies and organizations who offer free hosting services under limited conditions:

* GitHub


### URLS and DNS



### web server software for HTTP request routing: Apache vs nginx (and others?)

Web server software accepts and supervises the HTTP requests.

Two popular web server software are Apache and nginx.

* Apache


* nginx 

## References:

[1] Wikipedia. "Server (computing)." Wikimedia Foundation, Inc. https://en.wikipedia.org/wiki/Server_(computing)
[2] romkey. 2011. "WHY I DON’T SELF-HOST ANYMORE." [Posted 2011/05/03] *ROMKEY.COM*  https://romkey.com/2011/05/03/why-i-dont-self-host-anymore/
