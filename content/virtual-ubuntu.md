
**Steps:**

1 Download [Ubuntu Server 14.04.3 LTS ISO](http://www.ubuntu.com/download/server)
    Before you can set up the 'ca-help' web application using VirtualBox, you'll need to download your OS installation media.
    
2 Deploy Virtual Instance of Ubuntu Desktop

JOHANNES SCREENSHOTS:
Open VirtualBox and select New.
![](https://raw.githubusercontent.com/src-its/ca-web/master/images/1%20FirstImage.png)
Type "Ubuntu" in the name space, and VirtualBox will automatically fill in the rest.
![](https://raw.githubusercontent.com/src-its/ca-web/master/images/2%20OS.png)
Set the "Memory" to no more than half of your computer's RAM.
![](https://raw.githubusercontent.com/src-its/ca-web/master/images/3%20Memory.png)
Create a virtual hard disk.
![](https://raw.githubusercontent.com/src-its/ca-web/master/images/4%20HDD.png)
Set the hard disk type to VDI (VirtualBox Disk Image)
![](https://raw.githubusercontent.com/src-its/ca-web/master/images/5%20Disk%20File%20Type.png)
![](https://raw.githubusercontent.com/src-its/ca-web/master/images/6%20Storage.png)
![](https://raw.githubusercontent.com/src-its/ca-web/master/images/7%20HDD%20Size.png)
![](https://raw.githubusercontent.com/src-its/ca-web/master/images/8%20VB%20Start%20.png)
![](https://raw.githubusercontent.com/src-its/ca-web/master/images/9%20ISO%20Selection.png)
![](https://raw.githubusercontent.com/src-its/ca-web/master/images/10%20ISO%20Location.png)
![](https://raw.githubusercontent.com/src-its/ca-web/master/images/11%20ISO%20Start.png)
![](https://raw.githubusercontent.com/src-its/ca-web/master/images/12%20Hostname.png)
![](https://raw.githubusercontent.com/src-its/ca-web/master/images/13%20Username.png)
![](https://raw.githubusercontent.com/src-its/ca-web/master/images/14%20Password.png)
![](https://raw.githubusercontent.com/src-its/ca-web/master/images/15%20Encrypt.png)
![](https://raw.githubusercontent.com/src-its/ca-web/master/images/16%20TimeZone.png)
![](https://raw.githubusercontent.com/src-its/ca-web/master/images/17%20Partition.png)
![](https://raw.githubusercontent.com/src-its/ca-web/master/images/18%20PartitionSelect.png)
![](https://raw.githubusercontent.com/src-its/ca-web/master/images/20%20WriteChanges.png)




Open VirtualBox and select New 

![](http://i.stack.imgur.com/jxSEN.jpg)

Setup Wizard will appear and click at Next button.

![](http://i.stack.imgur.com/fl3x4.jpg)

Choose your guest OS and architecture (32 vs. 64 bit, e.g select Ubuntu) and click Next button

![](http://i.stack.imgur.com/Y3zUx.jpg)

Set your Base Memory (RAM) to reserve for your virtual machine and click Next button.

![](http://i.stack.imgur.com/F5Sri.jpg)

Tick at Startup Disk and Create New Hard disk and click at Next button.

![](http://i.stack.imgur.com/LlRnY.jpg)

Choose the type of file that you want to use for virtual disk and click Next button.

![](http://i.stack.imgur.com/HsbVL.png)

Choose your storage detail and click Next button.

![](http://i.stack.imgur.com/FPEuy.png)

Click next until it show the vm storage size. Enter the size of your virtual disk (in MB) and click Next button.

![](http://i.stack.imgur.com/rnLDr.png)

You will see the detail of your input here.  Finish the wizard by clicking the create button.

![](http://i.stack.imgur.com/L7bEX.jpg)

On VirtualBox main window, select START and pick your MEDIA SOURCE. In your case, select iso on your desktop.
Finish the installation as normal install.

Remove your installation .iso from the virtual optical disk drive before restarting the VM.

Install Guest Additions.

---

http://askubuntu.com/questions/142549/how-to-install-ubuntu-on-virtualbox

http://www.psychocats.net/ubuntu/virtualbox
