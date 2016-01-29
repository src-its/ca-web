Addison

### How to install configure ssh keys for GitHub on Ubuntu?


Generate a new SSH key using the following command:

    ssh-keygen -t rsa -b 4096 -C "your_email@example.com"


Be sure to substite in your own GitHub email address.


When you're prompted to "Enter a file in which to save the key," press Enter. This accepts the default file location.

Enter a file in which to save the key (/Users/you/.ssh/id_rsa): [Press enter]

At the prompt, type a secure passphrase. For more information, see "Working with SSH key passphrases".

    Enter passphrase (empty for no passphrase): [Type a passphrase]
    Enter same passphrase again: [Type passphrase again]

    In Git Bash, copy the alphanumeric key fingerprint you see:

    The key fingerprint is:

    nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8= your_email@example.com

    If you're using OpenSSH 6.8 or newer, the key fingerprint is:

    nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8= your_email@example.com

    Add the SSH key fingerprint you've generated to the ssh-agent and your GitHub account. For more information, see Adding a new SSH key to the ssh-agent and Adding a new SSH key to your GitHub account.


### References:

GitHub. 2016 "Generating a new SSH key" . *GitHub Inc.* https://help.github.com/articles/generating-a-new-ssh-key/
