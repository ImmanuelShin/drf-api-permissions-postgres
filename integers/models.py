from django.contrib.auth import get_user_model
from django.db import models

RATING_CHOICES = [
    (1, '1 - Poor'),
    (2, '2 - Below Average'),
    (3, '3 - Average'),
    (4, '4 - Above Average'),
    (5, '5 - Excellent'),
]

class Integer(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    description = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES, default=3) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name