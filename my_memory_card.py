from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QButtonGroup, QGroupBox, QRadioButton, QPushButton,QLabel,QVBoxLayout,QHBoxLayout, QMessageBox, QLineEdit
from random import shuffle

class Question():
    def __init__(self, question,o1,o2,o3,o4):
        self.question = question
        self.o1 = o1
        self.o2 = o2
        self.o3 = o3
        self.o4 = o4

app = QApplication([])


my_win = QWidget()
my_win.setWindowTitle("Memory Card")
my_win.move(100,100)
my_win.resize(200,100)
mayn_layot= QVBoxLayout()

a = QLabel()
g1 = QHBoxLayout()

g1.addWidget(a, alignment= Qt.AlignCenter)

a1 = QGroupBox("Варианты ответов")
c = QRadioButton()
c1 = QRadioButton()
c2 = QRadioButton()
c3 = QRadioButton()
qbg = QButtonGroup() 
qbg.addButton(c)
qbg.addButton(c1)
qbg.addButton(c2)
qbg.addButton(c3)

e = QHBoxLayout()
e1 = QVBoxLayout()
e2 = QVBoxLayout()
e1.addWidget(c)
e1.addWidget(c1)
e2.addWidget(c2)
e2.addWidget(c3)
e.addLayout(e1)
e.addLayout(e2)


a1.setLayout(e)
g2 = QHBoxLayout()
g2.addWidget(a1)




ot = QGroupBox("Результаты действия:")
l = QVBoxLayout()
t = QLabel("Прав ты или нет?")
t1 = QLabel("Правельно/Неправельно")
l.addWidget(t)
l.addWidget(t1)
ot.setLayout(l)

ot.hide()




a2 = QPushButton("Ответить")
g3 = QHBoxLayout()

g3.addWidget(a2, stretch = 3)

def otv():
    a1.hide()
    ot.show()
    a.setText("Самый сложный вопрос в мире!")
    a2.setText("Следующий вопрос")
def show_question():
    ot.hide()
    a1.show()
    a2.setText("Ответить")
    qbg.setExclusive(False)    
    c.setChecked(False)
    c1.setChecked(False)
    c2.setChecked(False)
    c3.setChecked(False)
    qbg.setExclusive(True)

ans = [c,c1,c2,c3]






def ask(q):
    shuffle(ans)
    ans[0].setText(q.o1)
    ans[1].setText(q.o2)
    ans[2].setText(q.o3)
    ans[3].setText(q.o4)
    a.setText(q.question)
    show_question()

#que = Question("Что находится в центре Земли?", "Буква м", "Земля", "Ядро", "Россия")





def check_answer():
    if ans[0].isChecked():
        StopAsyncIteration
        show_correct("Правильно!")
    else:
        if ans[1].isChecked() or ans[2].isChecked() or ans[3].isChecked():
            show_correct("Неправильно!")

def show_correct(res):
    t1.setText(res)
    otv()


def start_test():
    if "Ответить" == a2.text():
        otv()
    else:
        show_question()
        
questions_list = []

questions_list.appened(Question("Какой национальности не существует?", "Энци", "Чулымцы", "Смурфы", "Алеуты"))
questions_list.appened(Question("Что находится в центре Земли?", "Буква м", "Земля", "Ядро", "Россия"))
a2.clicked.connect(check_answer)



mayn_layot.addLayout(g1)
mayn_layot.addLayout(g2)
mayn_layot.addWidget(ot)
mayn_layot.addLayout(g3)
my_win.setLayout(mayn_layot)

my_win.show()
app.exec_()