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



class HousesView(APIView):
    """
    Retrive all or create new Houses instances
    """

    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAdminOrReadOnly]

    def get(self, request, format=None):
        """ Use this method to get all Houses instances"""

        objs = Houses.objects.all() #get data
        serializers = HousesSerializer(objs, many=True)

        data = {
            "message" : "success",
            "data_count" : objs.count(),
            "data" : serializers.data
        }

        return Response(data, status=status.HTTP_200_OK)

    @swagger_auto_schema(method= "post", request_body=HousesSerializer())
    @action(methods=["POST"], detail=True)
    def post(self, request, format=None):

            serializer = HousesSerializer(data=request.data)
            #get the data and deserialization

            if serializer.is_valid():
                serializer.save()
                return Response({"message":"success"}, status = status.HTTP_200_OK)
            
            return Response({"message":"failed", "error":serializer.errors}, status = status.HTTP_400_BAD_REQUEST)


        

class HousesDetailView(APIView):
    """
    Retrive, update or delete a Houses instance..
    """

    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAdminOrReadOnly]

    def get_object(self, house_id):
        """"Get a single instance using the provided house_id""" 

        try:
            return Houses.objects.get(id=house_id)
        except Houses.DoesNotExist:
            raise NotFound(detail = {"message", "House not found"})
        
    def get(self, request, house_id, format=None):
        obj = self.get_object(house_id)
        serializer = HousesSerializer(obj)

        data = {
            "message" :"success",
            "data" : serializer.data
        }
        return Response(data, status=status.HTTP_201_CREATED)


    @swagger_auto_schema(method="put", request_body=HousesSerializer())
    @action(methods=["PUT"], detail=True)
    def put(self, request, house_id, format=None):
        obj = self.get_object(house_id)
        serializer = HousesSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"success"}, status = status.HTTP_200_OK)
        
        return Response({"message":"failed", "error":serializer.errors}, status = status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(method="delete")
    @action(methods=["DELETE"], detail=True)
    def delete(self, request, house_id, formart=None):
        obj = self.get_object(house_id)
        if obj.Houses.count() == 0:

            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        raise PermissionDenied(detail={"message": "cannot delete this house because it contains real Houses."})



class LandsView(APIView):

    """
    Retrive all or create new Land instances.
    """
    
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAdminOrReadOnly]

    
    def get(self, request, format=None):

        objs = Lands.objects.all() #get data
        serializers = LandsSerializer(objs, many=True)

        data = {
            "message" : "success",
            "data_count" : objs.count(),
            "data" : serializers.data
        }

        return Response(data, status=status.HTTP_200_OK)

    @swagger_auto_schema(method="post", request_body=LandsSerializer())
    @action(methods=["POST"], detail=True)
    def post(self, request, format=None):

            serializer = LandsSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({"message":"success"}, status = status.HTTP_200_OK)
        
            return Response({"message":"failed", "error":serializer.errors}, status = status.HTTP_400_BAD_REQUEST)




    
class LandsDetailView(APIView):
    """
    Retrieve, update or delete a Lands instance
    """

    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAdminOrReadOnly]
    
    def get_object(self, land_id):
        """Get a single blog instance using the provided land_id"""
        try:
            return Lands.objects.get(id = land_id)
        except Lands.DoesNotExist:
            raise NotFound(detail = {"message": "Item not found"})
        
    def get(self, request, land_id, format=None):
        obj = self.get_object(land_id)
        serializer = LandsSerializer(obj)
        
        data = {
            "message":"success",
            "data": serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)


    @swagger_auto_schema(method="put", request_body=LandsSerializer())
    @action(methods=["PUT"], detail=True)
    def put(self, request, land_id, format=None):
        obj = self.get_object(land_id)
        serializer = LandsSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"success"}, status = status.HTTP_200_OK)
        
        return Response({"message":"failed", "error":serializer.errors}, status = status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(method="delete")
    @action(methods=["DELETE"], detail=True)   
    def delete(self, request, land_id, format=None):
        obj = self.get_object(land_id)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
