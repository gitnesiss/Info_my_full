[На главную страницу](../../README.md)

[В начало раздела микроэлектроники и одноплатных компьютеров](../README.md)

---

# Всё про RaspberryPi

# Содержание

- [Плата RaspberryPi]()

- [Подключение к RaspberryPi по SSH](#подключение-к-raspberry-по-ssh)

- [Библиотека для работы с GPIO](#библиотека-для-работы-с-gpio)

### Подключение к Raspberry по SSH

Чтобы работать с RaspberryPi по протоколу SSH (Secure Shell) нужно настроить это соединение. Как это сделать можно почитать по этим ссылкам:
1. [Microtechnics](https://microtechnics.ru/podklyuchenie-k-raspberry-pi-po-ssh/).
2. [MyRaspberry](https://myraspberry.ru/nastroit-ssh-na-raspberry-pi-%E2%80%94-eto-legko.html)
3. [Amperka](http://wiki.amperka.ru/rpi:installation:ssh#:~:text=%D0%9F%D0%BE%D0%B4%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%BF%D0%BE%20SSH%20%D0%BA%20%D0%BA%D0%BE%D0%BD%D1%81%D0%BE%D0%BB%D0%B8%20Raspberry%20Pi,-Raspberry%20Pi%20%D0%B7%D0%B0%D0%BF%D1%83%D1%89%D0%B5%D0%BD%D0%B0&text=%D0%97%D0%B0%D0%BF%D1%83%D1%81%D1%82%D0%B8%D1%82%D0%B5%20PuTTY.,%D0%BF%D0%BE%D0%BF%D1%80%D0%BE%D1%81%D0%B8%D1%82%20%D0%B2%D0%B2%D0%B5%D1%81%D1%82%D0%B8%20%D0%BB%D0%BE%D0%B3%D0%B8%D0%BD%20%D0%B8%20%D0%BF%D0%B0%D1%80%D0%BE%D0%BB%D1%8C.)

### Библиотека для работы с GPIO

#### PiGPIO

Для того чтобы использовать библиотеку pigpiod в  CPP-коде, нужно знать 2 вещи:

1. В программах CPP добавляется заголовок `<pigpiod_if2.h>`.

2. При компиляции добавьте флаг `-pthread -lrt -lpigpiod_if2` к параметрам компиляции g++, чтобы компилятор нашёл и связал программу с библиотекой pigpiod_if2.

#### WiringPi

Для того, чтобы использовать WiringPi в  CPP-коде, нужно знать 2 вещи:

1. В программах CPP добавляется заголовок `<wiringPi.h>`.

2. При компиляции добавьте флаг `-lwiringPi` к параметрам компиляции g++, чтобы компилятор нашёл и связал программу с библиотекой WiringPi.



#### Основные команды используемые при работе с RaspberryPi:

```
gpio -v       # вывести информацию о том, какой версии установлена библиотека
gpio readall  # вывод текущего состояния всех пинов 
```

При работе в ОС Rasbian есть команда, которая позволяет произвести основные настройки одноплатного компьютера:
```
sudo raspi-config
```

Чтобы посмотреть или произвести настройки RaspberryPi нужно запустить файл `config.txt`:
```
cat /boot/config.txt
```
Редактировать файл нужно с **root** правами.

Более подробно про **config.txt** можно прочитать [тут](https://wikihandbk.com/wiki/Raspberry_Pi:%D0%9D%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0/config.txt). 

Узнать температуру процессора, полученное значение нужно поделить на 1000:
```
cat /sys/class/thermal/thermal_zone0/temp
```
Узнать текущую частоту процессора:
```
cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq
```

Чтобы посмотреть серийный номер RaspberryPi и большую часть информации нужно ввести следующую команду:
```
cat /proc/cpuinfo
```

Выключение или перезагрузка SBC:
```
sudo poweroff

sudo reboot
```

---


[В начало документа](#всё-про-raspberrypi)

[В начало раздела микроэлектроники и одноплатных компьютеров](../README.md)

[На главную страницу](../../README.md)