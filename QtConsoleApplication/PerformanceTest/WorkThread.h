#pragma once
#include <QThread> 
#include "File.h"
class WorkThread :
	public QThread
{
	Q_OBJECT
public:
	WorkThread();
	 

	//获取图片，
	//创建线程管理
	//启动线程处理
	//关闭线程
	//销毁线程

	void run() override
	{

		//处理业务
	}
	~WorkThread();
private:
	BaseAPI baseapi;
};

