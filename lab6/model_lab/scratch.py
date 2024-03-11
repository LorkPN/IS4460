#import manage.py and validate settings
#equivalent to what Django does when you type "python manage.py shell" in the command line
#this makes it so you can run this script instead of copying the lines into a shell
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "model_lab.settings")

import django
django.setup()

from django.core.management import call_command
#end manage.py commands
from customer.models import Customer, Order

#Customers
Customer.objects.create(name="Matt Young", email="u1285039@utah.edu")
Customer.objects.create(name="Offa of Mercia", email="offarex@aol.com")
Customer.objects.create(name="Alfred the Great", email="vikingslayer@aol.com")
Customer.objects.create(name="Ethelred the Unready", email="denmarksux@aol.com")
Customer.objects.create(name="Cnut the Great", email="tidestaller@yahoo.com")
Customer.objects.create(name="Harald Hardrada", email="denmarkforever@yahoo.com")
Customer.objects.create(name="Henry I", email="goldenrule@gmail.com")
Customer.objects.create(name="Henry II", email="deathandtaxes@gmail.com")

cnut = Customer.objects.get(name="Cnut the Great")
henry1 = Customer.objects.get(name="Henry I")
henry2 = Customer.objects.get(name="Henry II")

#Orders
Order.objects.create(customer=cnut, total_price=56.71, total_items=7, order_date="1018-5-31")
Order.objects.create(customer=henry1, total_price=12.02, total_items=2, order_date="1120-7-7")
Order.objects.create(customer=henry1, total_price=9.72, total_items=1, order_date="1125-12-25")
Order.objects.create(customer=cnut, total_price=56.71, total_items=7, order_date="1019-5-7")
Order.objects.create(customer=henry2, total_price=112.53, total_items=15, order_date="1157-8-13")
Order.objects.create(customer=cnut, total_price=565.56, total_items=37, order_date="1030-11-11")