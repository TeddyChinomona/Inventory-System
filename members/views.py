from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from rest_framework.permissions import IsAuthenticated
from loguru import logger

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Name.objects.all()
    serializer_class = MemberSerializers
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data
        name = data.get('name')
        surname = data.get('surname')

        if Name.objects.filter(name = name).exists() and Name.objects.filter(surname = surname).exists():
            return HttpResponse(status = status.HTTP_406_NOT_ACCEPTABLE)
        return super().create(request, *args, **kwargs)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data  = request.data
        name = data.get('name')
        description = data.get('description')
        members = data.get('member')
        logger.info(f'name: {name}, description: {description}, members: {members}')
        if Product.objects.filter(name = name).exists():
            return HttpResponse(status.HTTP_409_CONFLICT)
        else:
            new_product = Product.objects.create(
                name = name,
                description = description
            )
            new_product.save()

            for data in members:
                surname = data.get('surname')
                logger.info(f'surname: {surname}')
                member_data = Name.objects.get(surname = data.get('surname'))
                new_product.member.add(member_data)
            serializer = ProductSerializers(new_product)
            return JsonResponse(serializer.data, status = status.HTTP_201_CREATED)