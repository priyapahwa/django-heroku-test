from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from testapp.models import TeamModel

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

class About(ListView):
    model = TeamModel
    template_name = "about.html"
    context_object_name = "all_team_list"

class BlogCreateView(CreateView): 
    model = TeamModel
    template_name = 'post_new.html'
    fields = '__all__'
    success_url = "/"
