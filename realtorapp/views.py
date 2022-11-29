from django.shortcuts import render
from .models import Houses, Lands
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from account.permissions import IsAdminOrReadOnly
from .serializers import HousesSerializer
from .serializers import LandsSerializer
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.authentication import JWTAuthentication