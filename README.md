# ربات استعلام حضور استاد در سامانه دان

این ربات برای اطلاع از حضور استاد در سامانه‌ی دان طراحی شده در این برنامه از کتابخانه های selenium و Tkinter استفاده شده و کمی از pygame نیز استفاده شده است

# Teacher present status for AZAD UNIVERSITIES
This bot has made for giving alert when teachers start class from Daan system for coding this bot I've used selenium , Tkinter and pygame

## راهنمایی نصب
ابتدا شما باید اخرین نسخه پایتون رو از لینک <a  href="https://www.python.org/downloads/">سایت</a> دانلود کنید.
 سپس باید فایل های مورد نظر را نصب کنید از طریق دستور
```bash
pip install requirements.txt
```
باید به‌نسبت سیستم‌عامل و ورژن کروم خود از<a href="https://chromedriver.chromium.org/downloads">لینک</a> درایور کروم را دانلود کرده
سپس باید مسیر فایل درایو کروم را در قسمت مشخص شده قرار دهید

```python
'''Line 50 main.py'''
browser = webdriver.Chrome(executable_path="PATH OF YOUR DRIVER WHICH YOU DOWNLOADED")

```
## Installation Guide
Firstly you have to had python on your system previously if you don't have python download the latest version from this
<a  href="https://www.python.org/downloads/">link</a>
then you have to run this command from your cmd or terminal
```bash
pip install requirements.txt
```
Then you have to download suitable chrome driver for your system and chrome version from this <a  href="https://chromedriver.chromium.org/downloads">link</a>
when you downloaded the driver you have to set driver path in 50 line of main.py
```python
'''Line 50 main.py'''
browser = webdriver.Chrome(executable_path="PATH OF YOUR DRIVER WHICH YOU DOWNLOADED")

```
## License & Copyright
Licensed under the [MIT License](LICENSE).
