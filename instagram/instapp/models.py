from django.db import models


class Profile(models.Model):
    profile_photo = models.CharField(max_length =1000)
    bio = models.CharField(max_length =1000)
    user = models.CharField(max_length =1000,)
    def __str__(self):
            return self.bio + ' - ' + self.user



class Image(models.Model):
    image = models.CharField(max_length=1000)
    image_name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=30)
    likes = models.CharField(max_length=30)
    comments = models.CharField(max_length=30)
    profile =models.ForeignKey(Profile, null = True,on_delete=models.CASCADE)


    def __str__(self):
        return self.image_name + ' - ' + self.image_caption


    def get_absolute_url(self):
        return reverse('instapp:detail', kwargs={'pk': self.pk})