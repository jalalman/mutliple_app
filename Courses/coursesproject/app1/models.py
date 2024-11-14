from django.db import models




class CourseManager(models.Manager):
    def basic_validator(self,postDate):
        error={}
        if len(postDate['name'])<5:
            error['name']="name should be more the 5 chars"
        if len(postDate['desc'])<15:
            error['desc']='description should be more that 15 chars'

        return error


# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=15)
    desc=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects= CourseManager()

def createCourse(data):
    Course.objects.create(name=data['name'],desc=data['desc'])


def get_all_course():

    return Course.objects.all()


def get_course_id(id):

    return Course.objects.get(id=id)

def deleteCourse(id):

    Course.objects.get(id=id).delete()


