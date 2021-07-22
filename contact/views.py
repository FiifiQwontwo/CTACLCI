from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages


# Create your views here.

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Request send successfuly")
            return redirect('ctac:home')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)


def success_view(request):
    return render(request, 'success.html')
