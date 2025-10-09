from rest_framework import serializers
from services.models import Service
from review.models import Review

class ServiceModelSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    class Meta:
        fields = '__all__'
        model = Service

    def validate(self, data):
        if data['price'] <= 0:
            raise serializers.ValidationError('O valor do serviço deve ser maior que R$0.0')
        
        if data.get('name'):
            service = Service.objects.filter(name__iexact=data['name'])

            if self.instance:
                service = service.exclude(pk=self.instance.pk)

            if service.exists():
                raise serializers.ValidationError('Já existe um serviço cadastrado com esse nome')
        
        if len(data['description']) > 200:
            raise serializers.ValidationError('A descrição do serviço não pode ultrapassar 200 caracteres')
        
        if data['duration'] < 0:
            raise serializers.ValidationError('A duração não pode ser negativa')
        
        return data
    

    def get_average_rating(self, obj):
        reviews = Review.objects.filter(service=obj)
        review_quantity = Review.objects.filter(service=obj).count()

        stars = 0
        if reviews.exists():
            for rev in reviews:
                stars += rev.stars
            return stars / review_quantity
        else:
            return 0