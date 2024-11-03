import os
from tkinter import END
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager # type: ignore
import time
from bs4 import BeautifulSoup # type: ignore
# Tạo trình điều khiển với ChromeDriverManager
trinh_dieu_khien = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Truy cập vào trang web
from ten import Player
from ten import Player_Manager

quan_ly_nguoi_choi=Player_Manager()

def lay_du_lieu_tu_web(url,id_bang_nguoi_choi,lengthPlayerData,ten_du_lieu):
    resultPlayerData=[]
    trinh_dieu_khien.get(url)
    try:
        time.sleep(3)
        # Lấy toàn bộ nội dung HTML sau khi trang đã tải xong
        html_content = trinh_dieu_khien.page_source
        soup = BeautifulSoup(html_content, 'html.parser')

        #tìm bảng dữ liệu 
        div_stats = soup.find('div', id=id_bang_nguoi_choi)
        table = div_stats.find('table')
        tbody = table.find('tbody')
        tr_list=tbody.find_all('tr')

        miss=25
        for ind,i in enumerate(tr_list):    
            if(ind==miss):
                    miss=miss+25+1
                    continue
            arr=[]
            for index, value in enumerate(i.find_all('td')):
                if(index==1):
                    a=value.find('a')
                    if(a is not None):
                        span1=a.find('span', recursive=False)
                        span2=span1.find("span")
                        span2.extract()
                s=value.text.strip()

                if index>=4 and index!=lengthPlayerData:
                    s=s.replace(",","")
                    s=kiem_tra_du_lieu(s)
                arr.append(s)
            arr.pop()
            resultPlayerData.append(arr)
    finally:
        print("Finish Page "+ten_du_lieu)
    return resultPlayerData

def kiem_tra_du_lieu(n):
    if n=='': return "N/a"
    return float(n)


duong_dan = 'https://fbref.com/en/comps/9/2023-2024/playingtime/2023-2024-Premier-League-Stats'
id_bang_nguoi_choi="div_stats_playing_time"
do_dai_du_lieu_nguoi_choi=28
ten_du_lieu="Playing Time"
danh_sach_nguoi_choi=lay_du_lieu_tu_web(duong_dan,id_bang_nguoi_choi,do_dai_du_lieu_nguoi_choi,ten_du_lieu)

# Dữ liệu người chơi

for i in danh_sach_nguoi_choi:
    p=quan_ly_nguoi_choi.findPlayerByNameandTeam(i[0],i[3])
    if p==None:
        new_p=Player(i[0],i[1],i[2],i[3],i[4])
        new_p.setPlayingTimeDetail(i[11:14],i[14:17],i[17:20],i[23:25])
        quan_ly_nguoi_choi.add_Player(new_p)

duong_dan="https://fbref.com/en/comps/9/2023-2024/stats/2023-2024-Premier-League-Stats"
id_bang_nguoi_choi="div_stats_standard"
do_dai_du_lieu_nguoi_choi=35
idSquadTable="stats_squads_standard_for"
lengthSquadData=32
ten_du_lieu="Standard"
danh_sach_nguoi_choi=lay_du_lieu_tu_web(duong_dan,id_bang_nguoi_choi,do_dai_du_lieu_nguoi_choi,ten_du_lieu)
#player data
for i in danh_sach_nguoi_choi:
    p=quan_ly_nguoi_choi.findPlayerByNameandTeam(i[0],i[3])
    if p!=None:
        p.setPlaying_time(i[6:9])
        p.setPerformance([i[13],i[14],i[11],i[16],i[17]])
        p.setExpected(i[18:21])
        p.setProgression(i[22:25])
        p.setPer90(i[25:])

duong_dan = 'https://fbref.com/en/comps/9/2023-2024/keepers/2023-2024-Premier-League-Stats'
id_bang_nguoi_choi="div_stats_keeper"
do_dai_du_lieu_nguoi_choi=25
ten_du_lieu="keeper"
danh_sach_nguoi_choi=lay_du_lieu_tu_web(duong_dan,id_bang_nguoi_choi,do_dai_du_lieu_nguoi_choi,ten_du_lieu)

for i in danh_sach_nguoi_choi:
    p=quan_ly_nguoi_choi.findPlayerByNameandTeam(i[0],i[3])
    if p!=None:
        p.setGoalkeeping(i[10:20],i[20:])      

duong_dan = 'https://fbref.com/en/comps/9/2023-2024/shooting/2023-2024-Premier-League-Stats'
id_bang_nguoi_choi="div_stats_shooting"
do_dai_du_lieu_nguoi_choi=24
ten_du_lieu="Shooting"
danh_sach_nguoi_choi=lay_du_lieu_tu_web(duong_dan,id_bang_nguoi_choi,do_dai_du_lieu_nguoi_choi,ten_du_lieu)

for i in danh_sach_nguoi_choi:
    p=quan_ly_nguoi_choi.findPlayerByNameandTeam(i[0],i[3])
    if p!=None:
        p.setShooting(i[7:19],i[19:])


duong_dan = 'https://fbref.com/en/comps/9/2023-2024/passing/2023-2024-Premier-League-Stats'
id_bang_nguoi_choi="div_stats_passing"
do_dai_du_lieu_nguoi_choi=30
ten_du_lieu="Passing"
danh_sach_nguoi_choi=lay_du_lieu_tu_web(duong_dan,id_bang_nguoi_choi,do_dai_du_lieu_nguoi_choi,ten_du_lieu)

for i in danh_sach_nguoi_choi:
    p=quan_ly_nguoi_choi.findPlayerByNameandTeam(i[0],i[3])
    if p!=None:
        p.setPassing(i[7:12],i[12:15],i[15:18],i[18:21],i[21:])


duong_dan = 'https://fbref.com/en/comps/9/2023-2024/passing_types/2023-2024-Premier-League-Stats'
id_bang_nguoi_choi="div_stats_passing_types"
do_dai_du_lieu_nguoi_choi=22
ten_du_lieu="Passing Types"
danh_sach_nguoi_choi=lay_du_lieu_tu_web(duong_dan,id_bang_nguoi_choi,do_dai_du_lieu_nguoi_choi,ten_du_lieu)

for i in danh_sach_nguoi_choi:
    p=quan_ly_nguoi_choi.findPlayerByNameandTeam(i[0],i[3])
    if p!=None:
        p.setPassTypes(i[8:16],i[16:19],i[19:22])

duong_dan = 'https://fbref.com/en/comps/9/2023-2024/gca/2023-2024-Premier-League-Stats'
id_bang_nguoi_choi="div_stats_gca"
do_dai_du_lieu_nguoi_choi=23
ten_du_lieu="Goal and short creation"
danh_sach_nguoi_choi=lay_du_lieu_tu_web(duong_dan,id_bang_nguoi_choi,do_dai_du_lieu_nguoi_choi,ten_du_lieu)

for i in danh_sach_nguoi_choi:
    p=quan_ly_nguoi_choi.findPlayerByNameandTeam(i[0],i[3])
    if p!=None:
        p.setGoalShotCreation(i[7:9],i[9:15],i[15:17],i[17:23])

duong_dan = 'https://fbref.com/en/comps/9/2023-2024/defense/2023-2024-Premier-League-Stats'
id_bang_nguoi_choi="div_stats_defense"
do_dai_du_lieu_nguoi_choi=23
ten_du_lieu="Defensive"
danh_sach_nguoi_choi=lay_du_lieu_tu_web(duong_dan,id_bang_nguoi_choi,do_dai_du_lieu_nguoi_choi,ten_du_lieu)

for i in danh_sach_nguoi_choi:
    p=quan_ly_nguoi_choi.findPlayerByNameandTeam(i[0],i[3])
    if p!=None:
        p.setDefensiveActions(i[7:12],i[12:16],i[16:23])

duong_dan = 'https://fbref.com/en/comps/9/2023-2024/possession/2023-2024-Premier-League-Stats'
id_bang_nguoi_choi="div_stats_possession"
do_dai_du_lieu_nguoi_choi=29
ten_du_lieu="Possession"
danh_sach_nguoi_choi=lay_du_lieu_tu_web(duong_dan,id_bang_nguoi_choi,do_dai_du_lieu_nguoi_choi,ten_du_lieu)

for i in danh_sach_nguoi_choi:
    p=quan_ly_nguoi_choi.findPlayerByNameandTeam(i[0],i[3])
    if p!=None:
        p.setPossession(i[7:14],i[14:19],i[19:27],i[27:29])

duong_dan = 'https://fbref.com/en/comps/9/2023-2024/misc/2023-2024-Premier-League-Stats'
id_bang_nguoi_choi="div_stats_misc"
do_dai_du_lieu_nguoi_choi=23
ten_du_lieu="Miscellaneous Stats"
danh_sach_nguoi_choi=lay_du_lieu_tu_web(duong_dan,id_bang_nguoi_choi,do_dai_du_lieu_nguoi_choi,ten_du_lieu)

for i in danh_sach_nguoi_choi:
    p=quan_ly_nguoi_choi.findPlayerByNameandTeam(i[0],i[3])
    if p!=None:
        p.setMiscStats(i[10:14]+i[18:20],i[20:23])


trinh_dieu_khien.quit()
quan_ly_nguoi_choi.filtering()

import csv
from bang import header
from bang import row
with open('C:/7. Python code/btl python/result.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    
    for player in quan_ly_nguoi_choi.list_player:
        r=row(player)
        writer.writerow(r)
print("Hoan thanh bai tap 1. ")


import pickle
import csv
import statistics
from bang import header,row,row2,header2,rowsquad # type: ignore
import pandas as pd
import os

ATTR_NUMBER=167 #loai bo 5 thuoc tinh dau

squads=['Arsenal','Aston Villa','Bournemouth','Brentford','Brighton',
                'Burnley','Chelsea','Crystal Palace','Everton','Fulham','Liverpool','Luton Town',
                'Manchester City','Manchester Utd','Newcastle Utd',"Nott'ham Forest",'Sheffield Utd','Tottenham','West Ham','Wolves']

output_directory = 'histograms'
os.makedirs(output_directory, exist_ok=True)  # Tạo thư mục nếu chưa tồn tại
df = pd.read_csv('result.csv')
df.replace("N/a", 0, inplace=True)
ATTR_NUMBER=172
for i in range(5, ATTR_NUMBER):
    df[df.columns[i]] = pd.to_numeric(df[df.columns[i]], errors='coerce').fillna(0)
top_3_rows = df.nlargest(3, df.columns[5])


#top3
if 1==1:
    for i in range(5, len(df.columns)):
        top_3_rows = df.nlargest(3, df.columns[i])
        print("Top3 cao nhất thuộc tính",i)
        print(top_3_rows.iloc[:, 0].values)
        print("Top 3 thấp nhất thuộc tính",i)
        bot_3_rows = df.nsmallest(3, df.columns[i])
        print(bot_3_rows.iloc[:, 0].values)

#tinh trung binh
if 1==1:
    with open('C:/7. Python code/btl python/result2.csv', mode='w', newline='', encoding='utf-8') as file:
 
        all_attr=[]
        for i in range(5,ATTR_NUMBER):
            arr=df.iloc[:, i]
            all_attr.append(arr)
        mean_value_list=[0]*(ATTR_NUMBER-5)
        median_value_list=[0]*(ATTR_NUMBER-5)
        std_dev_list=[0]*(ATTR_NUMBER-5)

        for index,arr in enumerate(all_attr):
            mean_value_list[index]=statistics.mean(arr)
            median_value_list[index]=statistics.median(arr)
            std_dev_list[index]=statistics.stdev(arr)

        writer = csv.writer(file)
        writer.writerow(header2)

        r=row2(0,"All",median_value_list,mean_value_list,std_dev_list)
        writer.writerow(r)


    
        for stt,squad in enumerate(squads):
            all_attr1=[]
            filtered_df  = df[df.iloc[:, 2] == squad]  
            mean_value_list1=[0]*(ATTR_NUMBER-5)
            median_value_list1=[0]*(ATTR_NUMBER-5)
            std_dev_list1=[0]*(ATTR_NUMBER-5)

            for i in range(5,ATTR_NUMBER):
                arr=filtered_df.iloc[:, i].values
                all_attr1.append(arr)

            for index,arr in enumerate(all_attr1):
                mean_value_list1[index]=statistics.mean(arr)
                median_value_list1[index]=statistics.median(arr)
                if len(arr)<2:
                    std_dev_list1[index]="N/a"
                else: std_dev_list1[index]=statistics.stdev(arr)
            
            writer = csv.writer(file)
            r=row2(stt+1,squad,median_value_list1,mean_value_list1,std_dev_list1)
            writer.writerow(r)

        
    print("Hoan Thanh bai 2. ")
    import subprocess
    subprocess.Popen(["start", r"result2.csv"], shell=True)



#ve bieu do
if 1==1:
    import matplotlib.pyplot as plt
    all_attr=[]
    for i in range(5,ATTR_NUMBER):
        arr=df.iloc[:, i]
        all_attr.append(arr)
    for index,arr in enumerate(all_attr):
        plt.figure(figsize=(8, 6))
        plt.hist(arr, bins=30, color='blue', alpha=0.7, edgecolor='black')
        plt.title(f'Histogram of Data {header[5+index]}')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        image_path = os.path.join(output_directory, f'histogram_{index}.png')  # Đặt tên file
        plt.savefig(image_path)  # Lưu hình ảnh
        plt.close()  # Đóng biểu đồ để giải phóng bộ nhớ



#tim doi chi so cao nhat
if 1==1:
    for i in range(5,ATTR_NUMBER):
        print("Chi so",i,end=" ")
        arr=[]
        for stt,squad in enumerate(squads):
            filtered_df  = df[df.iloc[:, 2] == squad]  
            sum_column_i = filtered_df.iloc[:, i].sum()
            p=[squad,sum_column_i]
            arr.append(p)
        res=sorted(arr,key=lambda x:-x[1])
        index = 5 + i
        if index < len(header):
            print(f"{header[index]}: {res[0][0]}")
        else:
            print(f"Index {index} is out of range for list 'header'")

        
