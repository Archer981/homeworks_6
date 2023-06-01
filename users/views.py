import json

from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, DeleteView, UpdateView, CreateView
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from users.models import User, Location
# from homeworks_6.settings import TOTAL_ON_PAGE
from users.serializers import UserSerializer, UserListSerializer, UserCreateUpdateSerializer, LocationSerializer


# class UserPaginator(PageNumberPagination):
#     page_size = 4


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateUpdateSerializer


# @method_decorator(csrf_exempt, name='dispatch')
# class UserCreateView(CreateView):
#     model = User
#
#     def post(self, request, *args, **kwargs):
#         data = json.loads(request.body)
#         locations = data.pop('locations')
#         new_user = User.objects.create(**data)
#         for loc_name in locations:
#             loc, _ = Location.objects.get_or_create(name=loc_name)
#             new_user.locations.add(loc)
#         return JsonResponse(new_user.serialize(), safe=False)


class UserListView(ListAPIView):
    queryset = User.objects.prefetch_related('locations').annotate(
        total_ads=Count('ad', filter=Q(ad__is_published=True))).order_by('username')
    serializer_class = UserListSerializer
    # pagination_class = UserPaginator

# class UserListView(ListView):
#     queryset = User.objects.prefetch_related('locations').annotate(
#         total_ads=Count('ad', filter=Q(ad__is_published=True)))
#
#     def get(self, request, *args, **kwargs):
#         super().get(request, *args, **kwargs)
#         paginator = Paginator(self.object_list.order_by('username'), TOTAL_ON_PAGE)
#         page_number = request.GET.get('page')
#         ads_on_pages = paginator.get_page(page_number)
#         return JsonResponse({
#             'total': paginator.count,
#             'num_pages': paginator.num_pages,
#             'items': [{**user.serialize(), 'total_ads': user.total_ads} for user in ads_on_pages]
#         }, safe=False)


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class UserDetailView(DetailView):
#     model = User
#
#     def get(self, request, **kwargs):
#         detail_user = self.get_object()
#         return JsonResponse(detail_user.serialize(), safe=False)


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateUpdateSerializer


# @method_decorator(csrf_exempt, name='dispatch')
# class UserUpdateView(UpdateView):
#     model = User
#     fields = '__all__'
#
#     def patch(self, request, *args, **kwargs):
#         super().post(request, *args, **kwargs)
#         user_data = json.loads(request.body)
#         self.object.first_name = user_data.get('first_name', self.object.first_name)
#         self.object.last_name = user_data.get('last_name', self.object.last_name)
#         self.object.username = user_data.get('username', self.object.username)
#         self.object.password = user_data.get('password', self.object.password)
#         self.object.role = user_data.get('role', self.object.role)
#         self.object.age = user_data.get('age', self.object.age)
#         if 'locations' in user_data:
#             self.object.locations.clear()
#             for loc_name in user_data['locations']:
#                 loc, _ = Location.objects.get_or_create(
#                     name=loc_name, defaults={'name': loc_name}
#                 )
#                 self.object.locations.add(loc)
#         return JsonResponse(self.object.serialize(), safe=False)


class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# @method_decorator(csrf_exempt, name='dispatch')
# class UserDeleteView(DeleteView):
#     model = User
#     success_url = '/'
#
#     def delete(self, request, *args, **kwargs):
#         super().delete(request, *args, **kwargs)
#         return JsonResponse({'Status': 'OK'}, safe=False, status=200)


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
