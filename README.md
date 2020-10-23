# Pizza Website

Backlogg: https://docs.google.com/spreadsheets/d/131Dxy4QplduNJaxo41rS0nOelqbk0bQTxoG1y0TOsho/edit#gid=0

Hemsida: https://fantastic4group.gitlab.io/pizza-website
**(För att hosta HTML sida används GitLab Pages, därför behövs .gitlab-ci.yml filen.)**

**Viktigt! Installera Node.js från https://nodejs.org/en/ . Sedan navigera till pizza-website foldern i valfri kommandoprompt och skriv in "npm install" . Detta krävs för att allt ska funka som det ska.**

# Kodningsstandard
**Spaces:** 4
<br>
**Kommentarer:** Engelska över funktionen, mellanslag mellan "//" och meningen, stor bokstav
<br>
**Namngivning:** Engelska, Klasser med storbokstav (UpperCamelCase)
<br>
**Variabel:** let, stor bokstav som delar upp flera ord i en variabel som "pizzaFooter". Liten bokstav i början (lowerCamelCase)
<br>
**Funktioner:** non lambda functions
<br>
**HTML/CSS:** Bara CSS inline i HTML filen när det är någonting som ändras med JavaScript

# Programmeringsspråk
HTML 5
<br>
CSS 3
<br>
Javascript (ECMAScript 2018)
<br>
Python 3.8.2

# Utvecklingsmiljöstandard
**Editor** - Visual Studio Code 1.48.2
<br>
Plugins för VSCode: 
- Live Server
- Beautify
- Beautify css/sass/scss/less
- Live Share
- Code Spell Checker
- Swedish - Code Spell Checker
- Python

**Fildelning** - GitLab
<br>
**OS** - Windows 10 1909
<br>
**Browsers** - Edge 85 / Chrome 85
<br>
**Skärmupplösning** - 2560x1440, 1920x1080
<br>
**Tester** - Selenium for Python
<br>
**Validering** - HTML Validator, CSS Validator
<br>
**Dokumentation** - Svenska, kortfattat med bilder
<br>
**Git Branches** 
- Branch namnen ska följa (lowerCamelCase) standarden. 
- De används när vi skapar nya funktioner som då måste godkännas av resten av gruppen via merge request.

**Alla Git Kommandon** - https://about.gitlab.com/images/press/git-cheat-sheet.pdf

**Annat** - node.js v.14.9.0, npm v.6.14.8


# Definition of Done
Godkänd av gruppen, både design och utseende. Samt kodmässigt, om det följer kodningsstandarden och är förståelig.
<br>
Bearbetat feedback från gruppmedlemmar.
<br>
Ska klara av tester
<br>
Överens med gruppens kodningsstandard
<br>
Koden ska vara kommenterad och dokumenterad
<br>
Koden ska gå igenom valideringen


# Tester Dokumentation
**Hur man sätter upp Selenium for Python för tester**
1. Installera senaste python och tryck på **Add Python to path**
1. Starta om datorn
1. Klona/pulla filerna från GitLab repot Pizza Website
1. Öppna **Git Bash** och kör kommandot `cd tests && ./setup.sh`
1. Sedan kör kommandot **python ./run.py -s argument1 -p argument2 -f argument3**
1. Scriptet tar argument. Argument1 kan antingen vara "local" eller "web". Local betyder att testa localhosten och web betyder att testa live sidan på gitlab
1. Argument2 spelar igentligen roll om argument1 är "local" då du ska skriva in localhost porten. Standard porten är 5500. Om din localhost port är 5500 så behöver du inte använda detta argument
1. Argument3 är för att välja vilken html fil som ska testas. Ex är "index.html" eller "kontakt.html"
1. Om allting dyker upp utan errors så hittar testerna allting
 
**Hur man skapar ett test i Selenium for Python**
1. Se till att du har den senaste versionen av filerna genom att pulla dem från GitLab.
1. Öppna **tests** mappen i valfri editor som kan köra Python. 
1. Skapa en ny python fil i mappen **pythonTests** med namnet på testet
1. Importera sedan webdriver från selenium: `from selenium import webdriver`
1. Skapa sedan en klass med samma namn som filen fast med stor bokstav i början
1. Skapa en `__init__` funktion med variablerna **driver** och **baseDivPath**: `def __init__(self, driver: webdriver.Chrome):`
1. Navigera till run.py filen och importera testet du skapat genom att skriva: `from pythonTests.(namn på testfilen) import TestKlassen`
1. Navigera tillbaka till test filen
1. Om du t.ex vill hitta texten i en h1 tagg med ID:et “title” så skriver du: 
`variabel1 = driver.find_element_by_id("title").text`
1. Efter du hämtar någonting från hemsidan så måste du använda `assert` för att veta om det du har hämtat är korrekt
1. Ett exempel skulle vara om du ville kontrollera om **variabel1** inte är en tom string: `assert variabel1 != “”`

# Screenshots av webbsidan
**För att använda**
1.  Gå in i "shot.json" via VSCode.
1.  Under rubriken "urls" kan man skriva in det adress man vill.
1.  Under rubriken "sizes" kan man skriva in det upplösning man vill.
1.  Starta "takeScreenshot.sh"
1.  Sedan alla screenshots ska sparas i scripts/screenshots

# HTML och CSS Validering
Koden valideras automatiskt via CI när man har pushat den. Annars kan man validera den lokalt genom att:
1. Starta Git Bash i **/scripts/validators mappen**
1. Skriv in **./runValidators.sh** för att starta filen
1. Sedan resultat visas i fönstret av valideringen

# Innehåll från internet

- Typsnitt är licensierat under Open Font License(OFL) http://scripts.sil.org/OFL
- Bild under titeln är licensierat under Pixabay License, gratis för kommersiellt bruk https://pixabay.com/sv/photos/pizza-mat-italian-bakad-ost-3007395/
- Bild i footer är från våran Product Owner

# Problemlogg 

- Använder man **flex-direction: row** (default om man inte specifierar något annat om **display: flex**) kan det behövas att lägga till **align-items: flex-start** för att fixa att vissa objekt inte stretchar i Safari (ex. bilder).
