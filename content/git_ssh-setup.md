### How to install/configure SSH keys for GitHub on Ubuntu
----
#### Checking for & Generating SSH keys
<a name="generate-key"></a>

Before generating a new SSH key, you should check to see if any SSH keys exist.

Open Git Bash and enter the following command:

    ls -al ~/.ssh
    #Lists the files in your .ssh directory, if they exist

Check your directory for an existing public SSH key.

By default, the filenames of the public keys are one of the following:

* `id_dsa.pub`
* `id_ecdsa.pub`
* `id_ed25519.pub`
* `id_rsa.pub`

If you see an existing key pair that you would like to use, you can [add it to the ssh-agent](#add-key-to-agent).

If not, then generate a new SSH key using the following command:

    ssh-keygen -t rsa -b 4096

You'll be prompted to select a location to save the file.  Either change it to your preferred location, or accept the default  by pressing `Enter`.

    Enter a file in which to save the key(/Users/you/.ssh/id_rsa): [Press enter]


#### Adding your SSH key to GitHub

To add your SSH key to GitHub, first navigate to your `.ssh` folder. Open `id_rsa.pub` (or whatever you named you file) in a text editor and copy its contents. Proceed with the following steps:

Go to `Settings`.

In the user settings sidebar, click `SSH keys`.

Click `Add SSH key`.

In the Title field, add a title that describes the key.

Paste your key into the `Key` field.

Click `Add key`.

Confirm the action by entering your GitHub password.


#### Adding your SSH key to the SSH Agent
<a name="add-key-to-agent"></a>

Ensure ssh-agent is enabled:

If you are using Git Bash, you can turn on ssh-agent using the following command:

    #start the ssh-agent in the background
    eval "$(ssh-agent -s)"
    Agent pid 59566

If you are using another terminal prompt, you can turn on ssh-agent using the following command: 

    #start the ssh-agent in the background
    eval $(ssh-agent -s)
    Agent pid 59566

Add your SSH key to the ssh-agent using the following command:

    ssh-add ~/.ssh/id_rsa


#### Testing and Connecting over SSH

When you test your connection, you'll need to authenticate this action using your password, which is the SSH key passphrase you created earlier. For more information on working with SSH key passphrases, see Working with SSH key passphrases.

Open Git Bash and enter `ssh -T git@github.com`

You may see a warning saying that the authenticity can't be established, type yes to continue.
Verify that the fingerprint in the warning matches the messsage you see, then type yes:

```
Hi username! You've successfully authenticated, but GitHub does not
provide shell access.
```
Verify that the resulting message contains your username. 
----
----
----
#### Troubleshooting
If you see a message that contains "access denied," follow these steps.

First, run this command to search for typos in the domain:

`ssh -vT git@github.com`
It should tell you that a connection is being made to aa GitHub IP on port 22.

Second, don't try to connect using your own user. Always use the 'git' user. Verify connection by typing:

`ssh -T git@github.com`

Third, make sure you have a key that is being used. Start by turning on your SSH Agent:

`eval "$(ssh-agent -s)"` with GitBash or `eval $(ssh-agent -s)` with another terminal.
Follow this command by verifying that you have a private key generated and loaded into SSH:

OpenSSH 6.7 or older: `ssh-add -l`
OpenSSH 6.8 or newer: `ssh-add -l -E md5`

This should print out a large string of numbers and letters. If not you need to [generate a new key](#generate-key).

Fourth, check that the key is trying to connect to git@github.com using this command:

`ssh -vT git@github.com`
If the output contains `type -1`, that means SSH couldn't find a file to use.

Finally, verify that the public key is attached to your account.
Start your SSH Agent in the background with `ssh-agent -s`.
Then take note of your public key fingerprint: 
OpenSSH 6.7 or older: `ssh-add -l`
OpenSSH 6.8 or newer: `ssh-add -l -E md5`
Go to GitHub and click `Settings`.
In the user settings sidebar, click SSH keys.
Compare the list of SSH keys with the output from the `ssh-add` command.
----
### References:

* GitHub. 2016 "Generating a new SSH key" . *GitHub Inc.* https://help.github.com/articles/generating-a-new-ssh-key/
* GitHub. 2016 "Checking for existing SSH keys" . *GitHub Inc.* https://help.github.com/articles/checking-for-existing-ssh-keys/
* GitHub. 2016 "Adding a new SSH key to your GitHub Account" . *GitHub Inc.* https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/
* GitHub. 2016 "Testing your SSH connection" . *GitHub Inc.* https://help.github.com/articles/testing-your-ssh-connection/
* GitHub. 2016 "Error: Permission denied (publickey)" . *GitHub Inc.* https://help.github.com/articles/error-permission-denied-publickey/
