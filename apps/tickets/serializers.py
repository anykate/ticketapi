from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Ticket, Category


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User

        # DO NOT INCLUDE 'PASSWORD' field here
        # fields = ('url', 'username', 'email',
        #           'is_active', 'is_staff', 'is_superuser', 'password',)

        fields = ('url', 'username', 'email',
                  'is_active', 'is_staff', 'is_superuser',)

        # These fields are displayed but not editable and have to be a part of 'fields' tuple
        read_only_fields = ('is_active', 'is_staff', 'is_superuser',)

        # These fields are only editable (not displayed) and have to be a part of 'fields' tuple
        extra_kwargs = {'password': {'write_only': True, 'min_length': 4}}

    # Update user password with hash - DO NOT DO THIS
    # def update(self, instance, validated_data):
    #     instance.set_password(validated_data['password'])
    #     instance.save()
    #     return instance


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('url', 'name', 'slug',)


# Serializers define the API representation.
class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id', 'title', 'ticket_id', 'user',
                  'content', 'category', 'created', 'modified',)
