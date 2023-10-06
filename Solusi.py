import re

def tiket_pesawat(a,b,c):
    print("Hasil Pencarian Tiket :")
    pesawat= open("tiket.txt","r").read()
    data=[]
    index=["index:v"]
    if len(re.findall(a,pesawat))==0:
        print("Tiket Tidak Ditemukan")
        main()
    elif len(re.findall(b,pesawat))==0:
        print("Tiket Tidak Ditemukan")
        main()
    else:
        for i in range(1,len(pesawat.splitlines())):
            if re.findall(a,pesawat.splitlines()[i]) and re.findall(b,pesawat.splitlines()[i]):
                daftari = pesawat.splitlines()[i].split("\t")
                if daftari[1]==a:
                    index+=daftari
                    data+=["\r"+str(i)+".\t"+daftari[0]+"\t"+daftari[1]+"\t"+daftari[2]+"\t"+"{:,.0f}".format(int(daftari[3]))]
                    print("\r"+str(i)+".\t"+daftari[0]+"\t"+daftari[1]+"\t"+daftari[2]+"\t"+"{:,.0f}".format(int(daftari[3])))
                    continue
        print("\n")
        milih = int(input("Pilihan Tiket Anda :"))
        if milih > len(data):
            print("Data Tidak Ditemukan")
        else:
            milih= int(index[milih*4])
            total_harga_tiket = (milih*c)+(milih*c*10/100)
            print("Total Harga Tiket Pesawat = ", total_harga_tiket)
            hotel(b,total_harga_tiket)

def hotel(d,e):
    print("\nPilihan Hotel :")
    dataHotel= open("hotel.txt","r").read().splitlines()
    data_2=[]
    for j in range(0,len(dataHotel)):
        if re.findall(d,dataHotel[j]):
            daftar_hotel = dataHotel[0].split("\t")
            daftar_harga = dataHotel[j].split("\t")
            for x in range(0,len(daftar_hotel)):
                data_2+=[daftar_hotel[x]+"\t"+daftar_harga[x].replace('"','').replace(' ','').replace('.00','')]
                print(daftar_hotel[x]+"\t"+daftar_harga[x].replace('"','').replace(' ','').replace('.00',''))
    pilih = str(input("Pilih Hotel :"))
    for n in range(0,len(data_2)):
        if re.findall(pilih,data_2[n]):
            inap = data_2[n].split("\t")[1]
            harga = e+ int(inap.replace(',',''))
            print("\nTotal Biaya = Rp"+"{:,.2f}".format(harga))

def main():
    print("=====Travelue=====")
    kota_asal = str(input("Kota Asal : "))
    kota_tujuan = str(input("Kota Tujuan : "))
    tanggal_keberangkatan = input("Tanggal Keberangkatan : ")
    Jumlah_penumpang = int(input("Jumlah Anggota Penumpang : "))
    tiket_pesawat(kota_asal,kota_tujuan,Jumlah_penumpang)

main()
        

