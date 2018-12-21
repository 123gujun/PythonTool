#pragma once

#include <string>
#include <vector>
#include <iostream>

#include <QSettings>
#include <QNetworkRequest>
#include <QNetworkReply>
#include <QNetworkAccessManager>
#include <QString>
#include <QImage>



std::vector<std::string> GetFiles(std::string & filepath);

QByteArray Image_To_utf8(QString ImgPath);



class BaseAPI :public QObject
{
	Q_OBJECT

public:
	BaseAPI();
	~BaseAPI();
	void get(const QString url);
	void post(const QString url, const QByteArray &data);

	void post(const QString url, QString &filename);

protected:
	virtual void requestFinished(QNetworkReply *reply, const QByteArray data, const int statusCode);

	public slots:
	void serviceRequestFinished(QNetworkReply *reply);

private:
	QNetworkRequest httpRequest;
	QNetworkAccessManager networkAccessManager;
	QSettings *settings;

};

