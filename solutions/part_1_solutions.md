# GitHub Agile Workflow

***In these exercises, we'll practice a basic GitHub workflow, useful when you want to contribute to a project.***

## Exercise I: Contribute to a project.

1. On GitHub, fork the workshop repository into your own GitHub account.

      **Solution:** 

      <img src="https://github.com/gtrensch/SoftwareDevInScience/blob/main/exercises/solutions/figures/fork.png" width=100% height=100%>
      
2. On your local machine, create a clone of the forked (your) workshop GitHub repository.

      **Solution:**
      
          git clone git@github.com:<your_GitHub_username>/SoftwareDevInScience

3. Create a new local branch.

      **Solution:**
      
          git checkout -b <branch_name>
      
      or 
      
          git branch <branch_name> 
          git checkout <branch_name>
      
      to show all branches: 
      
          git branch -a 

4. On the new branch, make any changes you want to the *printNumbers* example project and commit them.

      **Solution:**
      
      show repository status:
      
          git status

      add changes:
          
          git add *

      commit changes:
          
          git commit -m"<commit_message>"
          
      show repository status:
      
          git status
          
5. Push the new branch to your (forked) repository on GitHub.

      **Solution:**
      
          git push origin <branch_name>

6. Create and issue a pull request against the workshop repository.

      **Solution:** 
      
      <img src="https://github.com/gtrensch/SoftwareDevInScience/blob/main/exercises/solutions/figures/create_pull_request_01.png" width=70% height=70%>
      
      ----
      
      <img src="https://github.com/gtrensch/SoftwareDevInScience/blob/main/exercises/solutions/figures/create_pull_request_02.png" width=70% height=70%>
