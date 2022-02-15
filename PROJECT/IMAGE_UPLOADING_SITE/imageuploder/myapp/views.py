from django.shortcuts import render
from .forms import ImageForm
from .models import Image

# Create your views here.
def home(req):

    if req.method == 'POST':
        form = ImageForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()

    form = ImageForm()
    image = Image.objects.all()

    return render(req, 'myapp/home.html', {'form': form, 'image':image})