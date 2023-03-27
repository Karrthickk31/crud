from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_customer = models.BooleanField('Is customer', default=False)
    is_employee = models.BooleanField('Is employee', default=False)


class Instruction(models.Model):
    state_choices = [('All States', 'All States'), ('AL', 'AL'), ('AK', 'AK'), ('AZ', 'AZ'), ('AR', 'AR'), ('CA', 'CA'), ('CO', 'CO'), ('CT', 'CT'), ('DE', 'DE'), ('DC', 'DC'), ('FL', 'FL'), ('GA', 'GA'), ('HI', 'HI'), ('ID', 'ID'), ('IL', 'IL'), ('IN', 'IN'), ('IA', 'IA'), ('KS', 'KS'), ('KY', 'KY'), ('LA', 'LA'), ('ME', 'ME'), ('MD', 'MD'), ('MA', 'MA'), ('MI', 'MI'), ('MN', 'MN'), ('MS', 'MS'), ('MO', 'MO'), ('MT', 'MT'), ('NE', 'NE'), ('NV', 'NV'), ('NH', 'NH'), ('NJ', 'NJ'), ('NM', 'NM')]
    state = models.CharField(choices=state_choices, max_length=10)

    document_choices = [('All Documents', 'All Documents'), ('QCD', 'QCD'),('SWD', 'SWD'),('GWD', 'GWD'),('DIL', 'DIL')]
    document = models.CharField(choices=document_choices, max_length=20)

    client_choices = [('All Clients', 'All Clients'), ('TF', 'TF'), ('WFG', 'WFG'), ('SLINK', 'SLINK') ,('AMR', 'AMR')]
    client = models.CharField(choices=client_choices, max_length=20)
    
    #information = models.CharField(max_length=100)
    information = models.TextField()

    def __str__(self):
        return f"{self.information}"