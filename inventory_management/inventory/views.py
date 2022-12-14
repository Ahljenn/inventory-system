from django.shortcuts import render, redirect, get_object_or_404
from itertools import chain
from .models import *
from .forms import * 
# Views define the functions for each api end point
# Takes in HTTP request and returns a response (render)

# Create your views here.
def index(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

# Display Devices
# ================================================ #
def display_device(request, cls):
  items = cls.objects.all()
  context = {
    'items' : items,
    'header' : cls.name,
  }
  return render(request, 'index.html', context)

def display_desktops(request):
  return display_device(request, Desktop)

def display_laptops(request):
  return display_device(request, Laptop)

def display_mobiles(request):
  return display_device(request, Mobile)

def display_all(request):
  items = list(chain(Desktop.objects.all(), Laptop.objects.all(), Mobile.objects.all()))
  context = {
    'items' : items,
    'header' : 'All Items',
  }
  return render(request, 'index.html', context)
# ================================================ #



# Add Devices
# ================================================ #
def add_device(request, cls):
  '''Modularized view to take in a class (cls) as a parameter
     Generalized function to prevent rewriting of the interface
  '''
  if request.method == 'POST':
    form = cls(request.POST)

    if form.is_valid():
      form.save()
      return redirect('index')
      
  else:
    # Otherwise, display form
    form = cls()
    return render(request, 'add_new.html', {
      'form': form, 
      'header': cls.name + ' Device'
      })

def add_desktop(request):
  return add_device(request, DesktopForm)

def add_laptop(request):
  return add_device(request, LaptopForm)

def add_mobile(request):
  return add_device(request, MobileForm)
# ================================================ #



# Edit Devices
# ================================================ #
def edit_device(request, pk, model, modelForm):
  item = get_object_or_404(model, pk = pk)
  if request.method == 'POST':
    form = modelForm(request.POST, instance = item)
    if form.is_valid():
      form.save()
      return redirect('index')
  
  else:
    form = modelForm(instance = item)
    return render(request, 'edit_device.html', {'form': form})

def edit_desktop(request, pk):
  return edit_device(request, pk, Desktop, DesktopForm)

def edit_laptop(request, pk):
  return edit_device(request, pk, Laptop, LaptopForm)

def edit_mobile(request, pk):
  return edit_device(request, pk, Mobile, MobileForm)
# ================================================ #



# Delete Devices
# ================================================ #
def delete_device(request, pk, cls, header):

  cls.objects.filter(id = pk).delete()
  items = cls.objects.all()

  context = {
    'items': items,
    'header': header
  }

  return render(request, 'index.html', context)

def delete_desktop(request, pk):
  return delete_device(request, pk, Desktop, "Desktop")

def delete_laptop(request, pk):
  return delete_device(request, pk, Laptop, "Laptop")

def delete_mobile(request, pk):
  return delete_device(request, pk, Mobile, "Mobile")
# ================================================ #



# Other Dynamic Routes
# ================================================ #
def view_device(request, pk, cls):
  device = cls.objects.get(pk = pk)

  return render(request, 'view_device.html', {
    'device': device,
    'header': device.type
    })

def view_desktop(request, pk):
  return view_device(request, pk, Desktop)

def view_laptop(request, pk):
  return view_device(request, pk, Laptop)

def view_mobile(request, pk):
  return view_device(request, pk, Mobile)
# ================================================ #



# Send Action Request
# ================================================ #
def send_action(request, pk, cls):
  if request.method == 'POST':
    order = request.POST
    if form.is_valid():
      order = form.cleaned_data['order']
      device = cls.objects.get(pk = pk)
      device.order = order
      device.save()
  



# ================================================ #