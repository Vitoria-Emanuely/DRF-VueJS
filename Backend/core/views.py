from core.models import Certificado, Group
from rest_framework.serializers import ModelSerializer, SlugRelatedField, SerializerMethodField
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from datetime import timedelta


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['cod']

class CertificadoSerializer(ModelSerializer):
    expirated_at = SerializerMethodField()
    groups = SlugRelatedField(
        many=True,
        slug_field='cod',
        queryset = Group.objects.all()
    )
    class Meta:
        model = Certificado
        fields = [
            'id',
            'username',
            'name',
            'description',
            'groups',
            'expiration',
            'expirated_at',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at', 'expirated_at']
                                                                                
    def get_expirated_at (self, instance):
        return (instance.updated_at+timedelta(days=instance.expiration)).strftime("%Y-%m-%dT%H:%M:%S-03:00")     
        

class CertificadosList(ListCreateAPIView):
    queryset = Certificado.objects.all()
    serializer_class = CertificadoSerializer

class CertificadoDetail(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Certificado.objects.all()
    serializer_class = CertificadoSerializer
