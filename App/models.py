from django.db import models

class Singer(models.Model):
    Name = models.CharField(max_length=100)
    Phone = models.CharField(max_length=15)
    Email = models.EmailField(max_length=100)
    
    def __str__(self):
        return self.Name+str(self.id)

class Song(models.Model):
    singer = models.ManyToManyField(Singer)
    Name = models.CharField(max_length=100)
    Duration = models.CharField(max_length=5)
    Published_at = models.DateField(auto_now_add=True)

    def written_by(self):
        return ",".join([str(p) for p in self.singer.all()])
