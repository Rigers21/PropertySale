from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Property(models.Model):
    class Currency(models.TextChoices):
        EUR = 'EUR', _('EUR')
        CHF = 'CHF', _('CHF')

    class Parking(models.TextChoices):
        Yes = 'Yes', _('Yes')
        No = 'No', _('No')

    title = models.CharField(_('title'), max_length=256, null=True)
    slug = models.SlugField(_('slug'), max_length=256, unique=True)
    location = models.CharField(_('location'), max_length=50, null=False)
    city = models.CharField(_('city'), max_length=128, null=False)
    type = models.CharField(_('type'), max_length=128, null=False)
    plot_surface = models.CharField(_('plot surface'), max_length=20, null=False, default=0)
    construction_surface = models.CharField(_('construction surface'), max_length=20, null=False, default=0)
    bedroom = models.DecimalField(_('bedroom'), max_digits=4, decimal_places=0, default=1)
    suite = models.DecimalField(_('suit'), max_digits=4, decimal_places=0, default=0)
    toilet = models.DecimalField(_('toilet'), max_digits=4, decimal_places=0, default=1)
    parking = models.CharField(_('parking'), max_length=3, choices=Parking.choices, default=Parking.No)
    price = models.DecimalField(_('price'), max_digits=15, decimal_places=2, null=False)
    description = models.TextField(_('description'))
    currency = models.CharField(_('currency'), max_length=3, choices=Currency.choices, default=Currency.EUR)
    image = models.ImageField(_('image'), upload_to='properties/images')

    class Meta:
        db_table = 'properties'
        verbose_name = 'property'
        verbose_name_plural = 'properties'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Picture(models.Model):
    property = models.ForeignKey(Property, verbose_name=_('property'), on_delete=models.CASCADE,
                                 related_name='pictures')
    image = models.ImageField(_('image'), null=False, blank=False, upload_to='properties/images')

    class Meta:
        db_table = 'pictures'
        verbose_name = _('picture')
        verbose_name_plural = _('pictures')


class Contact(models.Model):
    name = models.CharField(_('name'), max_length=128, null=False)
    email = models.EmailField(_('email'), max_length=128, null=False)
    message = models.CharField(_('message'), max_length=528, null=False)

    class Meta:
        db_table = 'Contacts'
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')
