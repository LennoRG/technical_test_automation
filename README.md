# technical_test_automation

Instalar: pip install -r requirements.txt

////
Activar entorno virtual: source environment/bin/activate
Run Ejecutar por feature: behave ./src/Feature/script_one.feature 
Run por Tags = behave --tags=@Buy_Saucedemo ./src/Feature/buy_saucedemo.feature

//--- Ejecutar con Allure para generar reporte ---//

1.- Allure Tags run = behave -f allure_behave.formatter:AllureFormatter -o src/allure-results src/Feature/script_one.feature --tags=@ScriptOne

2.- allure generate src/allure-results —output -o src/allure-reports —clean && allure open —port 5000

3.- allure serve src/allure-results



// -------- Build Steps Jenkins-------- //
1.- pip3 --version
2.- python3 -m venv environment
3.- source environment/bin/activate
4.- pip3 install -r requirements.txt
5.- behave --version    
6.- behave -f allure_behave.formatter:AllureFormatter -o allure-results src/Feature/script_one.feature --tags=@ScriptOne