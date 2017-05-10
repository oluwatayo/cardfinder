from django.db import models
from django.core.urlresolvers import reverse

class Card(models.Model):
     CardType=models.CharField(max_length=250)
     value = models.CharField(max_length=2)
     card_img = models.FileField()

     def get_absolute_url(self):
          return reverse('lostcard:details', kwargs={'pk': self.pk})

     def __str__(self):
          return self.CardType

class Specs(models.Model):
     Org_Name = models.CharField(max_length=200)
     holder_name=models.CharField(max_length=250)
     id_card = models.CharField(max_length=100)
     email_add = models.EmailField(max_length=80)
     phone_no = models.CharField(max_length=20)
     card=models.ForeignKey(Card, on_delete=models.CASCADE)
     def __str__(self):
          return self.holder_name + "'s Card"


class CardFound(models.Model):
     CardType=models.CharField(max_length=250)
     value = models.CharField(max_length=2)
     card_img = models.FileField()
     def get_absolute_url(self):
          return reverse('lostcard:details', kwargs={'pk': self.pk})

     def __str__(self):
          return self.CardType

class SpecsFound(models.Model):
     Org_Name = models.CharField(max_length=200)
     holder_name=models.CharField(max_length=250)
     id_card = models.CharField(max_length=100)
     email_add_founder = models.EmailField(max_length=80)
     phone_no = models.CharField(max_length=20)
     card2=models.ForeignKey(CardFound, on_delete=models.CASCADE)
     def __str__(self):
          return self.holder_name + "'s Card"