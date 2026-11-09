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

## 2. Hoe de applicatie werkt
**Versleutelen**
1. De applicatie genereet automatisch een random 256-bit sleutel en laat deze op het terminal zien. (Base64)
2. De gebruiker voert daarna de tekst in die versleuteld gaat worden.
3. De applicatie genereert daarna een random nonce van 12 bytes.
4. De tekst wordt daarna versleuteld met de AES-256-GCM.
5. De applicatie laat de cipher en de nonce daarna zien. (Base64)

**Ontsleutelen**
1. De gebruiker voert de gegenereerde sleutel van hiervoor in.
2. De gebruiker voert de cipher en de nonce van hiervoor ook in.
3. De applicatie ontsleutelt de tekst en laat de originele tekst zien.
4. Als de sleutel, nonce of ciphertext nie klopt geeft de applicatie een foutmelding in plaats van onjuiste data.

Er wordt gebruikt gemaakt van `AESGCM` voor de library `cryptograpy` voor deze applicatie.
Base64 wordt hier gebruikt om de data leesbaar te maken als tekst en biedt zelf geen beveiliging.

## 3. Gekozen encryptiemethode, algroritme en rechtvaardiging
Ik heb gekozen voor AES-256 in GCM-modus. 
AES is de wereldwijde standaard en is jarenlang door experts geanalyseerd, en een 256-bit sleutel geeft de grootste beveiligingsmarge. 
GCM is gekozen omdat het naast geheimhouding ook integriteit controleert: wordt de ciphertext aangepast, dan mislukt het ontsleutelen. 
Oudere modi zoals ECB bieden dit niet. 
GCM vereist wel een unieke nonce per versleuteling met dezelfde sleutel. 
De applicatie genereert daarvoor een random 96-bit nonce met `os.urandom`.

## 4. Sleutelbeheer
**Generatie:**
De sleutel wordt gegeneerd met `AESGCM.generate_key(bit_length=256)`, die gebruikt maakt van een cryptografisch veilige random generator van het besturingssyteem.

**Opslag:**
De applicatie slaat de sleutel niet zelf op. De sleutel wordt 1 keer gegeven aan de gebruiker en moet deze sleutel zelf bewaren. Na het aflsuiten van de applicatie bestaat de sleutel niet meer in het geheugen.

**Uitwisseling:**
De gebruiker moet zelf de sleutel kopieëren en geeft deze aan een ander. De applicaite behandeld de uitwisseling zelf niet.

**Beveiligingsimplicaties en beperkingen:**
- De sleutel wordt als tekst op het scherm gegeven. Als er iemand is meekijkt, of de terminalgeschiedenis/screenshots heeft, kan de sleutel in de verkeerde handen komen.
- De sleutel wordt niet beschermd opgeslagen. Als de gebruiker de sleutel kwijt raakt, is de data verloren.
- Als de sleutel via een onveilige kanaal (bijvoorbeeld: e-mail of chat) wordt gedeeld, is de sterke encryptie waardeloos. Zelf de beste beveiliging faalt als de transfer van de sleutel onveilig is.
- Per versleuteling wordt een nieuwe sleutel gegenereerd. Dat is veilig (en voorkomt nonce-hergebruik met dezelfde sleutel), maar is heel onhandig om te gebruiken.
- **Schaalbaarheid:** bij symmetrische encryptie heeft elk paar gebruikers een eigen gedeelde sleutel nodig. 
  Het aantal benodigde sleutels groeit kwadratisch met het aantal gebruikers: elke nieuwe gebruiker heeft een aparte sleutel nodig met elke bestaande gebruiker. 
  Bij 1000 gebruikers zijn dat bijna 500.000 sleutels. 
  Het veilig genereren, distribueren, roteren en intrekken hiervan is in de praktijk nagenoeg onmogelijk te beheren.
  Daarom gebruikt men in de praktijk hybride systemen met asymmetrische sleuteluitwisseling (bijv. Diffie-Hellman/RSA) of een key management system (KMS).
## 5. Reflectie op Kerckhoff's Principe
Kerckhoff's Principe zegt dat een versleutelingssysteem veilig moet zijn, zelfs als alles over het systeem publiek bekend is, behalve de sleutel.

**Hoe de applicatie hieraan voldoet**
- AES-GCM is volledig openbaar gedocumenteerd en wordt wereldwijd gebruikt. Cryptografen hebben het algoritme jarenlang onderzocht, en de veiligheid ervan is niet afhankelijk van geheimhouding.
- De broncode staat openbaar op GitHub en de applicatie gebruikt de open-source library `cryptography`. De veiligheid rust dus op openbaar gecontroleerde code en niet op een geheim zelfbedacht ontwerp, wat precies de gedachte achter Kerckhoffs's Principe is.
- Het enige geheim is de 256-bit sleutel. De nonce en ciphertext zijn niet geheim en mogen publiek bekend zijn zonder dat de veiligheid in gevaar komt.

Tegelijk betekent dit dat, omdat alleen de sleutel geheim is, de veiligheid volledig afhangt van het sleutelbeheer. Dat is juist het zwakke punt van deze applicatie (zie hoofdstuk 4).
