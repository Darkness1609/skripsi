from owlready2 import *

onto = get_ontology(r"ontologi 3.owx").load()

with onto:
    class Padi(Thing):
        namespace = onto

    class Gejala(Thing):
        namespace = onto

    class Penyakit(Thing):
        namespace = onto
    
    class Hama(Thing):
        namespace = onto
    class memilikiGejala(Padi >> Gejala):
        domain = [Padi]
        range = [Gejala]

    class memilikiPenyakit(Padi >> Penyakit):
        domain = [Padi]
        range = [Penyakit]

    class memilikiHama(Padi >> Hama):
        domain = [Padi]
        range = [Hama]

    class Pengendalian(Thing):
        pass
nimfa_coklat = Gejala("Nimfa_Coklat")
nimfa_kuning = Gejala("Nimfa_Kuning")
telur_pada_tanaman = Gejala("Telur_Pada_Tanaman")
lebar = Gejala("Lebar")
malai_terpotong = Gejala("Malai_Terpotong")
bekas_makan_di_daun = Gejala("Bekas_makan_di_Daun")

pembengkakan_jaringan_akar_kait = Gejala("Pembengkakan_Jaringan_Akar_Kait")
pembengkakan_jaringan_akar = Gejala("Pembengkakan_Jaringan_Akar")
perubahan_bentuk = Gejala("Perubahan_Bentuk")
spot = Gejala("Spot")
daun_menguning = Gejala("Daun_Menguning")
pertumbuhan_terhambat = Gejala("Pertumbuhan_Terhambat")

kotoran_di_batang = Gejala("Kotoran_di_Batang")
lubang_di_batang = Gejala("Lubang_di_Batang")
bibit_mati = Gejala("Bibit_Mati")
mudah_dicabut = Gejala("Mudah_Dicabut")
malai_hampa = Gejala("Malai_Hampa")

nimfa = Gejala("Nimfa")
imago = Gejala("Imago")
tepi_daun_dihisap = Gejala("Tepi_Daun_Dihisap")
malai_membusuk = Gejala("Malai_Membusuk")
pola_makan_acak = Gejala("Pola_Makan_Acak")
daerah_menguning = Gejala("Daerah_Menguning")
bulir_kosong = Gejala("Bulir_Kosong")

tanaman_menguning = Gejala("Tanaman_Menguning")
hangus = Gejala("Hangus")
hangus_melingkar = Gejala("Hangus_Melingkar")
bekas_tusukan_menghitam = Gejala("Bekas_Tusukan_Menghitam")

tulang_daun_menguning = Gejala("Tulang_Daun_Menguning")
berubah_warna_kuning = Gejala("Berubah_Warna_Kuning")
pucuk_daun_menguning = Gejala("Pucuk_Daun_Menguning")
menular = Gejala("Menular")

bulir_mengarat = Gejala("Bulir_Mengarat")
bulir_menghitam = Gejala("Bulir_Menghitam")
musim_hujan = Gejala("Musim_Hujan")
serangan_merata = Gejala("Serangan_Merata")
malai_terkena_sedikit = Gejala("Malai_Terkena_Sedikit")
bulir_masak_susu = Gejala("Bulir_Masak_Susu")

pangkal_malai_membusuk = Gejala("Pangkal_Malai_Membusuk")
bentuk_belah_ketupat = Gejala("Bentuk_Belah_Ketupat")
benih_tertular = Gejala("Benih_Tertular")

terdapat_wereng_coklat = Gejala("Terdapat_Wereng_Coklat")
tanaman_kerdil = Gejala("Tanaman_Kerdil")
malai_tidak_terbentuk = Gejala("Malai_Tidak_Terbentuk")

terdapat_wereng_hijau = Gejala("Terdapat_Wereng_Hijau")

belalang = Hama("Belalang")
nematoda_akar_padi = Hama("Nematoda_Akar_Padi")
penggerek_batang_padi = Hama("Penggerek_Batang_Padi")
walang_sangit = Hama("Walang_Sangit")
wereng_coklat = Hama("Wereng_Coklat")
hawar_daun_bakteri = Penyakit("Hawar_Daun_Bakteri")
gosong_palsu = Penyakit("Gosong_Palsu")
blas_padi = Penyakit("Blas_Padi")
kerdil_rumput = Penyakit("Kerdil_Rumput")
virus_tungro = Penyakit("Virus_Tungro")


# Define SWRL rules
with onto:
    rule1 = Imp()
    rule1.set_as_rule("""memilikiGejala(?Padi, Nimfa_Coklat) ^ memilikiGejala(?Padi, Nimfa_Kuning) ^ memilikiGejala(?Padi, Telur_Pada_Tanaman) ^ memilikiGejala(?Padi, Lebar) ^ memilikiGejala(?Padi, Malai_Terpotong) ^ memilikiGejala(?Padi, Bekas_makan_di_Daun) -> memilikiHama(?Padi, Belalang)""")
    rule2 = Imp()
    rule2.set_as_rule("""memilikiGejala(?Padi, Pembengkakan_Jaringan_Akar_Kait) ^ memilikiGejala(?Padi, Pembengkakan_Jaringan_Akar) ^ memilikiGejala(?Padi, Perubahan_Bentuk) ^ memilikiGejala(?Padi, Spot) ^ memilikiGejala(?Padi, Daun_Menguning) ^ memilikiGejala(?Padi, Pertumbuhan_Terhambat)-> memilikiHama(?Padi, Nematoda_Akar_Padi)""")
    rule3 = Imp()
    rule3.set_as_rule("""memilikiGejala(?Padi, Kotoran_di_Batang) ^ memilikiGejala(?Padi, Lubang_di_Batang) ^ memilikiGejala(?Padi, Bibit_Mati) ^ memilikiGejala(?Padi, Mudah_Dicabut) ^ memilikiGejala(?Padi, Malai_Hampa) -> memilikiHama(?Padi, Penggerek_Batang_Padi)""")
    rule4 = Imp()
    rule4.set_as_rule("""memilikiGejala(?Padi, Nimfa) ^ memilikiGejala(?Padi, Imago) ^ memilikiGejala(?Padi, Tepi_Daun_Dihisap) ^ memilikiGejala(?Padi, Malai_Membusuk) ^ memilikiGejala(?Padi, Pola_Makan_Acak) ^ memilikiGejala(?Padi, Daerah_Menguning) ^ memilikiGejala(?Padi, Bulir_Kosong) -> memilikiHama(?Padi, Walang_Sangit)""")
    rule5 = Imp()
    rule5.set_as_rule("""memilikiGejala(?Padi, Nimfa) ^ memilikiGejala(?Padi, Imago) ^ memilikiGejala(?Padi, Tanaman_Menguning) ^ memilikiGejala(?Padi, Hangus) ^ memilikiGejala(?Padi, Hangus_Melingkar) ^ memilikiGejala(?Padi, Bekas_Tusukan_Menghitam) ^ memilikiGejala(?Padi, Bulir_Kosong) -> memilikiHama(?Padi, Wereng_Coklat)""")
    rule6 = Imp()
    rule6.set_as_rule("""memilikiGejala(?Padi, Tulang_Daun_Menguning) ^ memilikiGejala(?Padi, Berubah_Warna_Kuning) ^ memilikiGejala(?Padi, Pucuk_Daun_Menguning) ^ memilikiGejala(?Padi, Serangan_Merata) ^ memilikiGejala(?Padi, Menular) -> memilikiPenyakit(?Padi, Hawar_Daun_Bakteri)""")
    rule7 = Imp()
    rule7.set_as_rule("""memilikiGejala(?Padi, Bulir_Mengarat) ^ memilikiGejala(?Padi, Bulir_Menghitam) ^ memilikiGejala(?Padi, Serangan_Merata) ^ memilikiGejala(?Padi, Musim_Hujan) ^ memilikiGejala(?Padi, Malai_Terkena_Sedikit) ^ memilikiGejala(?Padi, Bulir_Masak_Susu) -> memilikiPenyakit(?Padi, Gosong_Palsu)""")
    rule8 = Imp()
    rule8.set_as_rule("""memilikiGejala(?Padi, Pangkal_Malai_Membusuk) ^ memilikiGejala(?Padi, Bentuk_Belah_Ketupat) ^ memilikiGejala(?Padi, Serangan_Merata) ^ memilikiGejala(?Padi, Benih_Tertular) -> memilikiPenyakit(?Padi, Blas_Padi)""")
    rule9 = Imp()
    rule9.set_as_rule("""memilikiGejala(?Padi, Terdapat_Wereng_Coklat) ^ memilikiGejala(?Padi, Spot) ^ memilikiGejala(?Padi, Tanaman_Kerdil) ^ memilikiGejala(?Padi, Malai_Tidak_Terbentuk) -> memilikiPenyakit(?Padi, Kerdil_Rumput)""")
    rule10 = Imp()
    rule10.set_as_rule("""memilikiGejala(?Padi, Terdapat_Wereng_Hijau) ^ memilikiGejala(?Padi, Spot) ^ memilikiGejala(?Padi, Daun_Menguning) ^ memilikiGejala(?Padi, Malai_Hampa) -> memilikiPenyakit(?Padi, Virus_Tungro)""")
    rule11 = Imp()
    rule11.set_as_rule("""memilikiGejala(?Padi, Malai_Terpotong) ^ memilikiGejala(?Padi, Bekas_makan_di_Daun) -> memilikiHama(?Padi, Belalang)""")
    rule12 = Imp()
    rule12.set_as_rule("""memilikiGejala(?Padi, Pembengkakan_Jaringan_Akar_Kait) ^ memilikiGejala(?Padi, Pembengkakan_Jaringan_Akar)-> memilikiHama(?Padi, Nematoda_Akar_Padi)""")
    rule13 = Imp()
    rule13.set_as_rule("""memilikiGejala(?Padi, Kotoran_di_Batang) ^ memilikiGejala(?Padi, Lubang_di_Batang) -> memilikiHama(?Padi, Penggerek_Batang_Padi)""")
    rule14 = Imp()
    rule14.set_as_rule("""memilikiGejala(?Padi, Nimfa) ^ memilikiGejala(?Padi, Imago) ^ memilikiGejala(?Padi, Bulir_Kosong) -> memilikiHama(?Padi, Walang_Sangit)""")
    rule15 = Imp()
    rule15.set_as_rule("""memilikiGejala(?Padi, Hangus) ^ memilikiGejala(?Padi, Hangus_Melingkar) -> memilikiHama(?Padi, Wereng_Coklat)""")
    rule16 = Imp()
    rule16.set_as_rule("""memilikiGejala(?Padi, Tulang_Daun_Menguning) ^ memilikiGejala(?Padi, Serangan_Merata) -> memilikiPenyakit(?Padi, Hawar_Daun_Bakteri)""")
    rule17 = Imp()
    rule17.set_as_rule("""memilikiGejala(?Padi, Bulir_Mengarat) ^ memilikiGejala(?Padi, Bulir_Menghitam) -> memilikiPenyakit(?Padi, Gosong_Palsu)""")
    rule18 = Imp()
    rule18.set_as_rule("""memilikiGejala(?Padi, Pangkal_Malai_Membusuk) ^ memilikiGejala(?Padi, Bentuk_Belah_Ketupat) -> memilikiPenyakit(?Padi, Blas_Padi)""")
    rule19 = Imp()
    rule19.set_as_rule("""memilikiGejala(?Padi, Terdapat_Wereng_Coklat) ^ memilikiGejala(?Padi, Tanaman_Kerdil) -> memilikiPenyakit(?Padi, Kerdil_Rumput)""")
    rule20 = Imp()
    rule20.set_as_rule("""memilikiGejala(?Padi, Terdapat_Wereng_Hijau) ^ memilikiGejala(?Padi, Daun_Menguning) -> memilikiPenyakit(?Padi, Virus_Tungro)""")
    



def predict_diseases(symptoms):
    new_plant = Padi("PadiBaru")

    for symptom in symptoms:
        symptom = Gejala(symptom)
        new_plant.memilikiGejala.append(symptom)

    sync_reasoner_pellet(infer_property_values = True, infer_data_property_values = True)

    predicted_diseases = list(new_plant.memilikiHama)+list(new_plant.memilikiPenyakit)
    predicted_diseases_name = list(map(lambda x: x.name,predicted_diseases))
    destroy_entity(new_plant)
    return predicted_diseases_name


# given_symptoms = [nimfa_coklat, nimfa_kuning, telur_pada_tanaman,lebar,malai_terpotong,bekas_makan_di_daun]
# given_symptoms = ["Nimfa_Coklat", "Nimfa_Kuning", "Telur_Pada_Tanaman", "Lebar", "Malai_Terpotong", "Bekas_makan_di_Daun"]
# predicted_diseases = predict_diseases(given_symptoms)

# print("Given symptoms:", given_symptoms)
# print("Predicted diseases:", predicted_diseases)

# for r in Gejala.instances():
#     print (r)