from django.db import models

class BookARI(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    url = models.CharField(max_length=500)
    n_characters = models.IntegerField()
    n_words = models.IntegerField()
    n_sentences = models.IntegerField()
    ari = models.IntegerField()
    age_range = models.CharField(max_length=50)
    grade_level = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title + ' ' + str(self.ari)


