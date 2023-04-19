import os
import django
from random import choice, randint

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from funkify.models import (
    WebServer,
    DatabaseServer,
    HighPerformanceSAN,
    HighCapacitySAN,
    GeoDNS,
    LoadBalancer,
)

def populate_web_servers(num=10):
    domains = [f"example{i}.com" for i in range(num)]

    for domain in domains:
        WebServer.objects.create(
            active_record=randint(0, 1),
            cpu=randint(2, 16),
            memory=randint(4, 64),
            domain=domain
        )

def populate_database_servers(num=5):
    database_types = ['PostgreSQL', 'MySQL', 'Oracle', 'SQLServer']

    for _ in range(num):
        DatabaseServer.objects.create(
            active_record=randint(0, 1),
            cpu=randint(2, 16),
            memory=randint(4, 64),
            database_type=choice(database_types)
        )

def populate_high_performance_sans(num=5):
    for _ in range(num):
        HighPerformanceSAN.objects.create(
            active_record=randint(0, 1),
            storage_capacity=randint(1024, 8192),
            iops=randint(10000, 50000)
        )

def populate_high_capacity_sans(num=5):
    for _ in range(num):
        HighCapacitySAN.objects.create(
            active_record=randint(0, 1),
            storage_capacity=randint(1024, 8192),
            redundancy_level=randint(1, 3)
        )

def populate_geo_dns(num=5):
    dns_zones = [f"geo_zone{i}.com" for i in range(num)]
    load_balancing_methods = ['Round Robin', 'Least Connections', 'Fastest Response']

    for dns_zone in dns_zones:
        GeoDNS.objects.create(
            active_record=randint(0, 1),
            load_balancing_method=choice(load_balancing_methods),
            dns_zone=dns_zone
        )

def populate_load_balancers(num=5):
    for _ in range(num):
        LoadBalancer.objects.create(
            active_record=randint(0, 1),
            virtual_servers=randint(1, 10),
            pool_size=randint(2, 20)
        )

if __name__ == '__main__':
    populate_web_servers()
    populate_database_servers()
    populate_high_performance_sans()
    populate_high_capacity_sans()
    populate_geo_dns()
    populate_load_balancers()
    print("Database populated successfully!")
