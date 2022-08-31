from rest_framework import serializers


class DispoSerializer(serializers.Serializer):
    is_active       = serializers.BooleanField()
    disposition     = serializers.CharField(max_length=5)


class CFSTableSerializer(serializers.Serializer):
    is_active       = serializers.BooleanField()
    type            = serializers.CharField(max_length=20)
    description     = serializers.CharField(max_length=20)



class CallSerializer(serializers.Serializer):
    id              = serializers.IntegerField()
    is_active       = serializers.BooleanField()
    created_time    = serializers.DateTimeField()
    dispatched_time = serializers.DateTimeField()
    closed_time     = serializers.DateTimeField()
    disposition     = DispoSerializer()
    location        = serializers.CharField(max_length=30)
    beat            = serializers.CharField(max_length=3)
    CFSType         = CFSTableSerializer()
    firstname       = serializers.CharField(max_length=30)
    lastname        = serializers.CharField(max_length=30)
    phone_number    = serializers.CharField(max_length=30)
    caller_location = serializers.CharField(max_length=30)
    plate           = serializers.CharField(max_length=10)
