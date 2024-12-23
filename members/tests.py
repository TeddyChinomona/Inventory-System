from rest_framework.test import APIClient
from rest_framework import status
from .models import Name
import pytest

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_member():
    def create(**kwargs):
        return Name.objects.create(**kwargs)
    
@pytest.mark.django_db
def get_info(create_member, api_client):
    create_member(name = 'ted',surname = 'chin', gender = 'M')
    
    response = api_client.get("/api/members/")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]["name"] == "ted"





