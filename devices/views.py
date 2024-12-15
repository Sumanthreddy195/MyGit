from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from base64 import b64decode
from .models import Device, Payload, RxInfo, TxInfo
from .serializers import PayloadSerializer

class PayloadAPIView(APIView):
    def post(self, request, *args, **kwargs):
        devEUI = request.data.get('devEUI')
        fCnt = request.data.get('fCnt')
        data_encoded = request.data.get('data')
        rx_info_data = request.data.get('rxInfo', [])
        tx_info_data = request.data.get('txInfo', {})

        device, created = Device.objects.get_or_create(devEUI=devEUI)

        if Payload.objects.filter(device=device, fCnt=fCnt).exists():
            return Response({"error": "Duplicate payload detected."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            data_hex = b64decode(data_encoded).hex()
        except Exception:
            return Response({"error": "Invalid Base64 data."}, status=status.HTTP_400_BAD_REQUEST)

        status_value = 'passing' if data_hex == '01' else 'failing'

        payload = Payload.objects.create(
            device=device,
            fCnt=fCnt,
            data_hex=data_hex,
            status=status_value
        )

        for rx_info in rx_info_data:
            RxInfo.objects.create(
                payload=payload,
                gatewayID=rx_info['gatewayID'],
                name=rx_info['name'],
                time=rx_info['time'],
                rssi=rx_info['rssi'],
                loRaSNR=rx_info['loRaSNR']
            )

        TxInfo.objects.create(
            payload=payload,
            frequency=tx_info_data['frequency'],
            dr=tx_info_data['dr']
        )

        device.latest_status = status_value
        device.save()

        serializer = PayloadSerializer(payload)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
