from django.contrib import admin
from .models import Resume

# Register your models here.
@admin.register(Resume)
class ResumeModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','dob','gender','city','pin','state','job_city','profile_img']


    