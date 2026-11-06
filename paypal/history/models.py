from django.db import models

class History(models.Model):
    HistoryType = (
        ('recharge', 'Recharge'),
        ('send_money', 'Send Money'),
    )
    type = models.CharField(max_length=255, choices=HistoryType)
    target_user = models.ForeignKey('user.User', related_name='target_user', on_delete=models.SET_NULL, null=True, blank=True)
    origin_user = models.ForeignKey('user.User', related_name='origin_user', on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    message = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

