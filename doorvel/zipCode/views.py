from django.http.response import JsonResponse
from django.views import View
from .models import Areas, ZipCode, Township

class ZipCodeView(View):

    def get(self, request, zip_code=None):
        if zip_code is not None:
            settlements = Areas.objects.select_related().filter(zip_code = zip_code)
            if len(settlements) > 0:
                city = ZipCode.objects.select_related().filter(zip_code = zip_code)
                state = Township.objects.select_related().filter(idtownship = city[0].idtownship.idtownship)
                dataResponse = {
                    'zip_code': zip_code,
                    'locality': city[0].idcity.name,
                    'federal_entity': {
                        'key': int(state[0].idstate.idstate),
                        'name': state[0].idstate.name,
                        'code': None
                    },
                    'settlements': [],
                    'municipality': {
                        'key': int(city[0].idtownship.idtownship),
                        'name': city[0].idtownship.name
                    }
                }
                for row in settlements:
                    objSettlement = {
                        'key' : int(row.id_area_cpcons),
                        'name' : row.name,
                        'zone_type' : row.idzonetype.name,
                        'settlement_type' : {
                            'name' : row.idareatype.name
                        }
                    }
                    dataResponse['settlements'].append(objSettlement)
                return JsonResponse(dataResponse)
            else:
                return JsonResponse({'message': 'Zip Code not found ...'})
