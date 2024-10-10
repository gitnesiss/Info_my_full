[На главную страницу](../../README.md)

[На страницу выбор протоколов](../README.md)

---






[алекс экзе](https://alex-exe.ru/radio/cleverhome/ptz-camera-control/)

```
unsigned char ptz_camera_adress;	//	адрес камеры

//	отправка данных по линии Rs-485
//	input: *data - указатель на массив отправляемых данных
void ptz_camera_send_data(char *data)
{
	rs485_mode_send_data();
	while (*data) 
	{
		send_uart(*data);
		++data;
	}
	rs485_mode_received_data();
}

//	отправка посылки PTZ камерам
//	input: adress - адрес камеры, cmd1 и cmd2 - каманда 1 и 2, data1 и data2 - данные 1 и 2
void ptz_camera_data_send(unsigned char adress,unsigned char cmd1,unsigned char cmd2,unsigned char data1,unsigned char data2)
{
	char ptz_camera_txBuff[7];
	ptz_camera_txBuff[0]=0xFF;
	ptz_camera_txBuff[1]=ptz_camera_adress;
	ptz_camera_txBuff[2]=cmd1;
	ptz_camera_txBuff[3]=cmd2;
	ptz_camera_txBuff[4]=data1;
	ptz_camera_txBuff[5]=data2;
	ptz_camera_txBuff[6]=ptz_camera_adress+cmd1+cmd2+data1+data2;
	ptz_camera_send_data(ptz_camera_txBuff);
}

//	камера вкл
void ptz_camera_on(void)
{
	ptz_camera_data_send(ptz_camera_adress,0x88,0x00,0x00,0x00);
}

//	камера выкл
void ptz_camera_off(void)
{
	ptz_camera_data_send(ptz_camera_adress,0x08,0x00,0x00,0x00);
}
```

[amperka](http://mypractic-forum.ru/viewtopic.php?t=44)

https://alex-exe.ru/tag/rs-485/

https://forum.amperka.ru/threads/%D0%9F%D0%BE%D0%BC%D0%BE%D0%B3%D0%B8%D1%82%D0%B5-%D1%81-%D0%B4%D0%B5%D0%BA%D0%BE%D0%B4%D0%B5%D1%80%D0%BE%D0%BC-pelco-d-%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4.11485/

https://habr.com/ru/articles/783352/

https://umnyjdomik.ru/protokol-pelco-d.html

https://alex-exe.ru/radio/cleverhome/ptz-camera-control/

https://lab85.ru/index.php/laboratoriya-stati/57-pelco-d-terminal

https://lab85.ru/index.php/laboratoriya-stati/37-terminal-dlya-raboty-s-com-portom-pod-windows





---

[В начало документа Языки программирования](#языки-программирования)

[На страницу выбор языков программирования](../README.md)

[На главную страницу](../../README.md)