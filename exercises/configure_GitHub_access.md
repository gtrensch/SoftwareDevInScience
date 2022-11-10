## First-Time Git Setup On Your Local Computer

If you are using Git on your computer for the first time, it will require at least a minimal configuration to set up your identity.
  - Open a terminal or your Git Bash and set your username and mail address. This information will be associated with your Git commits. Note that the username is not necessarily your GitHub username.
  
    `git config --global user.name "<your_username>"`
  
    `git config --global user.email "<your@mailaddress>"`

  - To verify your settings:

    `git config --global --list`

For more information see: *https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup*


## Configure GitHub Access

In August 2021 GitHub removed the support for password authentication. Instead, a personal access token or an SSH key-based secure authentication must be used.
  
### SSH Key-based Authentication (recommended method)

In order to set up an SSH key-based GitHub connection, perform the following steps:

- Open a terminal and run `ssh-keygen` to create an SSH key pair.

  `ssh-keygen -t rsa -b 4096 -f ~/.ssh/<ssh_key_filename>`
    
- Add your SSH public key to your GitHub account. 
     
   - When your are signed in to GitHub, go to: *https://github.com/settings/keys*
   - On your local computer, open the file `~/.ssh/<ssh_key_filename>.pub` (The public key is stored with the extension *.pub*!) in an editor and cut and paste the content into the field *Authentication Keys*.
      
- In order to test the GitHub SSH connection, use the command:
    
  `ssh -T git@github.com`
  
  If the connection could be established *ssh* will return:
  
  `Hi <your_GitHub_username>! You've successfully authenticated, but GitHub does not provide shell access.`
  
  Verify that your correct GitHub username is displayed. If this is not the case, you can explicitly set the username for the GitHub remote server in the `~/.ssh/config` file. See the hint below.
  
#### Hints :+1:

- For convinence it may be desirable not have to enter your passphrase at any authentication attempt. So you can add your private SSH key to the ssh-agent.
  
  `ssh-add ~/.ssh/<ssh_key_filename>`

- To explicitly set the usersame for the GitHub server used by SSH, add the following to the `~/.ssh/config` file. If the file does not already exist, you have to create it. 
    ``` 
    Host github.com github.com
        HostName github.com
        IdentityFile ~/.ssh/<ssh_key_filename>
        User <your_GitHub_username>`
    ``` 
   
 - SSH authentication will fail if the repository remote URLs are not SSH URLs. This can be verified using the following Git command.

   `git remote -v`
   
   Correct SSH URLs.
   ```
   origin git@github.com:<your_GitHub_username>/<repository_name> (fetch)
   origin git@github.com:<your_GitHub_username>/<repository_name> (push)
   ```

   HTTPS URLs do not work with SSH. (It's fine for token-based authentication.)
   ```
   origin https://github.com/<your_GitHub_username>/<repository_name> (fetch)
   origin https://github.com/<your_GitHub_username>/<repository_name> (push)
   ```
      
   The URLs can be set with following Git command and thus turned into SSH URLs .
     
   `git remote set-url origin git@github.com:<your_GitHub_username>/<repository_name>`
      
- More information on how connecting to GitHub with SSH is provided by GitHub here: *https://docs.github.com/en/authentication/connecting-to-github-with-ssh*

### Personal Access Token (not recommended)

  You can create a personal access token to use in place of a password: *https://github.com/settings/tokens*
