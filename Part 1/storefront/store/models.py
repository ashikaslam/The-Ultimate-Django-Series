from django.db import models




class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_products=models.ForeignKey("Product", on_delete=models.SET_NULL,related_name='+',null=True)



class Product(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    price=models.DecimalField(max_digits=6, decimal_places=2)
    inventory=models.ImageField()
    last_update=models.DateTimeField(auto_now=True)
    collection=models.ForeignKey(Collection, on_delete=models.PROTECT)
    """
Alternative on_delete Options:
CASCADE → Deletes all related Product instances when a Collection is deleted.
SET_NULL → Sets collection to NULL in Product when Collection is deleted (requires null=True).
SET_DEFAULT → Assigns a default collection when the referenced Collection is deleted.
DO_NOTHING → Prevents deletion but doesn't enforce protection (may cause database integrity issues).
    """
    Promotion =models.ManyToManyField(Promotion)


class Customer(models.Model):
    MEMBERSHIP_BRONZE="B"
    MEMBERSHIP_SILVER="S"
    MEMBERSHIP_GOLD="G"
    MEMBERSHIP_CHOICE=[
        (MEMBERSHIP_BRONZE,"BRONZE"),
        (MEMBERSHIP_SILVER,"SILVER"),
        (MEMBERSHIP_GOLD,"GOLD"),
    ]
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254,unique=True)
    phone=models.CharField(max_length=50)
    birth_date=models.DateField(null=True)
    membership=models.CharField(max_length=5,choices=MEMBERSHIP_CHOICE,default=MEMBERSHIP_BRONZE)

    # class Meta:
    #     db_table = 'store_customers'
    #     indexes = [
    #        models.Index(fields=["first_name","last_name"])
    #     ]
       



class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed'),
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status=models.CharField(max_length=50,choices=PAYMENT_STATUS_CHOICES,default=PAYMENT_STATUS_PENDING)



class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    zip = models.CharField(max_length=10)






class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed'),
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1,
        choices=PAYMENT_STATUS_CHOICES,
        default=PAYMENT_STATUS_PENDING
    )
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)




class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)



class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
