from django.db import models
from django.core.files.images import ImageFile
from io import BytesIO
import uuid
from django.utils import timezone
from PIL import Image
from django.core.files.base import ContentFile
# Create your models here.

class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    studentid = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    virtual_wallet_balance = models.DecimalField(max_digits=8, decimal_places=2,default=00.00)
    department_name = models.CharField(max_length=50)
    semester = models.IntegerField(default=0)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='O')
    dob = models.DateField(default='2000-01-01')
    address = models.CharField(max_length=200,default='None')
    mobileno = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    
class StudentImage(models.Model):
    faceid = models.AutoField(primary_key=True)
    studentid = models.ForeignKey(Student, on_delete=models.CASCADE)
    image = models.BinaryField()

    def save(self, *args, **kwargs):
        if not self.faceid:
            # Auto-increment faceid
            last_record = StudentImage.objects.last()
            if last_record:
                self.faceid = last_record.faceid + 1
            else:
                self.faceid = 1
        super(StudentImage, self).save(*args, **kwargs)

class MenuItem(models.Model):
    menuid = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    images = models.ImageField(upload_to='images',  default='') 

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('credit', 'Credit'),
        ('debit', 'Debit')
    )

    transaction_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    transaction_time = models.DateTimeField(default=timezone.now)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if not self.transaction_id:
            self.transaction_id = self.generate_transaction_id()
        super().save(*args, **kwargs)

    def generate_transaction_id(self):
        transaction_id = str(uuid.uuid4().hex[:6]).upper()
        while Transaction.objects.filter(transaction_id=transaction_id).exists():
            transaction_id = str(uuid.uuid4().hex[:6]).upper()
        return transaction_id

class Cart(models.Model):
    cartid = models.AutoField(primary_key=True)
    studentid = models.ForeignKey(Student, on_delete=models.CASCADE)
    item1 = models.ForeignKey(MenuItem, related_name='item1', on_delete=models.CASCADE, null=True, blank=True)
    item2 = models.ForeignKey(MenuItem, related_name='item2', on_delete=models.CASCADE, null=True, blank=True)
    item3 = models.ForeignKey(MenuItem, related_name='item3', on_delete=models.CASCADE, null=True, blank=True)
    item4 = models.ForeignKey(MenuItem, related_name='item4', on_delete=models.CASCADE, null=True, blank=True)
    item5 = models.ForeignKey(MenuItem, related_name='item5', on_delete=models.CASCADE, null=True, blank=True)


class Order(models.Model):
    orderid = models.AutoField(primary_key=True)
    studentid = models.ForeignKey(Student, on_delete=models.CASCADE)
    order_time = models.DateTimeField()
    ORDER_MODE_CHOICES = [('online', 'Online'), ('offline', 'Offline')]
    order_mode = models.CharField(max_length=7, choices=ORDER_MODE_CHOICES)
    item1 = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='orders_item1', null=True, blank=True)
    item2 = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='orders_item2', null=True, blank=True)
    item3 = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='orders_item3', null=True, blank=True)
    item4 = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='orders_item4', null=True, blank=True)
    item5 = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='orders_item5', null=True, blank=True)
    total_amount = models.DecimalField(max_digits=6, decimal_places=2)

    def save(self, *args, **kwargs):
        if not self.orderid:
            latest_order = Order.objects.order_by('-orderid').first()
            self.orderid = (latest_order.orderid + 1) if latest_order else 10000
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.orderid:05d}"
    

class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    studentid = models.ForeignKey(Student, on_delete=models.CASCADE)
    itemid = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    rating = models.IntegerField()
    submission_time = models.DateTimeField()