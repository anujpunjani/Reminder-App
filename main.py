from time import sleep
from plyer import notification
import schedule
from pyfiglet import figlet_format
from termcolor import colored

header = figlet_format("Python Reminds!")
header = colored(header, color="green")
# color not showing in some computers
print(header)


class Event:
    appIcon = "reminders.ico"
    appName = "Python"
    Timeout = 5
    quitTime = ""

    def __init__(self, title, message, time, remindEveryday):
        self.title = title
        self.message = message
        if remindEveryday in ("yes", 'y'):
            self._specificTimeScheduler(time, self._everydayNotifier)
        else:
            self._specificTimeScheduler(time, self._notifier)
        Event.quitTime = time

    def _notifier(self):
        notification.notify(
            title=self.title,
            message=self.message,
            timeout=Event.Timeout,
            app_icon=Event.appIcon,
            app_name=Event.appName
        )
        return schedule.CancelJob

    def _specificTimeScheduler(self, time, task):
        schedule.every().day.at(f"{time}").do(task)

    def _everyHourScheduler(self, task):
        schedule.every().hour.do(task)

    def _everydayNotifier(self):
        notification.notify(
            title=self.title,
            message=self.message,
            timeout=Event.Timeout,
            app_icon=Event.appIcon,
            app_name=Event.appName
        )


def Main():
    remindMe = True
    while remindMe:
        try:
            title = input("\nTitle of your reminder: ")
            descripton = input("Description of your reminder: ")
            time = input(
                "Time of your reminder(24 hour format, Eg. 13:10 (HH:MM(:SS)): ")

            remindEveryday = input("Schdule everyday (y/n): ")

            Event(title, descripton, time, remindEveryday)

        except schedule.ScheduleValueError as err:
            print("\nError: Invalid time format (valid format is HH:MM(:SS)?)\n")
            # print("Error: ", err)
            break

        remindMeMore = input("\nWant to Schedule more(y, n): ")
        if remindMeMore != 'y':
            remindMe = False
            print("\nBye! I will look after your reminders.")
            print("Program will automatically close after all reminders are done.")

    while True:
        schedule.run_pending()
        if not schedule.jobs:
            break
        sleep(1)

    print("\nI'm done, have a nice day ahead!\n")


if __name__ == '__main__':
    Main()
