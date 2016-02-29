### Self-hosting vs. Hosted Servers


#### Self-Hosting 

Almost any computer with an active Internet connection can be configured to operate as a web server. This allows a person to host a site or application on the [World Wide Web](https://en.wikipedia.org/wiki/World_Wide_Web) from home.

Hosting at home, or **self-hosting** is the lowest-cost, greatest-control option, but it also intrduces numerous potential challeges. [^romkey]

* **reliability of Internet delivery**
    - Servers are meant to be always on.  A common reason for setting up a server at home is to allow access to a file system from a remote machine (such as accessing your music library from your phone). Residential Internet service, however, is notoriously unreliable, as most homes are at risk of a variety of factors that could bring a sever offline [power outages, loss of service from the Internet Service Provider(ISP), etc.]<br/> [It's important to note that not every Internet Service Provider allows users to host a public web site from computers on their network. Many ISPs will use [port filtering]().

* **security**
    - Servers are exposed machines. It is rarely a good idea to put one's primary compter system online as a server, as doing so makes a machine extremely vulnerable to malicious hacking, Separte your computer from your server and learn how to to identify attacks and break-ins.

* **performance**  
    - The upload speed of most typical home broadband connections is significantly slower than the download speeds that one experiences when browsing the web, meaning that the pages you are serving out are likely to load very slowly for anyone attempting to view them (especially viewers in geographically distant areas).


* **URL and IP address routing** 
    - Getting a fixed IP address or setting up a dynamic DNS

<!-- here we need to elaboriate --> 


#### Commercially-Hosted Servers

Most people wishing to host a website opt for third-party hosting.  Advantages of hosted servers are that they are fast, always-on, powerful machines with access to lots of bandwidth.

<!--here we should introduce the advantages and disadvantages of hosted servers. cost is a factor.  hosted servers typically have a variety of options, which users can select according to need.  more powerful servers cost more.  consider comparing the prices of different hosting plans.  also discuss how not all servers allow for /root access; some (like GitHub) are configured for you -- so that you are offered one particular stack as a result of your desired CMS platform-->


Numerous companies offer to host web servers. Big names include:

* Amazon
* Google

There are even a few companies and organizations who offer free hosting services under limited conditions:

* GitHub

<!-- add to the list of examples above and add hyperlinks to the example -->

## References:
```
[^wikipedia]: Wikipedia. "Server (computing)." Wikimedia Foundation, Inc. https://en.wikipedia.org/wiki/Server_(computing)
[^romkey]: https://romkey.com/2011/05/03/why-i-dont-self-host-anymore/ "romkey. 2011. "WHY I DON’T SELF-HOST ANYMORE." [Posted 2011/05/03] *ROMKEY.COM*  https://romkey.com/2011/05/03/why-i-dont-self-host-anymore/"
[^netgear]: http://documentation.netgear.com/wgt624v4/enu/202-10234-01/WGT624_RM-05-04.html
```
