from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from profiles_api.permissions import UpdateOwnProfile, UpdateOwnStatus
from profiles_api import serializers
from profiles_api import models


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


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    Handle retrieving, creating, updating and deleting profiles
    """

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = (
        "name",
        "email",
    )


class UserLoginApiView(ObtainAuthToken):
    """
    Handle creating user authentication tokens
    """

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """
    Handles creating, reading and updating profile feed items
    """

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        UpdateOwnStatus,
        IsAuthenticated,
    )

    def perform_create(self, serializer):
        """
        Sets the user profile to the logged in user
        """
        serializer.save(user_profile=self.request.user)
