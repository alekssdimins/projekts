# projekts

cau

# izmantotās bibliotēkas

Šajā kodā tiek izmantotas divas galvenās bibliotēkas: `os` un `fitz` (no PyMuPDF bibliotēkas). Ļoti detalizēti paskaidrošu, kā šīs bibliotēkas tiek izmantotas un kā tās asociējas ar kodu:

1. **`os` bibliotēka:**
   - `import os`: Šī bibliotēka nodrošina operētājsistēmas (OS) funkcionalitāti, ļaujot manipulēt ar failiem, direktorijām un citiem sistēmas resursiem.
   - `os.listdir(directory)`: Izmanto, lai iegūtu visus failu nosaukumus norādītajā direktorijā (`directory`).

2. **`fitz` (PyMuPDF) bibliotēka:**
   - `import fitz`: PyMuPDF ir bibliotēka PDF failu apstrādei un manipulācijai.
   - `doc = fitz.open(pdf_path)`: Atver norādīto PDF failu (`pdf_path`) un saglabā saiti uz to mainīgajā `doc`.
   - `doc.page_count`: Atgriež kopējo lapu skaitu PDF failā.
   - `page = doc[page_num]`: Iegūst konkrēto lapu, izmantojot lapu numuru `page_num`.
   - `page.get_text()`: Atgriež tekstu no pašreizējās lapas.

#  koda nozīme

Šis kods veido programmu, kas atvieglo ikdienas uzdevumu apstrādāt saņemtos maksājumus no vairākām bankām. Tas ir īpaši noderīgs cilvēkam, kam pieder vairākas dzīvokļu ēkas, un kas saņem maksājumus kā PDF pielikumus. Lai gan kodā ir dažas funkcijas, kuru uzdevums ir apstrādāt tekstu un izgūt informāciju no PDF failiem, kopējā kodā ir iestrādāts šāds ikdienas uzdevums:

1. **Automatizēts PDF failu apstrāde:** Programmējot šo kodu, jūs nevarat tikai skatīties katru saņemto PDF failu manuāli, bet izmantojat Python, lai izveidotu automātisku sistēmu. Tas ietaupa laiku un samazina cilvēka iesaistīšanos procesā.
2. **Maksājumu informācijas analīze:** Programma ne tikai atver un lasa PDF failus, bet arī analizē to saturu, meklējot konkrētas frāzes un izgūstot svarīgu informāciju. Tas palīdz identificēt maksājuma veicēju, saņēmēju un summu, uzlabojot darba efektivitāti.
3. **Ērtības īpašniekam:** Šis projekts ir paredzēts kā instrumentu īpašniekam, kuram pieder vairākas īres īpašības. Programmējot šādu risinājumu, īpašniekam vairs nav jāpārbauda katru maksājumu manuāli, jo programma to dara automātiski, piedāvājot ātru un pārredzamu pārskatu par visiem saņemtajiem maksājumiem.
4. **Efektivitāte un precizitāte:** Programma darbojas vienmērīgi un precīzi, izvairoties no cilvēka kļūdām vai nepilnībām. Tā veic uzdevumu konsistenti un ātri, nodrošinot efektivitāti ikdienas darba apstrādē.

#  koda struktūras skaidrojums

extract_payment_info funkcija:
Šī funkcija atbild par informācijas ieguvi no teksta, kas tiek padots kā arguments.
Izmanto trīs meklēšanas paraugus (name_pattern, amount_pattern, un recipient_pattern), lai atrastu vārdu, maksājuma summu un saņēmēja informāciju.
Izmanto virknes funkciju find() un apstrādā atrastos indeksus, lai izgūtu konkrēto informāciju no teksta.
Ja informācija tiek atrasta, tā tiek izgūta un attīrīta no liekām atstarpēm (strip() funkcija), un rezultāts tiek atgriezts kā tuple ar trīs vērtībām: vārds, saņēmējs un summa.
process_payment_files funkcija:
Šī funkcija atbild par apstrādājamo PDF failu direktorijas norādīšanu un katram failam atbilstošu apstrādes darbību.
Iterē cauri visiem failiem direktorijā (os.listdir(directory)).
Ja faila paplašinājums ir '.pdf', tiek veikta apstrāde.
Atver katru PDF failu (fitz.open(pdf_path)) un iegūst tekstu no katras lapas (page.get_text()).
Izdrukā informāciju par attiecīgo PDF failu un izgūto tekstu.
Izmanto extract_payment_info funkciju, lai iegūtu vārdu, saņēmēju un summu no izgūtā teksta.
Izdrukā iegūto maksājuma informāciju.
main bloks:
Pēdējais bloks izsauc process_payment_files funkciju, norādot direktoriju, kur atrodas PDF faili ("/Users/alekssdimins/Desktop/projekts").
Tas tiek darīts, lai programmu palaistu un uzsāktu maksājumu informācijas apstrādi.
