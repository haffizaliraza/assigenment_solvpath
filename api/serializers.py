from rest_framework import serializers
from .models import User, Product, Price, ProductReview, LocalSellerDetail,LocalSellerUploadedData
from rest_framework.validators import UniqueTogetherValidator


# Model Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'dob', 'email', 'contact_no', 'state']

        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['username']
            )

        ]


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


class ProductReviewSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()

    class Meta:
        model = ProductReview
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'


class LocalSellerDetailSerializer(serializers.ModelSerializer):
    local_seller = serializers.StringRelatedField()

    class Meta:
        model = LocalSellerDetail
        fields = ['id', 'local_seller', 'shop_name', 'shop_address']


class LocalSellerUploadedDataSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = LocalSellerUploadedData
        fields = '__all__'
