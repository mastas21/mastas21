
from urllib import request, response
import requests
import constants


def fct(liste):
    
    response = requests.get(constants.BASE)
    dict=response.json()
    for nis in range(len(dict['features'])):
        for key in  dict['features'][nis]['geometry']['coordinates']:
            for i in key:
                if i == liste:
                    print('trouveeee')
                    print(dict['features'][nis]['properties']['MESSAGE_FR'])
                    break
        break
                
    
    return dict


fct([ -73.567031982444405, 45.490135392137702 ])