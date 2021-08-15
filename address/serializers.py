from rest_framework import serializers
from .models import Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields='__all__'

    def create(self, validated_data):
        if 'email' in validated_data:
            if Address.objects.filter(email=validated_data['email']).exists():
                raise serializers.ValidationError({"detail":"Email already exists!"})

        if 'number' in validated_data:
            if Address.objects.filter(number=validated_data['number']).exists():
                raise serializers.ValidationError({"detail":"Number already exists!"})

        if Address.objects.filter(street=validated_data['street'],city=validated_data['city'],country=validated_data['country'],zip=validated_data['zip']).exists():
            raise serializers.ValidationError({"detail":"Address already exists!"})

        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance
