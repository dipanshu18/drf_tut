from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers


class HelloApiView(APIView):
    """
    Test API View
    """

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """
        Returns a list of APIView feats
        """
        an_apiview = [
            "Uses HTTP methods as function (get, post, patch, put, delete)",
            "Is similar to a traditional Django view",
            "Gives you the most control over your application logic",
            "Is mapped manually to URLs",
        ]

        return Response({"message": "Hello", "an_apiview": an_apiview})

    def post(self, request):
        """
        Create a hello message with our name
        """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello, {name}"

            return Response({"message": message}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        """
        Handle a partial update of an object
        """
        return Response({"method": "PATCH"})

    def delete(self, request, pk=None):
        """
        Handle delete an object
        """
        return Response({"method": "DELETE"})


class HelloViewSet(viewsets.ViewSet):
    """
    Test API Viewsets
    """

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """
        Returns a list of items
        """

        a_viewset = [
            "User actions (list, create, retrieve, update, parital_update, destroy)",
            "Automatically maps to URLs using routers",
            "Provides more functionality with less code",
        ]

        return Response({"message": "Hello", "a_viewset": a_viewset})

    def create(self, request):
        """
        Create a new hello message
        """

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello, {name}!"

            return Response({"message": message}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """
        Handle getting an object by its ID
        """

        return Response({"http_method": "GET"})

    def update(self, request, pk=None):
        """
        Handle updating an object
        """

        return Response({"http_method": "PUT"})

    def partial_update(self, request, pk=None):
        """
        Handle partial update of an object
        """

        return Response({"http_method": "PATCH"})

    def destroy(self, request, pk=None):
        """
        Handle deleting of an object
        """

        return Response({"http_method": "DELETE"})
