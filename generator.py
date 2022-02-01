from PIL import Image
import csv

project_name = []


while j < 10000:


	# generate random integer values
  project_name=[]
	import random
	from random import choice

	# prepare a sequence, this example uses same rarity for every attribute, but you can change this up here
	 #Attribute 1
  beasts = [i for i in range(41)]
	beast = choice(beasts)
  
   #Attribute 2
	shirts = [i for i in range(31)]
	shirt = choice(shirts)
  
   #Attribute 3
	hats = [i for i in range(29)]
	hat = choice(hats)

   #Attribute 4
	eyes = [i for i in range(10)]
	eye = choice(eyes)
  
   #Attribute 5
	necklaces = [i for i in range(2)]
	neck = choice(necklaces)

	#you can put rules in here, such as "if cardinal, remove eyepatch" (because the combo didn't look good)
	if eyes == 2:
		if beast == 3:
			eyes = 0


	#combination defines the new pixelbeast
	project_name = [beast,shirt,necklace,hat,eyes]
	

	# check if project_name is unique
	exists = project_name in project_names
	
	if exists:
		#if not unique, skip creating beast. skip adding +1 to j, add +1 to k instead.
		print("DUPLICATE!")
		print(exists)
		k+=1
	else:
		print(project_name)
		project_names.append(project_name)


		#attributes are saved in a img folder using the schema [attribute]#.png
		layer1 = Image.open("img/beast"+str(beast)+".png")
		layer2 = Image.open("img/eye"+str(eyes)+".png")
		layer3 = Image.open("img/shirt"+str(shirt)+".png")
		layer4 = Image.open("img/necklace"+str(necklace)+".png")
		layer5 = Image.open("img/hat"+str(hat)+".png")
		layer6 = Image.open("img/background1.png")


		#set up new image
		final = Image.new("RGBA", layer1.size)
		final = Image.alpha_composite(final, layer1)
		final = Image.alpha_composite(final, layer2)
		final = Image.alpha_composite(final, layer3)
		final = Image.alpha_composite(final, layer4)
		#create name
		if j+1 <10:
			beastnumber = "#000"+str(j+1)
		if j+1 > 9:
			beastnumber = "#00"+str(j+1)
		if j+1 > 99:
			beastnumber = "#0"+str(j+1)
		if j+1 > 999:
			beastnumber = "#"+str(j+1)


		#save a version without background, and then a version with background.

		final2 = Image.alpha_composite(final, layer5).save("nobg/"+beastnumber+".png")
		final3 = Image.alpha_composite(final, layer5)
		final4 = Image.alpha_composite(layer6, final3).save("background/"+beastnumber+".png")



#print results in terminal
print(project_names)
x = len(project_names)
print(x)
print(k)

#print results in csv
out=open("result.csv","w")
output=csv.writer(out)
for row in project_names:
	output.writerow(row)

out.close()
