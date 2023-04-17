from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Recuiters
from .forms import RecruitersForm


def createProfile(request):
    if request.method == 'POST':
        form = RecruitersForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                recuiter = form.save()  # save the new Junior instance to the database
                # redirect to the detail page for the new Junior instance
                return redirect('showProfile', pk=recuiter.pk)
            except Exception as e:
                messages.error(request, f"Error saving form: {e}")
        else:
            print(form.errors)
            messages.error(request, "Form is not valid.")
    else:
        form = RecruitersForm()
    return render(request, 'createProfile.html', {'form': form})


def showProfile(request, pk):
    # retrieve the Junior instance with the given primary key, or return a 404 error
    recuiter = get_object_or_404(Recuiters, pk=pk)
    return render(request, 'showProfile.html', {'recuiter': recuiter})
