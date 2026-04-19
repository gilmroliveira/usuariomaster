from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

dados_mercado = {"wdo": "0.00", "win": "0.00", "btc": "0.00"}

@csrf_exempt
def update_dados(request):
    if request.method == 'POST':
        global dados_mercado
        dados_mercado = json.loads(request.body)
        return JsonResponse({"status": "sucesso"})
    return JsonResponse(dados_mercado)

