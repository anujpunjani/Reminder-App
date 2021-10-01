import time
from plyer import notification
import schedule

def water():
    print("1")
    notification.notify(
                title="DRINK WATER",
                message="peele bhai healthy hai",
                timeout=2

        )
def breakfast():
    print("2")
    notification.notify(
                title="HAVE YOUR BREAKFAST",
                message="3 eggs , brown bread,coffee",
                timeout=2

        )
def brunch():
    print("3")
    notification.notify(
                title="HAVE YOUR BRUNCH",
                message="bowl of fruits",
                timeout=2

        )
def lunch():
    print("4")
    notification.notify(
                title="HAVE YOUR LUNCH",
                message="roti, sabzi,salad, rice",
                timeout=2

        )
def evening_snacks():
    print("5")
    notification.notify(
                title="HAVE YOUR EVENING SNACKS",
                message="peanut butter bread",
                timeout=2

        )
def gym():
    print("6")
    notification.notify(
                title="GO TO GYM",
                message="its chest day today",
                timeout=2

        )
def dinner():
    print("7")
    notification.notify(
                title="HAVE YOUR DINNER",
                message="chicken breast , egg porch , rice , salad",
                timeout=2

        )
def milk():
    print("8")
    notification.notify(
                title="have your turmeric milk",
                message="peele natak mat kar",
                timeout=2

        )

schedule.every(30).seconds.do(water)        
schedule.every(50).seconds.do(gym)
schedule.every(30).seconds.do(water)        
schedule.every(50).seconds.do(gym)
schedule.every(30).seconds.do(water)        
schedule.every(50).seconds.do(gym)
schedule.every(30).seconds.do(water)        
schedule.every(50).seconds.do(gym)
schedule.every(30).seconds.do(water)        
schedule.every(50).seconds.do(gym)
schedule.every(30).seconds.do(water)        
schedule.every(50).seconds.do(gym)

while True:
    schedule.run_pending()
    time.sleep(1)

    