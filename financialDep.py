''' class to verify schedules and generate workers' salaries '''

from datetime import datetime

def calculateSalary(dataSchedules):

    print('---------------')

    for i in range(len(dataSchedules)):
        
        salary = 0

        #repetitive cycle for calculating daily wages
        for j in range(len(dataSchedules[i]['Schedules'])):
            payHour = 0

            day = dataSchedules[i]['Schedules'][j][0]

            #format timedate
            t1 = dataSchedules[i]['Schedules'][j][1]
            t2 = dataSchedules[i]['Schedules'][j][2]
            t1 = datetime.strptime(t1,'%H:%M')
            t2 = datetime.strptime(t2,'%H:%M')

            #verification of schedules to assign hourly pay.
            if day != 'SA' and day != 'SU':

                if t1 >= datetime.strptime('00:01', '%H:%M') and t2 <= datetime.strptime('09:00', '%H:%M'):
                    payHour = 25
                elif t1 >= datetime.strptime('09:01', '%H:%M') and t2 <= datetime.strptime('18:00', '%H:%M'):
                    payHour = 15
                elif t1 >= datetime.strptime('18:01', '%H:%M') and t2 >= datetime.strptime('00:00', '%H:%M'):
                    payHour = 20

            else:
                
                if t1 >= datetime.strptime('00:01', '%H:%M') and t2 <= datetime.strptime('09:00', '%H:%M'):
                    payHour = 30
                elif t1 >= datetime.strptime('09:01', '%H:%M') and t2 <= datetime.strptime('18:00', '%H:%M'):
                    payHour = 20
                elif t1 >= datetime.strptime('18:01', '%H:%M') and t2 >= datetime.strptime('00:00', '%H:%M'):
                    payHour = 25

            #calculate salary
            time = t2 - t1
            hours = int(time.seconds/3600)
            salary += hours * payHour
        
        print('Worker: '+dataSchedules[i]['Name'])
        print('Schedules: '+str(dataSchedules[i]['Schedules']))
        print('Salary: '+str(salary))
        print('---------------')