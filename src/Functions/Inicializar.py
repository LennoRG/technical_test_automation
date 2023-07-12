import os

class Inicializar():
    #DIRECTORIO BASE
    basedir = os.path.abspath(os.path.join(__file__, "../.."))
    DateFormat = '%d/%m/%Y'
    HourFormat = "%H%M%S"

    #JSON Data
    Json = basedir + u'/jsons'

    Environment = 'Test'

    #BROWSER DE PRUEBAS
    NAVEGADOR = u'Chrome'

    if Environment == 'Test':
        URL = 'https://www.aa.com/homePage.do?locale=es_MX'

    if Environment == 'PROD':
        URL = 'https://www.mercadolibre.com.mx/'

