#include "copytoolhmi.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    CopyToolHMI w;
    w.show();

    return a.exec();
}
