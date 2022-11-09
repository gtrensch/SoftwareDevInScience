# GitHub Agile Workflow

***In these exercises, we'll practice a basic GitHub workflow, useful when you want to contribute to a project.***

## Exercise I: Contribute to a project.

1. On GitHub, fork the workshop repository into your own GitHub account.

2. On your local machine, create a clone of the forked (your) workshop GitHub repository.

3. Create a new local branch.

4. On the new branch, make any changes you want to the *printNumbers* example project and commit them.

5. Push the new branch to your (forked) repository on GitHub.

6. Create and issue a pull request against the workshop repository.

## :+1: Hints ##

* If you are using Git on your computer for the first time, it will require some configuration.
  - Open a terminal or your Git Bash and set the username and the mail address that will be associated with your Git commits. Note that the username is not your GitHub username.
  
    `git config --global user.name "<your_username>"`
  
    `git config --global user.email "<your@mailaddress>"`

  - To verify your settings:

    `git config --global --list`

* Cloning a GitHub repository 
  - If you work with a GitHub Token: 
  
    `git clone https://github.com/<your_GitHub_username>/SoftwareDevInScience`

  - If you use SSH (recommended): 

    `git clone git@github.com:<your_GitHub_username>/SoftwareDevInScience`

* GitHub/git cheat sheet: *https://education.github.com/git-cheat-sheet-education.pdf*

* Gitk documentation: *https://git-scm.com/docs/gitk*

* How to fix error message *"authentication fails"* returned from `git push origin main`
 
  In August 2021 GitHub removed the support for password authentication. Instead, a personal access token or an SSH key-based secure authentication must be used.
  - For creating a user token go to: *https://github.com/settings/tokens*
  - SSH key (recommended)
    
    - To create an SSH key run:
      
      `ssh-keygen -t rsa -b 4096`
    
    - To add your SSH public key to your GitHub account: 
     
      *https://github.com/settings/keys*
      
    - To add your SSH private key to the ssh-agent:

      'ssh-add ~/.ssh/<private_ssh_key_filename>'
    
    - To test the GitHub SSH connection:
      
      `ssh -T git@github.com` 
      
    - Enable the SSH URL for a GitHub repoistory: 
     
      `git remote set-url origin git@github.com:<your_GitHub_username>/SoftwareDevInScience`
      
    - For connecting to GitHub with SSH se also: *https://docs.github.com/en/authentication/connecting-to-github-with-ssh*

