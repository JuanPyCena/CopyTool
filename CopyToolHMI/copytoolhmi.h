#ifndef COPYTOOLHMI_H
#define COPYTOOLHMI_H

#include <QMainWindow>

namespace Ui {
class CopyToolHMI;
}

class CopyToolHMI : public QMainWindow
{
    Q_OBJECT

public:
    explicit CopyToolHMI(QWidget *parent = 0);
    ~CopyToolHMI();

private:
    Ui::CopyToolHMI *ui;
};

#endif // COPYTOOLHMI_H
