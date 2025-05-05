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
The 404 page was tested by direct input because the validator received a 404 error.

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
| 404            | ![screenshot](documentation\readme\testing\html-validation\404-html.png)            | Pass: No Errors |

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
Add Post page 'Accessibility' is related to the Summernote field iFrame not having a title.
404 page 'Best Practices' and 'SEO' are lower due to the 404 error.
When trying to get lighthouse scores, I kept getting different values even when immediately running the test again. 


| Page           | Size    | Screenshot                                                                                   |
| -------------- | ------- | -------------------------------------------------------------------------------------------- |
| Index          | Desktop | ![screenshot](documentation\readme\testing\lighthouse\lighthouse-index-desktop.png)          |
| Index          | Mobile  | ![screenshot](documentation\readme\testing\lighthouse\lighthouse-index-mobile.png)           |
| Posts          | Desktop | ![screenshot](documentation\readme\testing\lighthouse\lighthouse-posts-desktop.png)          |
| Posts          | Mobile  | ![screenshot](documentation\readme\testing\lighthouse\lighthouse-posts-mobile.png)           |
| Post Detail    | Desktop | ![screenshot](documentation\readme\testing\lighthouse\lighthouse-post-detail-desktop.png)    |
| Post Detail    | Mobile  | ![screenshot](documentation\readme\testing\lighthouse\lighthouse-post-detail-mobile.png)     |
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
| 404            | Desktop | ![screenshot](documentation\readme\testing\lighthouse\lighthouse-404-desktop.png)            |
| 404            | Mobile  | ![screenshot](documentation\readme\testing\lighthouse\lighthouse-404-mobile.png)             |

## MANUAL TESTING

### Responsiveness

Full responsive testing was performed on mobile, tablet, and desktop following devices:

| Page        | Size    | Screenshot                                                                         |
| ----------- | ------- | ---------------------------------------------------------------------------------- |
| Index       | Desktop | ![screenshot](documentation\readme\responsiveness\desktop\index-desktop.png)       |
| Index       | Tablet  | ![screenshot](documentation\readme\responsiveness\tablet\index-tablet.png)         |
| Index       | Mobile  | ![screenshot](documentation\readme\responsiveness\mobile\index-mobile.png)         |
| Posts       | Desktop | ![screenshot](documentation\readme\responsiveness\desktop\posts-desktop.png)       |
| Posts       | Tablet  | ![screenshot](documentation\readme\responsiveness\tablet\posts-tablet.png)         |
| Posts       | Mobile  | ![screenshot](documentation\readme\responsiveness\mobile\posts-mobile.png)         |
| Post Detail | Desktop | ![screenshot](documentation\readme\responsiveness\desktop\post-detail-desktop.png) |
| Post Detail | Tablet  | ![screenshot](documentation\readme\responsiveness\tablet\post-detail-tablet.png)   |
| Post Detail | Mobile  | ![screenshot](documentation\readme\responsiveness\mobile\post-detail-mobile.png)   |
| Login       | Desktop | ![screenshot](documentation\readme\responsiveness\desktop\login-desktop.png)       |
| Login       | Tablet  | ![screenshot](documentation\readme\responsiveness\tablet\login-tablet.png)         |
| Login       | Mobile  | ![screenshot](documentation\readme\responsiveness\mobile\login-mobile.png)         |
| Sign up     | Desktop | ![screenshot](documentation\readme\responsiveness\desktop\sign-up-desktop.png)     |
| Sign up     | Tablet  | ![screenshot](documentation\readme\responsiveness\tablet\sign-up-tablet.png)       |
| Sign up     | Mobile  | ![screenshot](documentation\readme\responsiveness\mobile\sign-up-mobile.png)       |
| 404         | Desktop | ![screenshot](documentation\readme\responsiveness\desktop\404-desktop.png)         |
| 404         | Tablet  | ![screenshot](documentation\readme\responsiveness\tablet\404-tablet.png)           |
| 404         | Mobile  | ![screenshot](documentation\readme\responsiveness\mobile\404-mobile.png)           |

### Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page                                           | User Action                                         | Expected Result                                                                     | Pass/Fail | Comments |
| ---------------------------------------------- | --------------------------------------------------- | ----------------------------------------------------------------------------------- | --------- | -------- |
| **Navigation bar**                             |                                                     |                                                                                     |           |          |
|                                                | Click on Logo                                       | Redirection to Index page                                                           | Pass      |          |
|                                                | Click on Posts in navbar                            | Redirection to Posts page                                                           | Pass      |          |
|                                                | Click on New Post in navbar (not logged-in)         | Redirection to Login page                                                           | Pass      |          |
|                                                | Click on New Post in navbar (logged-in)             | Redirection to Add Post page                                                        | Pass      |          |
|                                                | Click on Logout in navbar                           | Redirection to Logout page                                                          | Pass      |          |
|                                                | Click on Register in navbar                         | Redirection to Sign up page                                                         | Pass      |          |
|                                                | Click on Login in navbar                            | Redirection to Login page                                                           | Pass      |          |
|                                                | Enter search terms and click search                 | Redirection to Posts page with posts filtered based on search terms                 | Pass      |          |
| **Base Template**                              |                                                     |                                                                                     |           |          |
|                                                | See login status (not logged-in)                    | User can see 'you are not logged in' message displayed                              | Pass      |          |
|                                                | See login status (logged-in)                        | User can see 'you are logged in as: (name)' message displayed                       | Pass      |          |
| **Footer**                                     |                                                     |                                                                                     |           |          |
|                                                | Click on each social media icon                     | Redirection to each social media website                                            | Pass      |          |
| **Index Page**                                 |                                                     |                                                                                     |           |          |
|                                                | Click on filter buttons                             | Latest posts are filtered by selected filter                                        | Pass      |          |
|                                                | Click on one of the posts                           | Redirection to relevant post-detail page                                            | Pass      |          |
|                                                | Click on 'see all posts' button                     | Redirection to Posts page                                                           | Pass      |          |
| **Posts Page**                                 |                                                     |                                                                                     |           |          |
|                                                | Click on a post                                     | Redirection to relevant post-detail page                                            | Pass      |          |
|                                                | Click on filter buttons                             | All posts are filtered by selected filter                                           | Pass      |          |
| **Post-detail Page (Not logged-in)**           |                                                     |                                                                                     |           |          |
|                                                | View post detail page                               | User is able to see correct post detail page                                        | Pass      |          |
|                                                | Try to edit or delete post                          | Unable to see edit/delete buttons for post or comments                              | Pass      |          |
|                                                | Scroll to comment section                           | 'Log in to leave a comment' message displayed                                       | Pass      |          |
| **Post-detail Page (Logged-in, not own post)** |                                                     |                                                                                     |           |          |
|                                                | Edit/Delete post                                    | User is unable to see edit/delete post buttons                                      | Pass      |          |
|                                                | Leave a comment                                     | User is able to leave a comment. Comment is greyed out by default until authorised. | Pass      |          |
|                                                | Edit/Delete comment                                 | User is able to see edit/delete buttons for their own comments.                     | Pass      |          |
| **Post-detail Page (Logged-in, own post)**     |                                                     |                                                                                     |           |          |
|                                                | Edit/Delete post                                    | User is able to see edit/delete buttons for their own posts                         | Pass      |          |
| **Add Post page**                              |                                                     |                                                                                     |           |          |
|                                                | Leave program name empty and try to Submit          | A required message popped up                                                        | Pass      |          |
|                                                | Leave the description empty and try to Submit       | A required message popped up                                                        | Pass      |          |
|                                                | Leave the details empty and try to Submit           | A required message popped up                                                        | Pass      |          |
|                                                | Fill in all inputs correctly and click Submit       | Redirection to Posts page and post successful notification shown                    | Pass      |          |
| **Edit Post page**                             |                                                     |                                                                                     |           |          |
|                                                | Leave program name empty and try to Submit          | A required message popped up                                                        | Pass      |          |
|                                                | Leave the description empty and try to Submit       | A required message popped up                                                        | Pass      |          |
|                                                | Leave the details empty and try to Submit           | A required message popped up                                                        | Pass      |          |
|                                                | Fill in all inputs correctly and click Submit       | Redirection to Posts page and post updated successfully notification shown          | Pass      |          |
| **Delete Post page**                           |                                                     |                                                                                     |           |          |
|                                                | Click confirm button                                | Redirected to Posts page and post is deleted                                        | Pass      |          |
|                                                | Click cancel button                                 | Redirected to Posts page and post is not deleted                                    | Pass      |          |
| **Edit Comment page**                          |                                                     |                                                                                     |           |          |
|                                                | Leave body section empty and try to Submit          | A required message popped up                                                        | Pass      |          |
|                                                | Enter text in body section and try to Submit        | Successful, notification is displayed, comment is greyed out until authorised       | Pass      |          |
|                                                | Click cancel button                                 | User is redirected back to the same post-detail page                                | Pass      |          |
| **Delete Comment page**                        |                                                     |                                                                                     |           |          |
|                                                | Click confirm button                                | Redirected to Posts page and post is deleted                                        | Pass      |          |
|                                                | Click cancel button                                 | Redirected to Posts page and post is not deleted                                    | Pass      |          |
| **Logout page**                                |                                                     |                                                                                     |           |          |
|                                                | Click Sign Out button                               | User is logged out and redirected to index page, notification displayed             | Pass      |          |
|                                                | Click cancel button                                 | Redirected to Index page and user stays logged in                                   | Pass      |          |
| **Login page**                                 |                                                     |                                                                                     |           |          |
|                                                | Leave username blank and try to Submit              | A required message popped up                                                        | Pass      |          |
|                                                | Leave password blank and try to Submit              | A required message popped up                                                        | Pass      |          |
|                                                | Enter valid username and password and try to Submit | Logged in successfully and notification displayed                                   | Pass      |          |
|                                                | Enter valid email and password and try to Submit    | Logged in successfully and notification displayed                                   | Pass      |          |
| **Sign Up page**                               |                                                     |                                                                                     |           |          |
|                                                | Leave email blank and try to Submit                 | A required message popped up                                                        | Pass      |          |
|                                                | Leave username blank and try to Submit              | A required message popped up                                                        | Pass      |          |
|                                                | Leave password blank and try to Submit              | A required message popped up                                                        | Pass      |          |
|                                                | Leave password (again) blank and try to Submit      | A required message popped up                                                        | Pass      |          |
|                                                | Enter invalid email address                         | A valid email reminder message popped up                                            | Pass      |          |
|                                                | Enter a username that is too short                  | A valid username message popped up                                                  | Pass      |          |
|                                                | Enter a password similar to the username            | An error message is displayed                                                       | Pass      |          |
|                                                | Enter a common password                             | An error message is displayed                                                       | Pass      |          |
|                                                | Enter passwords that do not match                   | An error message is displayed                                                       | Pass      |          |
|                                                | Enter a password containing only numbers            | An error message is displayed                                                       | Pass      |          |
|                                                | Enter a passwords that is less than 8 characters    | An error message is displayed                                                       | Pass      |          |
|                                                | Try to sign up with an existing user/email          | An error message is displayed                                                       | Pass      |          |
|                                                | Enter valid information                             | Successful, user redirected to index page and logged in                             | Pass      |          |
| **404 page**                                   |                                                     |                                                                                     |           |          |
|                                                | Click Home button                                   | User is redirected to the Index page                                                | Pass      |          |

### User Story Testing

| User Story                                                                                                                | Screenshot                                                                        |
| ------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| As a new user, I can sign up with a username and password so that I can create an account.                                | ![screenshot](documentation\readme\testing\user-stories\sign-up.png)              |
| As a returning user I can log in securely so that I can access my account and see authorised features.                    | ![screenshot](documentation\readme\testing\user-stories\log-in.png)               |
| As a logged-in user I can create a blog post so that I can share my workout routine.                                      | ![screenshot](documentation\readme\testing\user-stories\add-post.png)             |
| As a user I can choose a workout focus for my blog post so that other users can filter by workout focus and find my post. | ![screenshot](documentation\readme\testing\user-stories\select-workout-focus.png) |
| As a user I can view all blog posts so that I can stay up to date and find new workout routines.                          | ![screenshot](documentation\readme\testing\user-stories\view-all-posts.png)       |
| As a user I can view individual posts so that I can read the full blog entries.                                           | ![screenshot](documentation\readme\testing\user-stories\view-full-post.png)       |
| As the post's author I can edit and delete the post so that I can update or remove my own content.                        | ![screenshot](documentation\readme\testing\user-stories\edit-delete-post.png)     |
| As a logged-in user I can comment on a post so that I can join the discussion.                                            | ![screenshot](documentation\readme\testing\user-stories\post-comment.png)         |
| As a user I can see a list of approved comments under each post so that I can read other people's opinions.               | ![screenshot](documentation\readme\testing\user-stories\see-comments.png)         |
| As a user I can filter posts by workout focus so that find posts that are relevant to me.                                 | ![screenshot](documentation\readme\testing\user-stories\filter-posts.png)         |
| As a user I can search for posts by keywords so that I can find specific topics or authors.                               | ![screenshot](documentation\readme\testing\user-stories\search-posts.png)         |

### Solved Bugs

- Cards in posts.html were showing the database value for the workout focus. I found a solution on StackOverflow and changed the code to display the readable value.

- When trying to create a new post, I received the following error: IntegrityError at /posts/. I found that I had incorrectly set the author field as form.instance.user so changing this to form.instance.author to match my model fixed the issue.

- A user was able to edit an already approved comment that had been posted and the new comment would stay approved. To fix this, I added code to the EditComment view setting comment.approved to false when editing comment.

- A scrollbar was appearing along the bottom of the screen when on lower screen sizes. I noticed that inline margin properties were set making the elements extend beyond 100%. Removing these inline styles solved the problem.
