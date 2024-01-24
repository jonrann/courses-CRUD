from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateField(blank=True, null=True)
    # description = 'description from class Description'
    # comments = list of comments from class Comment

    def __str__(self) -> str:
        return self.name

class Description(models.Model):
    content = models.TextField(blank=True, null=True)
    course = models.OneToOneField(Course, on_delete=models.CASCADE, related_name='description')
    
    def __str__(self) -> str:
        return f"{self.course.name}"

# Courses can have many comments but comments can be made to ONE course
class Comment(models.Model):
    content = models.CharField(max_length=300)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments')
    # If i had a users model, i would make it so that comments belong to a user
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments_made)

    def __str__(self) -> str:
        return f"{self.course.name}"