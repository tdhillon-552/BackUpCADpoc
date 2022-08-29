from django.db import models
from django.urls import reverse

BEAT_CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('OOJ', 'OOJ')
]


class CallsignTable(models.Model):
    is_active       = models.BooleanField(default=True)
    callsign        = models.CharField(max_length=5)

    class Meta:
        verbose_name = 'callsign'

    def __str__(self):
        return self.callsign


class DispoTable(models.Model):
    is_active       = models.BooleanField(default=True)
    disposition     = models.CharField(max_length=5)

    class Meta:
        verbose_name = 'disposition'

    def __str__(self):
        return self.disposition


class CFSTable(models.Model):
    is_active       = models.BooleanField(default=True)
    type            = models.CharField(max_length=20)
    description     = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'CFStable'

    def __str__(self):
        return self.type


class PriorityTable(models.Model):
    priority            = models.CharField(max_length=2)

    class Meta:
        verbose_name = 'priority'

    def __str__(self):
        return self.priority


class CFS(models.Model):
    is_active       = models.BooleanField(default=True)
    created_time    = models.DateTimeField(auto_now=True)
    dispatched_time = models.DateTimeField(blank=True, null=True)
    closed_time     = models.DateTimeField(blank=True,  null=True)
    disposition     = models.ForeignKey(DispoTable, on_delete=models.CASCADE, blank=True, null=True)
    location        = models.CharField(max_length=30)
    beat            = models.CharField(max_length=3, choices=BEAT_CHOICES)
    CFSType         = models.ForeignKey(CFSTable, on_delete=models.CASCADE)
    firstname       = models.CharField(max_length=30, blank=True, null=True)
    lastname        = models.CharField(max_length=30, blank=True, null=True)
    phone_number    = models.CharField(max_length=30, blank=True, null=True)
    caller_location = models.CharField(max_length=30, blank=True, null=True)
    plate           = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        verbose_name = 'CFS'

    def get_absolute_url(self):
        return reverse('BackUpDispatch_home')


class NarrativeTable(models.Model):
    cfs_id          = models.ForeignKey(CFS, on_delete=models.CASCADE)
    narrative       = models.TextField(max_length=500, blank=True)

    class Meta:
        verbose_name = 'type'

    def __str__(self):
        return self.narrative

