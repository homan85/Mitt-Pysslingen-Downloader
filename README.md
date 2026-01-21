# Mitt Pysslingen Downloader

### Ett fristående och inofficiellt verktyg för nedladdning av media som laddats upp till Mitt Pysslingen.<br>
Material som finns i Mitt Pysslingen sparas inte alltid efter att barnet slutat på förskolan.<br>
Med **_Mitt Pysslingen Downloader_** kan du ladda ner och spara media som rör ditt barn, så att du kan behålla minnena för framtiden.

Ladda ner för 
<br>[Windows](https://github.com/homan85/Mitt-Pysslingen-Downloader/releases/download/1.0.0/Mitt.Pysslingen.Downloader-Windows.exe)
<br>[macOS (Apple Silicon)](https://github.com/homan85/Mitt-Pysslingen-Downloader/releases/download/1.0.0/MittPysslingenDownloader-macOS.Apple.Silicon.zip)
<br>[macOS (Intel)](https://github.com/homan85/Mitt-Pysslingen-Downloader/releases/download/1.0.0/MittPysslingenDownloader-macOS.Intel.zip)

# Så här ser applikationen ut
### Windows
<img width="476" height="450" src="https://github.com/user-attachments/assets/9ad8934b-80e9-4341-8b58-10173b8e1b8c" />

<img width="476" height="450" src="https://github.com/user-attachments/assets/614334fd-c5d8-4390-991b-9a95997c2c40" />

### macOS
<img width="476" height="450" src="https://github.com/user-attachments/assets/1cdc96e0-15b8-40d2-b275-d7c578dcd075" />
<img width="476" height="450" src="https://github.com/user-attachments/assets/39896537-babf-4cd7-92e9-295e33308524" />

## Viktigt gällande macOS

macOS kan visa en säkerhetsvarning första gången du kör Mitt Pysslingen Downloader.  
Detta är ett säkerhetsskydd i macOS och betyder **inte** att applikationen faktiskt är skadad.

### Om macOS säger att appen är “skadad”

1. Öppna **Terminal**
2. Kör följande kommando (anpassa sökvägen om applikationen ligger på annan plats):
```bash
sudo xattr -rd com.apple.quarantine /Applications/Mitt\ Pysslingen\ Downloader.app

```
3. Starta appen igen

### Varför händer detta?

Apple kräver att appar som laddas ner från internet ska vara:
1. signerade med Apple Developer ID
2. notariserade av Apple

Då detta är ett hobbyprojekt som distribueras utan Apple Developer-konto, visas dessa säkerhetsvarningar på macOS.

## Viktig information

_I Demo-läget är nedladdning av meddelanden och video spärrade och endast ett inlägg laddas ner. Allt som laddas ner har vattenstämpel._<br>
_Vid köp av licens för 50kr tas dessa begränsningar bort._

<sub>Detta projekt har **ingen koppling till**, och är **inte utvecklat, godkänt, sponsrat eller stödd av**
**AcadeMedia** eller **Pysslingen Förskolor**.
Namnet “Pysslingen” används enbart för att beskriva applikationens funktion och innebär ingen
association eller godkännande från varumärkesägaren.</sub><br>
<sub>Applikationen tillhandahålls i befintligt skick (“as is”), utan några garantier eller utfästelser, vare sig uttryckliga eller underförstådda.</sub>
<sub>Användning av applikationen sker på eget ansvar. Utvecklaren ansvarar inte för eventuell dataförlust, felaktig funktion eller andra konsekvenser som kan uppstå vid användning av programmet.</sub>
