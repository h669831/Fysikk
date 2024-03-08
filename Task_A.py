import csv


def main():
    outfile = 'coord_time.csv';
    coordinate_time = 0.0
    internal_time = 0
    simulated_time_delta = 60

    write_head(outfile)

    # Loop trough lines in input file.
    for i in range(0, 1440):
        height_and_velocity = read_height_and_velocity(i)  # Retrieve height and velocity from input files.
        delta_time = do_maths(height_and_velocity, simulated_time_delta)  # Calculate coordinate time delta.
        coordinate_time += delta_time  # Add calculated coordinate time delta.
        internal_time += simulated_time_delta  # Add simulated internal time delta.
        write_result(outfile, internal_time, coordinate_time)  # Write result to file.


# Append to output file
def write_result(outfile, internal, coordinate):
    try: 
        with open(outfile, 'a', newline='') as result:
            writer = csv.writer(result)
            data = [str(internal), str(' %.10f' % coordinate)]
            writer.writerow(data)
            
    finally: 
        result.close()


# Append CSV header to outfile
def write_head(outfile):
        try:
            with open(outfile, 'a', newline='') as file:
                writer = csv.writer(file)
                data = ["Internal time (s)", "Coordinate time (s)"]
                writer.writerow(data)
        finally:
            file.close()


# Read values from input file
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
        return height, velocity

    except Exception(BaseException):
        return None

# Perform calculations
def do_maths(h_v_tuple, delta_time):
    (height, velocity) = h_v_tuple  # Extract values form tuple.

    # Constants:
    speed_of_light = 299_792_458  # m/s
    gravitational_constant = 6.67408 * pow(10, -11)  # m^3 / (kg*s^2)
    earth_mass = 5.9722 * pow(10, 24)  # kg
    earth_radius = 6_371_000  # m
    utc_sync_constant = 6.969290134 * pow(10, -10)

    # Calculate gravitational and motion discrepancies.
    gravitational_discrepancy = (gravitational_constant*earth_mass)/((height+earth_radius)*speed_of_light**2)
    motion_discrepancy = (velocity**2)/(2*speed_of_light**2)

    # Calculate coordinate time delta and round to 10 decimal places.
    coordinate_time_delta = (1 - utc_sync_constant + gravitational_discrepancy + motion_discrepancy)*delta_time
    coordinate_time_delta = round(coordinate_time_delta, 11)

    return coordinate_time_delta


# Start script
main()
