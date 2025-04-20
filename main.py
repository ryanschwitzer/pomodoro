#Pomodoro Timer

from plyer import notification
from win10toast import ToastNotifier
import time


#$#@#$%%#U*%(#$@&*%@#(*Y%Y*@(BJFKDBHJKFDSHBUJKFHSOPIFDFDSFaf%#$(*))$@*()($*)@(#)))


def launch():
    #Create starting point for application
    while True:
        start = input('Would you like to start?: ').upper().strip()

        if (start == 'Y'):
            gather_inputs()
            break
        elif (start == 'N'):
            while True:
                end = input('Would you like to quit application?: ')

                if end == 'Y':
                    exit()
                    break
                elif end == 'N':
                    launch()
                    break
                else:
                    print('Invalid Input: Please use (Y/N)')
        else:
            print('Invalid Input: Please use (Y/N)\n')



def gather_inputs():
    print('\nYou will now select variables for application\n')

    while True:
        x = int(input('How many minutes would you like to work?: ').strip())

        y = int(input('\nHow many minutes would you like your breaks to be?: ').strip())

        z = int(input('\nHow many cycles would you like this to last?: ').strip())
    
        main(x, y, z)
        break



def main(work_minutes, break_minutes, cycles):
    print('Session Starts Now!')

    for i in range(cycles):
        print(f'Work session {i + 1} starts')
        notification_get(f'Work Session {i + 1} Starting', f'You will work for {work_minutes} minutes')
        time.sleep(work_minutes * 60)
        
        print(f'Break session {i + 1} starts')
        notification_get(f'Break Session {i + 1} Starting', f'You will have a break for {break_minutes} minutes')
        time.sleep(break_minutes * 60)

    print('Pomodoro Complete')
    notification_get('Complete!', 'You have successfully compelted the Pomodoro Session!')



def notification_get(title, message):
    notification.notify(
        title=title, 
        message=message,
        timeout=15
    )



if __name__ == "__main__":
    launch()