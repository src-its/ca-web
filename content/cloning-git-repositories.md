## How to clone a Git repository hosted on GitHub?

---
- [x] From the Git command line
- [ ] Using Pycharm

---

First, check that you have SSH keys:

    ls -la ~/.ssh
    #Lists the files in your .ssh directory, if they exist


Your keys should look like one the following:

```
* id_rsa.pem
* id_rsa
* id_rsa.pub
* id_dsa.pem
* id_dsa
* id_dsa.pub
* id_ecdsa.pem
* id_ed25519.pem
```

If you have these keys, then chances are that you've finished [setting up `ssh` keys for use with Git](https://github.com/src-its/ca-web/blob/master/content/git_ssh-setup.md).

At this point, go ahead and try to clone the repository.  [Use the command line]() : `git clone git@github.com:/user-name/repository`

Be sure to replaces `user-name` with your user name, and `repository` with your target repository. E.g., `git clone git@github.com:/src-its/ca-web`

Reference: 

    [1] : ["Git Documentation"](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository) 


## Related Articles:

* [Learn how to set up `ssh` keys for use with Git](https://github.com/src-its/ca-web/blob/master/content/git_ssh-setup.md)
