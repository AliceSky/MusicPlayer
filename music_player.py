import sys,os,time
import pyaudio,wave
from PyQt5.QtCore import Qt,QThread,pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QPushButton,QLabel,QHBoxLayout,QVBoxLayout

from Ui_musicplayer import Ui_MainWindow


class QtTest(QMainWindow, Ui_MainWindow):

    def __init__(self): 
        super(QtTest,self).__init__()
        self.setupUi(self)
      
        self.path = "D:\TestCode\wav"
        self.file_list = os.listdir(self.path)
        self.listWidget.addItems(self.file_list)  #对listwidget赋值，显示播放列表

        self.listWidget.itemClicked.connect(self.list_clicked) #列表绑定函数
        self.btn_2.clicked.connect(self.list_clicked) #播放键
        self.btn_3.clicked.connect(self.play_off_func) #停止键
 
    def list_clicked(self):
        song_name = self.listWidget.currentItem().text() #获取当前列表被按下的按键文本值
        self.song_path = os.path.join(self.path,song_name) #拼接得到按下的按键的音频绝对路径

        self.my_thread = MyThread(self.song_path) #将音频路径传参给线程
        self.my_thread.is_on = True 
        self.my_thread.start()
    
    def play_off_func(self):
        self.my_thread.is_on = False 
        
class MyThread(QThread):
    def __init__(self,song_of_path2): #线程接收传入的参数
        super(MyThread,self).__init__()
        self.is_on =True
        self.song_path = song_of_path2 

    def run(self):
        CHUNK = 1024
    
        s1 = wave.open(self.song_path,'rb') #打开音频
        s2 = pyaudio.PyAudio() #初始化PyAudio模块

        stream = s2.open(format = s2.get_format_from_width(s1.getsampwidth()),   #打开数据流
                            channels = s1.getnchannels(),
                            rate = s1.getframerate(),
                            output = True)
        while self.is_on:
            data = s1.readframes(CHUNK) #按帧读取数据
            if data == "":
                break
            stream.write(data) #将帧写入数据流，播放

        stream.stop_stream() #停止数据流
        stream.close() #关闭数据流
        s2.terminate() #关闭Pyaudio   



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QtTest()
    win.show()
    sys.exit(app.exec_()) 