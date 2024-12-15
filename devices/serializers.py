from rest_framework import serializers
from .models import Payload, RxInfo, TxInfo

class RxInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RxInfo
        fields = ['gatewayID', 'name', 'time', 'rssi', 'loRaSNR']

class TxInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TxInfo
        fields = ['frequency', 'dr']

class PayloadSerializer(serializers.ModelSerializer):
    devEUI = serializers.CharField(source='device.devEUI', read_only=True)  # Include devEUI from related Device

    class Meta:
        model = Payload
        fields = ['fCnt', 'data_hex', 'status', 'devEUI']
