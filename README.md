# FitSpace - Routines

![The website shown on a variety of screen sizes](/documentation/readme/main-image.png)

[View Live Website here.](https://fitspace-routines-b98f037ee6fe.herokuapp.com/)

[GitHub Repo](https://github.com/cajones93/fitspace-routines)

**Welcome to FitSpace - Routines**

**FitSpace - Routines** is a fitness blog where users share their workout routines to help others improve themselves. It is the ultimate place to find your perfect workout routine. Search for routines by workout focus to help reach your goals, and share your opinions in the comments. FitSpace - Routines is the place where fitness enthusiasts come together to build eachother up through community.

## CONTENTS

- [UX - User Experience](#ux)

  - [Colours Theme](#colours-theme)
  - [Typography](#typography)
  - [Wireframes](#wireframes)
  - [Data Schema](#data-schema)
  - [User stories](#user-stories)
  - [Agile Development](#agile-development)

- [Features](#features)

  - [Navigation Bar](#navigation-bar)
  - [Home page](#home-page)
  - [About us page](#about-us-page)
  - [Cafe Details page](#cafe-details-page)
  - [Community page](#community-page)
  - [Sign up page](#sign-up-page)
  - [Sign in page](#sign-in-page)
  - [Contact us page](#contact-us-page)
  - [Notified Pop-up](#notified-pop-up)
  - [The Footer](#the-footer)
  - [Custom Error Handler page](#custom-error-handler-page)
  - [Features left to implement](#features-left-to-implement)

- [Testing](#testing)

- [Deployment & Local deployment](#deployment-&-Local-deployment)

  - [Deployment](#deployment)
  - [Local Deployment](#local-deployment)

- [Credits](#credits)
  - [Content](#contents)
  - [Media](#media)
  - [Code](#code)
  - [Acknowledgments](#acknowledgments)

## UX

### User’s Goal

Users want to discover new workout routines. They want to search for a specific workout focus, find new routines, and share opinions in comments.

### Owner’s Goal

The site owner aims to build a fitness community where users will frequently visit the site. By hosting a fitness blog, the site owner can find fitness trends and monetise the site through advertisements, sponsorships, and partnerships.

### Colour Scheme

I found an appealing colour scheme on adobe trends. I wanted something unique and colourful. The blue was used for the background and contrasted with the greens as the primary colours. I used [WebAIM:Contrast Checker](https://webaim.org/resources/contrastchecker/) to check the contrast of my colours to ensure they are easy to read and meet accessibility standards.

![The colour theme of the website](/documentation/readme/colour-scheme.png)

### Typography

I used [Shadows Into Light](https://fonts.google.com/specimen/Shadows+Into+Light) for my headers and titles and paired it with [Montserrat](https://fonts.google.com/specimen/Montserrat) for general text and readability because I wanted to go with a unique font styling and found that these two contrasted well.

### Wireframes

[Desktop](documentation\readme\wireframes\desktop-wireframes.png)

[Mobile](documentation\readme\wireframes\mobile-wireframes.png)

I originally planned to have a hero image on the index page but decided against it during implementation.

### Data Schema

ADD LATER

### User stories

I used Github [Project Board](https://github.com/users/cajones93/projects/3/views/1) and issues to keep track of my user stories and acceptance criteria while implementing the project.

1. As a new user I can sign up with a username and password so that I can create an account
2. As a returning user I can log in securely so that I can access my account and see authorised features
3. As a logged-in user I can create a blog post so that I can share my workout routine
4. As a user I can choose a workout focus for my blog post so that other users can filter by workout focus and find my post
5. As a user I can view all blog posts so that I can stay up to date and find new workout routines
6. As a user I can view individual posts so that I can read the full blog entries
7. As the post's author I can edit and delete the post so that I can update or remove my own content
8. As a logged-in user I can comment on a post so that I can join the discussion
9. As a user I can see a list of approved comments under each post so that I can read other people's opinions
10. As a user I can filter posts by workout focus so that find posts that are relevant to me
11. As a user I can search for posts by keywords so that I can find specific topics or authors

User Stories and Acceptance Criteria helped me to ensure each feature met the desired functionality and user experience.

## Features

### Index Page

- The Index Page shows the latest 3 blog posts to give the user an introduction to the site. It has the short text introduction to what the user can expect on the site. There are filter buttons to allow a user to find workout routines that interest them and they are able to click the view all posts button to go to the Posts page. The search bar allows users to search for posts based on the author, content, and post titles.

![Index Page](documentation\readme\features\index-page.png)


### Posts Page

- The Posts page shows all of the blog posts so a user can find posts. Similar to the index page, there are filter buttons which will allow a user to find posts that interest them. The search bar allows users to search for posts based on the author, content, and post titles.

![Posts Page](documentation\readme\features\posts-page.png)

### Post Detail Page

- The Post Detail page shows the full information in the blog post. At the top, the user can see the post title, author, and when it was posted. The workout focus is highlighted so the user can clearly see the aim of the workout. Below this is the workout details, this is the body of the blog post. Under the post is the comments section. If the user is logged in, they are able to post a comment which will need to be approved before other users can see them. Before a comment is approved, it is shown in a faded state. If a user is logged in and has posted a comment, they are able to edit and delete their own comments. Similarly, a logged-in user can visit their own post and update or delete it. This functionality is hidden for other users.

![Post Detail](documentation\readme\features\post-detail-page.png)

### New Post Page

- A user can add a new post by navigating to the New Post Page. This page contains a form where the user inputs the workout title, selects the focus, enters a brief description, and the program details. The program details field can be edited using the controls displayed at the top of the field.

![New Post](documentation\readme\features\add-post-page.png)

- If a user is not logged-in, they are redirected to the login page.

### Edit Post Page

- The Edit Post Page looks identical to the new post page. When a user clicks the edit button on their own post, they are redirected to this page. The information is automatically populated so the user can make changes. Once the user submits their changes, they are redirected back to their post and an alert is shown to say the update was successful.

![Edit Post Page](documentation\readme\features\edit-post-page.png)

### Delete Post Page

- The Delete Post Page is a simple confirmation page asking the user if they are sure they want to delete the post. The user is shown a confirmation text containing the post title. An alert is displayed when the user is returned to the Posts Page.

![Delete Post Page](documentation\readme\features\delete-post-page.png)

### Edit Comment Page

- When a user edits their own comment, they are taken to the Edit Comment Page. This page is a simple one-field page where their original comment is auto-populated. When a user submits their changes, the comments needs to be approved again. An alert is displayed once the submit button is clicked notifying the user after being redirected back to the post.
![Edit Comment Page](documentation\readme\features\edit-comment-page.png)

### Delete Comment Page

- The Delete Comment Page is a simple confirmation page that displays the comment and asks the user if they want to delete it. An alert is displayed after being redirected back to the page to notify the user.
![Delete Comment Page](documentation\readme\features\delete-comment-page.png)

### Sign Up Page

- When a user clicks the Register navbar item, they are taken to the Sign Up Page. A user must input a valid email, username, password, and password confirmation. There are instructions on password requirements on the form. If the password is not valid, a message is displayed to the user.

![Sign Up Page](documentation\readme\features\sign-up-page.png)

![Invalid Password](documentation\readme\features\password-error.png)

### Log In Page

- The Log In Page allows a user to sign in using their username or email and their password. Upon successful log in, an alert is displayed to notify the user.

![Log In Page](documentation\readme\features\sign-in-page.png)
![Successful Sign In](documentation\readme\features\successful-sign-in.png)
![Sign In Error](documentation\readme\features\log-in-error.png)

### Log Out Page

- The Log Out Page is a simple confirmation page asking the user if they really want to sign out. An alert is displayed when redirected to notify the user.

![Log Out Page](documentation\readme\features\sign-out-page.png)

### The Header Section / Navbar

- The Header Section / Navbar is included with base.html and includes the navigation elements. The Navbar contains the brand logo, navigation elements, and a search bar. On larger screens, the elements are spread out along the top of the page. On smaller screens, the elements are condensed into an accordion button which extends downwards when clicked to save space.

![Navbar Long](documentation\readme\features\header-long.png)
![Navbar Short](documentation\readme\features\header-short.png)

### The Footer Section

- The Footer Section includes social media sites for users.
  The social media links are shown in the icon and when users click on them, they will open in a new tab which makes it easy for the users to keep connected via social media.

![The Footer](documentation\readme\features\footer-section.png)

### Features left to implement

- Voting system. I wanted to include a voting system for users to up/down vote to help keep track of sentiment. This would be another way for users to easily share their opinions.
- Profile pages. I would have liked to add a page where users would update their information and easily access their own posts. I wanted to add avatars for users to express themselves better.

## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file. 


## Deployment & Local Deployment

### Deployment

The Live deployed application can be found deployed on [Heroku](https://fitspace-routines-b98f037ee6fe.herokuapp.com/).

### Database

This project uses [Neon.tech](https://www.neon.tech) for the PostgreSQL Database. This was provided by Code Institute via a database-maker website for Code Institute Students.


### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.
For either method, you will need to install any applicable packages found within the _requirements.txt_ file.

- `pip install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("DATABASE_URL", "user's own value")
os.environ.setdefault("SECRET_KEY", "user's own value")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python manage.py makemigrations`
- Migrate the data to the database: `python manage.py migrate`
- Create a superuser: `python manage.py createsuperuser`
- Load fixtures (if applicable): `python manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python manage.py runserver`

### Heroku Deployment

The application was deployed to Heroku. In order to deploy, the following steps were taken:

1. If you have an account, login to Heroku. Otherwise create a new account.
2. Once signed in, click the "New" button in the top right corner, below the header and choose "Create new app".
3. Choose a unique name for the application and select your region. When done, click "Create app".
4. This brings you to the "Deploy" tab. From here, click the "Settings" tab and scroll down to the "Config Vars" section and click on "Reveal Config Vars" and set your environment variables.

| Key                     | Value                                                                |
| ----------------------- | -------------------------------------------------------------------- |
| `DATABASE_URL`          | user's own value                                                     |
| `DISABLE_COLLECTSTATIC` | 1 (_this is temporary, and can be removed for the final deployment_) |
| `SECRET_KEY`            | user's own value                                                     |

Heroku needs two (and one optional) additional files in order to deploy:

- requirements.txt
- Procfile
- .python-version

You can install this project's **requirements** (where applicable) using:

- `pip install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- _replace **app_name** with the name of your primary Django app name; the folder where settings.py is located_

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace _app_name_ with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
  - `git push heroku main`

The project should now be connected and deployed to Heroku!

## Credits

### Content

- The font styles in the FitSpace - Routines website were taken from Google Fonts [Lora](https://fonts.google.com/specimen/Lora) and [League Spartan](https://fonts.google.com/specimen/League+Spartan)
- Wireframes I created on Balsamiq Wireframes
- The Entity Relationship Diagram (ERD) I created on [Lucidchart](https://www.lucidchart.com/pages)
- The blog post information was generated by [Gemini](https://gemini.google.com/app)
- The comments texts were entered by myself.
- The general foundation of the site was created by following [Dee Mc's recipe sharing tutorial](https://www.youtube.com/watch?v=sBjbty691eI&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy) and later modified.
- How to display choice values correctly [StackOverflow](https://stackoverflow.com/questions/42733788/django-change-text-color-based-on-value-html-js)
- Accessing clean data [Django Documentation](https://docs.djangoproject.com/en/5.2/ref/forms/api/#accessing-clean-data)
- Get_Context_Data [Django Documentation](https://docs.djangoproject.com/en/5.2/topics/class-based-views/generic-display/)


### Media

- The logo and favicon were created on [Logo.com](https://logo.com/)
- The social media icons in the website were taken from [Flat Icon](https://www.flaticon.com/)

### Acknowledgments

I would like to thank you the following people:

- Course facilitator Marko
- My partner