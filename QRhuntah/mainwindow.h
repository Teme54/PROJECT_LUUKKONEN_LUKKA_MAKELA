#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "socketsignal.h"
#include <QtCore>


namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();
    void kep();
    void MyTimer();
    void resetTimer();
    void showConnectionStatus();

private slots:
    void on_pushButton_clicked();
    void keyPressEvent( QKeyEvent * event );
    void keyReleaseEvent(QKeyEvent * event);

    void on_pushButton_2_clicked();

    void on_pushButton_3_clicked();

    void on_pushButton_4_clicked();

    void myTimerSlot();



private:
    int luku = 10;
    const char *CarData;
    Ui::MainWindow *ui;
    SocketSignal stest;
    QTimer *timer;


};

#endif // MAINWINDOW_H
