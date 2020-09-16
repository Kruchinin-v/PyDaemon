import sys
import time
from custom_thread import MyThread
from time import strftime


class SigFunctionsCon:

    def __init__(self, ourdaemon):
        self.__ourdaemon = ourdaemon

    def SIGTERM(self):
        """
        действия при остановке демона
        :return:
        """
        now_time = strftime("%H:%M", time.localtime())
        sys.stdout.write(f"Остановлен в {now_time}\n")
        sys.exit(0)


class ReactFunctionCon:

    def __init__(self, ourdaemon):
        self.__ourdaemon = ourdaemon

    def start(self):
        self.__ourdaemon.start()

    def stop(self):
        self.__ourdaemon.stop()

    def status(self):
        self.__ourdaemon.status()

    def restart(self):
        self.__ourdaemon.restart()

    def stmess(self, message):
        print(message)
        self.__ourdaemon.start()


class StatCon:
    commands = "{start|stop|status}"
    strHelp = f"usage: {sys.argv[0]} {commands}"

    def time_alignment(self):
        """
        функция выравнивает время до ровной минуты
        :return:
        """
        now_time = strftime("%S", time.localtime())
        while now_time != '59':
            now_time = strftime("%S", time.localtime())
            time.sleep(1)

    def run(self):
        """
        Фукнция, которая выполняется при запуске демона.
        Тут необходимо указать действия, которые вы ожидаете от демона
        """
        now_time = strftime("%H:%M", time.localtime())
        print(f"\nЗапуск pydaemon в {now_time}")
        # время, когда нужно будет запускать скрипт
        time_run = ["10:00", "13:00", "16:00"]
        while True:
            self.time_alignment()
            now_time = strftime("%H:%M", time.localtime())
            if now_time in time_run:  # если сейчас выбранное время
                print(f"Запуск скрипта в {now_time}")
                my_thread = MyThread("/usr/bin/php",
                                     "/home/user/call.php")
                my_thread.start()
            # указать именно 56 секунд(или меньше), чтобы избежать ошибки,
            # когда уже есть несколько секунд и
            # следующая минута будет пропущена. Оставшиеся секунды выровняются
            # функцией time_alignment
            time.sleep(56)

    pidFile = "/var/log/python-daemon/daemon-naprimer.pid"

    inputter = "/dev/null"

    outputter = "/var/log/python-daemon/out-daemon.log"

    errorer = "/var/log/python-daemon/err-daemon.log"

