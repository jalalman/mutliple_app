from django.db import models

# Create your models here.
class Show(models.Model):
    title=models.CharField(max_length=50)
    network=models.CharField(max_length=50)
    releaseDate=models.CharField(max_length=50)
    desc=models.TextField(default="")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)



def create_show(data):

    show =Show.objects.create(title=data['title'],network=data['network'],releaseDate=data['releasedate'],desc=data['desc'])
    return show



def get_all_shows():

    return Show.objects.all()

def get_show(id):

    return Show.objects.get(id=id)


def updateShow(data):
    show=Show.objects.get(id=data['show_id'])
    show.title=data['title']
    show.network=data['network']
    show.releaseDate=data['releasedate']
    show.desc=data['desc']
    show.save()


def deleteShow(id):
    Show.objects.get(id=id).delete()