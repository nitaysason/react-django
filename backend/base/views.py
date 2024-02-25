from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Drugs
from rest_framework import serializers

class DrugsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drugs
        fields = '__all__'


@api_view(['GET'])
def drugs(req):
    pro_drugs = Drugs.objects.all()
    return Response(DrugsSerializer( pro_drugs, many=True).data)

@api_view(['POST'])
def adddrug(req):
    pro_drug = DrugsSerializer(data=req.data)
    if pro_drug.is_valid():
       pro_drug.save()
    return Response("post...")


@api_view(['DELETE'])
def deldrug(req, id=-1):
    pro_drug = Drugs.objects.get(id=id)
    pro_drug.delete()
    return Response("del...")


@api_view(['PUT'])
def updatedrug(req, id=-1): 
    pro_drug = Drugs.objects.get(id=id)
    serializer = DrugsSerializer(pro_drug, data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


