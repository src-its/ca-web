## How to clone a Git repository hosted on GitHub?

---
- [x] From the Git command line
- [x] Using Pycharm

---
## Using the Git Command Line

First, check that you have SSH keys:

    ls -la ~/.ssh
    #Lists the files in your .ssh directory, if they exist


Your keys should look like one the following:

```
id_rsa.pem
id_rsa
id_rsa.pub
id_dsa.pem
id_dsa
id_dsa.pub
id_ecdsa.pem
id_ed25519.pem
```

If you have these keys, then chances are that you've finished [setting up `ssh` keys for use with Git](https://github.com/src-its/ca-web/blob/master/content/git_ssh-setup.md). [If not, the follow the proceedure to set up your keys as linked here.](https://github.com/src-its/ca-web/blob/master/content/git_ssh-setup.md)

If you have ssh keys installed, try to clone the repository [using the command line]() : `git clone git@github.com:/user-name/repository`

Be sure to replace `user-name` with your user name, and `repository` with your target repository. E.g., `git clone git@github.com:/src-its/ca-web`

## Using PyCharm
You'll need your github account details registered in PyCharm -- you can do this by going under IDE Settings, selecting GitHub, and filling in the required security credentials. 

Next, in the main menu choose VCS > Checkout from Version Control > GitHub. A box titled "Select Git Hub Repository to Clone" will open. From there, you can use the drop-down box to choose the repository you want to clone, and give the project a name and file location. Click "Clone" to finalize these details and begin cloning the repository. 

### References:

* [Git Documentation: Getting a Git Repository](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)
* [PyCharm 5.0 Help: Registering GitHub Account in PyCharm](https://www.jetbrains.com/pycharm/help/registering-github-account-in-pycharm.html)
* [PyCharm 5.0 Help: Cloning a Repository](https://www.jetbrains.com/pycharm/help/cloning-a-repository-from-github.html)

### Related Articles:

* [Learn how to set up `ssh` keys for use with Git](https://github.com/src-its/ca-web/blob/master/content/git_ssh-setup.md)
