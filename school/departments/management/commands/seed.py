from django.core.management.base import BaseCommand
from departments.models import Students
from faker import Faker
from django.utils import timezone

fake = Faker()

class Command(BaseCommand):
    help = "Seed the Departments app with sample Students"

    def add_arguments(self, parser):
        parser.add_argument('--number', type=int, default=10, help='How many students to create')

    def handle(self, *args, **options):
        number = options['number']
        for _ in range(number):
            Students.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                registration=f"REG{fake.unique.random_number(digits=6)}",
                published_date=timezone.now(),
            )
        self.stdout.write(self.style.SUCCESS(f'Created {number} Students.'))
