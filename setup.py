import sys
from cx_Freeze import setup, Executable

base = None

if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable('dosya_adi.py', base=base)  # dönüştürmek istediğiniz Python dosyasının adını buraya yazın
]

options = {
    'build_exe': {
        'includes': ['sip'],  # Gerekli bağımlılıkları buraya ekleyin
    }
}

setup(
    name='DevS',
    version='1.0',
    description='Uygulama Açıklaması',
    executables=executables,
    options=options
)
