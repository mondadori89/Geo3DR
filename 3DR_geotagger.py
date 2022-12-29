import os

with open('logs/raw.log') as rawlog_file:
    log_lines = rawlog_file.readlines()

output_folder = 'logs'


# Colocar o número da primeira  imagem ex:   DSC00013.JPG -> 13   DSC00135.JPG -> 135
image_number = 13
# Colocar o altitude média do voo em relação ao mar
flight_altitude = 1200


cam_messages = ['EPSG:4326\n']

for i in range(len(log_lines)) :

    if log_lines[i].startswith('CAM, '):
        try:
            cam_data = log_lines[i].split(', ')
            cam_data2 = log_lines[i+1].split(', ')
            cam_lat = float(cam_data[4])
            cam_lat2 = float(cam_data2[4])
            cam_long = float(cam_data[5])
            cam_long2 = float(cam_data2[5])
            cam_alt = float(cam_data[6])
            print(cam_alt)
            cam_alt_mean = flight_altitude
        except:
            print(cam_lat2)

        if cam_lat != cam_lat2 and cam_long != cam_long2 and (cam_alt_mean - cam_alt) < 50: 
            image_name = "DSC0{:04d}.JPG".format(image_number)

            new_cam_line = f'{image_name}	{cam_long}	{cam_lat}	{cam_alt}\n'
            cam_messages.append(new_cam_line)

            image_number = image_number + 1


with open('logs/geo.txt', 'w') as cam_file:
    cam_file.writelines(cam_messages) 


