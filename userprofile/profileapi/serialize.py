from rest_framework import serializers
from .models import userProfile

class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 20)

class userProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = userProfile
        fields = ('id','email','name','password')
        exta_kwargs = {'password':{'write_only':True}}
    
    def create(self, validated_data):
        user = userProfile(
            email = validated_data['email'],
            name = validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user