#include "myserver.h"

MyServer::MyServer(QObject *parent) : QObject(parent)
{
        server = new QTcpServer(this);
        connect(server, SIGNAL(newConnection()), this, SLOT(newClientConnection()));
        if(!server->listen(QHostAddress::LocalHost, 5000))
        {
            qDebug() << "Server could not start";
        }
        else
        {
            qDebug() << "Server started!";
            qDebug() << "Server listening incoming connections";
        }
}
MyServer::~MyServer()
{
    qDebug() << "Close server and Delete Server Object";
    server->close();
    delete server;
    server = nullptr;
}
void MyServer::readyReadDataFromClient()
{
    // get the information
    QByteArray dataFromClient;
    dataFromClient = socket->readAll();
    // will write on server side window
    qDebug() << "Data from Client: " << dataFromClient;
    socket->write("Message OK\r\n");
}
void MyServer::clientDisconnect()
{
    qDebug() << "Client Disconnect";
}
void MyServer::newClientConnection()
{
    qDebug() << "Client connected";
    // Call nextPendingConnection() to accept the pending connection as a connected QTcpSocket.
    socket = server->nextPendingConnection();
    connect(socket, SIGNAL(readyRead()), this, SLOT(readyReadDataFromClient()));
    connect(socket, SIGNAL(disconnected()), this, SLOT(clientDisconnect()));
    socket->write("Welcome Client\r\n");
}
