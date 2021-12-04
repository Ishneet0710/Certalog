# Certalog

#### **Description**:
Certalog is a website that allows users to upload their certificates/licenses onto the website. Certalog is a catalog but for certificates so the users are able to see all their certificates at once in a "catalog" like page. This allows them to keep track of important certificates and not lose them. With Certalog, you wouldnt have to go finding for that certificate you need to add to your portfolio.

**Aim**: 
Allow users to keep track of their certificates and maintain them.

**Frontend**: HTML, CSS, JS, Bootstrap <br>
**Backend**: Flask<br>
**Database**: SQLAlchemy<br>
**Web Hosting**: Heroku

# Features
- Create your own account and authenticate
- Add certificates
- Able to see all the certificates at once
- Able to delete certificates
- single Platform for you to save your certificates
- Easy to track your portfolio (i.e how many certificates you have garnered)
- Fully functional for you to make your Certalog your own!
- Easy to filter certificates by tags!

**Environment setup**:\
`pip install -r requirements.txt`\
`cd Certalog`\
`flask run`

# Details about the files

#### **`init.py`**
- Create flask app and import the necessary modules and classes from the other python applications.

#### **`auth.py`**
- Authentication for the user
- Defines the login, logout, signup functions

#### **`models.py`**
- Create the User, Tag, Cert classes.
- Initialize the necessary database columns for each class inside them

#### **`views.py`**
- Creates various routes needed for the website and then renders the necessary templates when these routes are called upon

#### **`add.html`**
- Implements forms through which users can add new certificates

#### **`catalog.html`**
- Images of the certificates are present in the catalog page
- Also implements a search bar which searches for the certificate based on their tags

#### **`cert-details.html`**
- Redirected from the catalog page when user clicks on that certificate
- Shows relevant informations regarding the certificate, issuer, tags, date, comments, title

#### **`home.html`**
- Homepage which tells more about Certalog and its uses

#### **`login.html`**
- Login page

#### **`signup.html`**
- Sign-up page

#### **`success.html`**
- Tells user that their certificate has been uploaded successfully.
- Gives them options to either add more certificates and then redirecting them to add.html or return back to home.html

# Limitations
One major limitation of the website is that it is only able to show images in the catalog page. However, most of the certificates are in pdf format. However, this could be solved in the future by having a function in which the pdf is converted to jpg/png so that it can be seen on the catalog page.

# Improvements
- Implement update feature along with the already implemented delete function
- Make the UI/UX more user friendly
- Make the website more dynamic by integrating it with frontend written in React
- Add more features

# Credits
This was made as the final project for the Harvard CS50x Course. Through this project I was able to experience the entire full stack developmental cycle from the frontend to the backend and integrating the backend with the database. This was my first full stack project and hopefully more are to come!
