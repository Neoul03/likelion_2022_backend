from unittest import result
from googletrans import Translator

translator = Translator()

sentence = "안녕하세요 코드라이언입니다."

# sentence = input("언어를 감지할 문장을 입력해주세요 : ")
# detected = translator.detect(sentence)

# print(detected.lang)

result = translator.translate(sentence,'en')
print(result)