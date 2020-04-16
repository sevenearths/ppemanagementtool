from django.db import models
from django.contrib.humanize.templatetags.humanize import naturaltime

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
        ('?', 'Unknown'),
        ('1', '1 day'),
        ('2', '2 days'),
        ('2-3', '2-3 days'),
        ('>3', '3 or more days'),
    )
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True)
    stock_levels = models.PositiveIntegerField()
    supplies_left = models.CharField(max_length=3, choices=SUPPLIES_CHOICE, blank=False, default='?')
    other = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ['created']
        # Usage: Inventory.objects.latest()
        get_latest_by = 'created'

    def __str__(self):
        return self.hospital.name+' - '+self.stock.name+' ('+naturaltime(self.created)+')'
