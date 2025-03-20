from rest_framework import serializers
from.models import Product,Collection
from decimal import Decimal


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields=['id','title']



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields=['id','title','unit_price','collection','price_with_tax','inventory']
    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # unit_price = serializers.DecimalField(max_digits=6, decimal_places=2)
    price_with_tax = serializers.SerializerMethodField()
#     collection = serializers.HyperlinkedRelatedField(
#     queryset=Collection.objects.all(),
#     view_name='collection-detail'
# )

   # price_with_tax_2 = serializers.SerializerMethodField(method_name="calculate_tax")
   # collection_id = serializers.PrimaryKeyRelatedField(queryset=Collection.objects.all())
    #collection=serializers.StringRelatedField()
    # nested serializer
    # collection=CollectionSerializer()
    # def calculate_tax(self, product: Product):
    #     return round(product.unit_price * Decimal(1.1),2)
    def get_price_with_tax(self, obj):
        return round(float(obj.unit_price) * 1.1 ,2) # Assuming 10% tax
