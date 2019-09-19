import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','DjangoProjecr.settings')

import django
django.setup()

import random
from HelloApp.models import AccessRecord,Topic,Webpage,Users
import faker


topics = ['search','social','networking','marketing']

def add_Topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate(n):
    for _ in range(n):
        topic = add_Topic()
        fakege = faker.Faker()
        fake_url = fakege.url()
        fake_date = fakege.date()
        fake_name = fakege.company()

        webpge = Webpage.objects.get_or_create(topic = topic,url = fake_url,name = fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name = webpge,date = fake_date)[0]

def populateUser(n):
    for _ in range(n):
        fakege = faker.Faker()
        fake_name = fakege.name().split()
        fake_fname = fake_name[0]
        fake_lname = fake_name[1]
        fake_email = fakege.email()

        #Creating Entry
        Users.objects.get_or_create(fname = fake_fname,lname = fake_lname, email = fake_email)[0]

print('Populating')
# populate(20)
populateUser(20)
print('done')