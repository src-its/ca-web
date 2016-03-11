## What is Git Cloning?

Cloning is the process of creating a copy of an existing Git repository.  When cloning in Git, one is receiving a full copy of nearly all data for the repository&mdashl;every version of every file for the history of the project.[^git_basics]

## How to clone a Git repository hosted on GitHub?

---

- [ ] From the Git command line
- [x] Using Pycharm
- [x] Using Pycharm

---

### Using the Git Command Line

<!-- Note HTTP and SSH cloning -->

The command for cloning from the command is `git clone`.

<!--

`git clone https://github.com/git/git-scm.com.git`

`git clone https://github.com/git/git-scm.com.git my-git-scm`

The above command does the same thing as the previous one, but the target directory is called 'my-git-scm'.

 -->


### Using PyCharm

You will need your github account details registered in PyCharm -- you can do this by going under IDE Settings, selecting GitHub, and filling in the required security credentials. 

Next, in the main menu choose VCS > Checkout from Version Control > GitHub. A box titled "Select Git Hub Repository to Clone" will open. From there, you can use the drop-down box to choose the repository you want to clone, and give the project a name and file location. Click "Clone" to finalize these details and begin cloning the repository. 

## Cloning over SSH


First, check that you have the SSH keys:

    ls -la ~/.ssh
    #Lists the files in your .ssh directory, if they exist

Your keys should look like one of the following:

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

If you have these keys, then chances are that you've finished [setting up `ssh` keys for use with Git](https://github.com/src-its/ca-web/blob/master/content/git_ssh-setup.md). [If not, then follow the procedure to set up your keys as linked here.](https://github.com/src-its/ca-web/blob/master/content/git_ssh-setup.md)

If you have ssh keys installed, try to clone the repository [using the command line]() : `git clone git@github.com:/user-name/repository`

Be sure to replace `user-name` with your user name, and `repository` with your target repository. E.g., `git clone git@github.com:/src-its/ca-web`

### References:

* Git. n.d. ["Git Basics - Getting a Git Repository." *git-scm.*](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository) [Accessed 08 February 08, 2016]  [MIT license](https://github.com/git/git-scm.com/blob/master/MIT-LICENSE.txt)
* ["Cloning a Repository from GitHub." PyCharm 5.0 Help. December 10, 2015. Accessed February 08, 2016. https://www.jetbrains.com/pycharm/help/cloning-a-repository-from-github.html. ](https://www.jetbrains.com/pycharm/help/cloning-a-repository-from-github.html)
* ["Registering GitHub Account in PyCharm." PyCharm 5.0 Help. December 10, 2015. Accessed February 08, 2016. https://www.jetbrains.com/pycharm/help/registering-github-account-in-pycharm.html.](https://www.jetbrains.com/pycharm/help/registering-github-account-in-pycharm.html)

### Related Articles:

* [Learn how to set up `ssh` keys for use with Git](https://github.com/src-its/ca-web/blob/master/content/git_ssh-setup.md)


[^git_basics]: https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository "Git. n.d. Git Basics - Getting a Git Repository. *git-scm.*"
