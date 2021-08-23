from django.test import TestCase

# Create your tests here.
from servers.models import Publisher, Software, Server
# New Server
new_server = Server.objects.create(name='My New Server', status='True')

# New Publisher
new_publisher = Publisher.objects.create(name='My Publisher', status='True')


# New software
new_software = Software.objects.create(name='New Software', status='True', version='1.2.3', publisher=new_publisher)


# Add Software with Publisher to Server
new_server.software.add(new_software)


