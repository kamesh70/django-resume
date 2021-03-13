from django.db import models

# Create your models here.
STATE_CHOICE = (
    ('Andhra_Pradesh','Andhra_Pradesh'),
('Arunachal_Pradesh','Arunachal_Pradesh'),
('Assam','Assam'),
('Bihar', 'Bihar'),
('Chhattisgarh','Chhattisgarh' ),
('Goa','Goa' ),
 ('Gujarat','Gujarat'),

('Haryana','Haryana'),
('Himachal_Pradesh', 'Himachal_Pradesh'),
 ('Jharkhand','Jharkhand' ),

('Karnataka','Karnataka'),
('Kerala','Kerala'),
('Madhya_Pradesh','Madhya_Pradesh'),
 ('Maharashtra','Maharashtra'),
('Manipur','Manipur'),
('Meghalaya','Meghalaya'),
('Mizoram','Mizoram'),
('Nagaland','Nagaland'),
('Odisha','Odisha'),
('Punjab','Punjab'),
('Rajasthan','Rajasthan'),
('Sikkim','Sikkim'),
('Tamil_Nadu','Tamil_Nadu'),
('Telangana','Telangana'), 
('Tripura','Tripura'),
('Uttarakhand','Uttarakhand' ),
('Uttar_Pradesh','Uttar_Pradesh'),
('West_Bengal','West_Bengal')
)

class Resume(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=10)
    locality = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    state = models.CharField(max_length=50,choices=STATE_CHOICE)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=100)
    profile_img = models.ImageField(upload_to='profileimg', blank=True)
    my_file=models.FileField(upload_to='doc',blank=True)