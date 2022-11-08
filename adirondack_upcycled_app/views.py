from ast import For
from django.shortcuts import render
from .serializers import CategorySerializer, ListingSerializer
from .models import Category, Listing
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

class ListingView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        listings = Listing.objects.all()
        serializer = ListingSerializer(listings, many=True)
        return Response(serializer.data)
    
    def listing(self, request, *args, **kwargs):
        listings_serializer = ListingSerializer(ata=request.data)
        if listings_serializer.is_valid():
            listings_serializer.save()
            return Response(listings_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', listings_serializer.errors)
            return Response(listings_serializer.errors, status=status.HTTP_400_BAD_REQUEST)