from PyQt5 import QtCore, QtGui, QtWidgets
import PyPDF2
from PyQt5.QtWidgets import QLabel, QPushButton, QFileDialog,QVBoxLayout,QDialog, QLineEdit
import os
import sys
import keyring
from xhtml2pdf import pisa



class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        icon = QtGui.QIcon("icon.png")
        self.setWindowIcon(icon)
        self.setFixedSize(300, 150) 

        self.layout = QVBoxLayout()

        self.password_label = QLabel("Enter System Password:")
        self.password_label.setStyleSheet("")
        self.layout.addWidget(self.password_label)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.password_input)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.check_password)
        self.layout.addWidget(self.login_button)

        self.setLayout(self.layout)

    def check_password(self):
        entered_password = self.password_input.text()
        system_password = keyring.get_password("system", "user")  # Retrieve system password from keyring
        if entered_password == system_password:
            self.accept()
        else:
            self.password_input.clear()
            self.password_label.setText("Incorrect Password. Try again.")


class Ui_Bfinder(object):
    def setupUi(self, Bfinder):

        self.login_dialog = LoginDialog()
        if self.login_dialog.exec_() != QDialog.Accepted:
            sys.exit()

        Bfinder.setObjectName("Bfinder")
        Bfinder.resize(868, 586)
        Bfinder.setStyleSheet("\n"
        "background: rgb(119, 118, 123);")


        self.centralwidget = QtWidgets.QWidget(Bfinder)
        self.centralwidget.setObjectName("centralwidget")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 91, 61))
        self.label.setText("")
        self.label.setObjectName("label")


        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 20, 91, 81))
        self.label_2.setStyleSheet("background:transparent;")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setObjectName("label_2")


    
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 10, 231, 541))
        self.graphicsView.setStyleSheet("background: rgb(94, 92, 100);\n"
        "border-radius: 12px;\n"
        "border: 2px solid #00bf63;")
        self.graphicsView.setObjectName("graphicsView")


        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 120, 211, 71))
        self.widget.setStyleSheet("background:transparent;\n"
        "cursor:pointer;")
        self.widget.setObjectName("widget")


        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 141, 31))
        self.label_3.setStyleSheet("font: 81 11pt \"Cantarell\";\n"
        "font:bold;\n"
        "color: white;\n"
        "background:transparent;\n"
        "")
        self.label_3.setObjectName("label_3")
        self.label_3.mousePressEvent = self.change_password_dialog

        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(150, 30, 31, 31))
        self.label_4.setStyleSheet("background:transparent;")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("change.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        

        #Browser Button
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(740, 480, 101, 41))
        self.pushButton.setStyleSheet("\n"
        "font: 81 11pt \"Cantarell\";\n"
        "font:bold;\n"
        "color:white;\n"
        "border-radius:8px;\n"
        "background:#00bf63;\n"
        "")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.browse_directory)


        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(270, 340, 451, 211))
        self.scrollArea.setStyleSheet("background:rgb(94, 92, 100);\n"
        "color:white;\n"
        "border: 1px solid #00bf63;\n"
        "")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")


        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setLayout(QtWidgets.QVBoxLayout()) 
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 449, 209))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")


        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(360, 300, 261, 27))
        self.lineEdit.setStyleSheet("border:none;\n"
        "font: 81 11pt \"Cantarell\";\n"
        "font:bold;\n"
        "color: white;\n"
        "background:transparent;")
        self.lineEdit.setObjectName("lineEdit")


        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 480, 101, 41))
        self.pushButton_2.setStyleSheet("\n"
        "font: 81 11pt \"Cantarell\";\n"
        "font:bold;\n"
        "color:white;\n"
        "border-radius:8px;\n"
        "background:#00bf63;\n"
        "")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.print_report)

        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setGeometry(QtCore.QRect(270, 80, 451, 211))
        self.scrollArea_2.setStyleSheet("background:rgb(94, 92, 100);\n"
        "color:white;\n"
        "border: 1px solid #00bf63;\n"
        "box-shadow:0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);\n"
        "shadow-color:white;\n"
        "")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        

        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 449, 209))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")


        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        
        # Display security tips in scrollArea_2
        self.display_security_tips()
        
        
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(400, 40, 181, 27))
        self.lineEdit_2.setStyleSheet("border:none;\n"
        "font: 81 11pt \"Cantarell\";\n"
        "font:bold;\n"
        "color: white;\n"
        "background:transparent;")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(50, 200, 211, 71))
        self.widget_2.setStyleSheet("background:transparent;\n"
        "cursor:pointer;")
        self.widget_2.setObjectName("widget_2")


        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(20, 30, 141, 31))
        self.label_5.setStyleSheet("font: 81 11pt \"Cantarell\";\n"
        "font:bold;\n"
        "color: white;\n"
        "background:transparent;\n"
        "")
        self.label_5.setObjectName("label_5")
        self.label_5.mousePressEvent = self.show_usage_instructions


        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(150, 30, 31, 31))
        self.label_6.setStyleSheet("background:transparent;")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("doc.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")


        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(40, 280, 211, 71))
        self.widget_3.setStyleSheet("background:transparent;\n"
        "cursor:pointer;")
        self.widget_3.setObjectName("widget_3")


        self.label_7 = QtWidgets.QLabel(self.widget_3)
        self.label_7.setGeometry(QtCore.QRect(30, 30, 141, 31))
        self.label_7.setStyleSheet("font: 81 11pt \"Cantarell\";\n"
        "font:bold;\n"
        "color: white;\n"
        "background:transparent;\n"
        "")
        self.label_7.setObjectName("label_7")
        self.label_7.mousePressEvent = self.show_contact_information

        self.label_8 = QtWidgets.QLabel(self.widget_3)
        self.label_8.setGeometry(QtCore.QRect(160, 30, 31, 31))
        self.label_8.setStyleSheet("background:transparent;")
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("con.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")


        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(330, -160, 631, 601))
        self.label_9.setStyleSheet("background:none;")
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("ba.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")


        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(590, 110, 631, 601))
        self.label_10.setStyleSheet("background:none;")
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("ba.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")


        self.label_10.raise_()
        self.label_9.raise_()
        self.label.raise_()
        self.graphicsView.raise_()
        self.widget.raise_()
        self.pushButton.raise_()
        self.scrollArea.raise_()
        self.lineEdit.raise_()
        self.pushButton_2.raise_()
        self.scrollArea_2.raise_()
        self.lineEdit_2.raise_()
        self.widget_2.raise_()
        self.widget_3.raise_()
        self.label_2.raise_()
        Bfinder.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Bfinder)
        self.statusbar.setObjectName("statusbar")
        Bfinder.setStatusBar(self.statusbar)
        
        self.retranslateUi(Bfinder)
        QtCore.QMetaObject.connectSlotsByName(Bfinder)

    def retranslateUi(self, Bfinder):
        _translate = QtCore.QCoreApplication.translate
        Bfinder.setWindowTitle(_translate("Bfinder", "Bfinder"))
        self.label_3.setText(_translate("Bfinder", "Change password"))
        self.pushButton.setText(_translate("Bfinder", "Browse"))
        self.lineEdit.setText(_translate("Bfinder", "Potential bugs and vulnabilities found"))
        self.pushButton_2.setText(_translate("Bfinder", "Print Report"))
        self.lineEdit_2.setText(_translate("Bfinder", "Software Security Tips"))
        self.label_5.setText(_translate("Bfinder", "Documentation"))
        self.label_7.setText(_translate("Bfinder", "Contacts"))
    
    def change_password_dialog(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            new_password, ok = QtWidgets.QInputDialog.getText(None, "Change Password", "Enter New Password:", QtWidgets.QLineEdit.Password)
            if ok:
                keyring.set_password("system", "user", new_password)
                QtWidgets.QMessageBox.information(None, "Password Changed", "Password changed successfully.")
    
    
    def show_usage_instructions(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            instructions_text = '''Here are the instructions on how to use the application:\n
            \n1. Click the browser button then allocate where the project directory is\n
            \n2. Repeat for every folder in the directory selected
            \n3. Possible bugs and vulnabilities will shown on the window 
            \n4. Print them and put password as it is on your software'''
            QtWidgets.QMessageBox.information(None, "How to Use", instructions_text)
    def show_contact_information(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            contact_info = "Contact Information:\n\nEmail: example@example.com\nPhone: +1234567890"
            QtWidgets.QMessageBox.information(None, "Contact Information", contact_info)

    def browse_directory(self):
        directory_path = QFileDialog.getExistingDirectory(None, "Select Directory", "", QFileDialog.ShowDirsOnly)
        if directory_path:
            self.bug_report_data = self.scan_directory(directory_path)  # Store bug report data
            self.display_bug_report(self.bug_report_data)  # Display bug report

    from functions.sec_tip import get_random_security_tips
    def display_security_tips(self):
     security_tips = self.get_random_security_tips()  # Get random security tips
     layout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)  # Use QVBoxLayout for the layout
     for tip in security_tips:
        tip_label = QtWidgets.QLabel(tip)
        tip_label.setStyleSheet("font: 11pt \"Cantarell\";\n"
                                "color: white;\n"
                                "background: transparent;\n")
        layout.addWidget(tip_label)


   
          
    def display_bug_report(self, bug_report):
    # Clear previous contents from scroll view
      if not bug_report:
        label = QtWidgets.QLabel("                                          No bugs found! 😊")
        self.scrollAreaWidgetContents.layout().addWidget(label)
      else:
        for i in reversed(range(self.scrollAreaWidgetContents.layout().count())):
            self.scrollAreaWidgetContents.layout().itemAt(i).widget().deleteLater()
        # Add bug report to scroll view
        for idx, bug in enumerate(bug_report, start=1):
            if len(bug) >= 2:
                bug_type, file_path = bug[:2]  # Extract bug_type and file_path
                explanation = bug[2] if len(bug) == 3 else "No explanation available"
                label = QtWidgets.QLabel(f"{idx}. {bug_type}: {explanation}\nFile: {file_path}")
                self.scrollAreaWidgetContents.layout().addWidget(label)
            else:
                print(f"Issue with bug report format: {bug}")


    def scan_directory(self,directory):
        js_files = [file for file in os.listdir(directory) if file.endswith('.js')]
        html_files = [file for file in os.listdir(directory) if file.endswith('.html')]
        bug_report = []

        for js_file in js_files:
            bug_report.extend(self.scan_js_file(os.path.join(directory, js_file)))

        for html_file in html_files:
            bug_report.extend(self.scan_html_file(os.path.join(directory, html_file)))

        return bug_report
    
    def print_report(self):
        if self.bug_report_data:  # Check if bug report data is available
            self.generate_pdf_report(self.bug_report_data)  # Generate and print PDF report
            Report = "\n Report printed Successfully"
            QtWidgets.QMessageBox.information( None, "Report successfully",Report)

            if not self.bug_report_data:
               bad ="\n no report to print"
               QtWidgets.QMessageBox.warning( None, "No report",bad)
        else:
            print("No bug report data available.")

      

            
    #scan files
    from functions.bug_exp import scan_html_file
    from functions.bug_exp import scan_js_file
    from functions.bug_exp import get_bug_explanation
  
  
   

    def generate_pdf_report(self, bug_report):

        directory_path = os.path.dirname(bug_report[0][1]) if bug_report else "Unknown"
        directory_name = os.path.basename(directory_path)
        output_pdf = f"{directory_name}_report.pdf"

        # Create HTML content for the header
        header_html = f"""
         <div style=" display: flex;">
           
            <img src="pro.png" width="100" height="100"/>
         </div>


    
            """

        # Create HTML content for the table
        table_html = """
        <table style="border-collapse: collapse; width: 100% ; border: 1px solid black;     background-image: url('ba.png');
           background-size: cover;">
            <tr style="background-color: grey; color: whitesmoke; text-align: center; font-weight: bold;">
                <th style=" padding:8px;">Bug Type</th>
                <th>File</th>
                <th>Explanation</th>
            </tr>
        """
        for bug_type, file_path in bug_report:

            file_path_words =file_path.split('/')

            truncated_file_path='/'.join(file_path_words[:5])

            if len(file_path_words) > 5:
                truncated_file_path += '/...'
            explanation = self.get_bug_explanation(bug_type)
            
            table_html += f"""
            <tr ">
                <td style=" padding: 8px;">{bug_type}</td>
                <td style=" padding: 8px;">{truncated_file_path}</td>
                <td style=" padding-left: 12px;">{explanation}</td>
            </tr>
            """
        table_html += "</table>"

        # Combine HTML content for header and table
        html_content = f'<div>{header_html}</div><div>{table_html}</div>'

        # Generate PDF from HTML content
        with open(output_pdf, "wb") as pdf_file:
            pisa.CreatePDF(html_content, dest=pdf_file)

        # Encrypt the generated PDF with the system password
        system_password = keyring.get_password("system", "user")
        self.encrypt_pdf(output_pdf, system_password)

    def truncate_text(self, text, max_words):
        words = text.split()
        if len(words) > max_words:
            num_lines = len(words) // max_words + 1
            lines = [" ".join(words[i:i+max_words]) for i in range(0, len(words), max_words)]
            return "<br>".join(lines)
        else:
            return text
    def encrypt_pdf(self, pdf_path, password):
        # Open the existing PDF
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            # Create a new PDF writer object
            pdf_writer = PyPDF2.PdfWriter()
            # Add all pages of the existing PDF to the writer
            for page_num in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page_num])
            # Encrypt the PDF with the provided password
            pdf_writer.encrypt(password)
            # Write the encrypted PDF to a new file
            with open(pdf_path, 'wb') as encrypted_pdf:
                pdf_writer.write(encrypted_pdf)

   #bug explanation


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Bfinder = QtWidgets.QMainWindow()
    ui = Ui_Bfinder()
    ui.setupUi(Bfinder)
    Bfinder.setFixedSize(Bfinder.size())
    icon = QtGui.QIcon("icon.png")
    Bfinder.setWindowIcon(icon)
    Bfinder.show()
    sys.exit(app.exec_())
