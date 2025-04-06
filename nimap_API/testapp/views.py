from .models import Client, Project
from .serializers import ClientSerializer,ProjectSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class ClientAPI(APIView):
    def get(self, request):
        queryset = Client.objects.all()
        serializer = ClientSerializer(queryset, many=True)
        return Response({
            "data": serializer.data
        })

    def post(self, request):
        data = request.data
        serializer = ClientSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                "message": "data not saved",
                "errors": serializer.errors
            })
        serializer.save(created_by=request.user)
        return Response({
            "message": "data saved",
            "data": serializer.data
        })

    def delete(self, request):
        data = request.data
        if not data.get('id'):
            return Response({
                "message": "data not delete",
                "errors": "id is required"
            })
        client = Client.objects.get(id=data.get('id')).delete()
        return Response({
            "message": "data deleted"
        })

    def patch(self, request):
        data = request.data
        if not data.get('id'):
            return Response({
                "message": "data not updated",
                "errors": "id is required"
            })
        client = Client.objects.get(id=data.get('id'))
        serializer = ClientSerializer(
            client, data=data, partial=True
        )
        if not serializer.is_valid():
            return Response({
                "message": "data not saved",
                "errors": serializer.errors
            })
        serializer.save()
        return Response({
            "message": "data saved",
            "data": serializer.data
        })


class ProjectAPI(APIView):
    def get(self, request):
        queryset = Project.objects.all()
        serializer = ProjectSerializer(queryset, many=True)
        return Response({
            "data": serializer.data
        })

    def post(self, request):
        data = request.data
        serializer = ProjectSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                "message": "data not saved",
                "errors": serializer.errors
            })
        serializer.save(created_by=request.user)
        return Response({
            "message": "data saved",
            "data": serializer.data
        })


    def delete(self, request):
        data = request.data
        if not data.get('id'):
            return Response({
                "message": "data not delete",
                "errors": "id is required"
            })
        client = Project.objects.get(id=data.get('id')).delete()
        return Response({
            "message": "data deleted"
        })

    def patch(self, request):
        data = request.data
        if not data.get('id'):
            return Response({
                "message": "data not updated",
                "errors": "id is required"
            })
        client = Project.objects.get(id=data.get('id'))
        serializer = ProjectSerializer(
            client, data=data, partial=True
        )
        if not serializer.is_valid():
            return Response({
                "message": "data not saved",
                "errors": serializer.errors
            })
        serializer.save()
        return Response({
            "message": "data saved",
            "data": serializer.data
        })

