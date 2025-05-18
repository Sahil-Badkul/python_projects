import time
from plyer import notification

if __name__ == "__main__":
    while(True):
        notification.notify(
            title = "**Please Drink Water Now!!", 
            message = "Drinking water boosts energy levels, enhances brain function, and supports overall metabolic health",
            app_icon = "C:/Users/Lenovo/Desktop/DSA/Python Project/glassofwater.ico",
            timeout=2
        )
        time.sleep(60*60)

#"c:\Users\Lenovo\Desktop\DSA\Python Project\word_of_a_day_notification.py"