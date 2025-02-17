from django.contrib import admin

from .models import Poem, Verse


class VerseInline(admin.StackedInline):
    '''This class will display verses'''
    model = Verse
    extra = 3


class PoemAdmin(admin.ModelAdmin):
    '''This class tells the admin site to display verses attached to
    the poem they belong to'''
    inlines = [VerseInline]


admin.site.register(Poem, PoemAdmin)
