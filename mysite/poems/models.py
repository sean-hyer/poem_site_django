from django.db import models


# Create your models here.
class Poem(models.Model):
    '''This is a class to hold a poem, with a title and author'''
    title = models.CharField(max_length=100)
    love = models.BooleanField(verbose_name="Is this a love poem?")
    # Whether or not it's a love poem is a true/false thing
    author = models.CharField(max_length=30, default="Anonymous")
    # 30 is the max username length

    def __str__(self):
        '''This alters the display from "Poem object (1)" to "title"'''
        return f"{self.title}"


class Verse(models.Model):
    '''Each verse is attached to its host poem for display purposes'''
    poem = models.ForeignKey(Poem, on_delete=models.CASCADE)
    verse = models.TextField()


'''
REFERENCES

Field names with CreateView:
https://stackoverflow.com/questions/40475938/django-createview-field-labels
'''
