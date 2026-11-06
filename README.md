# Encryptie
Security &amp; Cyberwarfare - Week 5 - Encryptie

## Onderzoek

### Symmetrische encryptie
Voor een symmetrische encryptie gebruikt je dezelfde key voor het versleutelen en ontsleutelen. De voordeel is dat het snel en efficiënt is voor grote aantal data, maar moeten de gebruikers vooraf veilig de sleutels delen met elkaar.
### Asymmetrische encryptie
Voor asymmetrische encryptie gebruikt je een key pair: een public key om te versleutelen en een private key om ye ontsleutelen. Deze manier van encryptie lost het sleuteluitwisselingsprobleem op, maar is veel trager dan symmertrische encryptie en werkt liever met kleinere bestanden.

Hierbij nog een tabel voor de vergelijkingen:

|  | Symmetrisch | Asymmetrisch |
| --- | --- | --- |
| Sleutels | 1 gedeelde geheime sleutel | publiek/privaat paar |
| Snelheid | zeer snel | traag |
| Sleuteluitwisseling | lastig (vooraf veilig delen) | eenvoudig (publieke sleutel mag openbaar) |
| Typisch gebruik | bulkdata, opslag | sleuteluitwisseling, handtekeningen |

### Kerckhoff's Principe
Volgens Kercckhoff's Principe moet een systeem veilig zijn, ook zou alles behalve de sleutel publiek bekend zijn. De veilig licht dus bij de sleutel en niet in de geheimhouding van de algoritme. Dit is ook waarom we openbare, uitvoerig geanalyseerde standaarden gebruiken.
