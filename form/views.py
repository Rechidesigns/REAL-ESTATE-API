

from .serializers import BookInspectionSerializer
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import BookInspection
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import NotFound, PermissionDenied
from account.permissions import IsAdminOrReadOnly




# class AppointmentView(APIView):
#     queryset = BookInspection.objects.all()
#     serializer_class = BookInspectionSerializer

#     @swagger_auto_schema(method= "post", request_body=BookInspectionSerializer())
#     @action(detail=False, methods=['post'])
#     def book(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(serializer.data, status=status.HTTP_201_CREATED)

class BookInspectionView(APIView):
    """
    Retrive all or create new land/house Inspection booking instances
    """

    def get(self, request, format=None):
        """ Use this method to get all Houses instances"""

        objs = BookInspection.objects.all() #get data
        serializers = BookInspectionSerializer(objs, many=True)

        data = {
            "message" : "success",
            "data_count" : objs.count(),
            "data" : serializers.data
        }

        return Response(data, status=status.HTTP_200_OK)

    @swagger_auto_schema(method= "post", request_body=BookInspectionSerializer())
    @action(methods=["POST"], detail=True)
    def post(self, request, format=None):

            serializer = BookInspectionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"success"}, status = status.HTTP_200_OK)
            
            return Response({"message":"failed", "error":serializer.errors}, status = status.HTTP_400_BAD_REQUEST)


        

class BookInspectionDetailView(APIView):
    """
    Retrive, update or delete appointmet booking instance..
    """

    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAdminOrReadOnly]

    def get_object(self, appointment_id):
        """"Get a single instance using the provided appointment_id""" 

        try:
            return BookInspection.objects.get(id=appointment_id)
        except BookInspection.DoesNotExist:
            raise NotFound(detail = {"message", "appointment not found"})
        
    def get(self, request, appointment_id, format=None):
        obj = self.get_object(appointment_id)
        serializer = BookInspectionSerializer(obj)

        data = {
            "message" :"success",
            "data" : serializer.data
        }
        return Response(data, status=status.HTTP_201_CREATED)


    @swagger_auto_schema(method="put", request_body=BookInspectionSerializer())
    @action(methods=["PUT"], detail=True)
    def put(self, request, house_id, format=None):
        obj = self.get_object(house_id)
        serializer = BookInspectionSerializer(obj, data=request.data, partial=True)
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
