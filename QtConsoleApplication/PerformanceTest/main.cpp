#include <QtCore/QCoreApplication>
#include "File.h"
#include <QString>
#include <QTextCodec>

int main(int argc, char *argv[])
{
	QCoreApplication a(argc, argv);

	QTextCodec *codec = QTextCodec::codecForName("UTF-8");
	QTextCodec::setCodecForLocale(codec);

	std::string filepath = "D:\\WorkSpace\\1w\\";

	std::vector<std::string> vec = GetFiles(filepath);

	QString url = "http://192.168.10.240:10020/face_camera";

	BaseAPI api;

	std::vector<std::string>::const_iterator it = vec.begin();
	for (it; it != vec.end(); it++)
	{
		std::string fullname = filepath + (*it).c_str();
		QString str = fullname.c_str();
		api.post(url,str);
	}
	return a.exec();
}
