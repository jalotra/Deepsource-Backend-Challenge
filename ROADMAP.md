## What are the features ? 
* **User Management**
    - Schema : "Primary Key : Email Address", "Master_Password"
    - If a Email Address is already present, alert user! 
* **Password Management**
    - Schema : "Primary Key : User Email Address", Website Address, Website Name.
    - Have both randomised password >= 8 characters and user-defined password input. 
    - If some website is already has the password for this user, overwrite the previous password.

## Pages/Apps ?
* HomePage (Has both options(SignIn and SignUp))
    - SignIn (Takes UserEmailAddress and UserMasterPassword)
    - SignUp (Creates a new User in the database)

    - If SignIn is true, re-routes to the dashboard.

* Dashboard
    - A table that lists all the "website_address" : "website_name" : "password(this has to be hidden)". Also has buttons to "update" and "delete" some particular row.
    - Also has form/{a new route} to create a new password for a new wesbite.  

## UI
* Will use Jinja Templating Engine. 
* If time persists would try for ReactJs.