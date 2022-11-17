# Manage GitHub Projects

***In these exercises, we will use GitHub functionality to organize our software development work into projects and a Kanban-like workflow. We will extend our small Python example source code with new functionality, using the test-driven software development approach.***

## Exercise II: Create a GitHub project using a Kanban-like dashbord.

1. Under GitHub profile, create a new project and select the *Board* template.

     **Solution:**
     
     <img src="https://github.com/gtrensch/SoftwareDevInScience/blob/main/exercises/solutions/figures/create_project_01.png" width=70% height=70%>
     
     ----

     <img src="https://github.com/gtrensch/SoftwareDevInScience/blob/main/exercises/solutions/figures/create_project_02.png" width=70% height=70%>
     
     ----

     <img src="https://github.com/gtrensch/SoftwareDevInScience/blob/main/exercises/solutions/figures/create_project_03.png" width=70% height=70%>

     ----

     <img src="https://github.com/gtrensch/SoftwareDevInScience/blob/main/exercises/solutions/figures/create_project_04.png" width=70% height=70%>

2. Add at least two activity cards to the ToDo list, one for implementating a new function and another for a corresponding unit test. The unit test should describe test cases that correspond to the function you are plan to implement.

     **Solution:**
     
     <img src="https://github.com/gtrensch/SoftwareDevInScience/blob/main/exercises/solutions/figures/add_activity_cards_01.png" width=70% height=70%>
     
     Hint :+1: You must type a title and then hit enter to create a draft-card.
     
     ----
     
     <img src="https://github.com/gtrensch/SoftwareDevInScience/blob/main/exercises/solutions/figures/add_activity_cards_02.png" width=30% height=30%>
     
     
3. Add the project to your forked repository.

     **Solution:**
     
     <img src="https://github.com/gtrensch/SoftwareDevInScience/blob/main/exercises/solutions/figures/add_project.png" width=80% height=80%>

4. (optional) Explore other possibilities you have to set up a GitHub project.

     **Solution:**
     
     For example, create another project and chose a different template option.
     
     
## Exercise III: Test-driven development. Work with a partner and form a two-developers team.

1. Update your _'main branch'_ to be in sync with the GitHub workshop repository.

   **Solution:**

   add the workshop repository to Git using the alias _'upstream'_
     
          git remote add upstream https://github.com/gtrensch/SoftwareDevInScience
          
    show remote repositories
    
          git remote -v
          
    switch to main branch
     
          git checkout main
          
    fetch from remote repository with alias _'upstream'_ and updated the local reopistory
    
          git pull upstream main

2. Developer A: Create a new feature-branch for the project that you have set up in Exercise II. 

     **Solution:**
     
          git checkout -b <feature-branch>

2. Developer A: Implement the unit test cases that you have defined in Exercise II.

      **Solution:**
      
       Add, for example, a new unit test for a square function, e.g., _test_square.py_.

3. Developer A: Add, commit and push your changes.

     **Solution:**
     
          git add *
          
          git commit -m"<commit_message>"
          
          git push origin <feature-branch>

4. Developer B: Pull the feature-branch from Developer A and make it your current branch.

     **Solution:**
     
     add the remote repository of developer A:
      
          git remote add <developer_A_alias> https://github.com/<developer_A_github_username>/SoftwareDevInScience
          
          git fetch <developer_A_alias>
          
     switch to the feature-branch created by developer A:
     
          git checkout <feature-branch>

5. Developer B: Based on the current branch, create a new working-branch to implement the new functionality.

     **Solution:**
     
          git checkout -b <working-branch-xyz>

6. Developer B: Implement the functionality that your test cases define. Use the unit tests to verify the correctness of your implementation.

     **Solution:**
      
     Add, for example, a new functionn _square.py_ and run the test suite.

          Python runTestSuite.py 
         
7. Developer B: Add, commit and push your changes.

     **Solution:**
     
          git add *
          
          git commit -m"<commit_message>"
          
          git push origin <working-branch-xyz>

8. Developer B: Issue a pull request against the feature-branch.

     **Solution:** (see also solution Exercise I / 6.)

                                         pull request
          <developer_A/feature-branch> <-------------- <developer_B/working-branch>

9. Developer A: Code-review the pull request and merge it.

     **Solution:**

     <img src="https://github.com/gtrensch/SoftwareDevInScience/blob/main/exercises/solutions/figures/review_merge_pull_request_01.png" width=70% height=70%>
     
     ----

     <img src="https://github.com/gtrensch/SoftwareDevInScience/blob/main/exercises/solutions/figures/review_merge_pull_request_02.png" width=100% height=100%>
     
     ----

     <img src="https://github.com/gtrensch/SoftwareDevInScience/blob/main/exercises/solutions/figures/review_merge_pull_request_03.png" width=70% height=70%>
     

10. Developer A: Create a pull request from the feature-branch against the workshop repository.

     **Solution:**  (see also solution Exercise I / 6.)
     
                                 pull request
          <workshop_repo/main> <-------------- <developer_B_repo/feature-branch>

11. (optional) Use the graphical repository browser *gitk* to explore the history of your repository.

      **Solution:** 
      
          gitk

     <img src="https://github.com/gtrensch/SoftwareDevInScience/blob/main/exercises/solutions/figures/gitk.png" width=30% height=30%>
