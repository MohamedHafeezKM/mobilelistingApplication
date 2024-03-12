from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

# Create your views here.

from api.serializers import MobileSerializer
from api.models import Mobile

class MobileView(ViewSet):
    def list(self,request,*args,**kwargs):
        qs=Mobile.objects.all()
        deserializer=MobileSerializer(qs,many=True)
        return Response(data=deserializer.data)
    
    def create(self,request,*args,**kwargs):
        serializer=MobileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        mobile_object=Mobile.objects.get(id=id)
        deserializer=MobileSerializer(mobile_object,many=False)
        return Response(data=deserializer.data)
    
    def update(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        mobile_object=Mobile.objects.get(id=id)
        serializer=MobileSerializer(data=request.data,instance=mobile_object)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        Mobile.objects.get(id=id).delete()
        return Response({'message':'This mobile has been deleted'})