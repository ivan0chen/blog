from populate import base
from django.contrib.auth.models import User

def populate():
    print('Creating user accounts ... ', end='')
    User.objects.exclude(is_superuser=True).delete()
    for i in range(5):
        username = 'user' + str(i)
        User.objects.create_user(username=username, password=username, email=None)
    print('done')

if __name__ == '__main__':
    populate()