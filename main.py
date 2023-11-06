from googletrans import Translator

def main():
    translator  = Translator()

    while True:
        print("Ceviri yapmak istediginiz metni girin.(Cıkmak icin 'q' basın.) :")
        text = input()

        if text.lower() == 'q':
            print("Ceviri Programı Kapatılıyor")
            break

        print("Cevirmek istediginiz dil kodunu girin.(Örnegin en : ingilizce,fr:fransızca vs...) : ")
        target_language = input()

        try:
            translated = translator.translate(text,dest=target_language)
            print("Ceviri : ",translated.text)
        except  Exception as e :
            print("Ceviri yapılırken bir hata olustu : ",e)

if __name__ == "__main__" :
    main()
