import pytest

from drfa.views import APIView
from drfa.decorators import api_view

from rest_framework import status
from rest_framework.test import APIRequestFactory
from rest_framework.response import Response

pytestmark = pytest.mark.asyncio

factory = APIRequestFactory()


@pytest.fixture
def class_view():
    class AsyncView(APIView):
        async def get(self, request, *args, **kwargs):
            return Response({"method": "GET"})

        async def post(self, request, *args, **kwargs):
            return Response({"method": "POST", "data": request.data})

    return AsyncView.as_view()


@pytest.fixture
def function_view():
    @api_view(["GET", "POST", "PUT", "PATCH"])
    async def async_view(request):
        if request.method == "GET":
            return Response({"method": "GET"})
        elif request.method == "POST":
            return Response({"method": "POST", "data": request.data})
        elif request.method == "PUT":
            return Response({"method": "PUT", "data": request.data})
        elif request.method == "PATCH":
            return Response({"method": "PATCH", "data": request.data})

    return async_view


async def test_class_get_succeed(class_view):
    request = factory.get("/")
    response = await class_view(request)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {"method": "GET"}


async def test_class_post_succeed(class_view):
    request = factory.post("/", {"test": "foo"})
    response = await class_view(request)
    expected = {"method": "POST", "data": {"test": ["foo"]}}
    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected


async def test_class_options_succeeds(class_view):
    request = factory.options("/")
    response = await class_view(request)
    assert response.status_code == status.HTTP_200_OK


async def test_function_get_succeed(function_view):
    request = factory.get("/")
    response = await function_view(request)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {"method": "GET"}


async def test_function_post_succeed(function_view):
    request = factory.post("/", {"test": "foo"})
    response = await function_view(request)
    expected = {"method": "POST", "data": {"test": ["foo"]}}
    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected


async def test_function_options_succeeds(function_view):
    request = factory.options("/")
    response = await function_view(request)
    assert response.status_code == status.HTTP_200_OK
