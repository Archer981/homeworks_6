import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView

from ads.models import Ad, Category
from homeworks_6.settings import TOTAL_ON_PAGE
from users.models import User


@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateView):
    model = Ad

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        data['author'] = get_object_or_404(User, pk=data.get('author'))
        category, created = Category.objects.get_or_create(
            name=data.get('category'),
            defaults={'name': data.get('category')}
        )
        data['category'] = category
        new_ad = Ad.objects.create(**data)
        return JsonResponse(new_ad.serialize(), safe=False)


class AdListView(ListView):
    model = Ad

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        paginator = Paginator(self.object_list, TOTAL_ON_PAGE)
        page_number = request.GET.get('page')
        ads_on_pages = paginator.get_page(page_number)
        return JsonResponse({
            'total': paginator.count,
            'num_pages': paginator.num_pages,
            'items': [ad.serialize() for ad in ads_on_pages]
                            }, safe=False)


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, **kwargs):
        detail_ad = self.get_object()
        return JsonResponse(detail_ad.serialize(), safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdUpdateView(UpdateView):
    model = Ad
    fields = '__all__'

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        ad_data = json.loads(request.body)
        self.object.name = ad_data.get('name', self.object.name)
        self.object.price = ad_data.get('price', self.object.price)
        self.object.description = ad_data.get('description', self.object.description)
        if 'author' in ad_data:
            author = get_object_or_404(User, pk=ad_data.get('author'))
            self.object.author = author
        if 'category' in ad_data:
            category = get_object_or_404(Category, pk=ad_data.get('category'))
            self.object.category = category
        return JsonResponse(self.object.serialize(), safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdDeleteView(DeleteView):
    model = Ad
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({'Status': 'OK'}, safe=False, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AdUploadImageView(UpdateView):
    model = Ad
    fields = '__all__'

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        self.object.image = request.FILES.get('image')
        self.object.save()
        return JsonResponse(self.object.serialize(), safe=False)
