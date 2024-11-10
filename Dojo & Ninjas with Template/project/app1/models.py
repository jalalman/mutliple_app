from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=2)
    desc=models.TextField(default='')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Ninja(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    dojo=models.ForeignKey(Dojo,related_name='ninjas',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

def create_Dojo(data):

    Dojo.objects.create(name=data['name'],city=data['city'],state=['state'])
    print('done')
def getAllDojo():

    return Dojo.objects.all()

def create_ninja(data):
    this_dojo=Dojo.objects.get(id=data['dojo'])
    Ninja.objects.create(first_name=data['fname'],last_name=data['lname'],dojo=this_dojo)

def getAllNinja():
    return Ninja.objects.all()


def deleteDojo(id):
    temp = Dojo.objects.get(id=id)
    temp.delete()

def deleteNinja(id):
    temp = Ninja.objects.get(id=id)
    temp.delete()