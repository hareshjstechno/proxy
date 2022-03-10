from calendar import c
from hashlib import new
from io import open_code
import os,sys
import site
from time import sleep
import mysql.connector
import datetime
from dotenv import load_dotenv
load_dotenv()
import schedule
import random
from datetime import datetime
import smtplib, ssl
import requests
import json

from re import U
from MySQLdb import Connect
import requests
import json, sys
import mysql.connector
from bs4 import BeautifulSoup
import requests
prx = requests.Session()




host1=os.environ.get("DB_HOST"),
user=os.environ.get("DB_USERNAME"),
prot=os.environ.get('DB_PORT'),
password=os.environ.get("DB_PASSWORD"),
database=os.environ.get("DB_DATABASE")
host=host1[0]
user=user[0]
prot=prot[0]
password=password[0]
mydb = mysql.connector.connect(
  host=host,
  user=user,
  password=password,
  database=database
)

def vs_master(onevstwo,gameodds):
  j='none'
  try:
    sql_select_Query = "select * from vs_master"
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    j= records[-1][0]
  except:
    pass
    j=0 
  j=j+1
  try:
      mycursor = mydb.cursor()
      sql = "REPLACE INTO vs_master(id,name,gameodds) VALUES(%s, %s, %s) "
      val1=(j,onevstwo,gameodds)
      mycursor.execute(sql, val1)
      mydb.commit()
      print(mycursor, "record REPLACEed.")
  except:
      print("Error: unable to REPLACE data")


def sports_master(game_name0):
    j='1'
    k=1
    try:
      sql_select_Query = "select * from sports_master"
      cursor = mydb.cursor()
      cursor.execute(sql_select_Query)
      records = cursor.fetchall()
      j= records[-1][0]
    
    except:
      pass
    
    try:
        mycursor = mydb.cursor()
        sql = "REPLACE INTO sports_master(id,name,game_id) VALUES(%s, %s, %s) "
        val=(j,game_name0,k)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor, "record REPLACEed.")
    except:
        print("Error: unable to REPLACE data")

def league_master(league_name0):
    j='none'
    k=1
    try:
      sql_select_Query = "select * from league_master"
      cursor = mydb.cursor()
      cursor.execute(sql_select_Query)
      records = cursor.fetchall()
      j= records[-1][0]
  
    except:
      pass
      j=0
    j=j+1
    try:
      mycursor = mydb.cursor()
      sql = "REPLACE INTO league_master(id,name,game_id) VALUES(%s, %s, %s) "
      val=(j,league_name0,k)
      mycursor.execute(sql, val)
      mydb.commit()
      print(mycursor, "record REPLACEed.")
    except:
      print("Error: unable to REPLACE data")


def unique_key_master(uni):
  j='none'
  k=1
  try:
    sql_select_Query = "select * from vs_master"
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    j= records[-1][1]
  except:
    pass
  try:
    mycursor = mydb.cursor()
    sql = "REPLACE INTO unique_key_master(name,u_id) VALUES(%s, %s) "
    val=(j,uni)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor, "record REPLACEed.")
  except:
    print("Error: unable to REPLACE data")

def match1xbet(link):
  url = 'https://in.1x001.com/service-api/LineFeed/Get1x2_VZip?sports=66&count=20&lng=en&tz=5.5&mode=4&country=71&partner=71&getEmpty=true&virtualSports=true'
  prx.proxies = {"http":'{}'.format(link)}        
  data = prx.get(url).json()
  for i in data['Value']:
    odi='none'
    sql='none'
    t1_currunt_id='none'
    t2_currunt_id='none'
    date=i['S']
    date=str(datetime.fromtimestamp(date))
    date=date[0:10]
    try:
      t1_1_1x=str(i['E'][0]['C'])
      t_x_1x=str(i['E'][1]['C'])
      t2_2_1x=str(i['E'][2]['C'])
    except Exception as e:
      t1_1_1x='none'
      t2_2_1x='none'
      pass   
    Leauge_id_1x=str(i['LI'])
    l=str(i['KI'])
    Leauge_name_1x=str(i['L'])
    t1_name_1x=str(i['O1'])
    t1_id_1x=str(i['O1I'])
    t2_name_1x=str(i['O2'])
    t2_id_1x=str(i['O2I'])
    sports_name_1x=str(i['SE'])
    odi=(str(t1_1_1x)+'/'+str(t2_2_1x))
    gameodds=str(odi)  
   
    vs=t1_name_1x+' vs '+t2_name_1x
    onevstwo=vs
    vs_master(onevstwo,gameodds)
    uni=str(Leauge_id_1x)+str(t1_id_1x)+str(date)
    
    unique_key_master(uni)
    league_name0=Leauge_name_1x    
    league_master(league_name0)
    team_name0=t1_name_1x
    team_name0=t2_name_1x
    sql_select_Query = "select * from league_master"
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    for i in range(len(records)):
      mamn=records[i][0]
      nanm=records[i][1]
      if Leauge_name_1x==nanm:
        prince=mamn
        break
    i=1
    
    un1=t1_name_1x+t2_name_1x+date
    mycursor = mydb.cursor()
    sql_select_Query = "REPLACE into finaltable(date, team1_name, team2_name,uni) VALUES(%s,%s,%s,%s)"
    val1=(date,t1_name_1x,t2_name_1x,un1)
    mycursor.execute(sql_select_Query, val1)
    
    
    sql_select_Query = "select * from team_master where team_name='"+t1_name_1x+"'"
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    if len(records)>0:
      t1_currunt_id=records[0][0]
    else:
      mycursor = mydb.cursor()
      sql_select_Query = "REPLACE into team_master(team_name,game_id) VALUES(%s,%s)"
      val=(t1_name_1x,i)
      mycursor.execute(sql_select_Query, val)
      mydb.commit()
      sql_select_Query = "select * from team_master where team_name='"+t1_name_1x+"'"
      cursor = mydb.cursor()
      cursor.execute(sql_select_Query)
      records = cursor.fetchall()
          
      
      
      
      if len(records)>0:
        t1_currunt_id=records[0][0]
    sql_select_Query = "select * from team_master where team_name='"+t2_name_1x+"'"
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    
    if len(records)>0:
      t2_currunt_id=records[0][0]
    else:
      mycursor = mydb.cursor()
      sql_select_Query = "REPLACE into team_master(team_name, game_id) VALUES(%s,%s)"
      val=(t2_name_1x,i)
      mycursor.execute(sql_select_Query, val)
      mydb.commit()
      sql_select_Query = "select * from team_master where team_name='"+t2_name_1x+"'"
      cursor = mydb.cursor()
      cursor.execute(sql_select_Query)
      records = cursor.fetchall()
      
      if len(records)>0:
        t2_currunt_id=records[0][0]
    ghost0=(t1_currunt_id)
    ghost1=(t2_currunt_id)
    sql_select_Query = "select * from game_master where (team1_id='"+str(ghost0)+"' and team2_id='"+str(ghost1)+"') or (team1_id='"+str(ghost1)+"' and team2_id='"+str(ghost0)+"')"
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    # if len(records)>0:
    #   cno=int(records[0][0])
    # else:
    mycursor = mydb.cursor()
    sql_select_Query = "REPLACE into game_master(team1_id,team2_id,date) VALUES(%s,%s,%s)" 
    val = (str(ghost0),str(ghost1),date)
    mycursor.execute(sql_select_Query, val)
    mydb.commit()
    sql_select_Query = "select * from game_master where (team1_id='"+str(ghost0)+"' and team2_id='"+str(ghost1)+"') or (team1_id='"+str(ghost1)+"' and team2_id='"+str(ghost0)+"')"
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    cno=int(records[0][0])
    try:
        mycursor = mydb.cursor()
        mycursor = mydb.cursor()
        sql = "REPLACE INTO 1xbet(date ,leauge_id,leauge_name,l_id, team_1_id, team_1,t1_id, team_1_odds, team_2_id, team_2,t2_id, team_2_odds, team_x_odds, sports_name_1x, game_id, uni) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (date,Leauge_id_1x,Leauge_name_1x,prince, t1_id_1x, t1_name_1x,t1_currunt_id,t1_1_1x, t2_id_1x, t2_name_1x,t2_currunt_id, t2_2_1x, t_x_1x, sports_name_1x, cno, uni)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor, "record REPLACEed.")
    except :
        print("Error: unable to REPLACE data")

    sql_select_Query="UPDATE team_master SET onex_team_id = '{}' WHERE  team_name ='{}'".format(t1_id_1x,t1_name_1x)
    mycursor.execute(sql_select_Query)
    mydb.commit()
    sql_select_Query="UPDATE team_master SET onex_team_id = '{}' WHERE  team_name ='{}'".format(t2_id_1x,t2_name_1x)
    mycursor.execute(sql_select_Query)
    mydb.commit()
    
    
    sql_select_Query="UPDATE finaltable SET onex1 = '{}' WHERE  uni ='{}'".format(t1_1_1x, un1)
    mycursor.execute(sql_select_Query)
    mydb.commit()

    sql_select_Query="UPDATE finaltable SET onex2 = '{}' WHERE  uni ='{}'".format(t2_2_1x, un1)
    mycursor.execute(sql_select_Query)
    mydb.commit()


def matchcomeonbet(link):
  url = 'https://nodeprm.tsports.online/cache/48/en/in/Asia-Kolkata/init/34/welcome-popular.json'
  prx.proxies = {"http":'{}'.format(link)}        
  data = prx.get(url).json()
  for i in data['events']:
    team1_id_come='none'
    team1_name_come='none'
    team2_name_come='none'
    team1_odds_come='none'
    team2_odds_come='none'
    t1_currunt_id='none'
    t1_currunt_id='none'
    team2_id_come='none'
    team2_name_come='none'
    
    Leauge_id_come=str(i['tournament_id'])
    date_come=str(i['date_start'])
    date_come=(date_come[0:10])
    Leauge_name_come=str(i['tournament_name'])
    sports_name_come=str(i['sport_title'])
    s=i['main_odds']['main']
    
    
    try:
      news=list(s.keys())
      team1_name_come=str(i["teams"]["home"])
      team2_name_come=str(i["teams"]["away"])
      team1_odds_come=str(i['main_odds']['main'][str(news[0])]['odd_value'])
      team2_odds_come=str(i['main_odds']['main'][str(news[1])]['odd_value'])
      team1_id_come=str(i['main_odds']['main'][str(news[0])]['id'])
      team2_id_come=str(i['main_odds']['main'][str(news[1])]['id'])
      
    except:
      pass
    
    new_leauge=Leauge_name_come[-5:]
    if new_leauge=='Women':
      team1_name_come=team1_name_come+" (Women)"
      team2_name_come=team2_name_come+" (Women)"
      
    vs1=team1_name_come+' vs '+team2_name_come
    un1=team1_name_come+team2_name_come+date_come
    onevstwo=vs1
    odi=(str(team1_odds_come)+'/'+str(team2_odds_come))
    gameodds=str(odi)
    vs_master(onevstwo,gameodds)
    league_name0=Leauge_name_come
    league_master(league_name0)
   
    game_name0=sports_name_come
    sports_master(game_name0)
    uni=str(Leauge_id_come)+str(team1_id_come)+str(date_come)
    unique_key_master(uni)
    sql_select_Query = "select * from league_master"
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    for i in range(len(records)):
      mamn=records[i][0]
      nanm=records[i][1]
      if Leauge_name_come==nanm:
        prince=mamn
        break
    i=1
    mycursor = mydb.cursor()
    sql_select_Query = "REPLACE into finaltable(date, team1_name, team2_name,uni) VALUES(%s,%s,%s,%s)"
    val1=(date_come,team1_name_come,team2_name_come,un1)
    mycursor.execute(sql_select_Query, val1)
    
    
    sql_select_Query = "select * from team_master where team_name='"+team1_name_come+"'"
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    if len(records)>0:
      t1_currunt_id=records[0][0]
    else:
      mycursor = mydb.cursor()
      sql_select_Query = "REPLACE into team_master(team_name,game_id) VALUES(%s,%s)"
      val=(team1_name_come,i)
      mycursor.execute(sql_select_Query, val)
      mydb.commit()
    
           
      sql_select_Query = "select * from team_master where team_name='"+team1_name_come+"'"
      cursor = mydb.cursor()
      cursor.execute(sql_select_Query)
      records = cursor.fetchall()
      
    
    
    
    
      if len(records)>0:
        t1_currunt_id=records[0][0]
    sql_select_Query = "select * from team_master where team_name='"+team2_name_come+"'"
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()

    if len(records)>0:
      t2_currunt_id=records[0][0]
    else:
      mycursor = mydb.cursor()
      sql_select_Query = "REPLACE into team_master(team_name,game_id) VALUES(%s,%s)"
      val=(team2_name_come,i)
      mycursor.execute(sql_select_Query, val)
      mydb.commit()
    
      
      sql_select_Query = "select * from team_master where team_name='"+team2_name_come+"'"
      cursor = mydb.cursor()
      cursor.execute(sql_select_Query)
      records = cursor.fetchall()
      if len(records)>0:
        t2_currunt_id=records[0][0]
    
    ghost0=(t1_currunt_id)
    ghost1=(t2_currunt_id)
    sql_select_Query = "select * from game_master where (team1_id='"+str(ghost0)+"' and team2_id='"+str(ghost1)+"') or (team1_id='"+str(ghost1)+"' and team2_id='"+str(ghost0)+"')"
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    # if len(records)>0:
    #   cno=int(records[0][0])
    # else:
    mycursor = mydb.cursor()
    sql_select_Query = "REPLACE into game_master(team1_id,team2_id,date) VALUES(%s,%s,%s)" 
    val = (str(ghost0),str(ghost1),date_come)
    mycursor.execute(sql_select_Query, val)
    mydb.commit()
    
    sql_select_Query = "select * from game_master where (team1_id='"+str(ghost0)+"' and team2_id='"+str(ghost1)+"') or (team1_id='"+str(ghost1)+"' and team2_id='"+str(ghost0)+"')"
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    cno=int(records[0][0])
    
    try:
      mycursor = mydb.cursor()
      sql = "REPLACE INTO comeongame(date, leauge_id, leauge_name,l_id, team_1_id, team_1,t1_id, team_1_odds, team_2_id, team_2,t2_id,team_2_odds, sports_name ,game_id,uni) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"
      val = (date_come,Leauge_id_come,Leauge_name_come,prince,team1_id_come,team1_name_come,t1_currunt_id,team1_odds_come,team2_id_come,team2_name_come,t2_currunt_id,team2_odds_come,sports_name_come,cno,uni)
      mycursor.execute(sql, val)
      mydb.commit()
      print(mycursor, "record REPLACEed.")
    except:
      print("Error: unable to REPLACE data")


    sql_select_Query="UPDATE team_master SET comeon_team_id = '{}' WHERE  team_name ='{}'".format(team1_id_come, team1_name_come)
    mycursor.execute(sql_select_Query)
    mydb.commit()
    sql_select_Query="UPDATE team_master SET comeon_team_id = '{}' WHERE  team_name ='{}'".format(team2_id_come, team2_name_come)
    mycursor.execute(sql_select_Query)
    mydb.commit()
    
    sql_select_Query="UPDATE finaltable SET comeon1 = '{}' WHERE  uni ='{}'".format(team1_odds_come,un1)
    mycursor.execute(sql_select_Query)
    mydb.commit()
    sql_select_Query="UPDATE finaltable SET comeon2 = '{}' WHERE  uni ='{}'".format(team2_odds_come,un1)
    mycursor.execute(sql_select_Query)
    mydb.commit()
    
    
    
    
    
def matchwazamba(link):
  url='https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetUpcoming?timezoneOffset=-330&langId=83&skinName=wazamba&configId=26&culture=hi-in&countryCode=IN&deviceType=Desktop&numformat=en&integration=wazamba&sportId=149&showAllEvents=false&count=10'
  prx.proxies = {"http":'{}'.format(link)}        
  data = prx.get(url).json()
  for i in data['Result']['Items'][0]['Events']:                                                                                         
    sports_name_waz=i['SportName']
    leauge_id_waz=i['ChampId']
    leauge_name_waz=i['ChampName'] 
    date_waz=i['EventDate']
    date_waz=date_waz[0:10]
    try:
      team1_odds_waz=i['Items'][0]['Items'][0]['Price']
      a1=i['Items'][0]['Items'][0]['ColumnNums'][1]
      team2_odds_waz=i['Items'][0]['Items'][1]['Price']
      a11=i['Items'][0]['Items'][1]['ColumnNums'][1]
    except:
      team1_odds_waz=''
      a1=''
      team2_odds_waz=''
      a11=''
    a1=str(a1)
    a11=str(a11)
    team1_id_waz=i['Competitors'][0]['Id']
    team1_name_waz=i['Competitors'][0]['Name']
    team2_id_waz=i['Competitors'][1]['Id']
    team2_name_waz=i['Competitors'][1]['Name']
    new_leauge=leauge_name_waz[-5:]
    if new_leauge=='Women':
      team1_name_waz=team1_name_waz+' (Women)'
      team2_name_waz=team2_name_waz+' (Women)'
    vs2=team1_name_waz+' vs '+team2_name_waz
    un1=team1_name_waz+team2_name_waz+date_waz
    onevstwo=vs2
    odi=(str(team1_odds_waz)+'/'+str(team2_odds_waz))
    gameodds=str(odi)
    vs_master(onevstwo,gameodds)
    uni=str(leauge_id_waz)+str(team1_id_waz)+str(date_waz)
    unique_key_master(uni)
    league_name0=leauge_name_waz
    league_master(league_name0)
    team_name0=team1_name_waz
    team_name0=team2_name_waz
    sql_select_Query = "select * from league_master"
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    
    for i in range(len(records)):
      mamn=records[i][0]
      nanm=records[i][1]
      if leauge_name_waz==nanm:
        prince=mamn
        break
    i=1
    mycursor = mydb.cursor()
    sql_select_Query = "REPLACE into finaltable(date, team1_name, team2_name,uni) VALUES(%s,%s,%s,%s)"
    val1=(date_waz,team1_name_waz,team2_name_waz,un1)
    mycursor.execute(sql_select_Query, val1)
    
    sql_select_Query = "select * from team_master where team_name='"+team1_name_waz+"'"
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    if len(records)>0:
      t1_currunt_id=records[0][0]
    else:
      mycursor = mydb.cursor()
      sql_select_Query = "REPLACE into team_master(team_name,game_id) VALUES(%s,%s)"
      val=(team1_name_waz,i)
      mycursor.execute(sql_select_Query, val)
      mydb.commit()
  
          
      sql_select_Query = "select * from team_master where team_name='"+team1_name_waz+"'"
      cursor = mydb.cursor()
      cursor.execute(sql_select_Query)
      records = cursor.fetchall()
      
      if len(records)>0:
        t1_currunt_id=records[0][0]
    
    sql_select_Query = "select * from team_master where team_name='"+team2_name_waz+"'"
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    
    if len(records)>0:
      t2_currunt_id=records[0][0]
    else:
      mycursor = mydb.cursor()
      sql_select_Query = "REPLACE into team_master(team_name,game_id) VALUES(%s,%s)"
      val=(team2_name_waz,i)
      mycursor.execute(sql_select_Query, val)
      mydb.commit()
    
    
      
      
      sql_select_Query = "select * from team_master where team_name='"+team2_name_waz+"'"
      cursor = mydb.cursor()
      cursor.execute(sql_select_Query)
      records = cursor.fetchall()
      
      if len(records)>0:
        t2_currunt_id=records[0][0]
    
    ghost0=(t1_currunt_id)
    ghost1=(t2_currunt_id)
            
    sql_select_Query = "select * from game_master where (team1_id='"+str(ghost0)+"' and team2_id='"+str(ghost1)+"') or (team1_id='"+str(ghost1)+"' and team2_id='"+str(ghost0)+"')"
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    # if len(records)>0:
    #   cno=int(records[0][0])
    # else:
    mycursor = mydb.cursor()
    sql_select_Query = "REPLACE into game_master(team1_id,team2_id,date) VALUES(%s,%s,%s)" 
    val = (str(ghost0),str(ghost1),date_waz)
    mycursor.execute(sql_select_Query, val)
    mydb.commit()
    
    sql_select_Query = "select * from game_master where (team1_id='"+str(ghost0)+"' and team2_id='"+str(ghost1)+"') or (team1_id='"+str(ghost1)+"' and team2_id='"+str(ghost0)+"')"
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    cno=int(records[0][0])
    
    try:
        sql = "REPLACE INTO wazamba(date, leauge_id, leauge_name,l_id, team_1_id, team_1,t1_id, team_1_odds, team_2_id, team_2,t2_id, team_2_odds, sports_name, game_id, uni) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (date_waz,leauge_id_waz,leauge_name_waz,prince,team1_id_waz,team1_name_waz,t1_currunt_id,team1_odds_waz,team2_id_waz,team2_name_waz,t2_currunt_id,team2_odds_waz,sports_name_waz,cno,uni)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor, "record REPLACEed.")
    except:
        print("Error: unable to REPLACE data")
    mycursor = mydb.cursor()
    sql_select_Query="UPDATE team_master SET wazamba_team_id = '{}' WHERE  team_name ='{}'".format(team1_id_waz, team1_name_waz)
    mycursor.execute(sql_select_Query)
    mydb.commit()
    sql_select_Query="UPDATE team_master SET wazamba_team_id = '{}' WHERE  team_name ='{}'".format(team2_id_waz, team2_name_waz)
    mycursor.execute(sql_select_Query)
    mydb.commit()  
    
    sql_select_Query="UPDATE finaltable SET waz1 = '{}' WHERE  uni ='{}'".format(team1_odds_waz, un1)
    mycursor.execute(sql_select_Query)
    mydb.commit()
    sql_select_Query="UPDATE finaltable SET waz2 = '{}' WHERE  uni ='{}'".format(team2_odds_waz, un1)
    mycursor.execute(sql_select_Query)
    mydb.commit()
    sql_select_Query="UPDATE finaltable SET libra1 = '{}' WHERE  uni ='{}'".format(team1_odds_waz, un1)
    mycursor.execute(sql_select_Query)
    mydb.commit()
    sql_select_Query="UPDATE finaltable SET libra2 = '{}' WHERE  uni ='{}'".format(team2_odds_waz, un1)
    mycursor.execute(sql_select_Query)
    mydb.commit()


def leon_bet(link):
  team2_name_leon='none'
  team1_name_leon='none'
  r='none'
  url='https://leon.bet/api-2/betline/headline-matches?ctag=en-IN&flags=reg,mm2,rrc,urlv2&merged=true'
  prx.proxies = {"http":'{}'.format(link)}        
  r = prx.get(url).json()
  data=(r['events']['events'])
  for i in data:
      g3=i['league']['sport']['name']

      date=(i['kickoff'])/1000
      date=str(datetime.fromtimestamp(date))
      date=(date[0:10])
      if g3=='Cricket':
          leauge_id_leaon=i['league']['id']
          leauge_name_leon=i['league']['name']
          team1_name_leon=i['competitors'][0]['name']
          team2_name_leon=i['competitors'][1]['name']
          team1_id_leon=i['competitors'][0]['id']
          team2_id_leon=i['competitors'][1]['id']
          
          if team1_name_leon[-5:]=="Women":
            team1_name_leon=team1_name_leon[:-5]+"(Women)"
          
          if team2_name_leon[-5:]=="Women":
            team2_name_leon=team2_name_leon[:-5]+"(Women)"
          
          if team1_name_leon[-1:]=='w':
            team1_name_leon=team1_name_leon[:-1]+"(Women)"
         
          if team2_name_leon[-1:]=='w':
            team2_name_leon=team2_name_leon[:-1]+"(Women)"
          
          if team1_name_leon[-1:]=='W':
            team1_name_leon=team1_name_leon[:-1]+"(Women)"
         
          if team2_name_leon[-1:]=='W':
            team2_name_leon=team2_name_leon[:-1]+"(Women)"
          
          if team1_name_leon[-3:]=='(W)':
            team1_name_leon=team1_name_leon[:-3]+"(Women)"
         
          if team2_name_leon[-3:]=='(W)':
            team2_name_leon=team2_name_leon[:-3]+"(Women)"
          
          if team1_name_leon[-3:]=='(w)':
            team1_name_leon=team1_name_leon[:-3]+"(Women)"
         
          if team2_name_leon[-3:]=='(w)':
            team2_name_leon=team2_name_leon[:-3]+"(Women)"
          
          sports_name_leon='Cricket'
          try:
            team1_odds_leon=i['markets'][0]['runners'][0]['price']
            r=i['markets'][0]['runners'][1]['name']
            team2_odds_leon=i['markets'][0]['runners'][1]['price']
          except:
            team1_odds_leon='none'
            r='none'
            team2_odds_leon='none'
          vs3=team1_name_leon+' vs '+team2_name_leon
          un1=team1_name_leon+team2_name_leon+date
          onevstwo=vs3
          odi=(str(team1_odds_leon)+'/'+str(team2_odds_leon))
          gameodds=str(odi)
          vs_master(onevstwo,gameodds)
          uni=str(leauge_id_leaon)+str(team1_id_leon)+str(date)
          unique_key_master(uni)
          league_name0=leauge_name_leon
          league_master(league_name0)
          team_name0=team1_name_leon
          team_name0=team2_name_leon
          sql_select_Query = "select * from league_master"
          cursor = mydb.cursor()
          cursor.execute(sql_select_Query)
          records = cursor.fetchall()
          
          for i in range(len(records)):
            mamn=records[i][0]
            nanm=records[i][1]
            if leauge_name_leon==nanm:
              prince=mamn
              break
          
          i=1
          
          mycursor = mydb.cursor()
          sql_select_Query = "REPLACE into finaltable(date, team1_name, team2_name,uni) VALUES(%s,%s,%s,%s)"
          val1=(date,team1_name_leon,team2_name_leon,un1)
          mycursor.execute(sql_select_Query, val1)
          
          sql_select_Query = "select * from team_master where team_name='"+team1_name_leon+"'"
          cursor = mydb.cursor()
          cursor.execute(sql_select_Query)
          records = cursor.fetchall()
          if len(records)>0:
            t1_currunt_id=records[0][0]
          else:
            mycursor = mydb.cursor()
            sql_select_Query = "REPLACE into team_master(team_name,game_id) VALUES(%s,%s)"
            val=(team1_name_leon,i)
            mycursor.execute(sql_select_Query, val)
            mydb.commit()
            
            sql_select_Query = "select * from team_master where team_name='"+team1_name_leon+"'"
            cursor = mydb.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()
            
            if len(records)>0:
              t1_currunt_id=records[0][0]
          
          sql_select_Query = "select * from team_master where team_name='"+team2_name_leon+"'"
          cursor = mydb.cursor()
          cursor.execute(sql_select_Query)
          records = cursor.fetchall()
          
          if len(records)>0:
            t2_currunt_id=records[0][0]
          else:
            mycursor = mydb.cursor()
            sql_select_Query = "REPLACE into team_master(team_name,game_id) VALUES(%s,%s)"
            val=(team2_name_leon,i)
            mycursor.execute(sql_select_Query, val)
            mydb.commit()

            


            sql_select_Query = "select * from team_master where team_name='"+team2_name_leon+"'"
            cursor = mydb.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()
            
            if len(records)>0:
              t2_currunt_id=records[0][0]
          
          ghost0=(t1_currunt_id)
          ghost1=(t2_currunt_id)
          
                    
          sql_select_Query = "select * from game_master where (team1_id='"+str(ghost0)+"' and team2_id='"+str(ghost1)+"') or (team1_id='"+str(ghost1)+"' and team2_id='"+str(ghost0)+"')"
          cursor = mydb.cursor()
          cursor.execute(sql_select_Query)
          records = cursor.fetchall()
          # if len(records)>0:
          #   cno=int(records[0][0])
          # else:
          mycursor = mydb.cursor()
          sql_select_Query = "REPLACE into game_master(team1_id,team2_id,date) VALUES(%s,%s,%s)" 
          val = (str(ghost0),str(ghost1),date)
          mycursor.execute(sql_select_Query, val)
          mydb.commit()
          
          sql_select_Query = "select * from game_master where (team1_id='"+str(ghost0)+"' and team2_id='"+str(ghost1)+"') or (team1_id='"+str(ghost1)+"' and team2_id='"+str(ghost0)+"')"
          cursor = mydb.cursor()
          cursor.execute(sql_select_Query)
          records = cursor.fetchall()
          cno=int(records[0][0])
          
          try:
              mycursor = mydb.cursor()
              sql = "REPLACE INTO leonbet(date,leauge_id, leauge_name,l_id, team_1_id, team_1,t1_id, team_1_odds, team_2_id, team_2,t2_id, team_2_odds, sports_name, game_id,uni) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
              val = (date, leauge_id_leaon,leauge_name_leon,prince,team1_id_leon,team1_name_leon,t1_currunt_id,team1_odds_leon,team2_id_leon,team2_name_leon,t2_currunt_id,team2_odds_leon,sports_name_leon,cno,uni)
              mycursor.execute(sql, val)
              mydb.commit()
              print(mycursor, "record REPLACEed.")
          except:
              print("Error: unable to REPLACE data")
          mycursor = mydb.cursor()
          sql_select_Query="UPDATE team_master SET leon_team_id = '{}' WHERE  team_name ='{}'".format(team1_id_leon, team1_name_leon)
          mycursor.execute(sql_select_Query)
          mydb.commit()
          sql_select_Query="UPDATE team_master SET leon_team_id = '{}' WHERE  team_name ='{}'".format(team2_id_leon, team2_name_leon)
          mycursor.execute(sql_select_Query)
          mydb.commit()
          
          sql_select_Query="UPDATE finaltable SET leone1 = '{}' WHERE  uni ='{}'".format(team1_odds_leon, un1)
          mycursor.execute(sql_select_Query)
          mydb.commit()
          sql_select_Query="UPDATE finaltable SET leone2 = '{}' WHERE  uni ='{}'".format(team2_odds_leon, un1)
          mycursor.execute(sql_select_Query)
          mydb.commit()
            
          
                  

def librabet(link):
    url='https://sb2frontend-altenar2.biahosted.com/api/Sportsbook/GetUpcoming?timezoneOffset=-330&langId=83&skinName=librabet&configId=26&culture=hi-in&countryCode=IN&deviceType=Desktop&numformat=en&integration=librabet&sportId=149&showAllEvents=false&count=10'
    prx.proxies = {"http":'{}'.format(link)}        
    r = prx.get(url).json()
    data=r['Result']['Items'][0]['Events']
    for i in data:
        sport_name_lib=i['SportName']
        leauge_id_lib=i['ChampId']
        leauge_name_lib=i['ChampName'] 
        date_lib=i['EventDate']
        date_lib=str(date_lib[0:10])
        # r=i['Items'][0]['Name']
        try:
          team1_id_lib=i['Items'][0]['Id']
          team1_odds_lib=i['Items'][0]['Items'][0]['Price']
          a1=i['Items'][0]['Items'][0]['ColumnNums'][1]
          team2_odds_lib=i['Items'][0]['Items'][1]['Price']
          a11=i['Items'][0]['Items'][1]['ColumnNums'][1]
        
        except:
          team1_id_lib=''
          team1_odds_lib=''
          team2_odds_lib=''
          a1=''
          a11=''

        a1=str(a1)
        
        a11=str(a11)
        team1_id_lib=i['Competitors'][0]['Id']
        team1_name_lib=i['Competitors'][0]['Name']
        team2_id_lib=i['Competitors'][1]['Id']
        team2_name_lib=i['Competitors'][1]['Name']
        new_leauge=leauge_name_lib[-5:]
        if new_leauge=="Women":
          team1_name_lib=team1_name_lib+" (Women)"        
          team2_name_lib=team2_name_lib+" (Women)"        
        
        vs4=team1_name_lib+' vs '+team2_name_lib
        un1=team1_name_lib+team2_name_lib+date_lib
        onevstwo=vs4
        odi=(str(team1_odds_lib)+'/'+str(team2_odds_lib))
        gameodds=str(odi)
        vs_master(onevstwo,gameodds)
        uni=str(leauge_id_lib)+str(team1_id_lib)+str(date_lib)
        unique_key_master(uni)
        league_name0=leauge_name_lib
        league_master(league_name0)
        team_name0=team1_name_lib
        team_name0=team2_name_lib
        
        mycursor = mydb.cursor()
        sql_select_Query = "select * from league_master"
        cursor = mydb.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        
        for i in range(len(records)):
          mamn=records[i][0]
          nanm=records[i][1]
          if leauge_name_lib==nanm:
            prince=mamn
            break
        
        i=1
        
        mycursor = mydb.cursor()
        sql_select_Query = "REPLACE into finaltable(date, team1_name, team2_name,uni) VALUES(%s,%s,%s,%s)"
        val1=(date_lib,team1_name_lib,team2_name_lib,un1)
        mycursor.execute(sql_select_Query, val1)
      
        
        sql_select_Query = "select * from team_master where team_name='"+team1_name_lib+"'"
        cursor = mydb.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        if len(records)>0:
          t1_currunt_id=records[0][0]
        else:
          mycursor = mydb.cursor()
          sql_select_Query = "REPLACE into team_master(team_name,game_id) VALUES(%s,%s)"
          val=(team1_name_lib,i)
          mycursor.execute(sql_select_Query, val)
          mydb.commit()
      
          sql_select_Query = "select * from team_master where team_name='"+team1_name_lib+"'"
          cursor = mydb.cursor()
          cursor.execute(sql_select_Query)
          records = cursor.fetchall()
          
          if len(records)>0:
            t1_currunt_id=records[0][0]
        
        sql_select_Query = "select * from team_master where team_name='"+team2_name_lib+"'"
        cursor = mydb.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        
        if len(records)>0:
          t2_currunt_id=records[0][0]
        else:
          mycursor = mydb.cursor()
          sql_select_Query = "REPLACE into team_master(team_name,game_id) VALUES(%s,%s)"
          val=(team2_name_lib,i)
          mycursor.execute(sql_select_Query, val)
          mydb.commit()
          
          
          


          sql_select_Query = "select * from team_master where team_name='"+team2_name_lib+"'"
          cursor = mydb.cursor()
          cursor.execute(sql_select_Query)
          records = cursor.fetchall()
          
          if len(records)>0:
            t2_currunt_id=records[0][0]
        
        ghost0=(t1_currunt_id)
        ghost1=(t2_currunt_id)
        
        sql_select_Query = "select * from game_master where (team1_id='"+str(ghost0)+"' and team2_id='"+str(ghost1)+"') or (team1_id='"+str(ghost1)+"' and team2_id='"+str(ghost0)+"')"
        cursor = mydb.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        # if len(records)>0:
        #   cno=int(records[0][0])
        # else:
        mycursor = mydb.cursor()
        sql_select_Query = "REPLACE into game_master(team1_id, team2_id, date) VALUES(%s,%s,%s)" 
        val = (str(ghost0),str(ghost1),date_lib)
        mycursor.execute(sql_select_Query, val)
        mydb.commit()
        
        sql_select_Query = "select * from game_master where (team1_id='"+str(ghost0)+"' and team2_id='"+str(ghost1)+"') or (team1_id='"+str(ghost1)+"' and team2_id='"+str(ghost0)+"')"
        cursor = mydb.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        cno=int(records[0][0])
            
        
          
        try:
            sql = "REPLACE INTO librabet(date, leauge_id, leauge_name,l_id, team_1_id, team_1,t1_id, team_1_odds, team_2_id, team_2,t2_id, team_2_odds, sports_name, game_id,uni) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (date_lib,leauge_id_lib,leauge_name_lib,prince,team1_id_lib,team1_name_lib,t1_currunt_id,team1_odds_lib,team2_id_lib,team2_name_lib,t2_currunt_id,team2_odds_lib,sport_name_lib,cno,uni)  
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor, "record REPLACEed.")
        except:
            print("Error: unable to REPLACE data")
        mycursor = mydb.cursor()
        sql_select_Query="UPDATE team_master SET libra_team_id = '{}' WHERE  team_name ='{}'".format(team1_id_lib, team1_name_lib)
        mycursor.execute(sql_select_Query)
        mydb.commit()
        sql_select_Query="UPDATE team_master SET libra_team_id = '{}' WHERE  team_name ='{}'".format(team2_id_lib, team2_name_lib)
        mycursor.execute(sql_select_Query)
        mydb.commit() 
        
        sql_select_Query="UPDATE finaltable SET libra1 = '{}' WHERE  uni ='{}'".format(team1_odds_lib, un1)
        mycursor.execute(sql_select_Query)
        mydb.commit()
        sql_select_Query="UPDATE finaltable SET libra2 = '{}' WHERE  uni ='{}'".format(team2_odds_lib, un1)
        mycursor.execute(sql_select_Query)
        mydb.commit()
        
    
      
def casumo(link):
    prince='none'
    team1_name_csm=''
    team2_name_csm=''
    team1_odds_csm=''
    team2_odds_csm=''
    team1_id_csm=''
    team2_id_csm=''
    r='none'
    url='https://eu-offering.kambicdn.org/offering/v2018/ca/listView/cricket.json?lang=en_GB&market=IN&client_id=2&channel_id=1&ncid=1642566158289&useCombined=true'
    
    prx.proxies = {"http":'{}'.format(link)}        
    r = prx.get(url).json()
    data=(r['events'])
    for i in data:
        date_csm=i['event']['start']
        date_csm=str(date_csm[0:10])
        leauge_id_csm=i['event']['path'][1]['id']
        leauge_name_csm=i['event']['path'][1]['name']
        sports_name_csm=i['event']['sport']
        try:
            w=i['betOffers'][0]['outcomes'][0]['odds']
            team1_id_csm=i['betOffers'][0]['outcomes'][0]['id']
            team1_name_csm=i['betOffers'][0]['outcomes'][0]['participant']
        except:
            w='none'
        try:
            team2_id_csm=i['betOffers'][0]['outcomes'][1]['id']
            w1=i['betOffers'][0]['outcomes'][1]['odds']
            team2_name_csm=i['betOffers'][0]['outcomes'][1]['participant']
        except:
            try:
              team2_id_csm=i['betOffers'][0]['outcomes'][2]['id']
              team2_name_csm=i['betOffers'][0]['outcomes'][2]['participant']
              w1=i['betOffers'][0]['outcomes'][2]['odds']
            except:
              w1='none'
        team=team1_name_csm[-3:]
        team1_name_csm1=team1_name_csm[:-3]
        if team=='U19':
          team1_name_csm=team1_name_csm1+' (U-19)'
        
        team=team2_name_csm[-3:]
        team2_name_csm1=team2_name_csm[:-3]
        if team=='U19':
          team2_name_csm=team2_name_csm1+' (U-19)'
        
        team=team1_name_csm[-3:]
        team1_name_csm1=team1_name_csm[:-3]
        if team=='(W)':
          team1_name_csm=team1_name_csm1+'(Women)'
        
        team=team2_name_csm[-3:]
        team2_name_csm1=team2_name_csm[:-3]
        if team=='(W)':
          team2_name_csm=team2_name_csm1+'(Women)'
        
        team=team1_name_csm[-1:]
        team1_name_csm1=team1_name_csm[:-1]
        if team=='w':
          team1_name_csm=team1_name_csm1+'(Women)'
        
        team=team2_name_csm[-1:]
        team2_name_csm1=team2_name_csm[:-1]
        if team=='w':
          team2_name_csm=team2_name_csm1+'(Women)'
      
        try:  
            team1_odds_csm=int(w)/1000
        except:
            pass
        try:
            team2_odds_csm=int(w1)/1000
        except:
            pass
        vs5=team1_name_csm+' vs '+team2_name_csm
        un1=team1_name_csm+team2_name_csm+date_csm
        onevstwo=vs5
        odi=(str(team1_odds_csm)+'/'+str(team2_odds_csm))
        gameodds=str(odi)
        vs_master(onevstwo,gameodds)
        uni=str(leauge_id_csm)+str(team1_id_csm)+str(date_csm)
        unique_key_master(uni)
        league_name0=leauge_name_csm
        league_master(league_name0)
        team_name0=team1_name_csm
        team_name0=team2_name_csm
        sql_select_Query = "select * from league_master"
        cursor = mydb.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        
        for i in range(len(records)):
          mamn=records[i][0]
          nanm=records[i][1]
          if leauge_name_csm==nanm:
            prince=mamn
            break
        
        i=1
    
        mycursor = mydb.cursor()
        sql_select_Query = "REPLACE into finaltable(date, team1_name, team2_name,uni) VALUES(%s,%s,%s,%s)"
        val1=(date_csm,team1_name_csm,team2_name_csm,un1)
        mycursor.execute(sql_select_Query, val1)
            
        
        
        sql_select_Query = "select * from team_master where team_name='"+team1_name_csm+"'"
        cursor = mydb.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        if len(records)>0:
          t1_currunt_id=records[0][0]
        else:
          mycursor = mydb.cursor()
          sql_select_Query = "REPLACE into team_master(team_name,game_id) VALUES(%s,%s)"
          val=(team1_name_csm,i)
          mycursor.execute(sql_select_Query, val)
          mydb.commit()
          sql_select_Query = "select * from team_master where team_name='"+team1_name_csm+"'"
          cursor = mydb.cursor()
          cursor.execute(sql_select_Query)
          records = cursor.fetchall()
          
          if len(records)>0:
            t1_currunt_id=records[0][0]
        
        sql_select_Query = "select * from team_master where team_name='"+team2_name_csm+"'"
        cursor = mydb.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        
        if len(records)>0:
          t2_currunt_id=records[0][0]
        else:
          mycursor = mydb.cursor()
          sql_select_Query = "REPLACE into team_master(team_name,game_id) VALUES(%s,%s)"
          val=(team2_name_csm,i)
          
          
     
          
          
          
          mycursor.execute(sql_select_Query, val)
          mydb.commit()
          sql_select_Query = "select * from team_master where team_name='"+team2_name_csm+"'"
          cursor = mydb.cursor()
          cursor.execute(sql_select_Query)
          records = cursor.fetchall()
          
          if len(records)>0:
            t2_currunt_id=records[0][0]
        
        ghost0=(t1_currunt_id)
        ghost1=(t2_currunt_id)
        
        sql_select_Query = "select * from game_master where (team1_id='"+str(ghost0)+"' and team2_id='"+str(ghost1)+"') or (team1_id='"+str(ghost1)+"' and team2_id='"+str(ghost0)+"')"
        cursor = mydb.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        # if len(records)>0:
        #   cno=int(records[0][0])
        # else:
        mycursor = mydb.cursor()
        sql_select_Query = "REPLACE into game_master(team1_id,team2_id,date) VALUES(%s,%s,%s)" 
        val = (str(ghost0),str(ghost1),date_csm)
        mycursor.execute(sql_select_Query, val)
        mydb.commit()
        
        sql_select_Query = "select * from game_master where (team1_id='"+str(ghost0)+"' and team2_id='"+str(ghost1)+"') or (team1_id='"+str(ghost1)+"' and team2_id='"+str(ghost0)+"')"
        cursor = mydb.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        cno=int(records[0][0])
        try:         
          mycursor = mydb.cursor()
          sql = "REPLACE INTO casumo(date, leauge_id, leauge_name,l_id, team_1_id, team_1, t1_id, team_1_odds, team_2_id, team_2, t2_id, team_2_odds, sports_name, game_id, uni) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
          val = (date_csm,leauge_id_csm,leauge_name_csm,prince,team1_id_csm,team1_name_csm,t1_currunt_id,team1_odds_csm,team2_id_csm,team2_name_csm,t2_currunt_id,team2_odds_csm,sports_name_csm,cno,uni)  
          mycursor.execute(sql, val)
          mydb.commit()
          print(mycursor, "record REPLACEed.")
        except:
          print("Error: unable to REPLACE data")
        mycursor = mydb.cursor()
        sql_select_Query="UPDATE team_master SET casumo_team_id = '{}' WHERE  team_name ='{}'".format(team1_id_csm, team1_name_csm)
        mycursor.execute(sql_select_Query)
        mydb.commit()
        sql_select_Query="UPDATE team_master SET casumo_team_id = '{}' WHERE  team_name ='{}'".format(team2_id_csm, team2_name_csm)
        mycursor.execute(sql_select_Query)
        mydb.commit()
        
        sql_select_Query="UPDATE finaltable SET casumo1 = '{}' WHERE  uni ='{}'".format(team1_odds_csm, un1)
        mycursor.execute(sql_select_Query)
        mydb.commit()
        sql_select_Query="UPDATE finaltable SET casumo2 = '{}' WHERE  uni ='{}'".format(team2_odds_csm, un1)
        mycursor.execute(sql_select_Query)
        mydb.commit()
        
        
        
        

def migrate():
  try:  
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE game_master(id INT(6) AUTO_INCREMENT PRIMARY KEY, team1_id INT(6), team2_id INT(6), date VARCHAR(50))")
    print("Table created successfully")
    
    sql="ALTER TABLE game_master ADD UNIQUE unique_index(team1_id, team2_id, date)"
    mycursor.execute(sql)
    print("Table Alter successfully")
  except:
    print("Error creating table:")
    
  try:
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE vs_master(id INT(6) PRIMARY KEY, name  VARCHAR(60) UNIQUE, gameodds VARCHAR(60))")
    print("Table created successfully")
  except:
    print("Error creating table:")
      
  try:
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE sports_master(id INT(6) PRIMARY KEY, name  VARCHAR(60) UNIQUE, game_id INT(6))")
    print("Table created successfully")
  except:
    print("Error creating table:")
 
  try:
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE team_master(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, team_name  VARCHAR(60), game_id INT(6), onex_team_id VARCHAR(60), casumo_team_id VARCHAR(60), leon_team_id VARCHAR(60), libra_team_id VARCHAR(60), comeon_team_id VARCHAR(60), wazamba_team_id VARCHAR(60))")
    print("Table created successfully")
  except:
    print("Error creating table:")
 
  try:
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE league_master(id INT(6) PRIMARY KEY, name  VARCHAR(60) UNIQUE, game_id INT(6))")
    print("Table created successfully")
  except:
    print("Error creating table:")    
  
  try:
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE comeongame(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,date VARCHAR(30), leauge_id VARCHAR(30), leauge_name VARCHAR(60), l_id VARCHAR(30), team_1_id VARCHAR(30), team_1 VARCHAR(30), t1_id VARCHAR(30), team_1_odds VARCHAR(30), team_2_id VARCHAR(30), team_2 VARCHAR(30), t2_id VARCHAR(30), team_2_odds VARCHAR(30), sports_name VARCHAR(30), game_id INT(6), uni VARCHAR(100) UNIQUE)")
    print('Table created successfully')
  except:
    print('Error creating table:')
  try:
    mycursor.execute("CREATE TABLE 1xbet(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, date VARCHAR(50), leauge_id VARCHAR(30), leauge_name VARCHAR(60), l_id VARCHAR(30), team_1_id VARCHAR(30), team_1 VARCHAR(30), t1_id VARCHAR(30), team_1_odds VARCHAR(30), team_2_id VARCHAR(30), team_2 VARCHAR(30), t2_id VARCHAR(30), team_2_odds VARCHAR(30), team_x_odds VARCHAR(30), sports_name_1x VARCHAR(30), game_id INT(6),uni VARCHAR(100) UNIQUE )")
    mycursor = mydb.cursor()
    print('Table created successfully')
  except:
    print('Error creating table:')
  try:
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE wazamba(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,date VARCHAR(30), leauge_id VARCHAR(30), leauge_name VARCHAR(60), l_id VARCHAR(30), team_1_id VARCHAR(30), team_1 VARCHAR(30), t1_id VARCHAR(30), team_1_odds VARCHAR(30), team_2_id VARCHAR(30), team_2 VARCHAR(30), t2_id VARCHAR(30), team_2_odds VARCHAR(30), sports_name VARCHAR(30), game_id INT(6), uni VARCHAR(100) UNIQUE )")
    print("Table created successfully")
  except:
    print("Error creating table:")    
  try:
      mycursor = mydb.cursor()
      mycursor.execute("CREATE TABLE leonbet(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, date VARCHAR(50), leauge_id VARCHAR(30), leauge_name VARCHAR(60), l_id VARCHAR(30), team_1_id VARCHAR(30), team_1 VARCHAR(30), t1_id VARCHAR(30), team_1_odds VARCHAR(30), team_2_id VARCHAR(30), team_2 VARCHAR(30), t2_id VARCHAR(30), team_2_odds VARCHAR(30), sports_name VARCHAR(30), game_id INT(6), uni VARCHAR(100) UNIQUE)")
      print("Table created successfully")
  except:
      print("Error creating table:")   
  try:
      mycursor = mydb.cursor()
      mycursor.execute("CREATE TABLE librabet(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,date VARCHAR(30), leauge_id VARCHAR(30), leauge_name VARCHAR(60),l_id VARCHAR(30), team_1_id VARCHAR(30), team_1 VARCHAR(30),t1_id VARCHAR(30), team_1_odds VARCHAR(30), team_2_id VARCHAR(30), team_2 VARCHAR(30),t2_id VARCHAR(30), team_2_odds VARCHAR(30), sports_name VARCHAR(30), game_id INT(6),uni VARCHAR(100) UNIQUE)")
      print("Table created successfully")
  except:
      print("Error creating table:")
  try:
      mycursor = mydb.cursor()
      mycursor.execute("CREATE TABLE casumo(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,date VARCHAR(30), leauge_id VARCHAR(30), leauge_name VARCHAR(60), l_id VARCHAR(30), team_1_id VARCHAR(30), team_1 VARCHAR(30), t1_id VARCHAR(30), team_1_odds VARCHAR(30), team_2_id VARCHAR(30), team_2 VARCHAR(30),t2_id VARCHAR(30), team_2_odds VARCHAR(30), sports_name VARCHAR(30), game_id INT(6), uni VARCHAR(100) UNIQUE)")
      print("Table created successfully")
  except:
      print("Error creating table:")       
  
  try:
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE finaltable(id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, date VARCHAR(30), team1_name VARCHAR(30), team2_name VARCHAR(60), onex1 VARCHAR(30), onex2 VARCHAR(30), casumo1 VARCHAR(30), casumo2 VARCHAR(30), comeon1 VARCHAR(30), comeon2 VARCHAR(30), leone1 VARCHAR(30),leone2 VARCHAR(30), libra1 VARCHAR(30), libra2 VARCHAR(30), waz1 VARCHAR(30), waz2 VARCHAR(30),uni VARCHAR(100) UNIQUE)")
    print("Table created successfully")
  except:
    print("Error creating table:") 




def proxy():
    li=list()
    url='https://free-proxy-list.net/'
    page=requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    value = soup.find(class_="modal-body")
    value=value.text
    data=value.split('\n')
    data.reverse()
    data.pop()
    data.pop()

    for i in range(len(data)):
        n=data[i]
        if n != '':

          link='https://{}'.format(n)
          li.append(link)   
    return li 
  
def location(ip_address):
  try:
    request_url = 'https://geolocation-db.com/jsonp/' + ip_address
    response = requests.get(request_url)
    result = response.content.decode()
    result = result.split("(")[1].strip(")")
    result  = json.loads(result)
    print(result)
  except:
    pass


def datascrap():
  li=proxy()
  c=random.choice(li)
  n=c.split('//')[1]
  n=n.split(':')[0]
  print('Your IP Locations:')
  location(n)
  try:
    match1xbet(c)
  except:
    pass
  try:
    matchcomeonbet(c)
  except:
    pass
  try:
    leon_bet(c)
  except:
    pass
  try:
    casumo(c)
  except:
    pass
  try:
    librabet(c)
  except:
    pass
  try:
    matchwazamba(c)
  except:
    pass





def que():
  date1=str(datetime.now())
  date=date1[0:10]
  sql ='select * from finaltable where date like "%s"'%date
  cursor = mydb.cursor()
  cursor.execute(sql)
  records = cursor.fetchall()
  return records


def mail_send():
    table='''
        <table style="  white-space:nowrap; border: 1px solid black; border-collapse: collapse; vertical-align:top">
          <tr style="  white-space:nowrap; border: 1px solid black; border-collapse: collapse; vertical-align:top">
              <th style="  white-space:nowrap; border: 1px solid black; border-collapse: collapse; vertical-align:top"><b>Date</b></th>
              <th style="  white-space:nowrap; border: 1px solid black; border-collapse: collapse; vertical-align:top"><b>Team1 name</b></th>
              <th style="  white-space:nowrap; border: 1px solid black; border-collapse: collapse; vertical-align:top"><b>Team2 name</b></th>
              <td style="  white-space:nowrap; border: 1px solid black; border-collapse: collapse; vertical-align:top"><b>Bookie 1 Name</b></td>
              <td style="  white-space:nowrap; border: 1px solid black; border-collapse: collapse; vertical-align:top"><b>Bookie 2 Name</b></td>
              <td style="  white-space:nowrap; border: 1px solid black; border-collapse: collapse; vertical-align:top"><b>Bookie 1 odds</b></td>
              <td style="  white-space:nowrap; border: 1px solid black; border-collapse: collapse; vertical-align:top"><b>Bookie 2 odds</b></td>
              <td style="  white-space:nowrap; border: 1px solid black; border-collapse: collapse; vertical-align:top"><b>profit</b></td>
          </tr>
            
              '''
    r=que()
    li, li1, li2=list(), list(), list()
    for i in r:
      id=i[0]
      date=i[1]
      t1name=i[2]
      t2name=i[3]
      onex1=i[4]
      onex2=i[5]
      casumo1=i[6]
      casumo2=i[7]
      comeongame1=i[8]
      comeongame2=i[9]
      leonebet1=i[10]
      leonebet2=i[11]
      librabet1=i[12]
      librabet2=i[13] 
      wazamba1=i[14]
      wazamba2=i[15]
      if id not in li:
        li.append(id)
        d=date
        t1=t1name
        t2=t2name
        li1.append(onex1)
        li2.append(onex2)

        li1.append(casumo1)
        li2.append(casumo2)
        
        li1.append(comeongame1)
        li2.append(comeongame2)

        li1.append(leonebet1)
        li2.append(leonebet2)

        li1.append(librabet1)
        li2.append(librabet2)

        li1.append(wazamba1)
        li2.append(wazamba2)
        new=['onexbet','casumo','comeongame','leonebet','librabet','wazamba']
        for i in range(len(li1)):
          for j in range(len(li2)):
              stake=10
              try:
                team1=float(li1[i])
                team2=float(li2[j])
                  
                stake1=stake/(1+(team1/team2))
                stake2=stake/(1+(team2/team1))
                payout1=stake1*team1
                payout1=round(payout1,2)
                totalprofite=payout1-stake
                totalprofite=round(totalprofite,2)
                if totalprofite>0:
                  
                  totalprofiteper=(totalprofite*100)/stake
                  bookie1=new[i]
                  bookie2=new[j]
                  stake1=round(stake1,2)
                  stake2=round(stake2,2)
                  totalprofite=round(totalprofite,2)
                  totalprofiteper=round(totalprofiteper,2)
                  x='''
                  stack1 : {}<br>
                  stack2 : {}<br>
                  profit : {}<br>
                  profit percentage : {}%<br>
                  
                  '''.format(stake1,stake2,totalprofite,totalprofiteper)
                  table1='''
                        <tr style="  white-space:nowrap; border: 1px solid black; border-collapse: collapse; vertical-align:top">
                          <td style="  white-space:nowrap; border: 1px solid black; border-collapse: collapse; vertical-align:top">{}</td>
                          <td style="  white-space:nowrap; border: 1px solid black; border-collapse: collapse; vertical-align:top">{}</td>
                          <td style="  white-space:nowrap; border: 1px solid black; border-collapse: collapse; vertical-align:top">{}</td>
                          <td style="  white-space:nowrap; border: 1px solid black; border-collapse: collapse; vertical-align:top">{}</td>
                          <td style="  white-space:nowrap; border: 1px solid black; border-collapse: collapse; vertical-align:top">{}</td>
                          <td style="  white-space:nowrap; border: 1px solid black; border-collapse: collapse; vertical-align:top">{}</td>
                          <td style="  white-space:nowrap; border: 1px solid black; border-collapse: collapse; vertical-align:top">{}</td>
                          <td style="  white-space:nowrap; border: 1px solid black; border-collapse: collapse; vertical-align:top">{}</td>
                        </tr>
                      '''.format(d,t1,t2,bookie1,bookie2,team1,team2,x)
                  x=str()
                  table=table+table1
              except:
                pass
        li1=list() 
        li2=list() 
    table=table+"""
          </table>"""
    with open('/home/jstechno-8/run/config.json') as json_file:
      json_data = json.load(json_file)
    your_email=json_data[0]['email']
    your_password=json_data[0]['password']
    emails=json_data[0]['receiver']
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(your_email, your_password)
    names = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
MIME-Version: 1.0
Content-type: text/html
Subject:Arbitrage Opportunity

Hello Sir/ma'am

<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">
 
<body style="margin:0;padding:0;word-spacing:normal;background-color:#FFFFFF;">
 {}
</body>
</html>

""".format(table)
    message = "Hello " + names
    server.sendmail(your_email, emails, message)
    print("Email has been sent!")

# def send():
#    mail_send()
def send():
 d=str(datetime.now())
 if d[11:16]=='09:59':
   schedule.every().day.at("10:00").do(mail_send)
   sleep(60)
   schedule.run_pending()
 else:
   print('time',d[11:16])


# start=str(datetime.now())

if len(sys.argv) <= 1:
    print('you havent given enough info')
else:
    function = sys.argv[1]
    if function == 'datascrap':
        if len(sys.argv)==2:
          datascrap()

if len(sys.argv) <= 1:
    print('you havent given enough info')
else:
    function = sys.argv[1]
    if function == 'migrate':
        if len(sys.argv)==2:
          migrate()
  
if len(sys.argv) <= 1:
    print('you havent given enough info')
else:
    function = sys.argv[1]
    if function == "send_mail":
        if len(sys.argv)==2:
          send()      
       
         
# end=str(datetime.now())
# start=start[14:19]
# end=end[14:19]
# start=start.split(':')
# end=end.split(':')
# start=float(str(start[0])+"."+str(start[1]))
# end=float(str(end[0])+"."+str(end[1]))

# print('start time : ',start)
# print('end time : ',end)
# print('total time : ',end-start)
