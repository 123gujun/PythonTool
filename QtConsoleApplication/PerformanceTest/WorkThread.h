#pragma once
#include <QThread> 
#include "File.h"
class WorkThread :
	public QThread
{
	Q_OBJECT
public:
	WorkThread();
	 

	//��ȡͼƬ��
	//�����̹߳���
	//�����̴߳���
	//�ر��߳�
	//�����߳�

	void run() override
	{

		//����ҵ��
	}
	~WorkThread();
private:
	BaseAPI baseapi;
};

