from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class AboutChurch(models.Model):
    """A brief description about the church"""
    name = models.CharField(max_length=225, null=True, blank=True)
    about_church = models.TextField(max_length=500, null=True, blank=True)
    email_account = models.CharField(max_length=225, null=True, blank=True)
    facebook_link = models.CharField(max_length=225, null=True, blank=True)
    website_link = models.CharField(max_length=225, null=True, blank=True)
    location = models.CharField(max_length=225, null=True, blank=True)
    twitter_link = models.CharField(max_length=225, null=True, blank=True)
    instagram_link = models.CharField(max_length=225, null=True, blank=True)
    image = models.ImageField(default='', blank=True, upload_to='images')
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(350, 200)], format='JPEG',
                                     options={'quality': 60})

    def __str__(self):
        """Return a string representation of the model"""
        return self.name

    class Meta:
        verbose_name_plural = 'AboutChurch'

    def save_details(self):
        self.save()

    def delete_details(self):
        self.delete()


class PastorsProfile(models.Model):
    """A description about the church Bishop """
    name = models.CharField(max_length=225, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    image = models.ImageField(default='', blank=True, upload_to='images')
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(350, 200)],
                                     format='JPEG',
                                     options={'quality': 60})

    def __str__(self):
        """Return a string representation of the model"""
        return self.name

    class Meta:
        verbose_name_plural = 'PastorsProfile'

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


class ChurchServices(models.Model):
    """A description of the available services"""
    service_name = models.CharField(max_length=225, null=True, blank=True)
    service_details = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        """Return a string representation of the model"""
        return self.service_name

    class Meta:
        verbose_name_plural = 'ChurchServices'

    def save_programs(self):
        self.save()

    def delete_programs(self):
        self.delete()


class Project(models.Model):
    """A description about my previous projects"""
    project_title = models.CharField(max_length=225, null=True, blank=True)
    project_link = models.CharField(max_length=225, null=True, blank=True)
    project_description = models.CharField(max_length=225, null=True, blank=True)
    project_image = models.ImageField(default='', blank=True, upload_to='images')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model"""
        return self.project_title

    class Meta:
        verbose_name_plural = 'projects'

class Event(models.Model):
    """Something about upcoming events"""
    event_name = models.CharField(max_length=225, null=True, blank=True)
    event_description = models.TextField(max_length=500, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model"""
        return self.event_name

    class Meta:
        verbose_name_plural = 'events'

class Giving(models.Model):
    """A description of giving methods"""
    name = models.CharField(max_length=255, null=True, blank=True)
    payment_images = models.ImageField(default='', upload_to='images')

    def __str__(self):
        """Return a string representation of the model"""
        return self.event_name

    class Meta:
        verbose_name_plural = 'givings'

class Contact(models.Model):
    """Contact information"""
    email = models.CharField(max_length=255, null=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(null=True)

    def __str__(self):
        return str(self.email)

    class Meta:
        verbose_name_plural = 'contacts'
