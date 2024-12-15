from django.db import models

class Device(models.Model):
    devEUI = models.CharField(max_length=16, unique=True)
    latest_status = models.CharField(max_length=10, choices=[('passing', 'Passing'), ('failing', 'Failing')], null=True, blank=True)

    def __str__(self):
        return self.devEUI

class RxInfo(models.Model):
    payload = models.ForeignKey('Payload', on_delete=models.CASCADE, related_name='rx_info')
    gatewayID = models.CharField(max_length=16)
    name = models.CharField(max_length=50)
    time = models.DateTimeField()
    rssi = models.IntegerField()
    loRaSNR = models.FloatField()

    def __str__(self):
        return f"{self.gatewayID} - {self.time}"

class TxInfo(models.Model):
    payload = models.OneToOneField('Payload', on_delete=models.CASCADE, related_name='tx_info')
    frequency = models.BigIntegerField()
    dr = models.IntegerField()

    def __str__(self):
        return f"Frequency: {self.frequency}, DR: {self.dr}"

class Payload(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='payloads')
    fCnt = models.IntegerField()
    data_hex = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=[('passing', 'Passing'), ('failing', 'Failing')])
    received_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('device', 'fCnt')

    def __str__(self):
        return f"{self.device.devEUI} - fCnt: {self.fCnt}"
