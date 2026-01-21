# Mitt Pysslingen Downloader

### Ett fristående och inofficiellt verktyg för nedladdning av media från Mitt Pysslingen

Material som laddas upp i Mitt Pysslingen sparas inte alltid efter att barnet slutat på förskolan.  
Med **Mitt Pysslingen Downloader** kan du ladda ner och spara bilder, filmer och dokument som rör ditt barn, så att minnena kan bevaras även i framtiden.

---

## ⬇️ Ladda ner

- **Windows**  
  👉 [Mitt Pysslingen Downloader.exe](https://github.com/homan85/Mitt-Pysslingen-Downloader/releases/download/1.0.0/Mitt.Pysslingen.Downloader-Windows.exe)
  
- **macOS (Apple Silicon)**  
  👉 [Mitt Pysslingen Downloader.dmg](https://github.com/homan85/Mitt-Pysslingen-Downloader/releases/download/1.0.0/MittPysslingenDownloader-macOS.Apple.Silicon.zip)
  
- **macOS (Intel)**  
  👉 [Mitt Pysslingen Downloader.dmg](https://github.com/homan85/Mitt-Pysslingen-Downloader/releases/download/1.0.0/MittPysslingenDownloader-macOS.Intel.zip)

---

## 📱 Varför finns ingen mobil- eller surfplatteversion?

Mitt Pysslingen Downloader är medvetet utvecklad endast för **Windows** och **macOS**.

Applikationen är byggd för att ladda ner, bearbeta och spara **stora mängder filer** (bilder, filmer, dokument och PDF:er) direkt till användarens filsystem. Denna typ av funktionalitet är kraftigt begränsad eller inte tillåten på mobil- och surfplattformar.

Exempel på begränsningar:

- Mycket begränsad filsystemåtkomst på smartphones och surfplattor  
- Restriktioner kring bakgrundsarbete och längre nedladdningar  
- Säkerhetssandlådor som förhindrar fri filhantering  
- Plattformsspecifika regler som skulle kräva omfattande kompromisser i funktionalitet  

En mobil- eller surfplatteversion skulle därför riskera att bli **instabil, ofullständig eller kraftigt begränsad** jämfört med datorversionen.

För att säkerställa en **stabil, förutsägbar och komplett användarupplevelse** är applikationen därför begränsad till datorplattformar där användaren har full kontroll över sina filer.

---

## 🖥️ Så här ser applikationen ut

### Windows
<img width="476" height="450" src="https://github.com/user-attachments/assets/9ad8934b-80e9-4341-8b58-10173b8e1b8c" />
<img width="476" height="450" src="https://github.com/user-attachments/assets/614334fd-c5d8-4390-991b-9a95997c2c40" />

### macOS
<img width="476" height="450" src="https://github.com/user-attachments/assets/1cdc96e0-15b8-40d2-b275-d7c578dcd075" />
<img width="476" height="450" src="https://github.com/user-attachments/assets/39896537-babf-4cd7-92e9-295e33308524" />

---

## ⚠️ Viktigt gällande macOS

macOS kan visa en säkerhetsvarning första gången du kör Mitt Pysslingen Downloader.  
Detta är ett inbyggt säkerhetsskydd i macOS och betyder **inte** att applikationen är skadlig.

### Om macOS säger att appen är ”skadad”

1. Öppna **Terminal**
2. Kör följande kommando (anpassa sökvägen om appen ligger på annan plats):

```bash
sudo xattr -rd com.apple.quarantine /Applications/Mitt\ Pysslingen\ Downloader.app
```
3. Starta applikationen igen

### Varför händer detta?

Apple kräver att appar som laddas ner från internet ska vara:
1. signerade med ett Apple Developer ID
2. notariserade av Apple

Då detta är ett hobbyprojekt som distribueras utan Apple Developer-konto visas dessa säkerhetsvarningar.

---

## ℹ️ Viktig information

I Demo-läget är nedladdning av meddelanden och video spärrade och endast ett inlägg laddas ner.  
Allt nedladdat material innehåller vattenstämpel.

Vid köp av licens för **50 kr** tas dessa begränsningar bort.

---

Detta projekt har **ingen koppling till**, och är **inte utvecklat, godkänt, sponsrat eller stödd av**
**AcadeMedia** eller **Pysslingen Förskolor**.  
Namnet ”Pysslingen” används enbart för att beskriva applikationens funktion och innebär ingen
association eller godkännande från varumärkesägaren.

Applikationen tillhandahålls i befintligt skick (“as is”), utan några garantier eller utfästelser,
vare sig uttryckliga eller underförstådda.

Användning av applikationen sker på eget ansvar. Utvecklaren ansvarar inte för eventuell dataförlust,
felaktig funktion eller andra konsekvenser som kan uppstå vid användning av programmet.
