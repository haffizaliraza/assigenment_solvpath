from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from .constants import USER_STATE_CHOICES, FILE_STATE_CHOICES


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, dob, email, contact_no, state,
                    password=None):
        if not username:
            raise ValueError('User must have an username')
        if not first_name:
            raise ValueError('User must have an First Name')
        if not last_name:
            raise ValueError('User must have an Last Name')
        if not dob:
            raise ValueError('User must have an Date Of Birth')
        if not email:
            raise ValueError('User must have an Email')
        if not contact_no:
            raise ValueError('User must have an Contact No')
        if not state:
            raise ValueError('User must have an state')

        user = self.model(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            dob=dob,
            email=self.normalize_email(email),
            contact_no=contact_no,
            state=state
        )

        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, dob, email, contact_no, password=None):
        user = self.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            dob=dob,
            email=self.normalize_email(email),
            contact_no=contact_no,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(verbose_name="First Name", max_length=50)
    last_name = models.CharField(verbose_name="Last Name", max_length=50)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    dob = models.DateField(verbose_name="Date Of Birth")
    email = models.CharField(max_length=50)
    contact_no = models.IntegerField(verbose_name="Contact No")
    state = models.SmallIntegerField(verbose_name='User State', choices=USER_STATE_CHOICES, default=1)
    date_joined = models.DateTimeField(verbose_name="Date Registered", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="Last Login", auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', 'first_name', 'last_name', 'dob', 'email', 'contact_no', 'state']

    objects = UserManager()

    def __str__(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    @property
    def token(self):
        return ''


class Product(models.Model):
    product_name = models.CharField(verbose_name="Product Name", max_length=100)
    product_description = models.CharField(verbose_name="Product Description", max_length=1000)
    product_image = models.CharField(verbose_name="Product Image", max_length=1500)
    min_price = models.IntegerField(verbose_name="Minimum Price")
    max_price = models.IntegerField(verbose_name="Maximum Price")
    offered_by = models.IntegerField(verbose_name="Offered By", default=False)

    def __str__(self):
        return self.product_name


class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    reference_site = models.CharField(verbose_name="Reference Site", max_length=1000)
    product_price = models.IntegerField(verbose_name="Product Price")


    def __str__(self):
        return str(self.product)


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_reviews = models.CharField(verbose_name="Product Reviews", max_length=1000)


    def __str__(self):
        return self.product_reviews


class LocalSellerDetail(models.Model):
    id = models.AutoField(primary_key=True)
    local_seller = models.ForeignKey(User, on_delete=models.CASCADE)
    shop_name = models.CharField(verbose_name="Shop Name", max_length=100)
    shop_address = models.CharField(verbose_name="Shop Address", max_length=1000)

    def __str__(self):
        return self.shop_name


class LocalSellerUploadedData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    file_state = models.SmallIntegerField(verbose_name='File State', choices=FILE_STATE_CHOICES, default=1)
    ls_product_file = models.FileField(verbose_name="Upload CSV File", default=False, upload_to='media/LocalSellerData/')
    created = models.DateTimeField(verbose_name='Creation date',auto_now_add=True,editable=False)

    def __str__(self):
        template = '{0.user} {0.file_state}'
        return template.format(self)

