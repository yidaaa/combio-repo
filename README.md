## Module Repository

This project is inspired by the need of a common module repository for students taking the same unique major as me, since the modules we take has a lack of module reviews on larger module websites due to the small number of students taking this major, as well as having information on multiple sources due to the major being cross faculty. I've decided to create a prototype and will hand it over to the official univiersity club pertaining to my course and see if they would want to maintain it in the future for my juniors. 

From this project, I get to practise and combine everything that I have learnt from project 0 to project 4 for this final project. I implemented the search functions using what I've learnt in project 1. Creation and form updating on the front end are learnt from projects 2. APIs and backend are learnt from project 3. Project 4 is a good summary of all previous projects, and taught me the use of pagination. However, for my project 4, I felt that I didn't implement my functions well and my code ended up really messy. A lot of functions are hard coded and had a hard time scaling. For example, since the updating of data into the database takes time and sometimes reloading is faster than the time it uploads due to large number of data, I used setTimeInterval functions to solve this problem, making my codes messy. Therefore, I made a point to ensure that my code can be scaled and reused. This time, I alerted the user instead, giving an appropriate time for the database to upload, before the page fetches the updated database. 

Additionally, the module has only taught the storing of text-based data. I've wanted to learn how to store image data and files, even if it is stored locally. To eliminate the problem of having too many picture uploads, I delete the original photo each time a new one is uploaded, therefore the database only stores, at maximum equal to the number of users number of photos. A default image is also set for new users.  

When doing this project, I've decided to learn bootstrap since most of my previous projects are rather lacking in asthetics and uses basic CSS. Hence, I've spent a lot of time trying to make the application asthetically pleasing, by using cards, nav bars, forms, buttons, alerts, page numbering and file upload components from bootstrap, on top of my own CSS, such as making profile pictures in circles and giving the whole applciation a color scheme. 

Below are a summarised version of the functions I've implemented. 

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
