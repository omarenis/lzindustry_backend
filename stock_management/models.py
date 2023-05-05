from django.db.models import Model, CharField, FloatField, BigIntegerField, TextField, DateTimeField, ForeignKey, \
    CASCADE, SET_NULL, ImageField
from rest_framework.serializers import ModelSerializer, ImageField as ImageFieldSerializer


class Item(Model):
    promo = ForeignKey(to='Promo', on_delete=SET_NULL, null=True)
    store = ForeignKey(to='Store', null=False)
    product = ForeignKey(to='Product', null=False)
    price = FloatField(null=False)
    tva = FloatField(null=False, default=0.19)
    current_quantity = FloatField(null=False, default=1)


# Create your models here.
class Product(Model):
    admin = ForeignKey(to='auth_module.Profile', on_delete=SET_NULL, null=True)
    image = ImageField(upload_to='images/products', null=False)
    category = ForeignKey(to='Category', on_delete=SET_NULL, null=True)
    promo = ForeignKey(to='Promo', on_delete=SET_NULL, null=True)
    code = CharField(null=False, unique=True, max_length=255)
    title = CharField(null=False, unique=True, max_length=255)
    description = TextField(null=False)
    current_quantity = BigIntegerField(null=False, default=1)
    tva = FloatField(null=False)

    class Meta:
        db_table = 'products'


class Category(Model):
    promo = ForeignKey(to='Promo', on_delete=SET_NULL, null=True)
    image = ImageField(upload_to='images/categories', null=False)
    label = CharField(null=False, unique=True, max_length=255)
    description = TextField(null=False)
    number_products = BigIntegerField(null=False, default=0)

    class Meta:
        db_table = 'categories'


class Brand(Model):
    label = CharField(null=False, unique=True, max_length=255)
    number_products = BigIntegerField(null=False, default=0)

    class Meta:
        db_table = 'brands'


class Promo(Model):
    label = CharField(null=False, unique=True, max_length=255)
    datetime_start = DateTimeField(null=False)
    datetime_end = DateTimeField(null=False)
    percentage = FloatField(null=False)
    number_products = BigIntegerField(null=False, default=0)

    class Meta:
        db_table = 'promos'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class PromoSerializer(ModelSerializer):
    class Meta:
        model = Promo
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    category = CategorySerializer(read_only=True)
    promo = PromoSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'code', 'description', 'price', 'current_quantity', 'tva', 'image', 'category',
                  'promo']
