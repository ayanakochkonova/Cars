from django.db import models
class PostCar(models.Model):
    TYPE_CAR = (
        ('Crossover', 'Crossover'),
        ('Hatchback', 'Hatchback'),
        ('SUV', 'SUV'),
        ('Sedan', 'Sedan'),
    )
    title = models.CharField(max_length=50)
    description = models.TextField()
    type_car = models.CharField(max_length=50, choices=TYPE_CAR, null=True)
    image = models.ImageField(upload_to="")
    cost = models.PositiveIntegerField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
