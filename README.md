# technical_test_automation

Activar entorno virtual: source environment/bin/activate
Run Ejecutar por feature: behave ./src/Feature/buy_saucedemo.feature 
Run por Tags = behave --tags=@Buy_Saucedemo ./src/Feature/buy_saucedemo.feature

//--- Ejecutar con Allure para generar reporte ---//

1.- Allure Tags run = behave -f allure_behave.formatter:AllureFormatter -o src/allure-results src/Feature/script_one.feature --tags=@ScriptOne

2.- allure generate src/allure-results —output -o src/allure-reports —clean && allure open —port 5000

3.- allure serve src/allure-results