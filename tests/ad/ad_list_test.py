import pytest
from rest_framework import status

from ads.serializers import AdListSerializer, AdDetailSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def test_ad_list(client):
    ad_list = AdFactory.create_batch(4)
    response = client.get('/ad/')
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        "count": 4,
        "next": None,
        "previous": None,
        "results": AdListSerializer(ad_list, many=True).data
    }


@pytest.mark.django_db
def test_ad_retrieve(client, access_token):
    ad = AdFactory.create()
    response = client.get(f'/ad/{ad.pk}/', HTTP_AUTHORIZATION=f'Bearer {access_token}')
    assert response.status_code == status.HTTP_200_OK
    assert response.data == AdDetailSerializer(ad).data


@pytest.mark.django_db
def test_ad_create(client, user, category, access_token):
    data = {
        "author": user.username,
        "name": "Что-то очень интересное",
        "category": category.name,
        "price": 100,
        "is_published": False
    }
    expected_data = {
        "id": 6,
        "author": user.username,
        "category": category.name,
        "is_published": False,
        "name": "Что-то очень интересное",
        "price": 100,
        "description": None,
        "image": None
    }
    response = client.post('/ad/', data=data, HTTP_AUTHORIZATION=f'Bearer {access_token}')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data == expected_data
