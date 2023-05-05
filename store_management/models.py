from django.db.models import Model, TextField, CharField, ImageField, FloatField, ForeignKey, SET_NULL


# Create your models here.
class Localisation(Model):
    governorate = TextField(null=False)
    region = TextField(null=False)
    delegation = TextField(null=False)
    zip_code = CharField(null=False, max_length=4)


class Store(Model):
    manager = ForeignKey(to='auth_module.Profile', on_delete=SET_NULL, null=True)
    name = TextField(null=False)
    number_products = FloatField(default=0)
    localisation = ForeignKey(to='Localisation')
    number_tags = FloatField(null=False, default=0)
    address = TextField(null=False)
