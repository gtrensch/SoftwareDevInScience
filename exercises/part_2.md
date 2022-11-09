# Manage GitHub Projects

***In these exercises, we will use GitHub functionality to organize our software development work into projects and a Kanban-like workflow. We will extend our small Python example source code with new functionality, using the test-driven software development approach.***

## Exercise II: Create a GitHub project using a Kanban-like dashbord.

1. Under GitHub profile, create a new project and select the *Board* template.

2. Add at least two activity cards to the ToDo list, one for implementating a new function and another for a corresponding unit test. The unit test should describe test cases that correspond to the function you are plan to implement.

3. Add the project to your forked repository.

4. (optional) Explore other possibilities you have to set up a GitHub project.

## Exercise III: Test-driven development. Work with a partner and form a two-developers team.

1. Update your _'main branch'_ to be in sync with the GitHub workshop repository.

    ## :+1: Hint ##

    * In order to be able to pull from a repository it needs to be added to Git: `git remote add <aliasname> <repository URL>`

      _'origin'_ is the default alias set by Git when a repository is cloned.
  
      Use the alias _'upstream'_ for the workshop repository.
    ##  

2. Developer A: Create a new feature-branch for the project that you have set up in Exercise II. 

2. Developer A: Implement the unit test cases that you have defined in Exercise II.

3. Developer A: Add, commit and push your changes.

4. Developer B: Pull the feature-branch from Developer A and make it your current branch. 

5. Developer B: Based on the current branch, create a new working-branch to implement the new functionality.

6. Developer B: Implement the functionality that your test cases define. Use the unit tests to verify the correctness of your implementation.

7. Developer B: Add, commit and push your changes.

8. Developer B: Issue a pull request against the feature-branch.

9. Developer A: Code-review the pull request and merge it.

10. Developer A: Create a pull request from the feature-branch against the workshop repository. 

11. (optional) Use the graphical repository browser *gitk* to explore the history of your repository.
