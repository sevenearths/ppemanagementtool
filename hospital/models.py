from django.db import models

class Hospital(models.Model):
    name = models.CharField(max_length=30)
    ref = models.CharField(max_length=30)
    diaplay_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name+' ('+self.ref+')'

    def slug(self):
        return self.name.lower().replace(' ', '-')

class Stock(models.Model):
    name = models.CharField(max_length=60)
    ref = models.CharField(max_length=30)

    def __str__(self):
        return self.name+' ('+self.ref+')'

class Inventory(models.Model):
    SUPPLIES_CHOICE = (
        ('1', '1 day'),
        ('2', '2 days'),
        ('2-3', '2-3 days'),
        ('>3', '3 or more days'),
    )
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True)
    levels = models.PositiveIntegerField()
    supplies_left = models.CharField(max_length=3, choices=SUPPLIES_CHOICE)
    other = models.CharField(max_length=255, blank=True, null=True)