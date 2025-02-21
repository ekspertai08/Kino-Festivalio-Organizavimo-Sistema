Kino Festivalių Organizavimo Sistema
Projekto Aprašymas
Sukurkite komandine eilute (CLI/Terminal) valdomą kino festivalių organizavimo programą, kuri padėtų organizatoriams efektyviai valdyti filmų programą, tvarkyti seansus ir rezervacijas. Programa turėtų išsaugoti duomenis tarp paleidimų, kad užtikrintų informacijos vientisumą.

Pagrindinės Funkcijos
1. Filmų registracija (Organizatorius)
Reikalavimai:
•	Galimybė pridėti naują filmą į festivalio programą.
•	Kiekvienas filmas turi turėti šiuos atributus (gali turėti ir daugiau):
o	Pavadinimas
o	Trukmė (minutėmis)
o	Žanras (drama, komedija ir t.t.)
o	Režisierius
o	Išleidimo metai
o	Amžiaus reitingas (pvz., "N-13", "N-18")
Duomenų saugojimas:
•	Informacija turi išlikti tarp paleidimų.
•	Galimi formatai: JSON, Pickle, CSV ar TXT
2. Filmų Pašalinimas ir Atnaujinimas (Organizatorius)
Reikalavimai:
•	Filmus galima pašalinti pagal pavadinimą.
•	Filmų duomenis galima atnaujinti, pakeičiant bet kurį atributą.
•	Programa turi patikrinti, ar filmas egzistuoja, kad nepašalintų neegzistuojančio filmo.

3. Filmų Peržiūra ir Paieška (Žiūrovas & Organizatorius)
Reikalavimai:
•	Rodyti visų įvestų filmų sąrašą su aiškia informacija.
•	Galimybė ieškoti filmų pagal:
o	Pavadinimą
o	Režisierių vardą
•	Galimybė filtruoti filmus pagal tipą (AnimacinisFilmas, DokumentinisFilmas).

4. Seansų Planavimas (Organizatorius)
Reikalavimai:
•	Filmai gali būti priskirti konkrečioms datoms ir laikams.
•	Programa turi patikrinti, ar tuo pačiu metu nėra suplanuota kito filmo.
•	Seansų informacija turi išlikti tarp paleidimų.

5. Bilietų Rezervacija (Žiūrovas)
Reikalavimai:
•	Žiūrovai gali rezervuoti vietas į pasirinktus seansus.
•	Seansas turi ribotą vietų skaičių.
•	Programa turi neleisti rezervuoti daugiau vietų, nei yra likę.

6. Naudotojų Valdymas (Organizatorius & Žiūrovas)
Reikalavimai:
•	Organizatoriai gali valdyti filmų programą ir seansus.
•	Žiūrovai gali peržiūrėti filmus ir rezervuoti bilietus.
•	Prisijungimas atliekamas per unikalų naudotojo vardą (be slaptažodžio).

7. Filmų Reitingavimas (Žiūrovas)
Reikalavimai:
•	Žiūrovai gali įvertinti matytus filmus (balais nuo 1 iki 10).
•	Vidutinis filmo įvertinimas atnaujinamas ir rodomas filmų sąraše.
•	Programa turi neleisti tam pačiam vartotojui vertinti to paties filmo daugiau nei vieną kartą.







Techniniai Reikalavimai
Pradinė Pavyzdinė Programos Struktūra
/kino_festivalis/
│── app.py  # Programos įėjimo taškas
│── config.py  # Konfigūracijos nustatymai
│── /models/  # Duomenų modeliai
│   │── film.py  # Filmų klasės
│   │── seansas.py  # Seanso modelis
│   │── vartotojas.py  # Vartotojo modelis
│── /services/  # Logikos sluoksnis
│   │── film_service.py  # Operacijos su filmais
│   │── seansas_service.py  # Operacijos su seansais
│   │── rezervacija_service.py  # Bilietų rezervacija
│   │── data_handler.py  # Duomenų įrašymas ir nuskaitymas
│── /data/  # Duomenų saugojimas
│   │── films.pickle
│   │── reservations.pickle
│── /views/  # CLI sąsaja
│   │── interface.py  # Vartotojo sąsaja
Stabilumas ir Klaidos
•	Programa neturėtų "nulūžti" dėl neteisingos vartotojo įvesties.
•	Naudoti try/except klaidų valdymą.
•	Aiškiai pateikti klaidų žinutes.
•	Programa turi veikti, kol naudotojas nuspręs ją išjungti.
Duomenų Išsaugojimas
•	Visi duomenys turi išlikti tarp programos paleidimų.
•	Rekomenduojama naudoti PICKLE formatą.

Papildomi (Bonus) Funkcionalumai
1.	Spalvotas terminalo išdėstymas naudojant colorama.
2.	Išplėstį filtravimo sistema filmų paieškai pagal kelis kriterijus vienu metu.
3.	Statistikos modulis, skaičiuojantis populiariausius filmus pagal rezervacijas.
4.	Finansų valdymas, skaičiuojantis pajamas pagal parduotus bilietus.
5.	Automatinė rezervacijų atšaukimo sistema, jei vartotojas nepatvirtina rezervacijos laiku.
6.	Filmo vertinimo sistema (1-10 įvertinimai ir atsiliepimai). Prie egzistuojančio funkcionalumo pridėti ir atsiliepimus.
7.	Dvi visiškai atskiros rolės, su skirtingais prisijungimais, žiūrovams išlieka unikalus id, organizatoriams reikia slaptažodžio ir vardo.
Projekto Diegimas ir Versijų Kontrolė
GitHub naudojimas:
•	Bent 3 šakos (feature-films, feature-seats, feature-booking).
•	Bent 5 commit'ai su aiškiais pranešimais.
Programa kaip .exe
•	Jei įmanoma, sukurti .exe failą naudojant pyinstaller (neprivaloma Mac naudotojams).
Sėkmės kuriant projektą!

Projekto kūrimo etapai

Programos struktūros planavimas
Apibrėžti, kokius duomenis programa naudos.
Nuspręsti, kaip organizuoti programos modulius.
Sudaryti pradinę funkcijų ir klasių schemą.
Objektinių klasių kūrimas ir paveldimumas
Sukurti Filmas klasę su bendrais atributais ir metodais.
Sukurti AnimacinisFilmas ir DokumentinisFilmas klases, paveldinčias iš Filmas.
Perašyti metodus, jei reikia, kad būtų aiškiai matoma skirtis tarp filmų tipų.
Duomenų saugojimo mechanizmo įgyvendinimas
Sukurti funkcijas filmų ir seansų įrašymui bei nuskaitymui iš failo.
Užtikrinti, kad duomenys išlieka tarp programos paleidimų.
Vartotojo sąsajos kūrimas
Realizuoti paprastą interaktyvią komandų eilutės sąsają (CLI).
Sukurti meniu su aiškiomis parinktimis vartotojui.
Testavimas ir klaidų valdymas
Įdiegti klaidų valdymą naudojant try/except.
Išbandyti programą su įvairiais įvesties scenarijais.
GitHub workflow įgyvendinimas
Sukurti pagrindinę programos versiją.
Versijų valdymui naudoti šakas (feature-films, feature-seats, bugfix-errors).
Kiekvienas pakeitimas turi būti logiškai pateiktas commit žinutėse.
Programos pakavimas į .exe formatą
Naudoti pyinstaller su atitinkamais nustatymais.