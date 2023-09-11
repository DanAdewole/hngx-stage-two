from rest_framework import serializers

from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["id", "name"]
        
        def clean(self):
            cleaned_data = super().clean()
            name = cleaned_data.get("name")
            
            if not isinstance(name, str):
                raise serializers.ValidationError("Name must be a string")
            
    