#include "File.h"
#include <QDir>
#include<QStringList>
#include<qDebug>
#include <QBuffer>
#include <QJsonObject>
#include <QJsonDocument>
#include <QJsonArray>


//从当前路径获取文件
std::vector<std::string> GetFiles(std::string & filepath)
{
	QDir dir(filepath.c_str());

	if (! dir.exists())
		qDebug() << "file path is not exist";
	dir.setFilter(QDir::Files | QDir::NoDotAndDotDot | QDir::NoSymLinks);
	QStringList list = dir.entryList();

	QStringList::const_iterator iterator = list.begin();
	std::vector<std::string> vec;
	while (iterator != list.end()) {
		QFileInfo fileInfo(QString(filepath.c_str()) + (*iterator));
		QString suffix = fileInfo.suffix();
		if(suffix == "png" || suffix == "jpg")
		    vec.push_back((*iterator).toLocal8Bit().constData());
		iterator++;
	}
	return vec;
}



//图片文件转utf-8格式的文件
QByteArray Image_To_utf8(QString ImgPath)
{
	QFile file(ImgPath);
	if (!file.open(QIODevice::ReadOnly) || file.size() == 0)
	{
		file.close();
		return NULL;
	}
	QByteArray fdata = file.readAll();
	if (fdata.isEmpty()) {
		return NULL;
	}
	file.close();
    
	return fdata.toBase64();
}


BaseAPI::BaseAPI()
{
	httpRequest.setRawHeader("Content-Type", "application/json");
	httpRequest.setRawHeader("Accept-Encoding", "gzip, deflate");
	httpRequest.setRawHeader("Accept", "*/*");

	QObject::connect(&networkAccessManager, SIGNAL(finished(QNetworkReply*)), this, SLOT(serviceRequestFinished(QNetworkReply*)));
}

BaseAPI::~BaseAPI()
{
	networkAccessManager.disconnect();
	if (settings) {
		delete settings;
		settings = nullptr;
	}
}

void BaseAPI::get(const QString url)
{
	httpRequest.setUrl(QUrl(url));
	networkAccessManager.get(httpRequest);
}

void BaseAPI::post(const QString url, const QByteArray &data)
{
	httpRequest.setUrl(QUrl(url));
	networkAccessManager.post(httpRequest, data);
}
void BaseAPI::post(const QString url, QString &filename)
{
	QString imageStr = Image_To_utf8(filename);

	QByteArray tmp  = Image_To_utf8(filename);
	QJsonValue value(imageStr);

	QJsonArray arr;
	arr.append(value);

	QJsonDocument  doc;
	doc.setArray(arr);
	QByteArray bte = doc.toJson(QJsonDocument::Compact);

	httpRequest.setUrl(url);

	QByteArray  array("{\"time\":1516002690,\"cid\":\"290200001263\",\"faces\":");

	array.append(QString(bte.data()) + "," + "\"image\":\"" + tmp.data() + "\"}");

	//qDebug() << "===== " <<array.data();	


	httpRequest.setHeader(QNetworkRequest::ContentTypeHeader, QVariant("application/json"));

	
	networkAccessManager.post(httpRequest,array);
}

void BaseAPI::serviceRequestFinished(QNetworkReply *reply)
{
	QString str  = reply->attribute(QNetworkRequest::HttpReasonPhraseAttribute).toString();

	std::cout << "BaseAPI...serviceRequestFinished...statusCode:" << str.toStdString().c_str() << std::endl;

	if (reply->error() == QNetworkReply::NoError) {
		requestFinished(reply, reply->readAll(), 0);
	}
	else {
		requestFinished(reply, "", 0);
	}

	// At the end of that slot, we won't need it anymore
	reply->deleteLater();
}

void BaseAPI::requestFinished(QNetworkReply *reply, const QByteArray data, const int statusCode)
{

	std::cout << "网络连上了 = " << data.toStdString().c_str()<<std::endl;
}