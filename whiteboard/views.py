from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from whiteboard.permissions import IsOwnerOrReadOnly
from .serializer import WhiteboardSerializer
from .models import Whiteboard
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class WhiteboardList(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Whiteboard.objects.all()
    serializer_class = WhiteboardSerializer

class WhiteboardDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Whiteboard.objects.all()
    serializer_class = WhiteboardSerializer