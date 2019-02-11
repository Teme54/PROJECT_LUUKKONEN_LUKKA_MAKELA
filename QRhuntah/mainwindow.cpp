#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "QMessageBox"
#include <QKeyEvent>
#include <QDebug>
#include <QThread>
#include "socketsignal.h"





MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    qDebug() << "constmain";
    ui->setupUi(this);
    MyTimer();
}

MainWindow::~MainWindow()
{
    qDebug() << "destmain";
    delete ui;
}

void MainWindow::on_pushButton_clicked()
{
    MainWindow::close();
    //stest.connected("CMD");
    //qDebug() << stest.checkConnection();

}
void MainWindow::keyPressEvent( QKeyEvent * event)
{
    QByteArray msg;
    //char key = event->key() == Qt::Key_W;
   //MyTCPSocketClass *objectMyTCPSocketClass;
     //objectMyTCPSocketClass = new MyTCPSocketClass();
    if(stest.checkConnection())
    {

        resetTimer();

        switch(event->key())
        {
        case Qt::Key_W :
            ui->dirLabel->setText("W");
            qDebug() << "W";

            break;
        case Qt::Key_A :
            ui->dirLabel->setText("A");

            qDebug() << "A";
            break;
        case Qt::Key_S :
            ui->dirLabel->setText("S");
            qDebug() << "S";
            break;
        case Qt::Key_D :
            ui->dirLabel->setText("D");
            qDebug() << "D";
            break;
        default : ui->dirLabel->setText("?");
            break;
        }
        msg.setNum(event->key());
        stest.connected(msg);
    }
    else qDebug() << "No connection";

    //objectMyTCPSocketClass->connectToServer(event->key());
    //delete objectMyTCPSocketClass;
    //objectMyTCPSocketClass= nullptr;
}
void MainWindow::keyReleaseEvent(QKeyEvent *event)
{

      // MyTCPSocketClass *objectMyTCPSocketClass;
      // objectMyTCPSocketClass = new MyTCPSocketClass();

       if (event->isAutoRepeat() == false)
       {
           if(timer->isActive())
           {
               qDebug() << "KEEEEEEEEEEEEEEEEEEeeee";
           }
           else timer->start(500);
       }
}

void MainWindow::kep()
{

}

void MainWindow::on_pushButton_2_clicked() //reset button
{
    stest.connected("KILL");
}

void MainWindow::on_pushButton_3_clicked() //connect button
{
    stest.ConnectToServer();
    showConnectionStatus();
}

void MainWindow::on_pushButton_4_clicked() //disconnect button
{
    stest.connected("EXIT"); 
    ui->label_2->setText("Not connected");
}
void MainWindow::MyTimer()
{
    timer = new QTimer(this);
    connect(timer, SIGNAL(timeout()), this, SLOT(myTimerSlot()));
    //timer->start(2000);
}
void MainWindow::myTimerSlot()
{
    timer->stop();
    qDebug() << "stop";
    stest.connected("STOP");

}
void MainWindow::resetTimer()
{
    timer->stop();
    //showConnectionStatus(); //check connection frequently
}
void MainWindow::showConnectionStatus()
{
    if(stest.checkConnection()) ui->label_2->setText("Connected");
    else ui->label_2->setText("Not connected");
}
