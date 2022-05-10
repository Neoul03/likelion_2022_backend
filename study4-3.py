from googletrans import Translator

translator = Translator()

sentence = input("감지 할 언어를 입력해주세요 : ")
# sentence = "안녕하세요 코드라이언입니다."
detected = translator.detect(sentence)

print(detected.lang)