# System Resource Widget

Windows masaüstünde CPU ve RAM kullanımını küçük, sürekli üstte kalan bir widget olarak gösteren basit Python uygulaması.

## Özellikler

- CPU kullanım yüzdesi
- RAM kullanım yüzdesi
- Kullanılan / toplam RAM miktarı
- 1 saniyede bir otomatik güncelleme
- Çerçevesiz ve her zaman üstte pencere
- Fareyle sürükleyerek taşıma
- Harici GUI framework gerektirmez; Tkinter kullanır

## Gereksinimler

- Python 3.10+
- `psutil`

## Kurulum

```powershell
python -m pip install -r requirements.txt
```

## Çalıştırma

```powershell
python main.py
```

## EXE oluşturma

İsterseniz PyInstaller ile tek dosyalık Windows uygulamasına dönüştürebilirsiniz:

```powershell
python -m pip install pyinstaller
pyinstaller --noconsole --onefile --name SystemResourceWidget main.py
```

Oluşan `.exe` dosyası `dist` klasöründe bulunur.

## Lisans

MIT
