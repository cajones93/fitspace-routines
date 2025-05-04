# Testing

Return to the [README.md](README.md) file.

## CONTENTS

- [AUTOMATED TESTING](#automated-testing)
  - [HTML](#html)
  - [CSS](#css)
  - [JavaScript](#javascript)
  - [Python](#python)
  - [Lighthouse](#lighthouse)
- [MANUAL TESTING](#manual-testing)
  - [Responsiveness](#responsiveness)
  - [Defensive Programming](#defensive-programming)
  - [User Story Testing](#user-story-testing)
- [SOLVED BUGS](#solved-bugs)

## AUTOMATED TESTING

### HTML

The recommended [HTML W3C Validator](https://validator.w3.org) was used to validate all HTML files.

| Page           | Screenshot                                                                          | Notes           |
| -------------- | ----------------------------------------------------------------------------------- | --------------- |
| Index          | ![screenshot](documentation\readme\testing\html-validation\index-html.png)          | Pass: No Errors |
| Posts          | ![screenshot](documentation\readme\testing\html-validation\posts-html.png)          | Pass: No Errors |
| Post-Detail    | ![screenshot](documentation\readme\testing\html-validation\post-detail-html.png)    | Pass: No Errors |
| Add Post       | ![screenshot](documentation\readme\testing\html-validation\add-post-html.png)       | Pass: No Errors |
| Edit Post      | ![screenshot](documentation\readme\testing\html-validation\edit-post-html.png)      | Pass: No Errors |
| Delete Post    | ![screenshot](documentation\readme\testing\html-validation\delete-post-html.png)    | Pass: No Errors |
| Edit Comment   | ![screenshot](documentation\readme\testing\html-validation\edit-comment-html.png)   | Pass: No Errors |
| Delete Comment | ![screenshot](documentation\readme\testing\html-validation\delete-comment-html.png) | Pass: No Errors |
| Sign Up        | ![screenshot](documentation\readme\testing\html-validation\signup-html.png)         | Pass: No Errors |
| Login          | ![screenshot](documentation\readme\testing\html-validation\login-html.png)          | Pass: No Errors |
| Logout         | ![screenshot](documentation\readme\testing\html-validation\logout-html.png)         | Pass: No Errors |

### CSS

The recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) was used to validate my CSS file.

| Page     | Screenshot                                                    | Notes           |
| -------- | ------------------------------------------------------------- | --------------- |
| base.css | ![screenshot](documentation\readme\testing\css\css-valid.png) | Pass: No Errors |

### JavaScript

No custom JavaScript was used in this project.

### Python

The recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) was used to validate all of my Python files.
The only errors returned were 'line too long' errors which have been excluded from the notes in below tables.

#### Validation For Main App

| File        | Screenshot                                                                | Notes           |
| ----------- | ------------------------------------------------------------------------- | --------------- |
| settings.py | ![screenshot](documentation\readme\testing\python\main\main-settings.png) | Pass: No Errors |
| urls.py     | ![screenshot](documentation\readme\testing\python\main\main-urls.png)     | Pass: No Errors |

#### Validation For Home App

| File     | Screenshot                                                             | Notes           |
| -------- | ---------------------------------------------------------------------- | --------------- |
| urls.py  | ![screenshot](documentation\readme\testing\python\home\home-urls.png)  | Pass: No Errors |
| views.py | ![screenshot](documentation\readme\testing\python\home\home-views.png) | Pass: No Errors |

#### Validation For Blog App

| File      | Screenshot                                                              | Notes           |
| --------- | ----------------------------------------------------------------------- | --------------- |
| forms.py  | ![screenshot](documentation\readme\testing\python\blog\blog-forms.png)  | Pass: No Errors |
| models.py | ![screenshot](documentation\readme\testing\python\blog\blog-models.png) | Pass: No Errors |
| urls.py   | ![screenshot](documentation\readme\testing\python\blog\blog-urls.png)   | Pass: No Errors |
| views.py  | ![screenshot](documentation\readme\testing\python\blog\blog-views.png)  | Pass: No Errors |

### Lighthouse

All pages were checked with lighthouse to identify any issues. Each page was checked in mobile and desktop sizes.

| Page           | Size    | Screenshot                                                                                   |
| -------------- | ------- | -------------------------------------------------------------------------------------------- |
| Index          | Desktop | ![screenshot](documentation\readme\testing\lighthouse\lighthouse-index-desktop.png)          |
| Index          | Mobile  | ![screenshot](documentation\readme\testing\lighthouse\lighthouse-index-mobile.png)           |
| Posts          | Desktop | ![screenshot](documentation\readme\testing\lighthouse\lighthouse-posts-desktop.png)          |
| Posts          | Mobile  | ![screenshot](documentation\readme\testing\lighthouse\lighthouse-posts-mobile.png)           |
| Add Post       | Desktop | ![screenshot](documentation\readme\testing\lighthouse\lighthouse-add-post-desktop.png)       |
| Add Post       | Mobile  | ![screenshot](documentation\readme\testing\lighthouse\lighthouse-add-post-mobile.png)        |
| Edit Post      | Desktop | ![screenshot](documentation\readme\testing\lighthouse\lighthouse-edit-post-desktop.png)      |
| Edit Post      | Mobile  | ![screenshot](documentation\readme\testing\lighthouse\lighthouse-edit-post-mobile.png)       |
| Delete Post    | Desktop | ![screenshot](documentation\readme\testing\lighthouse\lighthouse-delete-post-desktop.png)    |
| Delete Post    | Mobile  | ![screenshot](documentation\readme\testing\lighthouse\lighthouse-delete-post-mobile.png)     |
| Edit Comment   | Desktop | ![screenshot](documentation\readme\testing\lighthouse\lighthouse-edit-comment-desktop.png)   |
| Edit Comment   | Mobile  | ![screenshot](documentation\readme\testing\lighthouse\lighthouse-edit-comment-mobile.png)    |
| Delete Comment | Desktop | ![screenshot](documentation\readme\testing\lighthouse\lighthouse-delete-comment-desktop.png) |
| Delete Comment | Mobile  | ![screenshot](documentation\readme\testing\lighthouse\lighthouse-delete-comment-mobile.png)  |
| Login          | Desktop | ![screenshot](documentation\readme\testing\lighthouse\lighthouse-login-desktop.png)          |
| Login          | Mobile  | ![screenshot](documentation\readme\testing\lighthouse\lighthouse-login-mobile.png)           |
| Sign Up        | Desktop | ![screenshot](documentation\readme\testing\lighthouse\lighthouse-signup-desktop.png)         |
| Sign Up        | Desktop | ![screenshot](documentation\readme\testing\lighthouse\lighthouse-signup-mobile.png)          |
| Logout         | Desktop | ![screenshot](documentation\readme\testing\lighthouse\lighthouse-logout-desktop.png)         |
| Logout         | Mobile  | ![screenshot](documentation\readme\testing\lighthouse\lighthouse-logout-mobile.png)          |

## MANUAL TESTING

### Responsiveness

Full responsive testing was performed on the following devices:

- Laptop:
  - Macbook Air 2012 13 inch screen
  - Lenovo Ideapad 14 inch screen
- Mobile Devices:
  - IPhone 13
  - Samsung galaxy Note 9

Each device tested the site using the following browsers:

- Google Chrome
- Safari

### Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page                                           | User Action                                           | Expected Result                                                                     | Pass/Fail | Comments |
| ---------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------------------------------------- | --------- | -------- |
| **Navigation bar**                             |                                                       |                                                                                     |           |          |
|                                                | Click on Logo                                         | Redirection to Index page                                                           | Pass      |          |
|                                                | Click on Posts in navbar                              | Redirection to Posts page                                                           | Pass      |          |
|                                                | Click on New Post in navbar (not logged-in)           | Redirection to Login page                                                           | Pass      |          |
|                                                | Click on New Post in navbar (logged-in)               | Redirection to Add Post page                                                        | Pass      |          |
|                                                | Click on Logout in navbar                             | Redirection to Logout page                                                          | Pass      |          |
|                                                | Click on Register in navbar                           | Redirection to Sign up page                                                         | Pass      |          |
|                                                | Click on Login in navbar                              | Redirection to Login page                                                           | Pass      |          |
|                                                | Enter search terms and click search                   | Redirection to Posts page with posts filtered based on search terms                 | Pass      |          |
| **Base Template**                              |                                                       |                                                                                     |           |          |
|                                                | See login status (not logged-in)                      | User can see 'you are not logged in' message displayed                              | Pass      |          |
|                                                | See login status (logged-in)                          | User can see 'you are logged in as: (name)' message displayed                       | Pass      |          |
| **Footer**                                     |                                                       |                                                                                     |           |          |
|                                                | Click on each social media icon                       | Redirection to each social media website                                            | Pass      |          |
| **Index Page**                                 |                                                       |                                                                                     |           |          |
|                                                | Click on filter buttons                               | Latest posts are filtered by selected filter                                        | Pass      |          |
|                                                | Click on one of the posts                             | Redirection to relevant post-detail page                                            | Pass      |          |
|                                                | Click on 'see all posts' button                       | Redirection to Posts page                                                           | Pass      |          |
| **Posts Page**                                 |                                                       |                                                                                     |           |          |
|                                                | Click on a post                                       | Redirection to relevant post-detail page                                            | Pass      |          |
|                                                | Click on filter buttons                               | All posts are filtered by selected filter                                           | Pass      |          |
| **Post-detail Page (Not logged-in)**           |                                                       |                                                                                     |           |          |
|                                                | View post detail page                                 | User is able to see correct post detail page                                        | Pass      |          |
|                                                | Try to edit or delete post                            | Unable to see edit/delete buttons for post or comments                              | Pass      |          |
|                                                | Scroll to comment section                             | 'Log in to leave a comment' message displayed                                       | Pass      |          |
| **Post-detail Page (Logged-in, not own post)** |                                                       |                                                                                     |           |          |
|                                                | Edit/Delete post                                      | User is unable to see edit/delete post buttons                                      | Pass      |          |
|                                                | Leave a comment                                       | User is able to leave a comment. Comment is greyed out by default until authorised. | Pass      |          |
|                                                | Edit/Delete comment                                   | User is able to see edit/delete buttons for their own comments.                     | Pass      |          |
| **Post-detail Page (Logged-in, own post)**     |                                                       |                                                                                     |           |          |
|                                                | Edit/Delete post                                      | User is able to see edit/delete buttons for their own posts                         | Pass      |          |

| **Add Post page**                              |                                                       |                                                                                     |           |          |
|                                                | Leave program name empty and try to Submit            | A required message popped up                                                        | Pass      |          |
|                                                | Leave the description empty and try to Submit         | A required message popped up                                                        | Pass      |          |
|                                                | Leave the details empty and try to Submit             | A required message popped up                                                        | Pass      |          |
|                                                | Fill in all inputs correctly and click Submit         | Redirection to Posts page and post successful notification shown                    | Pass      |          |
| **Edit Post page**                             |                                                       |                                                                                     |           |          |
|                                                | Leave program name empty and try to Submit            | A required message popped up                                                        | Pass      |          |
|                                                | Leave the description empty and try to Submit         | A required message popped up                                                        | Pass      |          |
|                                                | Leave the details empty and try to Submit             | A required message popped up                                                        | Pass      |          |
|                                                | Fill in all inputs correctly and click Submit         | Redirection to Posts page and post updated successfully notification shown          | Pass      |          |
| **Delete Post page**                           |                                                       |                                                                                     |           |          |
|                                                | Click confirm button                                  | Redirected to Posts page and post is deleted                                        | Pass      |          |
|                                                | Click cancel button                                   | Redirected to Posts page and post is not deleted                                    | Pass      |          |
| **Edit Comment page**                          |                                                       |                                                                                     |           |          |
|                                                | Leave body section empty and try to Submit            | A required message popped up                                                        | Pass      |          |
|                                                | Enter text in body section and try to Submit          | Successful, notification is displayed, comment is greyed out until authorised       | Pass      |          |
|                                                | Click cancel button                                   | User is redirected back to the same post-detail page                                | Pass      |          |
| **Delete Comment page**                        |                                                       |                                                                                     |           |          |
|                                                | Click confirm button                                  | Redirected to Posts page and post is deleted                                        | Pass      |          |
|                                                | Click cancel button                                   | Redirected to Posts page and post is not deleted                                    | Pass      |          |
| **Logout page**                                |                                                       |                                                                                     |           |          |
|                                                | Click Sign Out button                                 | User is logged out and redirected to index page, notification displayed             | Pass      |          |
|                                                | Click cancel button                                   | Redirected to Index page and user stays logged in                                   | Pass      |          |
| **Login page**                                 |                                                       |                                                                                     |           |          |
|                                                | Leave username blank and try to Submit                | A required message popped up                                                        | Pass      |          |
|                                                | Leave password blank and try to Submit                | A required message popped up                                                        | Pass      |          |
|                                                | Enter valid username and password and try to Submit   | Logged in successfully and notification displayed                                   | Pass      |          |
|                                                | Enter valid email and password and try to Submit      | Logged in successfully and notification displayed                                   | Pass      |          |
| **Sign Up page**                               |                                                       |                                                                                     |           |          |
|                                                | Leave email blank and try to Submit                   | A required message popped up                                                        | Pass      |          |
|                                                | Leave username blank and try to Submit                | A required message popped up                                                        | Pass      |          |
|                                                | Leave password blank and try to Submit                | A required message popped up                                                        | Pass      |          |
|                                                | Leave password (again) blank and try to Submit        | A required message popped up                                                        | Pass      |          |
|                                                | Enter invalid email address                           | A valid email reminder message popped up                                            | Pass      |          |
|                                                | Enter a username that is too short                    | A valid username message popped up                                                  | Pass      |          |
|                                                | Enter a password similar to the username              | An error message is displayed                                                       | Pass      |          |
|                                                | Enter a common password                               | An error message is displayed                                                       | Pass      |          |
|                                                | Enter passwords that do not match                     | An error message is displayed                                                       | Pass      |          |
|                                                | Enter a password containing only numbers              | An error message is displayed                                                       | Pass      |          |
|                                                | Enter a passwords that is less than 8 characters      | An error message is displayed                                                       | Pass      |          |
|                                                | Enter valid information                               | Successful, user redirected to index page and logged in                             | Pass      |          |

### User Story Testing

| User Story                                                                                                                                      | Screenshot                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| As a new user, I can create an account so that I can access the cafe's community features, reviews post and comments.                           | ![screenshot](documentation/testing/user-story/signup.png)       |
| As a member, I can sign in to the webpage so that I can access my account and enjoy customized features and contents.                           | ![screenshot](documentation/testing/user-story/signin.png)       |
| As a cafe visitor, I can write reviews about my experiences at the cafe so that I can provide feedback and help others make informed decisions. | ![screenshot](documentation/testing/user-story/review.png)       |
| As a site visitor, I can click on the About link so that I can read about the site.                                                             | ![screenshot](documentation/testing/user-story/about-us.png)     |
| As a site visitor, I can click on the Community page so that I can read topics and see what the trends are on the site.                         | ![screenshot](documentation/testing/user-story/forum-member.png) |
| As a visitor, I can use the 'Contact Us' feature to get in touch with the admin of the page so that I can ask questions or provide feedback.    | ![screenshot](documentation/testing/user-story/contactus.png)    |
| As a community member, I can participate in forum discussions so that I can share ideas, ask questions, and engage with other cafe enthusiasts. | ![screenshot](documentation/testing/user-story/forum-form.png)   |
| As an Admin of the page I can edit the About content so that the content stays updated with the previous information.                           | ![screenshot](documentation/testing/user-story/about-edit.png)   |
| As an admin I can manage post on the site so that the cafes and coffee shop information stay update and accurate.                               | ![screenshot](documentation/testing/user-story/post-edit.png)    |

### Solved Bugs

- During testing the lighthouse This issue "Mixed Content" occured. I have searched on the internet and end up in Slack community where I found the solution. I added `STATICFILES_STORAGE =
'cloudinary_storage.storage.StaticHashedCloudinaryS
torage'` to the settings.py file to ensure `HTTPS` is used instead of `HTTP` and eliminate the console warnings for Cloudinary-hosted images.

- During testing the functionalities on each page, I found that the contact form isn't handled incoming POST request from the contact form. To solve this, I write the POST handler in the view, and save the submitted data to the database. (Followed the steps from Challenge: Handle the form POST request- I Think Therefore I blog from CI learning platform and modified as the site needed.) Lastly, I checked the admin panel to ensure that the contact request has been saved and the confirmation pop-up displayed properly.

- One of my users report that when he clicked Edit button on his review, he must scroll down to see the existing review which makes it not so good UX. To improve this, I have created a JS functionality to make it scroll down automatically when user clicked Edit both on Reviews and comment section.
