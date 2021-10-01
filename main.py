import time
from plyer import notification
import schedule


class Event:
    appIcon = "reminders.ico"
    Timeout = 5
    quitTime = ""

    def __init__(self, title, message, time):
        self.title = title
        self.message = message
        self._specificTimeScheduler(time, self._notifier)
        Event.quitTime = time

    def _notifier(self):
        notification.notify(
            title=self.title,
            message=self.message,
            timeout=Event.Timeout,
            app_icon=Event.appIcon
        )

    def _specificTimeScheduler(self, time, task):
        schedule.every().day.at(f"{time}").do(task)


remindMe = True
while remindMe:
    try:
        title = input("\nTitle of your reminder: ")
        descripton = input("Description of your reminder: ")
        Time = input(
            "Time of your reminder(24 hour format, Eg. 13:10 (HH:MM(:SS)): ")

        timeValidation = Time.split(':')
        if timeValidation:
            if len(timeValidation) > 3 or len(timeValidation) < 2:
                remindMe = False
                raise schedule.ScheduleValueError("Invalid time format")

    except schedule.ScheduleValueError as err:
        print("Error:", err)
        break

    Event(title, descripton, Time)

    remindMeMore = input("\nWant to Schedule more(y, n): ")
    if remindMeMore != 'y':
        remindMe = False
        print("\nBye! I will look after your reminders.")
        # print("Program will automatically close after all reminders are done.")

while True:
    schedule.run_pending()
    time.sleep(1)
