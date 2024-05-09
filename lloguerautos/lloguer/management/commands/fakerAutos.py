from django.core.management.base import BaseCommand
from faker import Faker
from faker_vehicle import VehicleProvider
from lloguer.models import Automobil

fake = Faker()
fake.add_provider(VehicleProvider)

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Generando datos...")

        # Generar 200 coches falsos
        for _ in range(200):
            marca = fake.vehicle_make()
            modelo = fake.vehicle_model()
            matricula = fake.license_plate()
            automovil = Automobil(marca=marca, model=modelo, matricula=matricula)
            automovil.save()

        self.stdout.write(self.style.SUCCESS('¡Se han generado 200 coches!'))

