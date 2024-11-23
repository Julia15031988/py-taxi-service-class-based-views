from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, DetailView
from taxi.models import Driver, Car, Manufacturer


def index(request):
    context = {
    "num_drivers": Driver.objects.count(),
    "num_cars": Car.objects.count(),
    "num_manufacturers": Manufacturer.objects.count(),
    }

    return render(request, "taxi/index.html", context=context)


class ManufacturerListView(generic.ListView):
    model = Manufacturer
    template_name = "taxi/manufacturer_list.html"
    queryset = Manufacturer.objects.all().order_by("name")
    paginate_by = 5

class CarListView(generic.ListView):
    model = Car
    template_name = "taxi/car_list.html"
    context_object_name = "car_list"
    queryset = Car.objects.select_related("manufacturer").all()
    paginate_by = 5

class CarDetailView(DetailView):
    model = Car


class DriverListView(ListView):
    model = Driver
    template_name = "taxi/driver_list.html"
    context_object_name = "driver_list"
    paginate_by = 5


class DriverDetailView(DetailView):
    model = Driver
    queryset = Driver.objects.prefetch_related('car_set__manufacturer').all()
