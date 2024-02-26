#oppgave A
import csv

def oppgave_a ():
      with open('coord_time.csv') as data:
            reader = csv.reader(data)
            coord_times = list(reader)
            number_of_lines = len(coord_times)
            last_coord_time = float(coord_times[-1][0])
            data.close()
            
            expected_time = 60*number_of_lines
            accumlated_discrepancy = expected_time - last_coord_time

            print(accumlated_discrepancy)

#accumulated discrepancy is = 3.859230491798371e-05 s
#oppgave_a()

#oppgave b

def oppgave_b (): 
    discrepancy_constant = 3 * (10**-9) #s/m
    measured_time_discrepancy = 3.859230491798371e-05 #s
    location_discrepancy = measured_time_discrepancy/discrepancy_constant

    print (location_discrepancy)

#location_discrepancy = 12864.101639327902m 

#oppgave_b()
    
#oppgave c

def oppgave_c (): 
    discrepancy_constant = 3 * (10**-9) #s/m
    number_of_seconds = discrepancy_constant * 500

    print(number_of_seconds)

#number of seconds before 500m discrepancy = 1.5000000000000002e-06
#oppgave_c()

#oppgave d
    
def oppgave_d(): 
     