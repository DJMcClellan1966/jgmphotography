from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Saved

@login_required(login_url="/accounts/signup")
def saved_image(request, saved_id):
    image = get_object_or_404(Saved, pk=saved_id)
    return render(request, 'slideshow/carousel.html', {'image':image})
