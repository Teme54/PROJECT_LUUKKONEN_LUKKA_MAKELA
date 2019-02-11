#ifndef SOCKETSIGNAL_H
#define SOCKETSIGNAL_H

#include <QObject>
#include <QTcpSocket>
#include <QDebug>
#include <QAbstractSocket>
#include <QWidget>
#include <QMainWindow>
#include "ui_mainwindow.h"


class SocketSignal : public QMainWindow
{
    Q_OBJECT
public:
    explicit SocketSignal(QWidget *parent = nullptr);
    ~SocketSignal();
    void ConnectToServer();


signals:
    void finished();


public slots:
    void connected(QByteArray msg);
    void disconnected();
    void bytesWritten(qint64);
    void readyRead();
    bool checkConnection();

private:
    QTcpSocket *socket;



};

#endif // SOCKETSIGNAL_H
