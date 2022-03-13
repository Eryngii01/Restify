from rest_framework import serializers

from restaurants.models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    # Custom serializer field to show owner name instead of id
    # Two queries, since we're checking the User model as well
    owner = serializers.CharField(source='owner.get_full_name', read_only=True)

    class Meta:
        model = Restaurant
        fields = ['name', 'address', 'logo', 'postal_code', 'phone_number', 'owner', 'followers', 'likes']