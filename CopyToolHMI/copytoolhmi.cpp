#include "copytoolhmi.h"
#include "ui_copytoolhmi.h"

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
