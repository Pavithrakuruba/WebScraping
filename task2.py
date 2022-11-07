# from unicodedata import name
# from bs4 import BeautifulSoup
# import requests
# import json
# import pprint

# a=open("first_task.json","r")
# data=a.read()
# print(movie)
# def movie_year():
    # year=[]
    # movie_dict={}
    # for i in years:
    #     years=["year_of_release"]
    #     if year not in i:
    #         movie_dict.update(year)
    #         for j in movie:
    #             if movie not in j:
    #                 year.append(movie)
    #                 print()

# a=open("first_task.json","r")
# movies=a.read()
# # print(b)
# with open("first_task.json","r")as f:
#     c=json.loads(movies)
#     # print(c)
#     years=[]
#     for i in c:
#         # print(i)
#         year=i["year_of_release"]
#         if year not in years:
#             years.append(year)
#             print(years)
    # b={i:[] for i in years}
    # for j in c:
    #     year=i["year_of_release"]
    #     for x in b:
    #         if str(x)==str(year):
    #             b[x].append(j)
                    
    # print(b)

            
            

    # print(years)
        # years.sort()
    # if i["year_of_release"]==movies:
    #     print(movies)
    # movie_dict={}
    # for j in movies:
        # print(movies)


    #     movie_list=[]
    #     for k in data:
    #         # movie_list=[]
    #         if k["year"]==j:
    #             movie_list.append(k)
    #     movie_dict.update({j:movie_list})
    #     pprint.pprint(movie_dict)
    # return movie_dict
        
    
# f=open('task2.json', 'w')
# f.write(json.dumps(i,indent=4))
# f.close()

        # year_list=[]
        # if year not in years:
        #     year_list.append(year)
        #     print(year_list)

# f=open('task2.json', 'w')
# f.write(json.dumps(d,indent=4))
# f.close()

import json


f=open("first_task.json","r")
r=f.read()
movie=json.loads(r)
# print(movie)

def group_by_year():
    year_list=[]
    dict={}
    for i in movie:
        year=i["year_of_release"]
        # print(year)
        movie2=[]
        if year not in year_list:
            year_list.append(year)
            # print(year_list)
            for j in movie:
                if j["year_of_release"]==year:
                    movie2.append(j)
                    # print(movie2)
                else:
                    pass
            dict[year]=movie2
    # print(dict)
    return dict

movie3=group_by_year()

with open ("task2.json","w") as f:
    a=json.dump(movie3,f,indent=4)

