## Module Repository

This project is inspired by the need of a common module repository for students taking the same unique major as me, since the modules we take has a lack of module reviews on larger module websites due to the small number of students taking this major, as well as having information on multiple sources due to the major being cross faculty. I've decided to create a prototype and will hand it over to the official univiersity club pertaining to my course and see if they would want to maintain it in the future for my juniors. 

## Functions:
1. New users: Regstriation should use actual name and student identification number

2. All modules page: 
    - Contains a list of all modules
    - Contains a search by module code
    - Contains a search by module name
    - Contains a create new module button
    - If there is only 1 search result, bring the user directly to the module page. If there is more than 1 search result, list out all the modules

3. Create new Module: Users who are signed in should be able to create a module page 
    - Module Page includes: module name, module code and module summary
    - Fails if module code already exists
    - Returns user to the created page

4. For each module page: 
    - Has a create review button
    - Max of 5 reviews per page
    - User should be able to click next and previous, if applicable
    - User should also be able to access each page number directly

5. Review section: 
    - Reviews includes: Name, year and semester of module taken, lecturer of module, module review in text 
    - Reviews should all be sorted by year

6. Create review:
    - Users who are signed in should be able to create a review on the module's page
    - Review form includes: Year and semester of module taken, lecturer of module, module review in text

7. Edit summary of Module:
    - All users should be able to update module summary as teaching materials change over time

8. Edit Review:
    - Only the creater can edit their review

9. Profile page:
    - Shows profile card
    - Shows total number of reviews
    - Max of 5 reviews per page
    - User should be able to click next and previous, if applicable
    - User should also be able to access each page number directly

10. Profile card:
    - Shows profile picture
    - Shows total number 
    - Allows upload of profile picture
    - Users should have a default profile picture
