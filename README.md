# Django-Framework---Creating-a-Simple-Blog-Application
This is a simple blog application made using the Django Framework 


------------
The TechBlog
------------

The TechBlog is a simple blog application created using the django framework where, the admin and registered users and groups can post stories and blogs according to their liking. 

The detailed documentation is in the "mysite/documentation" directory.

-----------
Quick Start
-----------

1. Add "blog" to the "settings.py/INSTALLED_APPS":

    INSTALLED_APPS = [
        ..............,
        ..............,
        ..............,
        "blog",
    ]

2. Include the "blog" in URLconf in the "mysite/urls.py":
    
    [
        ..................................,
        path('blog/', include('blog.url')),
    ]

3. Migrate to create the blog models:

    python manage.py makemigrations
    python manage.py migrate

4. Start the development server using the command stated below and visit the site http://127.0.0.1:8000/admin post your first blog (admin needs to be enabled): 

    python manage.py runserver

5. Visit http://127.0.0.1/8000 to view the posts.







