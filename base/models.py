from django.db import models

# Create your models here.

class Quote(models.Model):
    class QuoteTypeChoice(models.TextChoices):
        lagos = 'Lagos', 'Lagos'
        inter_state = 'Inter-State', 'Inter-State'
    name = models.CharField(max_length=255)
    email = models.EmailField()
    quote_type = models.CharField(max_length=255,default=QuoteTypeChoice.lagos, choices=QuoteTypeChoice.choices)
    date_requested = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.quote_type} delivery quote requested by {self.name}'