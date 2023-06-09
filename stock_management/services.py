from common.repositories import Repository
from common.services import Service
from stock_management.models import Product, Category, Promo, Brand

PRODUCT_FIELDS = {
    'title': {'type': 'string', 'required': True, 'unique': True},
    'code': {'type': 'string', 'required': True, 'unique': True},
    'description': {'type': 'string', 'required': True},
    'price': {'type': 'float', 'required': True},
    'tva': {"type": 'float', 'required': True},
    'image': {'type': 'file', 'required': True},
    'ingredients': {'type': 'text', 'required': True},
    'category': {'type': 'foreign_key', 'required': True},
    'promo': {'type': 'foreign_key', 'required': False},
    'current_quantity': {'type': 'integer', 'required': True}
}

CATEGORY_FIELDS = {
    'label': {'type': 'string', 'required': True, 'unique': True},
    'description': {'type': 'string', 'required': True},
    'image': {'type': 'image', 'required': True}
}

BRAND_FIELDS = {
    'label': {'type': 'string', 'required': True}
}

PROMO_FIELDS = {
    'label': {'type': 'string', 'required': True, 'unique': True},
    'datetime_start': {'type': 'datetime', 'required': True},
    'datetime_end': {'type': 'datetime', 'required': True},
    'percentage': {'type': 'float', 'required': True}
}


class ProductService(Service):

    def __init__(self, repository=Repository(model=Product), fields=None):
        if fields is None:
            fields = PRODUCT_FIELDS
        super().__init__(repository, fields)

    def create(self, data: dict):
        product = super().create(data)

        product.category.number_products += 1
        product.category.save()

        product.brand.number_products += 1
        product.brand.save()

        if product.promo is not None:
            product.promo.number_products += 1
            product.promo.save()
        return product

    def delete(self, pk: int):
        product = self.repository.retrieve(pk=pk)
        category = product.category
        brand = product.brand
        promo = product.promo
        deleted = super().delete(pk)
        if deleted:
            category.number_products -= 1
            category.save()

            brand.number_products =- 1
            brand.save()

            if promo is not None:
                promo.number_products -= 1
                promo.save()
        return deleted


class CategoryService(Service):

    def __init__(self, repository=Repository(model=Category), fields=None):
        if fields is None:
            fields = CATEGORY_FIELDS
        super().__init__(repository, fields)


class PromoService(Service):
    def __init__(self, repository=Repository(model=Promo), fields=None):
        if fields is None:
            fields = PROMO_FIELDS
        super().__init__(repository, fields)


class BrandService(Service):
    def __init__(self, repository=Repository(model=Brand), fields=None):
        if fields is None:
            fields = BRAND_FIELDS
        super().__init__(repository, fields)
