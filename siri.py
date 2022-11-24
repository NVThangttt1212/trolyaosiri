# đầu tiên ta cần install thư viện các thư viện 
# speech_recognition bằng câu lệnh pip install SpeechRecognition
# pip install gTTS
# import os
# import time
# import playsound
# pip install playsound==1.2.2
# pip install wikipedia
import speech_recognition as sr
from gtts import gTTS
import os
import playsound
import wikipedia #ta cài thêm thư viện wikipedia để botSiri thông minh hơn 
from datetime import date # thư viện này để cập nhật giờ 
today = date.today()

from datetime import datetime
now = datetime.now()


r = sr.Recognizer() # lấy dữ liệu từ giọng nói 
#tiếp theo là phát âm thanh từ loa máy tính của mình
def speak(text):
    tts = gTTS(text=text, lang='vi')
    #lưu vào mp3 
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)# để sau mỗi lần nói thì filename sẽ được xóa và thành file mới

while True: # để cho code luôn đúng và chạy tới khi có lệnh dừng 
    with sr.Microphone() as source:
        
        audio_data = r.record(source, duration=3)
        # ở đây ta gán dữ liệu mà microphone lắng nghe trong vòng 3 giây vào audio_data
        print("Recognizing...")
        #tiếp theo ta lấy dữ liệu từ audio_data chuyển sang dạng text 
        try:
            text = r.recognize_google(audio_data, language="vi")# sử dụng thư viện recognize_google để chuyển đổi 
        except:
            text = ""
        print(text)
    #để chạy chương trình ta mở terminal và nhập lệnh .\siri.py
    #phần try except để nếu không nghe được thì trả về giá trị rỗng

    #phần này là siri hiểu được những gì 
    if text == "":
        botSiri = "tôi đang lắng nghe bạn đây"
        speak(botSiri)
    #elif in để trong câu nói của mình có chứa từ đó thì sẽ trả lời ...
    elif "Xin chào" in text:
        botSiri = "chào bạn bạn có khỏe không"
        print(botSiri)
        speak(botSiri)
    elif "ngày bao nhiêu" in text:
        botSiri =today.strftime("hôm nay là ngày %d/%m/%Y") 
        print(botSiri)
        speak(botSiri)
    elif "Mấy giờ" in text:
        botSiri =now.strftime("%H:%M:%S") 
        print(botSiri)
        speak(botSiri)
    elif "học" in text:
        botSiri ="bạn đang học xử lý ngôn ngữ tự nhiên"
        print(botSiri)
        speak(botSiri)
    elif text: 
        wikipedia.set_lang("vi")
        wikipedia.summary(text, sentences=1) # phần text là thông tin tìm kiếm /sentences để đọc dòng đầu trong kết quả tìm kiếm 
        print(botSiri)
        speak(botSiri)
    elif "tạm biệt" in text:
        botSiri = "tạm biệt hẹn gặp lại bạn"
        print(botSiri)
        speak(botSiri)
        break
    #với trường hợp nói vào mà máy không hiểu 
    else: 
        botSiri = "bạn muốn nói gì với tôi"
        speak(botSiri)






