from datetime import datetime

from rest_framework.fields import SerializerMethodField
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from ads.models import Ad, Category, Selection
from users.models import User, Location
from users.serializers import LocationSerializer


class UserLocationSerializer(ModelSerializer):
    locations = LocationSerializer(many=True)

    class Meta:
        model = User
        exclude = ['password']


class AdSerializer(ModelSerializer):
    author = UserLocationSerializer()
    category = SlugRelatedField(slug_field='name', many=False, queryset=Location.objects.all())

    class Meta:
        model = Ad
        fields = '__all__'


class AdListSerializer(ModelSerializer):
    price = SerializerMethodField()
    category = SlugRelatedField(slug_field='name', many=False, queryset=Category.objects.all())
    author = UserLocationSerializer()

    def get_price(self, obj):
        return f'{obj.price} по состоянию на {datetime.now()}'

    class Meta:
        model = Ad
        fields = ['id', 'name', 'author', 'price', 'category']


class AdDetailSerializer(ModelSerializer):
    author = UserLocationSerializer()
    category = SlugRelatedField(slug_field='name', many=False, queryset=Location.objects.all())

    class Meta:
        model = Ad
        fields = '__all__'


class AdCreateSerializer(ModelSerializer):
    author = UserLocationSerializer()
    category = SlugRelatedField(slug_field='name', many=False, queryset=Location.objects.all())

    class Meta:
        model = Ad
        fields = '__all__'


class SelectionSerializer(ModelSerializer):
    class Meta:
        model = Selection
        fields = '__all__'


class SelectionCreateSerializer(ModelSerializer):
    owner = SlugRelatedField(slug_field='username', read_only=True)

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['owner'] = request.user
        return super().create(validated_data)

    class Meta:
        model = Selection
        fields = '__all__'
