from django.shortcuts import render
from testapp import forms
from testapp.models import Movie


# Create your views here.
def index_view(request):
    return render(request,'testapp/index.html')



def add_movie_view(request):
    form=forms.MovieForm()
    if request.method=='POST':
        form=forms.MovieForm(request.POST)
        if form.is_valid():
            form.save()
        return index_view(request)
    return render(request,'testapp/addmovie.html',{'form':form})

def list_movie_view(request):
    movie_list=Movie.objects.all()
    return render(request,'testapp/listmovie.html',{'movie_list':movie_list})
