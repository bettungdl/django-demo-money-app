from django.db import models

class Wallet(models.Model):
    balance = models.DecimalField(max_digits=10000, decimal_places=2, default=0.00)

    def __str__(self):
        return str(self.id)

    