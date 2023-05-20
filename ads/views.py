import json

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Ad, Category


class IndexView(View):
    def get(self, request):
        return JsonResponse({'status': 'ok'}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdListPostView(View):
    def get(self, request):
        data = Ad.objects.all()
        return JsonResponse([i.serialize() for i in data], safe=False)

    def post(self, request):
        data = json.loads(request.body)
        new_ad = Ad.objects.create(**data)
        return JsonResponse(new_ad.serialize(), safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryListPostView(View):
    def get(self, request):
        data = Category.objects.all()
        return JsonResponse([i.serialize() for i in data], safe=False)

    def post(self, request):
        data = json.loads(request.body)
        new_category = Category.objects.create(**data)
        return JsonResponse(new_category.serialize(), safe=False)


class AdIdView(DetailView):
    model = Ad

    def get(self, request, **kwargs):
        detail_ad = self.get_object()
        return JsonResponse(detail_ad.serialize(), safe=False)


class CategoryIdView(DetailView):
    model = Category

    def get(self, request, **kwargs):
        detail_category = self.get_object()
        return JsonResponse(detail_category.serialize(), safe=False)
