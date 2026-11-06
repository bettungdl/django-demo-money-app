import stripe
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from wallet.models import Wallet
from user.models import User
from history.models import History

stripe.api_key = 'sk_test_51Q3YBg09y9kf8XbPA8t0gXs6VxImX7AdIu6rVwtSUTHUyFXlCcpEtSYLJwmACahFz7cOj3SMorPQk2m9gKej4Reh00optEq1Cq'

class RechargeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        totalAmount = int(float(request.data['amount'])*100)
        
        stripe.Charge.create(
            source = request.data['token'],
            amount = totalAmount,
            currency = 'mxn',
        )

# este es si todo salio bien
        wallet = Wallet.objects.get(pk=request.user.wallet_id)
        wallet.balance = float(wallet.balance) + float(request.data['amount'])
        wallet.save()

        History.objects.create(
            type='recharge',
            origin_user=self.request.user,
            target_user=self.request.user,
            amount=request.data['amount'],
            message='Recarga de saldo'
        )

        return Response(' Recarga exitosa! El saldo actual es de: ' + str(wallet.balance) + ' MXN', status=status.HTTP_200_OK)

class SendMoneyView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        wallet = Wallet.objects.get(pk=request.user.wallet_id)
        wallet.balance = float(wallet.balance) - float(request.data['amount'])
        wallet.save()

        user_dest = User.objects.get(pk=request.data['userId'])
        wallet_dest = Wallet.objects.get(pk=user_dest.wallet_id)
        wallet_dest.balance = float(wallet_dest.balance) + float(request.data['amount'])
        wallet_dest.save()
        
        History.objects.create(
            type='send_money',
            origin_user=self.request.user,  
            target_user=user_dest,
            amount=request.data['amount'],
            message=request.data['message']
        )

        return Response(' Transferencia exitosa! ', status=status.HTTP_200_OK)
