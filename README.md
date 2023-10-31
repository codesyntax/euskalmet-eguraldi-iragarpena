# Euskalmeten eguraldi iragarpena

Python programa honek [Euskalmeten APIa](https://opendata.euskadi.eus/api-euskalmet/-/how-to-use-meteo-rest-services/) darabil herrietako iragarpena deskargatu eta JSON baten edonoren esku jartzeko.exit

Momentuz proba gisa Antzuola eta Eibarko iragarpenak ekartzen ditu, baina oso erraza da beste edozein herritakoa ere ekartzea.

## Nola erabili

Zure ordenagailuan erabili nahi baduzu zera egin:

1. Lortu API erabiltzeko gako bat [Euskalmeten webgunetik](https://opendata.euskadi.eus/api-euskalmet/-/api-de-euskalmet/)

2. Sortu ingurune aldagai hauek:

   - EUSKALMET_API_EMAIL: gakoa erregistratzeko erabili duzun eposta helbidea
   - EUSKALMET_API_PRIVATE_KEY: Euskalmetek emandako gako pribatua

3. Instalatu dependentziak (zure ingurunea ez kakazteko, instalazio eta exekuzioarako python ingurune birtual bat erabiltzea gomendatzen dut):

```
pip install -r requirements.txt
```

4. Exekutatu `main.py` fitxategia:

```bash
python main.py
```

5. Exekuzioak `forecasts` izeneko karpetan dagokion herriko iragarpena sortuko du JSON formatuan. Ondoren JSON hori nahi duzun moduan tratatu dezakezu. Exekuzioan jatorrizko JSONa pixka bat moldatzen dut: eguraldiaren sinboloak errazago kudeatzeko fitxategien izena zein den lortzen dut (aldatu nahi badituzu) eta URL osoa ere gordetzen dut (Euskalmet-en irudiak erabili nahi badituzu). Euskalmeten irudiak deskargatu nahi badituzu erabili `download_images.py` scripta eta `images` karpetara irudi guztiak deskargatuko dizkizu.

## Exekuzio automatikoa

GitHub Actions zerbitzuari esker script hau UTC orduko 6:00, 12:00, 16:00 eta 20:00tan exekutatzen da.
