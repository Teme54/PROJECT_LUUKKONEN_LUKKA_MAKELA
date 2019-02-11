#include "mainwindow.h"
#include <QApplication>
#include <QString>
#include <QDebug>
#include "socketsignal.h"


int main(int argc, char *argv[])
{

   QApplication a(argc, argv);
   MainWindow w;
   w.show();
   w.showConnectionStatus();
   return a.exec();

}
