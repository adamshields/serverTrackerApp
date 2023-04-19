import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from funkifymorphic.models import ServerResource, SANResource, GTMResource, LTMResource

def create_server_resource(active_record, cpu, memory, domain):
    server = ServerResource(active_record=active_record, cpu=cpu, memory=memory, domain=domain)
    server.save()
    return server

def create_san_resource(active_record, storage_capacity, redundancy_level):
    san = SANResource(active_record=active_record, storage_capacity=storage_capacity, redundancy_level=redundancy_level)
    san.save()
    return san

def create_gtm_resource(active_record, load_balancing_method, dns_zone):
    gtm = GTMResource(active_record=active_record, load_balancing_method=load_balancing_method, dns_zone=dns_zone)
    gtm.save()
    return gtm

def create_ltm_resource(active_record, virtual_servers, pool_size):
    ltm = LTMResource(active_record=active_record, virtual_servers=virtual_servers, pool_size=pool_size)
    ltm.save()
    return ltm

def populate():
    # Create some ServerResources
    create_server_resource(1, 8, 16, 'example.com')
    create_server_resource(2, 16, 32, 'example2.com')

    # Create some SANResources
    create_san_resource(1, 1024, 2)
    create_san_resource(2, 2048, 3)

    # Create some GTMResources
    create_gtm_resource(1, 'Round Robin', 'example.com')
    create_gtm_resource(2, 'Least Connections', 'example2.com')

    # Create some LTMResources
    create_ltm_resource(1, 10, 20)
    create_ltm_resource(2, 15, 30)

if __name__ == '__main__':
    print('Populating the database... Please wait.')
    populate()
    print('Population complete!')
