from django.db import models

# Create your models here.

class OurTeam(models.Model):
    name = models.CharField(max_length=30)
    specialization = models.CharField(max_length=15)
    image = models.ImageField(null=False, upload_to="team/")
    facebook_profile_link = models.URLField()
    twitter_profile_link = models.URLField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        managed = True
        verbose_name = 'Our Team'
        verbose_name_plural = 'Our Team'
        ordering = ('-date_added',)
        

class Testimony(models.Model):
    name = models.CharField(max_length=30, default="Anonymous")
    title = models.CharField(max_length=50, help_text="e.g Deliverance from depression. Short and precise.")
    testimony = models.TextField()
    location = models.CharField(max_length=10, help_text="State, Country - e.g Lagos, Nigeria")
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default="logo.png", upload_to="testimonials/")
    
    def __str__(self) -> str:
        return f"{self.name}'s Testimony"
    
    class Meta:
        verbose_name = "Testimony"
        verbose_name_plural = "Testimonies"
        ordering = ("-date_created",)

class Mail(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.name} left a message for you"
    
    class Meta:
        managed = True
        verbose_name = 'Mail'
        verbose_name_plural = 'Mails'
        ordering = ("-date_sent",)
    

        