import requests
from django.core.management.base import BaseCommand
from commercial.models import Products

class Command(BaseCommand):
    help = 'Fetch products from Fake Store API and save them to the database'

    def handle(self, *args, **kwargs):
        response = requests.get('https://fakestoreapi.com/products')
        products = response.json()

        for product_data in products:
            # Create a product entry in the database
            Products.objects.create(
                title=product_data['title'],
                price=product_data['price'],
                description=product_data['description'],
                category=product_data['category'],
                image=product_data['image']
            )
            self.stdout.write(self.style.SUCCESS(f"Added product: {product_data['title']}"))