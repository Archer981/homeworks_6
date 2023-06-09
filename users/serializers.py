from rest_framework import fields
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from users.models import User, Location


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']


class UserListSerializer(ModelSerializer):
    total_ads = fields.IntegerField()

    class Meta:
        model = User
        fields = ['id', 'username', 'total_ads']


class UserCreateUpdateSerializer(ModelSerializer):
    locations = SlugRelatedField(slug_field='name', many=True, queryset=Location.objects.all())

    def is_valid(self, *, raise_exception=False):
        for loc_name in self.initial_data.get('locations', []):
            loc, _ = Location.objects.get_or_create(name=loc_name)
        return super().is_valid(raise_exception=raise_exception)

    # def create(self, validated_data):
    #     new_user = User.objects.create(**validated_data)
    #     for loc_name in self._lacations:
    #         loc, _ = Location.objects.get_or_create(name=loc_name)
    #         new_user.locations.add(loc)
    #     return new_user
    #
    # def update(self, instance, validated_data):
    #     if self._lacations:
    #         instance.locations.clear()
    #         for loc_name in self._lacations:
    #             loc, _ = Location.objects.get_or_create(name=loc_name)
    #             instance.locations.add(loc)
    #     return instance

    class Meta:
        model = User
        fields = '__all__'


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
