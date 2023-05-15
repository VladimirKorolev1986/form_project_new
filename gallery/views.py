from django.shortcuts import render
from django.views import View
from .forms import GelleryUploadForm
from django.http import HttpResponseRedirect


def storage_file(file):
    with open(f'gallery_tmp/{file}', 'wb+') as new_file:
        for chunk in file.chunks():
            new_file.write(chunk)


# Create your views here.
class GalleryView(View):
    def get(self, request):
        form = GelleryUploadForm()
        return render(request, 'gallery/load_file.html', {'form': form})

    def post(self, request):
        form = GelleryUploadForm(request.POST, request.FILES)
        if form.is_valid():
            storage_file(form.cleaned_data['image'])
            return HttpResponseRedirect('load_image')
        return render(request, 'gallery/load_file.html', {'form': form})
