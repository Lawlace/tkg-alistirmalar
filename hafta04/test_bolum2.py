# Lab, Bölüm 2: Testleri bu dosyaya SİZ yazacaksınız.
#
# Aşağıda örnek olarak bir test var. Yanına her fonksiyon için kendi testlerinizi ekleyin.
# Çalıştırmak için bu klasörde:  python -m pytest test_bolum2.py test_hatali_surumler.py -v

import pytest

from bolum2 import sifre_gucu, otopark_ucreti, yuzde_degisim

# Şifre testleri

def test_kisa_sifre_zayif():
    assert sifre_gucu("abc") == "zayıf"

def test_kisa_sifre_zayiforta():
    assert sifre_gucu("abcd") == "zayıf"

def test_sifre_bos():
    with pytest.raises(ValueError):
        sifre_gucu("")

def test_sifre_orta():
    assert sifre_gucu("abcabcab") == "orta"

def test_sifre_ortaguclu():
    assert sifre_gucu("abcabcabc") == "orta"

def test_sifre_guclu():
    assert sifre_gucu("abcabcabcabc") == "güçlü"

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
    assert otopark_ucreti(126) == 40

def test_otopark_ucreti_180denbuyuk():
    assert otopark_ucreti(192) == 60

# Yüzde değişim testleri

def test_yuzde_degisim_eski_deger():
    with pytest.raises(ValueError):
        yuzde_degisim(0, 15)

def test_yuzde_normal_deger():
    assert yuzde_degisim(100,150) == 50
