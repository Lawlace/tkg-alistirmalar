# Lab, Bölüm 2: Testleri bu dosyaya SİZ yazacaksınız.
#
# Aşağıda örnek olarak bir test var. Yanına her fonksiyon için kendi testlerinizi ekleyin.
# Çalıştırmak için bu klasörde:  python -m pytest test_bolum2.py test_hatali_surumler.py -v

import pytest

from bolum2 import sifre_gucu, otopark_ucreti, yuzde_degisim

# Şifre testleri

def test_kisa_sifre_zayif():
    assert sifre_gucu("abc") == "zayıf"

def test_sifre_bos():
    with pytest.raises(ValueError):
        sifre_gucu("")

def test_sifre_orta():
    assert sifre_gucu("abcabcabc")

def test_sifre_guclu():
    assert sifre_gucu("abcabcabcabcabc") == "güçlü"

# Otopark ücreti testleri

def test_otopark_ucreti_negatif():
    with pytest.raises(ValueError):
        otopark_ucreti(-1) 

def test_otopark_ucreti_15denkucuk():
    assert otopark_ucreti(12) == 0
    assert otopark_ucreti(15) == 0


def test_otopark_ucreti_60denkucuk():
    assert otopark_ucreti(60) == 20
    assert otopark_ucreti(26) == 20

def test_otopark_ucreti_180denkucuk():
    assert otopark_ucreti(180) == 40
    assert otopark_ucreti(126) == 60

def test_otopark_ucreti_180denbuyuk():
    assert otopark_ucreti(192) == 60

# Yüzde değişim testleri

def test_yüzde_eski_deger_0_olamaz():
    with pytest.raises(ValueError):
        yuzde_degisim(0,15)
