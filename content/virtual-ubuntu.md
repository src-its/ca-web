
## Configuring and Deploying Ubuntu Server as a VirtualBox application


----

Your Ubuntu Server virtual machine (VM) loads by borrowing the resources of your host operating system and storing your virtual machine on a specific space on your host system's hard disk.

----


1. Download [Ubuntu Server 14.04.3 LTS ISO](http://www.ubuntu.com/download/server)
    - Before you can set up the 'ca-help' web application using VirtualBox, you'll need to download your OS installation media.  We'll be using Ubuntu Server for this project. 


    
2. Deploy Virtual Instance of Ubuntu Server

    - Open VirtualBox and select `New`: <br /> ![VirtualBox intialization screen](/images/1%20FirstImage.png)<br />

Setup Wizard will appear and click at Next button. <br/> ![](http://i.stack.imgur.com/fl3x4.jpg)

   - Enter your OS type.  When you start typing 'Ubuntu', VirtualBox will attempt to help you select the correct OS.  Be sure to select the 64 bit version of the installation  <br /> ![VirtualBox set-up OS selection](/images/2%20OS.png) <br />
    
    - Set the 'Memory' to about half of your available RAM. This parameter will affect the speed of your machine.  You can allocate more or less RAM to balance your preferences and usage requirements. This setting can be adjusted again after you  create your virtual appliance and changes take effect on image start-up.  <br /> ![VirtualBox set-up memory allocation](/images/3%20Memory.png)
    
   - Create a virtual hard disk.<br/>![VirtualBox set-up memory allocation](/images/4%20HDD.png)

   - Set the hard disk type to VDI (VirtualBox Disk Image)<br/> ![VirtualBox select hard disk type](/images/5%20Disk%20File%20Type.png)

   - Set your VM storage size. Between 20 and 40 GB should suffice for a moderately-sized web site. <br /> ![VirtualBox set-up storage](/images/6%20Storage.png)

   - Set your location where you intend to store your VM <br/>  ![VirtualBox set-up file location and size](/images/7%20HDD%20Size.png)


 Enter the size of your virtual disk (in MB) and click Next button.  <br/> ![](http://i.stack.imgur.com/rnLDr.png)


----

At this point, you have a configured VirtualBox machine image. The VirtualBox Set-Up Wizard will have dumped you back into the start-up menu, but your machine isn't yet fully configured.  Before you can start it up, you'll need to link an *.ISO image of your OS from which your image can be booted.

----

If you try to start up the image, Virtual Box may prompt to you select your host drive.  The screenshots that follow show the disk selection process when starting a newly-created image for Mac.

   - ![selection prompt](https://raw.githubusercontent.com/src-its/ca-web/master/images/8%20VB%20Start%20.png)

   - ![ISO image](https://raw.githubusercontent.com/src-its/ca-web/master/images/9%20ISO%20Selection.png)

   - ![selection confirmation](https://raw.githubusercontent.com/src-its/ca-web/master/images/10%20ISO%20Location.png)

---

Alternatively, you can pre-define the *.ISO.  Simply move (`mv`) your VirtualBox *.ISO file from your downloads folder into your VirtualBox folder and then link it to your machines from the 'Settings' menu.

---


   - ![](https://raw.githubusercontent.com/src-its/ca-web/master/images/11%20ISO%20Start.png)

   - ![](https://raw.githubusercontent.com/src-its/ca-web/master/images/12%20Hostname.png)

   - ![](https://raw.githubusercontent.com/src-its/ca-web/master/images/13%20Username.png)

   - ![](https://raw.githubusercontent.com/src-its/ca-web/master/images/14%20Password.png)

   - ![](https://raw.githubusercontent.com/src-its/ca-web/master/images/15%20Encrypt.png)

   - ![](https://raw.githubusercontent.com/src-its/ca-web/master/images/16%20TimeZone.png)

   - ![](https://raw.githubusercontent.com/src-its/ca-web/master/images/17%20Partition.png)

   - ![](https://raw.githubusercontent.com/src-its/ca-web/master/images/18%20PartitionSelect.png)

   - ![](https://raw.githubusercontent.com/src-its/ca-web/master/images/20%20WriteChanges.png)





You will see the detail of your input here.  Finish the wizard by clicking the create button.  <br/> ![](http://i.stack.imgur.com/L7bEX.jpg)

On VirtualBox main window, select START and pick your MEDIA SOURCE. In your case, select iso on your desktop.
Finish the installation as normal install.

Remove your installation .iso from the virtual optical disk drive before restarting the VM.

Install Guest Additions.

---

http://askubuntu.com/questions/142549/how-to-install-ubuntu-on-virtualbox

http://www.psychocats.net/ubuntu/virtualbox
