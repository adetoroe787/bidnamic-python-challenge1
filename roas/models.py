
from django.db import models

class campaign(models.Model):
    campaign_id = models.CharField(max_length=255)
    structure_value = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.structure_value

class ad_group(models.Model):
    ad_group_id = models.CharField(max_length=255)
    campaign = models.ForeignKey(campaign, on_delete=models.CASCADE)
    alias = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.ad_group_id


class search_terms(models.Model):
    date = models.DateField()
    ad_group = models.ForeignKey(ad_group, on_delete=models.CASCADE)
    campaign = models.ForeignKey(campaign, on_delete=models.CASCADE)
    clicks = models.CharField(max_length=255)
    cost = models.FloatField()
    conversion_value = models.FloatField(max_length=255)
    conversions = models.CharField(max_length=255)
    search_term = models.CharField(max_length=500)
    roas = models.FloatField(default=0.04)

    def save(self, *args, **kwargs):
        self.roas = self.conversion_value / self.cost

        super(search_terms, self).save(*args, **kwargs)

    def __str__(self):
        return self.search_term
        

