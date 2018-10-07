from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView


from .models import RestaurantLocation
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm


def restaurant_createview(request):
    form =RestaurantLocationCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/restaurants/')
    if form.errors:
        errors = form.errors

    template_name = 'restaurants/form.html'
    context = {'form': form, 'errors': errors}
    return render(request, template_name, context)


def restaurants_listview(request):
    template_name = 'restaurants/restaurants_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, template_name, context)


class RestaurantListView(ListView):
    """
        Since model name is RestaurantLocation and it is a list view so if
        we name the html file as restaurantlocation_list then django will
        detect template_name automatically
    """
    # template_name = 'restaurants/restaurantlocation_list.html'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug)
                | Q(category__icontains=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()

        return queryset


class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()

    # def get_object(self, *args, **kwargs):
    #     rest_id = self.kwargs.get('rest_id')
    #     # Also pk=rest_id can be used
    #     obj = get_object_or_404(RestaurantLocation, id=rest_id)
    #     return obj


# class RestaurantCreateView(CreateView):
#     form_cla

