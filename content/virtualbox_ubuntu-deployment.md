
## Configuring and Deploying Ubuntu Server as a VirtualBox application


----

Your Ubuntu Server virtual machine (VM) loads by borrowing the resources of your host operating system and storing your virtual machine on a specific space on your host system's hard disk.

----


1. Download [Ubuntu Desktop 14.04.3 LTS ISO](http://www.ubuntu.com/download/desktop)
    - Before you can set up the 'ca-help' web application using VirtualBox, you'll need to download your OS installation media.  We'll be using Ubuntu Desktop for this project. 

2. Deploy Virtual Instance of Ubuntu Desktop

    - Open VirtualBox and select `New`: <br /> ![VirtualBox intialization screen](/images/1%20FirstImage.png)<br />

    - Setup Wizard will appear and click at Next button. <br/> ![](http://i.stack.imgur.com/fl3x4.jpg)

   - Enter your OS type.  When you start typing 'Ubuntu', VirtualBox will attempt to help you select the correct OS.  Be sure to select the 64 bit version of the installation  <br /> ![VirtualBox set-up OS selection](/images/2%20OS.png) <br /> Note: VirtualBox requires some hardware virtualization capability to be native to your system before it can emulate 64 bit machines. Most recently manufactured computers have this capability, so if you don't see any 64-bit options in the system select dropdown you can usually fix this by going into BIOS and enabling hardware virtualization. 

<!-- Operating systems that are not 64 bit do not allow 64 bit installation, preventing the use of the Ubuntu server through Virtual Box. Instead install a 32 bit version of Ubuntu. -->    
   
    - Set the 'Memory' to about half of your available RAM. This parameter will affect the speed of your machine.  You can allocate more or less RAM to balance your preferences and usage requirements. This setting can be adjusted again after you  create your virtual appliance and changes take effect on image start-up.  <br /> ![VirtualBox set-up memory allocation](/images/3%20Memory.png)
    
   - Create a virtual hard disk.<br/>![VirtualBox set-up memory allocation](/images/4%20HDD.png)

   - Set the hard disk type to VDI (VirtualBox Disk Image)<br/> ![VirtualBox select hard disk type](/images/5%20Disk%20File%20Type.png)

   - Set your VM storage size. Between 20 and 40 GB should suffice for a moderately-sized web site. <br /> ![VirtualBox set-up storage](/images/6%20Storage.png)

   - Set your location where you intend to store your VM <br/>  ![VirtualBox set-up file location and size](/images/7%20HDD%20Size.png)

   - Enter the size of your virtual disk (in MB) and click Next button.  <br/> ![](http://i.stack.imgur.com/rnLDr.png)

----

   - At this point, you have a configured VirtualBox machine image.
   - Once you have completed the set-up, VirtualBox will print out the detail of your input.  Finish the wizard by clicking the create button.  <br/> ![](http://i.stack.imgur.com/L7bEX.jpg)
   - The VirtualBox Set-Up Wizard will then dump you back into the start-up menu, but your machine isn't yet fully configured.  Before you can start it up, you'll need to link an *.ISO image of your OS from which your image can be booted. <br /> ![selection prompt](https://raw.githubusercontent.com/src-its/ca-web/master/images/8%20VB%20Start%20.png)

----

-  If you try to start up the image, Virtual Box may prompt to you select your host drive.  The screenshots that follow show the disk selection process when starting a newly-created image for Mac.
<br /> ![ISO image](https://raw.githubusercontent.com/src-its/ca-web/master/images/9%20ISO%20Selection.png)
<br /> ![selection confirmation](https://raw.githubusercontent.com/src-its/ca-web/master/images/10%20ISO%20Location.png)
<br /> ![](https://raw.githubusercontent.com/src-its/ca-web/master/images/11%20ISO%20Start.png)

---

   - Alternatively, you can pre-define your initial boot-up *.ISO. <br/><br/> First, move (`mv`) your VirtualBox *.ISO file to wherever you wish to save your VirtualBox files and then link it to your machines from the 'Settings' menu.
<br/>
<br/>On VirtualBox main window, select START and pick your MEDIA SOURCE.
   

<!-- The original instructions stated to remove your installation `.ISO` from the virtual optical disk drive before restarting the VM. Not sure if this is necessary (or recommended). -->

<!-- We should elaborate on this section with images. -->


---

---

---

**Next Step:** Install Guest Additions.

* Update your APT database:  `sudo apt-get update`
* Install the latest security updates:  `sudo apt-get upgrade`
* Install required packages:  `sudo apt-get install build-essential module-assistant`
* Configure your system for building kernel modules:  `sudo m-a prepare`
* Click on Install Guest Additions… from the Devices menu
* Mount the virtual CD Rom: `sudo mount /dev/cdrom /media/cdrom`
* Change directory to the virtual CD Rom Drive: `cd /media/cdrom`
* Install Guest Editions: `sudo ./VBoxLinuxAdditions.run`
* Restart VM by entering: `sudo reboot`
* To check that Guest Editions are installed: lsmod | grep vboxguest

<-- I got the above instructions from the site linked below.  IT doesn't work. Tried `sudo apt-get install virtualbox-guestadditions-utils`. didn't help -->

---

## References:

* http://askubuntu.com/questions/142549/how-to-install-ubuntu-on-virtualbox
* http://www.psychocats.net/ubuntu/virtualbox
* https://mylinuxramblings.wordpress.com/2014/12/06/how-to-install-virtualbox-guest-editions-in-ubuntu-server-14-04/
* 
<!-- we need to add a complete list of citations on this page-->
