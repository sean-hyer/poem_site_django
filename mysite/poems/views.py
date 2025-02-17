from django.shortcuts import get_object_or_404, render
# from django.views.generic.edit import CreateView
# No longer in use
from django.urls import reverse_lazy
from .models import Poem, Verse
from extra_views import CreateWithInlinesView, InlineFormSetFactory


class VerseInline(InlineFormSetFactory):
    '''This is part of the poem creation'''
    model = Verse
    fields = ['poem', 'verse']


class PoemCreateView(CreateWithInlinesView):
    '''This class lets the user submit a poem'''
    model = Poem
    inlines = [VerseInline]
    fields = ["title", "love", "author"]
    success_url = reverse_lazy("home")
    template_name = 'poem_form.html'


def detail(request, poem_id):
    '''
    This function sends a specific poem to the detail view,
    or raises an error if it doesn't exist
    '''
    poem = get_object_or_404(Poem, pk=poem_id)
    return render(request, "detail.html", {"poem": poem})


def poems(request):
    '''
    This function gets a list of all poems not set as love poems,
    and then calls them to the appropriate page
    '''
    gen_poem_list = Poem.objects.filter(love=False)
    context = {"gen_poem_list": gen_poem_list}
    return render(request, "poems.html", context)


def love(request):
    '''
    This function gets a list of all poems which ARE set as love poems,
    and then calls them to the appropriate page
    '''
    love_poem_list = Poem.objects.filter(love=True)
    context = {"love_poem_list": love_poem_list}
    return render(request, "love.html", context)


'''
REFERENCES

Making queries of a database in Django:
https://docs.djangoproject.com/en/5.1/topics/db/queries/

Editing two models with one form:
https://stackoverflow.com/questions/17179266/django-create-two-models-with-a-createview
'''
