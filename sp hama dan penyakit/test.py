import model

list_gejala_test =[["Bulir_Menghitam","Imago","Pembengkakan_Jaringan_Akar_Kait","Kotoran_di_Batang","Terdapat_Wereng_Coklat","Perubahan_Bentuk","Lubang_di_Batang"],["Pertumbuhan_Terhambat","Pembengkakan_Jaringan_Akar","Terdapat_Wereng_Coklat","Malai_Hampa","Pembengkakan_Jaringan_Akar_Kait"]]

for i in list_gejala_test:
    ontology_model = model.PemodelanOntologi()
    print(ontology_model.predict_diseases(i))
