from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QComboBox
from PyQt5.QtGui import QFont, QIcon
import sys
from config import WND_WIDTH, WND_HEIGHT, SIZE, FNT_SIZE, BORDER_W, ICON, TITLE, HELP, FONT
from converter import WordDocx
from saveload import SaveLoad


class TurtleConvert(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle(TITLE)
        self.setFixedSize(WND_WIDTH, WND_HEIGHT)
        icon: QIcon = QIcon(ICON)
        self.setWindowIcon(icon)
        self.converter: WordDocx = WordDocx()
        
        # Font
        font: QFont = QFont()
        font.setFamily(FONT)
        font.setPointSize(FNT_SIZE)
        
        # Help label
        lbl_border: str = f'border: {BORDER_W}px solid black;'
        hlp_txt: str = SaveLoad.load_file(HELP)
        hlp_pos: tuple[int, int] = 0, 0
        hlp_sizes: tuple[int, int] = SIZE * 25, SIZE * 2
        self.help: QLabel = QLabel(self)
        self.help.setText(hlp_txt)
        self.help.setFont(font)
        self.help.setFixedSize(hlp_sizes[0], hlp_sizes[1])
        self.help.setStyleSheet(lbl_border)
        self.help.move(hlp_pos[0], hlp_pos[1])   
        
        # Options combobox
        self.opts: QComboBox = QComboBox(self)
        self.cb_lst: list[str] = ['pdf to word', 'word to pdf']
        self.default_opt: str = self.cb_lst[0]
        [self.opts.addItem(item) for item in self.cb_lst]
        op_sizes: tuple[int, int] = SIZE * 7, SIZE * 2
        op_pos: tuple[int, int] = 0, hlp_sizes[1]
        self.opts.setFont(font)
        self.opts.setFixedSize(op_sizes[0], op_sizes[1])
        self.opts.move(op_pos[0], op_pos[1])
        
        # Button confirm
        btn1_txt: str = 'Confirm'
        btn1_pos: tuple[int, int] = op_pos[0] + op_sizes[0], op_pos[1]
        btn1_sizes: tuple[int, int] = SIZE * 6, SIZE * 2
        self.btn_conv: QPushButton = QPushButton(self)
        self.btn_conv.setText(btn1_txt)
        self.btn_conv.setFont(font)
        self.btn_conv.setFixedSize(btn1_sizes[0], btn1_sizes[1])
        self.btn_conv.move(btn1_pos[0], btn1_pos[1])
        self.btn_conv.clicked.connect(self.convert)
        
        # Button quit
        btn2_txt: str = 'Quit'
        btn2_pos: tuple[int, int] = btn1_pos[0] + btn1_sizes[0], btn1_pos[1]
        btn2_sizes: tuple[int, int] = WND_WIDTH - btn1_sizes[0] - op_sizes[0], btn1_sizes[1]
        self.btn_quit: QPushButton = QPushButton(self)
        self.btn_quit.setText(btn2_txt)
        self.btn_quit.setFont(font)
        self.btn_quit.setFixedSize(btn2_sizes[0], btn2_sizes[1])
        self.btn_quit.move(btn2_pos[0], btn2_pos[1])
        self.btn_quit.clicked.connect(self.quit)
    
    def convert(self) -> None:
        value: str = self.opts.currentText()
        if value == self.cb_lst[0]:
            self.converter.to_word = True
        else:
            self.converter.to_word = False
        self.converter.convert()
    
    def quit(self) -> None:
        self.destroy()
        QApplication.quit()
    

if __name__ == '__main__':
    app: QApplication = QApplication(sys.argv)
    conv: TurtleConvert = TurtleConvert()
    conv.show()
    sys.exit(app.exec_())
