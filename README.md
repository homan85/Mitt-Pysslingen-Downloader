# Mitt Pysslingen Downloader

Ett fristående och inofficiellt verktyg för nedladdning av media som laddats upp till Mitt Pysslingen.

## macOS

macOS kan visa en säkerhetsvarning första gången du kör Mitt Pysslingen Downloader.  
Detta beror på att applikationen inte är signerad med ett Apple Developer-konto.

### Om macOS säger att appen är “skadad”

Detta är ett säkerhetsskydd i macOS och betyder **inte** att applikationen faktiskt är skadad.

Om detta inträffar:

1. Öppna **Terminal**
2. Kör följande kommando (anpassa sökvägen om applikationen ligger på annan plats):

```bash
sudo xattr -rd com.apple.quarantine /Applications/Mitt\ Pysslingen\ Downloader.app

```

Starta appen igen

### Varför händer detta?

Apple kräver att appar som laddas ner från internet ska vara:
1. signerade med Apple Developer ID
2. notariserade av Apple

Då detta är ett hobbyprojekt som distribueras utan Apple Developer-konto, visas dessa säkerhetsvarningar på macOS.

## Viktig information
Detta projekt har **ingen koppling till**, och är **inte utvecklat, godkänt, sponsrat eller stödd av**
**AcadeMedia** eller **Pysslingen Förskolor**.

Namnet “Pysslingen” används enbart för att beskriva applikationens funktion och innebär ingen
association eller godkännande från varumärkesägaren.
