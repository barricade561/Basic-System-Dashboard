# Basic System Dashboard

## English

Basic System Dashboard is a lightweight Windows desktop widget designed to display real-time CPU and RAM usage in a compact, always-on-top interface. It is intended for users who want a simple system monitor without opening Task Manager or installing a full monitoring suite.

The application updates system statistics every second and presents CPU usage, RAM usage percentage, and used/total memory information in an unobtrusive desktop window. The widget can be dragged anywhere on the screen and closed directly from its interface.

### Features

- Real-time CPU usage percentage
- Real-time RAM usage percentage
- Used and total RAM information
- Automatic refresh every second
- Compact borderless desktop widget
- Always-on-top window
- Drag-and-drop positioning
- Lightweight resource usage
- Windows executable support

### Run the Windows Executable

If you do not want to install Python, download and run:

`release/SystemResourceWidget.exe`

The executable is automatically built on a Windows runner using GitHub Actions and PyInstaller whenever the source code is updated.

> Note: The executable is not digitally signed with a commercial Windows code-signing certificate. Windows SmartScreen may therefore display an "Unknown publisher" warning when the application is launched for the first time.

### Run from Source

Developers can also run the application directly from the Python source code.

```powershell
python -m pip install -r requirements.txt
python main.py
```

### Automated Windows Build

The workflow located at:

`.github/workflows/build-windows-exe.yml`

uses a Windows GitHub Actions runner and PyInstaller to generate `SystemResourceWidget.exe`. The resulting executable is stored as a GitHub Actions artifact and can also be placed under:

`release/SystemResourceWidget.exe`

### License

MIT License

---

## Türkçe

Basic System Dashboard, Windows masaüstünde gerçek zamanlı CPU ve RAM kullanımını küçük ve sürekli üstte kalan bir arayüz üzerinden göstermek için geliştirilmiş hafif bir sistem izleme uygulamasıdır. Görev Yöneticisi'ni açmadan veya kapsamlı bir sistem izleme yazılımı kurmadan temel donanım kullanım değerlerini takip etmek isteyen kullanıcılar için tasarlanmıştır.

Uygulama sistem istatistiklerini her saniye yeniler; CPU kullanım yüzdesini, RAM kullanım yüzdesini ve kullanılan/toplam bellek miktarını kompakt bir masaüstü penceresinde gösterir. Widget ekran üzerinde istenilen konuma sürüklenebilir ve kendi arayüzü üzerinden kapatılabilir.

### Özellikler

- Gerçek zamanlı CPU kullanım yüzdesi
- Gerçek zamanlı RAM kullanım yüzdesi
- Kullanılan ve toplam RAM miktarı
- Her saniye otomatik yenileme
- Kompakt ve çerçevesiz masaüstü widget'ı
- Her zaman üstte kalan pencere
- Sürükleyerek konumlandırma
- Düşük kaynak kullanımı
- Windows `.exe` desteği

### Windows EXE Dosyasını Çalıştırma

Python kurmak istemiyorsanız aşağıdaki dosyayı indirip doğrudan çalıştırabilirsiniz:

`release/SystemResourceWidget.exe`

`.exe` dosyası, kaynak kod güncellendiğinde GitHub Actions ve PyInstaller kullanılarak Windows ortamında otomatik olarak oluşturulur.

> Not: Uygulama ticari bir Windows kod imzalama sertifikası ile dijital olarak imzalanmamıştır. Bu nedenle Windows SmartScreen ilk çalıştırmada "Bilinmeyen yayıncı" uyarısı gösterebilir.

### Kaynak Koddan Çalıştırma

Geliştiriciler uygulamayı Python kaynak kodu üzerinden de çalıştırabilir.

```powershell
python -m pip install -r requirements.txt
python main.py
```

### Otomatik Windows Derlemesi

Aşağıdaki workflow dosyası:

`.github/workflows/build-windows-exe.yml`

Windows tabanlı bir GitHub Actions runner üzerinde PyInstaller kullanarak `SystemResourceWidget.exe` dosyasını oluşturur. Oluşturulan `.exe` dosyası GitHub Actions artifact'ı olarak saklanabilir ve ayrıca şu konuma yerleştirilebilir:

`release/SystemResourceWidget.exe`

### Lisans

MIT Lisansı
