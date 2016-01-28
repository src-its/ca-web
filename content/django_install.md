## Installing the Django [web framework]()


1. If using the server edition of Ubuntu, [enable the universe repository](https://help.ubuntu.com/community/Repositories/CommandLine).

1. Install the following linux packages:

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

3. Fix image libraries

   Ubuntu has these in an 'unusual' location for debian, so the following links ensure that things like Pillow find them.

        sudo ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib
        sudo ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib
        sudo ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib

> **Note:** Make sure these links are valid if you are installing into a new version of Ubuntu (other than 14.04)

1. Install the geospatial libraries

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

