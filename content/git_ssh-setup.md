Addison

### How to install/configure SSH keys for GitHub on Ubuntu
    

##### Check for & generate SSH keys
Before generating a new SSH key, you should check to see if any SSH keys exist.

Open Git Bash and enter the following command:

    ls -al ~/.ssh
    #Lists the files in your .ssh directory, if they exist
Check your directory for an existing public SSH key.

By default, the filenames of the public keys are one of the following:

* id_dsa.pub
* id_ecdsa.pub
* id_ed25519.pub
* id_rsa.pub

If you see an existing key pair that you would like to use, you can add it to the ssh-agent. 

If not, then generate a new SSH key using the following command:

    ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
Be sure to put your email in to replace the example one.

Accept the default file location when you see "Enter a file in which to save the key," by pressing Enter.

    Enter a file in which to save the key(/Users/you/.ssh/id_rsa): [Press enter]

At the prompt, type a secure passphrase.

    Enter passphrase (empty for no passphrase): [Type a passphrase]
    Enter same passphrase again: [Type passphrase again]

In Git Bash, copy the alphanumeric key fingerprint you see. It should look like:

    nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8= your_email@example.com

If you're using OpenSSH 6.8 or newer, the key fingerprint should look like:

    nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8= your_email@example.com

##### Add your SSH key to the SSH Agent
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

##### Add your SSH key to GitHub
Copy the SSH key.

Use your SSH key filename to replace the example filename. When copying your key, don't add any newlines or whitespace.

    $ clip < ~/.ssh/id_rsa.pub
    # Copies the contents of the id_rsa.pub file to your clipboard
If this doesn't work, you can locate the hidden .ssh folder to find the file and manually copy its content using a text editor.
Go to Settings.

In the user settings sidebar, click SSH keys.

Click Add SSH key.

In the Title field, add a title that describes the key.
Paste your key into the "Key" field.
Click Add key.
Confirm the action by entering your GitHub password.

##### Test your SSH connection

When you test your connection, you'll need to authenticate this action using your password, which is the SSH key passphrase you created earlier. For more information on working with SSH key passphrases, see Working with SSH key passphrases.

Open Git Bash and enter:

ssh -T git@github.com
# Attempts to ssh to GitHub
You may see one of these warnings:

The authenticity of host 'github.com (192.30.252.1)' can't be established.
RSA key fingerprint is 16:27:ac:a5:76:28:2d:36:63:1b:56:4d:eb:df:a6:48.
Are you sure you want to continue connecting (yes/no)?
The authenticity of host 'github.com (192.30.252.1)' can't be established.
RSA key fingerprint is nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
Are you sure you want to continue connecting (yes/no)?
Note: The example above lists the GitHub IP address as 192.30.252.1. When pinging GitHub, you may see a range of IP addresses. For more information, see What IP addresses does GitHub use that I should whitelist?
Verify that the fingerprint in the message you see matches the following message, then type yes:

Hi username! You've successfully authenticated, but GitHub does not
provide shell access.
Verify that the resulting message contains your username. If you see a message that contains "access denied," see Error: Permission denied (publickey).

If you receive a message about "access denied," you can read these instructions for diagnosing the issue.

If you're switching from HTTPS to SSH, you'll need to update your remote repository URLs.

### References:

GitHub. 2016 "Generating a new SSH key" . *GitHub Inc.* https://help.github.com/articles/generating-a-new-ssh-key/
GitHub. 2016 "Generating a new SSH key" . *GitHub Inc.* https://help.github.com/articles/checking-for-existing-ssh-keys/
GitHub. 2016 "Generating a new SSH key" . *GitHub Inc.* https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/
GitHub. 2016 "Generating a new SSH key" . *GitHub Inc.* https://help.github.com/articles/testing-your-ssh-connection/
