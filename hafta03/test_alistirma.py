# Hafta 3: Testleri bu dosyaya SİZ yazacaksınız.
#
# Aşağıda örnek olarak bir test var. Yanına her fonksiyon için kendi testlerinizi ekleyin.
# Çalıştırmak için bu klasörde:  python -m pytest -v

import pytest

from alistirma import kargo_ucreti, bilet_fiyati, ortalama

# Kargo Testleri

def test_kargo_buyuk_sipariste_ucretsiz():
    assert kargo_ucreti(800) == 0
    assert kargo_ucreti(500) == 0

def test_kargo_negatif_olamaz():
    with pytest.raises(ValueError):
        kargo_ucreti(-42)
    with pytest.raises(ValueError):
        kargo_ucreti(-1)

def test_kargo_500denbuyukse_50():
    assert kargo_ucreti(0) == 50
    assert kargo_ucreti(232) == 50
    assert kargo_ucreti(499) == 50



# Bilet Testleri

def test_bilet_yas_negatif_olamaz():
    with pytest.raises(ValueError):
        bilet_fiyati(-12)

def test_bilet_6dankucukse_0():
    assert bilet_fiyati(0) == 0
    assert bilet_fiyati(5) == 0
    assert bilet_fiyati(6) == 0

def test_bilet_17dankucukse_50():
    assert bilet_fiyati(7) == 50
    assert bilet_fiyati(12) == 50
    assert bilet_fiyati(17) == 50

def test_bilet_65danbuyukse_60():
    assert bilet_fiyati(68) == 60
    assert bilet_fiyati(65) == 60

def test_bilet_18_64_100():
    assert bilet_fiyati(18) == 100
    assert bilet_fiyati(32) == 100
    assert bilet_fiyati(64) == 100

# Not Ortalaması Testleri

def test_normal_ortalama_deger():
    assert ortalama([70, 85]) == 77.5
    assert ortalama([60, 70, 80]) == 70.0

def test_ortalama_tek_deger():
    assert ortalama([42]) == 42.0

def test_ortalama_sifir():
    assert ortalama([0,0,0]) == 0.0

def test_ortalama_bos_liste():
    with pytest.raises(ValueError):
        ortalama([])

