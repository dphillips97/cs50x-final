Executive Summary
---

This project fulfills the requirements for completion of CS50W: Web Programming with Python and JavaScript at HarvardX. Dogtracks is a web portal designed to simplify the task of coordinating with a person you trust to watch your pets while you're at work or out of town. As a pet owner, you can manage your pets' information and request visits. As the pet-sitter, you can review these requests and update their status accordingly. This project serves as a demo of the basic functions of using Dogtracks as a pet owner and a pet sitter.

Distinctiveness and Complexity
---

Many of the design decisions extended and built upon those that we covered in class, and I have attempted to provide attribution in the code comments. I will explain the key design decisions that I made and why they are distinct from earlier projects below.

**Decision 1**: Use of a full-featured external CSS library, BulmaCSS, not covered in class. The course touched on CSS libraries, primarily the widely-used Bootstrap. While covered in lecture and included in some of the assignments' code, use of Bootstrap was largely left up to the student - its inclusion or exclusion did not affect an assignment's acceptability. 

This project makes extensive use of Bulma, a library that was not mentioned in the course. Bulma, in particular, is largely focused on reducing the code required to make a website responsive. 

I made extensive use of Bulma's form components due to the difference in model fields. That is, I have fields of type date, charfield, and ImageField (discussed further below).  Rather than handing off the styling of a form to Django as ```{{  form.as_p  }}```, I chose to style each field to make the most of Bulma's form field attribute.

**Decision 2**: Implementation of the image upload function, which almost broke my brain. We were introduced to image storage in Commerce. However, we simply specified a link to an image that was hosted elsewhere online. Dogtracks, in contrast, allows users to upload images of their pets rather than a string specifying an image URL. Doing so required a model field type that was not covered in class (ImageField) and an import of the Pillow image processing library. This also required changing settings in settings.py that I learned about through Django documentation.

**Decision 3**: Extension of model functionality using property decorators. Dogtracks uses a model method that finds the duration of a visit from two given dates. The calculation itself is simple, especially since Django takes care of importing the relevant datetime library. Since visits are not presumably updated too often, I decided to calculate the duration within the model and store it in the database rather than calculate it every time a model instance is called. Decorators were introduced in the Python lecture, but implementation of a practical decorator to a Django model was not covered.

**Decision 4**: Extension of admin panel. We used the admin panel to more easily manage model instances, such as adding passengers, flights, and airports. Dogtracks extends what we learned in class by adding filters and customizing column titles using Django's built-in functions. 

I originally planned to create an admin view similar to the user's view. I realized that Django already offers a powerful and modifiable admin panel. While extensive modifications are complex, I could demonstrate filters and calculations. For example, an admin may wish to know how many animals are present in a single visit. This required a lookup that spanned 3 tables total (Visits to User to Animal) to return the count of pets at a particular visit. This required more complex object oriented code than we had written so far. Fortunately, an article on RealPython.com clearly described this procedure.

> "Customize the Django Admin with Python". Real Python, Real Python, 29 May 2021, realpython.com/customize-django-admin-python/.

Key Contents
---

```dogtracks.js``` contains functions for redirects and the filter visits function in the user's dashboard. The latter incorporates an API call.

```noun-pet.png``` is the default image displayed for a user when a pet picture is not specified.

```views.py``` contains code that renders the dashboard and forms; allows for editing of pets and visits; handlkes JSON requests to filter visit types; and handles logins, logouts, and user registration.

There are 7 HTML templates specifying layout common to all pages, form structure, and the main view called ```dashboard.html```.

```admin.py``` has been updated to allow the admin to see the count of pets per user.

```models.py``` includes the main models (User, Animal, and Visit) and their ModelForm versions and cleaning methods.

```final/media/images/``` is the directory that images are uploaded to.

How to run
---

I used pipenv to manage 2 libraries: Pillow and Django. Install pipenv through pip, and navigate to the directory that this project lives in. pipenv automatically detects requirements.txt and converts it to a pipfile which pipenv can update.


