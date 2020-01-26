import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demoproject1.settings')

import django
django.setup()

from faker import Faker

fake = Faker()

# print(fake.name())

from cbvapp.models import Post
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model



# print(User.objects.get(id=1))
user = get_user_model().objects.get(id=1)
for _ in range(10):
    post = Post(title=fake.name() ,author=user, body=fake.sentence())
    post.save()