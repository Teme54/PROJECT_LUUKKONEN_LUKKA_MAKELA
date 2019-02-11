#include "socketsignal.h"
#include <QMainWindow>


SocketSignal::SocketSignal(QWidget *parent) : QMainWindow(parent)
{
    socket = new QTcpSocket(this);

    connect(socket, SIGNAL(connected()),this, SLOT(connected()));
    connect(socket, SIGNAL(disconnected()),this, SLOT(disconnected()));
    connect(socket, SIGNAL(readyRead()),this, SLOT(readyRead()));
    connect(socket, SIGNAL(bytesWritten(qint64)),this, SLOT(bytesWritten(qint64)));


    qDebug() << "ob created";
}
SocketSignal::~SocketSignal()
{
    delete socket;
    socket = nullptr;
    qDebug() << "10: Socket Deleted";
}
void SocketSignal::ConnectToServer()
{

    qDebug() << "Connecting....";
    socket->connectToHost("192.168.1.101", 5560);
    if(!socket->waitForConnected(2000))
    {
    qDebug() << "Error: " << socket->errorString();
    //socket->deleteLater();
    //exit(0);
    return;
    }
    qDebug() << "Connected";
}
void SocketSignal::connected(QByteArray msg)
{
    if(msg == "KILL") socket->write(msg);
    else if (msg == "EXIT") socket->write(msg);
    else socket->write("REPEAT " + msg);     // "HEAD / HTTP/1.0\r\n\r\n\r\n!"
}
void SocketSignal::disconnected()
{
    qDebug() << "Disconnected " << checkConnection();

}
void SocketSignal::bytesWritten(qint64 bytes)
{
    qDebug() << "Written: " << bytes;

}
void SocketSignal::readyRead()
{
    qDebug() << "Reading....";
    qDebug() << socket->readAll();

}
bool SocketSignal::checkConnection()
{
     bool connected = (socket->state() == QTcpSocket::ConnectedState);
     return connected;
}
