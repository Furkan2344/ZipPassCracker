import zipfile
from tqdm import tqdm

wordlist = input("Wordlist konumu: ")
zipDosya = input("Zip dosyası: ")

zipDosya = zipfile.ZipFile(zipDosya)

kelimeSayisi = len(list(open(wordlist, "rb")))

print("Wordlistte bulunan toplam kelime sayısı: ", kelimeSayisi)

with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=kelimeSayisi, unit="word"):
        try:
            zipDosya.extractall(pwd=word.strip())
        except:
            continue
        print("\nŞifre bulundu: ",word.decode().strip())
        exit(0)
    print("Şifre bulunamadı")