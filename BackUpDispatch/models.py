from django.db import models

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


class CFSTable(models.Model):
    is_active       = models.BooleanField(default=True)
    type            = models.CharField(max_length=20)
    description     = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'type'

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
    dispatched_time = models.DateTimeField()

    location        = models.CharField(max_length=30)
    beat            = models.CharField(max_length=3, choices=BEAT_CHOICES)
    CFSType         = models.ForeignKey(CFSTable, on_delete=models.CASCADE)
    firstname       = models.CharField(max_length=30)
    lastname        = models.CharField(max_length=30)
    phone_number    = models.CharField(max_length=30)
    caller_location = models.CharField(max_length=30)
    plate           = models.CharField(max_length=10)


class NarrativeTable(models.Model):
    cfs_id          = models.ForeignKey(CFS, on_delete=models.CASCADE)
    narrative       = models.TextField

    class Meta:
        verbose_name = 'type'

    def __str__(self):
        return self.narrative

