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
    QString m_directory;
    bool m_remove_after_copying = false;

private slots:
    void on_ok_button_clicked();
};

#endif // COPYTOOLHMI_H
