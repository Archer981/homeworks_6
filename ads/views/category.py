import json

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from rest_framework.viewsets import ModelViewSet

from ads.models import Category
from ads.serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# @method_decorator(csrf_exempt, name='dispatch')
# class CategoryCreateView(CreateView):
#     model = Category
#
#     def post(self, request, *args, **kwargs):
#         data = json.loads(request.body)
#         new_ad = Category.objects.create(**data)
#         return JsonResponse(new_ad.serialize(), safe=False)
#
#
# class CategoryListView(ListView):
#     model = Category
#
#     def get(self, request, *args, **kwargs):
#         super().get(request, *args, **kwargs)
#         data = self.object_list.order_by('name')
#         return JsonResponse([category.serialize() for category in data], safe=False)
#
#
# class CategoryDetailView(DetailView):
#     model = Category
#
#     def get(self, request, **kwargs):
#         detail_ad = self.get_object()
#         return JsonResponse(detail_ad.serialize(), safe=False)
#
#
# @method_decorator(csrf_exempt, name='dispatch')
# class CategoryUpdateView(UpdateView):
#     model = Category
#     fields = '__all__'
#
#     def patch(self, request, *args, **kwargs):
#         super().post(request, *args, **kwargs)
#         category_data = json.loads(request.body)
#         self.object.name = category_data.get('name', self.object.name)
#         return JsonResponse(self.object.serialize(), safe=False)
#
#
# @method_decorator(csrf_exempt, name='dispatch')
# class CategoryDeleteView(DeleteView):
#     model = Category
#     success_url = '/'
#
#     def delete(self, request, *args, **kwargs):
#         super().delete(request, *args, **kwargs)
#         return JsonResponse({'Status': 'OK'}, safe=False, status=200)
