import csv, sys, os

project_dir = "/Users/priyam/Desktop/django/old_projects/beta/beta/beta"

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from users.models import Users
from newspapers.models import Newspapers
from pincode.models import Pincode

# data = csv.reader(open("/Users/priyam/Desktop/django/old_projects/beta/beta/newspaper_data.csv"),delimiter=",")

data = csv.reader(open("/Users/priyam/Desktop/django/old_projects/beta/beta/pincode.csv"),delimiter=",")

for row in data:
	instance = Pincode()
	instance.pin=row[0]
	
	instance.save()
	