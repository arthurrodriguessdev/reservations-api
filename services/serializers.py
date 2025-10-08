from rest_framework import serializers
from services.models import Service


#Serializer puro, na mão
'''class ServiceSerializer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    duration = serializers.IntegerField()
    description = serializers.CharField()'''

#Serializer usando model serializer
class ServiceModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Service

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError('O valor do serviço deve ser maior que R$0.0')
        return value
    
    def validate_name(self, value):
        service = Service.objects.filter(name__iexact=value)

        if self.instance:
            service = service.exclude(pk=self.instance.pk)
        if service.exists():
            raise serializers.ValidationError('Já existe um serviço cadastrado com esse nome')
        return value
    
    def validate_description(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('A descrição do serviço não poode ultrapassar 200 caracteres')
        return value