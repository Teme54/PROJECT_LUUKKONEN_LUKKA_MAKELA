#ifndef MYSERVER_H
#define MYSERVER_H

#include <QObject>
#include <QTcpSocket>
#include <QTcpServer>
#include <QDebug>

class MyServer : public QObject
{
    Q_OBJECT
public:
    explicit MyServer(QObject *parent = nullptr);
    ~MyServer();

signals:
    void finished();

public slots:
    void newClientConnection();
    void readyReadDataFromClient();
    void clientDisconnect();

private:
    QTcpServer *server;
    QTcpSocket *socket;
};

#endif // MYSERVER_H
