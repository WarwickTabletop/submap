import json
from collections import defaultdict

from django.urls import reverse
from django.http import JsonResponse, HttpResponseForbidden
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, DetailView

# Create your views here.
from mapper.models import Map, APIKey


class MapView(DetailView):
    model = Map
    template_name = "mapper/map.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['lines'] = str(self.object.map).strip().splitlines()

        if self.object.names:
            names = json.loads(self.object.names)
            data['names'] = names
        return data


@method_decorator(csrf_exempt, name="dispatch")
class CreateMap(View):

    def post(self, request):
        result = {}

        if "key" not in request.POST or APIKey.objects.filter(slug__exact=request.POST['key']).count() != 1:
            return HttpResponseForbidden("Invalid API key")

        if "map" in request.POST:
            m = Map.objects.create(map=request.POST['map'], names=request.POST.get('names', ""))
            result['url'] = reverse("map", kwargs={'slug': m.slug})
        else:
            result['error'] = "Missing map"

        return JsonResponse(result)
