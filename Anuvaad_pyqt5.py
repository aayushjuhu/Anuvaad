import threading
import time
from playsound import playsound
import googletrans
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import speech_recognition as sr
import pyttsx3

lang = googletrans.LANGUAGES
lang_list = list(lang.values())
translator = googletrans.Translator()
engine = pyttsx3.init()
engine.setProperty('rate', 100)
voices = engine.getProperty('voices')

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('logo_anuvaad.ico'))
        self.setWindowTitle('अनुvaad')
        self.bg = QLabel(self)
        self.bg.setPixmap(QPixmap('bg_anuvaad.png'))
        self.blur_effect = QGraphicsBlurEffect()
        self.bg.setGraphicsEffect(self.blur_effect)
        self.bg.adjustSize()
        self.setGeometry(80, 200, 1800, 680)
        self.setFixedSize(1800, 680)
        # logo
        self.logo = QLabel(self)
        self.logo.setPixmap(QPixmap('anu_logo.png'))
        self.logo.setStyleSheet('background: #AD2323; border-radius: 10')
        self.logo.adjustSize()
        self.logo.move(740, 20)
        self.adjustSize()
        # left box
        self.t = QTextEdit(self)
        self.t.setFont(QFont('mangal', 18))
        self.t.setStyleSheet('background: #D9D9D9; border-radius: 20; border: 8px solid black')
        self.t.move(10, 140)
        self.t.setFixedSize(600, 400)
        # right box
        self.t1 = QTextEdit(self)
        self.t1.setFont(QFont('Mangal', 18))
        self.t1.setStyleSheet('background: #D9D9D9; border-radius: 20; border: 8px solid black')
        self.t1.move(1180, 140)
        self.t1.setFixedSize(600, 400)
        # mic
        self.mic = QPushButton(self)
        self.mic.setIcon(QIcon('mic.png'))
        self.mic.setIconSize(QSize(80, 100))
        self.mic.setStyleSheet("background: black; border-radius: 10")
        self.mic.setFixedSize(60, 90)
        self.mic.move(20, 40)
        self.mic.clicked.connect(lambda: self.command())

        # speaker left
        self.ttsl = QPushButton(self)
        self.ttsl.setIcon(QIcon('tts_anuvaad.png'))
        self.ttsl.setIconSize(QSize(80, 100))
        self.ttsl.setStyleSheet("background: black; border-radius: 10")
        self.ttsl.setFixedSize(100, 90)
        self.ttsl.move(100, 40)
        self.ttsl.clicked.connect(lambda: self.ttsleft())
        # speaker right
        self.ttsl = QPushButton(self)
        self.ttsl.setIcon(QIcon('tts_anuvaad.png'))
        self.ttsl.setIconSize(QSize(80, 100))
        self.ttsl.setStyleSheet("background: black; border-radius: 10")
        self.ttsl.setFixedSize(100, 90)
        self.ttsl.move(1660, 40)
        self.ttsl.clicked.connect(lambda: self.ttsright())
        # Translate button
        self.translate = QPushButton('Translate', self)
        self.translate.setFont(QFont('Berlin Sans FB Demi', 40))
        self.translate.setStyleSheet("background: black; color: #00B0F0; border-radius: 10")
        self.translate.move(700, 280)
        self.translate.setFixedSize(400, 100)
        self.translate.clicked.connect(lambda: self.trans())
        # combo left
        self.c1 = QComboBox(self)
        self.c1.setFont(QFont('Berlin Sans FB Demi', 18))
        self.c1.setStyleSheet('border-radius: 10; background: white; border: 4px solid black')
        self.c1.addItems(lang_list)
        self.c1.setCurrentText('english')
        self.c1.move(100, 580)
        self.c1.setFixedSize(400, 40)
        # combo right
        self.c = QComboBox(self)
        self.c.setFont(QFont('Berlin Sans FB Demi', 18))
        self.c.setStyleSheet('border-radius: 10; background: white; border: 4px solid black')
        self.c.addItems(lang_list)
        self.c.setCurrentText('english')
        self.c.move(1280, 580)
        self.c.setFixedSize(400, 40)
        self.show()

    def trans(self):
        self.t1.setReadOnly(False)
        global to_language_key
        global from_language_key
        global transl
        global transr
        global tran
        global v
        global v1
        to_language_key = ""
        from_language_key = ""

        try:
            for key, value in lang.items():
                if value == self.c1.currentText():
                    from_language_key = key
                    v1 = value
            for key, value in lang.items():
                if value == self.c.currentText():
                    to_language_key = key
                    v = value
            print(from_language_key)
            print(to_language_key)
            transr = self.t.toPlainText()
            print("user:" + transr)
            transl = translator.translate(text=transr, src=from_language_key, dest=to_language_key)
            tran = transl.text
            print(tran)
            self.t1.setText(tran)
            self.t1.setReadOnly(True)
        except Exception as e:
            print("अनुvaad", e)

    def ttsright(self):
        if v == 'french':
            engine.setProperty('voice', voices[1].id)
            engine.say(tran)
            engine.runAndWait()
        elif v == 'german':
            engine.setProperty('voice', voices[4].id)
            engine.say(tran)
            engine.runAndWait()
        elif v == 'marathi':
            engine.setProperty('voice', voices[2].id)
            engine.say(tran)
            engine.runAndWait()
        elif v == 'hindi':
            engine.setProperty('voice', voices[2].id)
            engine.say(tran)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[0].id)
            engine.say(tran)
            engine.runAndWait()

    def ttsleft(self):
        if v1 == 'french':
            engine.setProperty('voice', voices[1].id)
            engine.say(transr)
            engine.runAndWait()
        elif v1 == 'german':
            engine.setProperty('voice', voices[4].id)
            engine.say(transr)
            engine.runAndWait()
        elif v1 == 'marathi':
            engine.setProperty('voice', voices[2].id)
            engine.say(transr)
            engine.runAndWait()
        elif v1 == 'hindi':
            engine.setProperty('voice', voices[2].id)
            engine.say(transr)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[0].id)
            engine.say(transr)
            engine.runAndWait()

    def command(self):
        global to_language_key
        global from_language_key
        global audio
        global r
        to_language_key = ''
        from_language_key = ''
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listen")
            t = threading.Thread(target=self.speak())
            t.daemon = True
            t.start()
            audio = r.listen(source)
            try:
                for key, value in lang.items():
                    if value == self.c1.currentText():
                        from_language_key = key
                for key1, value in lang.items():
                    if value == self.c.currentText():
                        to_language_key = key1
                global transr
                global transl
                global tran
                print(from_language_key)
                playsound('anuvaad.mp3', False)
                query = r.recognize_google(audio, language=from_language_key)
                transr = query.capitalize()
                transl = translator.translate(text=transr, src=from_language_key, dest=to_language_key)
                tran = transl.text
                self.t.setText(transr)
                print("user:" + transr)
                self.t1.setText(str(tran))
                print(tran)

            except Exception as e:
                print("अनुvaad", e)

    def speak(self):
        playsound('anuvaad1.mp3', False)



app = QApplication([])
mw = MainWindow()
mw.show()
app.exec_()
