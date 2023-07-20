Feature: Buy Saucedemo

   @ScriptOne
   Scenario: Informacion Vuelos
     Given Open the application
     When Load the data json
     Then Clinc Informacion de viaje
     Then Clik Estado Vuelo
     Then Click Numero de vuelo
     Then Ingresa nuemero de vuelo
     Then Click en buscar vuelos
     Then Validar resultados de vuelo
     