app=QtGui.QApplication(sys.argv)

Form=QtGui.QWidget()
ui=Ui_Form()
ui.setupUi(Form)
Form.shou()

sys.exit(app.exec_())
