import csv


def main ():
    coordinate_time = 0.0
    internal_time = 0.0
    simulated_time_delta = 60

    for i in range(1,1441):
        internal_time += simulated_time_delta
        height_and_veloicty = read_height_and_velocity(i)
        delta_time = do_maths(height_and_veloicty, simulated_time_delta)
        coordinate_time += delta_time
        write_result(coordinate_time)

def write_result(coordinate_time):
    try: 
        with open('coord_time.csv', 'a', newline='') as result:
            writer = csv.writer(result)
            data = [str('%.10f' % coordinate_time)]
            writer.writerow(data)
            
    finally: 
        result.close() 


def read_height_and_velocity(current_line):
    try: 
        with open('h_data.csv') as height_data:
            reader = csv.reader(height_data)
            height = list(reader)[current_line]
            height_data.close()

        with open('v_data.csv') as velocity_data:
            reader = csv.reader(velocity_data)
            velocity = list(reader)[current_line]
            velocity_data.close()

        height = float(height[0])
        velocity = float(velocity[0])
        return(height,velocity)
    
    except: 
        return None

def do_maths(h_v_tupel, delta_time): 
    (height, velocity) = h_v_tupel
    c = 299_792_458 #m/s
    G = 6.67408 * pow(10,-11) #m^3 / (kg*s^2)
    M = 5.9722 *pow (10,24) #kg
    R = 6_371_000 #m
    L = 6.969290134 * pow(10,-10)

    gravitational_discrepancy = (G*M)/((height+R)*c**2)
    motion_discrepancy = (velocity**2)/(2*c**2)

    coordinate_time_delta = (1 - L + gravitational_discrepancy + motion_discrepancy)*delta_time
    coordinate_time_delta = round(coordinate_time_delta, 10)

    return (coordinate_time_delta)

main()
