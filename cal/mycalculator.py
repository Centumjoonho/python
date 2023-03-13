import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic  # UI를 연결한다

# .ui파일  불러오기
from_class = uic.loadUiType("calculator.ui")[0]
calculator_list = ["+", "-", "÷", "x"]


# 화면의 클래스 선언


class Window(QWidget, from_class):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setupUi(self)
        #
        self.btn_1.clicked.connect(self.btn_1_click)
        self.btn_2.clicked.connect(self.btn_2_click)
        self.btn_3.clicked.connect(self.btn_3_click)
        self.btn_4.clicked.connect(self.btn_4_click)
        self.btn_5.clicked.connect(self.btn_5_click)
        self.btn_6.clicked.connect(self.btn_6_click)
        self.btn_7.clicked.connect(self.btn_7_click)
        self.btn_8.clicked.connect(self.btn_8_click)
        self.btn_9.clicked.connect(self.btn_9_click)
        self.btn_0.clicked.connect(self.btn_0_click)
        #
        self.btn_del.clicked.connect(self.btn_delete_click)
        self.btn_plus.clicked.connect(self.btn_plus_click)
        self.btn_minus.clicked.connect(self.btn_minus_click)
        self.btn_obelus.clicked.connect(self.btn_obelus_click)
        self.btn_times.clicked.connect(self.btn_times_click)
        self.btn_equal.clicked.connect(self.btn_equal_click)
        self.btn_point.clicked.connect(self.btn_point_click)


##########################
###### 클릭 이벤트 ##########
##########################

    def btn_1_click(self):
        self.number("1")

    def btn_2_click(self):
        self.number("2")

    def btn_3_click(self):
        self.number("3")

    def btn_4_click(self):
        self.number("4")

    def btn_5_click(self):
        self.number("5")

    def btn_6_click(self):
        self.number("6")

    def btn_7_click(self):
        self.number("7")

    def btn_8_click(self):
        self.number("8")

    def btn_9_click(self):
        self.number("9")

    def btn_0_click(self):
        self.number("0")


# 삭제


    def btn_delete_click(self):
        self.del_num()
# 사칙연산

    def btn_plus_click(self):
        self.plus()

    def btn_minus_click(self):
        self.minus()

    def btn_times_click(self):
        self.times()

    def btn_obelus_click(self):
        self.obelus()
# 결과

    def btn_equal_click(self):
        self.equal()
# 기호

    def btn_point_click(self):
        self.point()


################################
############ 기능 함수 ###########
###############################

    def number(self, num):
        # display text 값을 가져와서 exist_text 변수에 입력
        exist_text = self.display.toPlainText()
        self.display.setText(exist_text + num)  # 기존값 + 새로운 값

    def del_num(self):
        exist_text = self.display.toPlainText()
        # 문자열 [:-1]은 index 0 ~ 마지막 문자열 전까지
        self.display.setText(exist_text[:-1])


###### 사칙연산 ######


    def plus(self):
        # 사칙연산 마지막 입력 값만 유지 조건문
        exist_text = self.display.toPlainText()
        if exist_text[-1] in calculator_list:
            self.display.setText(exist_text[:-1])
        self.number("+")

    def minus(self):
        exist_text = self.display.toPlainText()
        if exist_text[-1] in calculator_list:
            self.display.setText(exist_text[:-1])
        self.number("-")

    def obelus(self):
        exist_text = self.display.toPlainText()
        if exist_text[-1] in calculator_list:
            self.display.setText(exist_text[:-1])
        self.number("/")

    def times(self):
        exist_text = self.display.toPlainText()
        if exist_text[-1] in calculator_list:
            self.display.setText(exist_text[:-1])
        self.number("*")
##### 결과 #####

    def equal(self):
        exist_text = self.display.toPlainText()

        try:
            # Eval 함수는 문자열 식 값을 산수 하여 int로 반환
            answer = eval(exist_text)
            answer_round = round(answer, 1)
            # setText 에 맞는 형변환
            self.display_result.setText(str(answer_round))
            # display 화면 초기화
            self.display.setText("")

        except Exception as e:
            print("error", e)
##### 기호 ####

    def point(self):
        exist_text = self.display.toPlainText()
        if exist_text[-1] in calculator_list:
            self.display.setText(exist_text[:-1])
        self.number(".")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myCalc = Window()

    sys.exit(app.exec_())
