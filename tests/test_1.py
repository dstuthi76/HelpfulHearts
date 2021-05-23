import pytest
from django.contrib.auth.models import User
from app.views import ProductView
from django.db import connection

@pytest.fixture
def fixture_1():
    print('hi')
    return 1

def test_example(fixture_1):
    num=fixture_1
    assert 1==num

@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('test','test@gmail.com''test')
    assert User.objects.count() == 1

@pytest.fixture()
def user_1(db):
    return User.objects.create_user("test-user")
@pytest.mark.django_db
def test_set_check_password(user_1):
    user_1.set_password("new-password")
    assert user_1.check_password("new-password") is True

@pytest.mark.django_db
def test_product_create():
    User.objects.create_user('test','test@gmail.com''test')
    assert User.objects.count() == 1


@pytest.fixture()
def test_details(rf, admin):
    request = rf.get('/')
    request.user = admin
    response = ProductView(request)
    assert response.status_code == 200


@pytest.fixture()
def test_details1(rf, admin):
    request = rf.get('appointmentform/')
    request.user = admin
    response = DocView(request)
    assert response.status_code == 200

