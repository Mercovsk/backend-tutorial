from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)

    @property
    def sale_price(self):
        return f"{float(self.price) * 0.8:.2f}"
    
    def bulk_order_price(self):
        if self.price >= 250:
            return f"{float(self.price) - 50:.2f}"
        else:
            return f"{float(self.price) - 15:.2f}"
        
    def __str__(self):
        return self.title
