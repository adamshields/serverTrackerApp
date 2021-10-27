from django.test import TestCase

# Create your tests here.
from devices.models import Publisher, Software, Device
# New Device
new_device = Device.objects.create(name='My New Device', status='True')

# New Publisher
new_publisher = Publisher.objects.create(name='My Publisher', status='True')


# New software
new_software = Software.objects.create(name='New Software', status='True', version='1.2.3', publisher=new_publisher)


# Add Software with Publisher to Device
new_device.software.add(new_software)


