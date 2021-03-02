import json
import requests

my_file =open("saral_request.json","r")
data = json.load(my_file)
for course in data:
    print(course)
courses=[]
for course in range(len(data["availableCourses"])):
    print(course+1,":-", data["availableCourses"][course]['name'],data["availableCourses"][course]['id'])
    courses.append(data["availableCourses"][course]['id'])
id=int(input("Select any course:- "))
parent_name=open("parent_file.json")
parent_data=json.load(parent_name)
parent_index=[]
for parents in range(len(parent_data['data'])):
    print(parents+1,":-", parent_data['data'][parents]['name'], parent_data['data'][parents]['parent_exercise_id'])
    parent_index.append(parent_data['data'][parents]['parent_exercise_id'])
    if 'childExercises' in parent_data['data'][parents]:
        for child in range(len(parent_data['data'][parents]['childExercises'])):
            print("         ",child,":-", parent_data['data'][parents]['childExercises'][child]['name'],parent_data['data'][parents]['childExercises'][child]['id'])
id1=int(input("Select any parents for knowing its child :- "))
child_index=[]
for parents in parent_data['data']:
    if parents['id']==parent_index[id1-1]:
        print(parents['name'])
        for child in range(len(parents['childExercises'])):
            print("         ",child+1,":-", parents['childExercises'][child]['id'], parents['childExercises'][child]['name'])
            child_index.append(parents['childExercises'][child]['id'])
            # id3=int(input("choose id for getting slug"))
#         slugs=[] 
#         for i in range(len(parents['childExercises'])):
# slug_name=open("slug_file.json")
# slug_data=json.load(slug_name)
# slug_data.read()
# print(slug_data)
# slug_name=open("slug_file.json")
# slug_name.read()
# slug_data=json.load(slug_name)
# print(slug_name)
# slug_name.close()
#         slugs.append(slug_data['content'])
#         print(slugs)
#         id3=int(input("choose id for getting slug"))
#         slug=slugs[id3-1]
#         print(slugs)
#         k=id3-1
#         while i <= len(slugs):
#             pre_next=input("what next contant you want (p/n)")
#             if pre_next=="p":
#                 k=k-1
#                 if k==0:
#                     print("last page")
#                     break
#                 else:
#                     print(k)
#                     print(slugs[k])
#                     continue
#             elif pre_next=="n":
#                 k=k+1
#                 if k==len(slugs)+1:
#                     print("last page")
#                     break
#                 else:
#                     print(k)
#                     print(slugs[id3])
#                     continue
#             else:
#                 print("write properly")
#                 continue          
#             i+=1