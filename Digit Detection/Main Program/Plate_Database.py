import pandas as pd
import numpy as np

main('\Test_car_images_dataset\VHK1164.jpg')
users = []
plates = []
result = licPlate.strChars


new_user = input('please enter the name of the new user: ')
new_plate = input('please enter the new license plate with capital letters: ')
users = np.append(users, new_user)
plates = np.append(plates, new_plate)

user_data = {'User': users, 'Plate': plates}
user_df = pd.DataFrame(data = user_data)	

for plate in user_df.Plate.unique():
	if plate == result:
		print('Welcome')
		break
	else:
		print('No matches found')

    
