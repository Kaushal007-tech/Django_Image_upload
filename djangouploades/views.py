from djangouploades.models import Movie
from django.http import Http404
from django.shortcuts import render ,redirect
from .forms import UploadForm
from django.http import HttpResponse


def movie(request,movie_id):
    movie = Movie.objects.get(pk=movie_id)
    if movie is not None:
        return render(request,"movies/movie.html",{"movie":movie})
    else:
        raise Http404("movie does not found")
        
        
def home(request):
    return HttpResponse("This is home page")
        
def upload(request):
    if request.POST:
        form = UploadForm(request.POST,request.FILES)
        print(request.FILES) 
        
        if form.is_valid():
            form.save()
        return redirect(home)
    return render(request,"movies/upload.html",{"form":UploadForm})