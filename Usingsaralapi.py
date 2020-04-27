import requests
import json
variable=requests.get('http://saral.navgurukul.org/api/courses')
var=variable.text
o_file=open('API.json','w')
json.dump(var,o_file)
o_file.close()
r_file=open('API.json','r')
L_data=json.load(r_file)
D_file=json.loads(L_data)
id_list=[]
num=1
for c in D_file:
	for i in D_file[c]:
		for j in i:
			if j=='name':
				print(num,'.',i[j])
				num+=1
			elif j=='id':
				id_list.append(i[j])
				
chose_cource=int(input('  ENTER ANY COURCE     '))
user_id=id_list[chose_cource-1]
variable_for_id=requests.get(f'http://saral.navgurukul.org/api/courses/{user_id}/exercises')
var_id=variable_for_id.text
id_file=open('api.json','w')
json.dump(var_id,id_file)
id_file.close()
id_file2=open('api.json','r')
id_Dta=json.load(id_file2)
id_data=json.loads(id_Dta)
num=1
excersie_list=[]
slug_list=[]
for e in id_data:
	for ex in id_data[e]:
		for exercise in ex:
			if exercise=='name':
				print(num,'.',ex[exercise])
				excersie_list.append(ex[exercise])
				num+=1
			elif exercise=='slug':
				slug_list.append(ex[exercise])
# print(slug_list)
# print(excersie_list)
choose_exercise=int(input(' ENTER EXERCISE YOU WANT TO PRACITICE '))
user_slug=slug_list[choose_exercise-1]
variable_for_slug=requests.get(f'http://saral.navgurukul.org/api/courses/{user_id}/exercise/getBySlug?slug={user_slug}')
var_for_slug=variable_for_slug.text
slug_file=open('slugfile.json','w')
slug_file.write(var_for_slug)
slug_file.close()

slugfile=open('slugfile.json','r')
slug_data=json.load(slugfile)
slugfile.close()
for CONTENT in slug_data:
	if CONTENT=='content':
		print(slug_data[CONTENT])


