#include "copytoolhmi.h"
#include "ui_copytoolhmi.h"
#include <QMessageBox>
#include <iostream>

CopyToolHMI::CopyToolHMI(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::CopyToolHMI)
{
    ui->setupUi(this);
}

CopyToolHMI::~CopyToolHMI()
{
    delete ui;
}

void CopyToolHMI::on_ok_button_clicked()
{
    m_directory = ui->fieldDirectory->text();
    m_remove_after_copying = ui->checkBoxRemove->isChecked();

    std::cout << "m_directo" << std::endl;
    std::cout << m_remove_after_copying << std::endl;
}
