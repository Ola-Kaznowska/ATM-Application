from alive_progress import alive_bar
from time import sleep



print("Hello.")
sleep(1)




update_windows = input("A new application update for Windows has been found. Would you like to download it? Yes/No: ")


for i in range(2):
     if update_windows == "Yes" or "No":
         print()
         with alive_bar(100) as bar:
             for i in range(100):
                sleep(1)
                bar()