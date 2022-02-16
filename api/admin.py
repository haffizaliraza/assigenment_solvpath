from django.contrib import admin
from .models import User, Product,Price,ProductReview,LocalSellerDetail,LocalSellerUploadedData


# Register your models here.

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Price)
admin.site.register(ProductReview)
admin.site.register(LocalSellerDetail)
admin.site.register(LocalSellerUploadedData)


