Feature: Buy Saucedemo

   @ScriptTwo
   Scenario: Buy
     Given Open the application
     When Load the data json
     Then Clinc Informacion de viaje
     Then Clik Estado Vuelo
     Then Click Numero de vuelo
     Then Numero de vuelo vacio
     Then Click en buscar vuelos
     Then Validar resultados de vuelo vacio