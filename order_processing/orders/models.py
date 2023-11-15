from django.db import models

class Orders(models.Model):
    id = models.AutoField(primary_key = True)
    created_at = models.DateTimeField(auto_now=True)
    item_name  = models.TextField()
    customer_id  = models.IntegerField()
    count  = models.IntegerField()
    shipment_status = models.TextField(default="")

    def __str__(self):
        return self.name
