---
Title: Example Django Poem Website
---
## Description

This is an example website for hosting user-submitted poems.

It uses Django to create a SQL framework which stores each poem as a collection of verses.

## How To

To use this website, you will need to set up a [Django Environment](https://www.djangoproject.com/).
You will also need to download [Django Extra Views](https://github.com/AndrewIngram/django-extra-views) for this to work.
You can do this through pip by running the command:
pip install django-extra-views

You can also install and run the whole thing through a docker container.
The command is $docker run -it -p 8000:8000 shyer2k/poem_website

## To Do

Right now, there is no way to add a poem containing more than five verses.
Right now, the only two poem categories are love poems and general poems. More could be added.
The CSS is included in the base template, not in a static file.

## Credits

Sean Hyer
django-extra-views created by [Andrew Ingram](https://github.com/AndrewIngram/)
