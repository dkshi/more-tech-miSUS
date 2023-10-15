import psycopg2
import json
import pandas as pd



conn = psycopg2.connect(database="postgres", user="postgres", password="qwerty", host="26.132.86.192",
                        port="5436")

with open("atms.json", encoding='utf-8') as file:
    data_atm = json.load(file)
with open("offices.json", encoding='utf-8') as file:
    data_offices = json.load(file)


# заполнеие office
cur = conn.cursor()
rko_map = {"есть РКО": True, "нет РКО": False}
for office in data_offices:
    office['rko'] = rko_map.get(office['rko'], False)
    cur.execute(
        "INSERT INTO offices (salepoint_name, address, rko, office_type, salepoint_format, suo_availability, has_ramp, latitude, longitude, metro_station, distance, kep, my_branch) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (office['salePointName'], office['address'], office['rko'], office['officeType'], office['salePointFormat'],
         office['suoAvailability'], office['hasRamp'], office['latitude'], office['longitude'], office['metroStation'],
         office['distance'], office['kep'], office['myBranch'])
    )

# заполнение таблицы offices_hours
open_hours_list = []
open_hours_dict = {}

for item in data_offices:
    open_hours_list.append(item['openHours'])

for i in range(len(open_hours_list)):
    open_hours_dict[i + 1] = open_hours_list[i]

for key, value in open_hours_dict.items():
    if value[0]['days'] == 'пн-чт':
        open_hours_dict[key] = [{'days': 'пн', 'hours': value[0]['hours']}, {'days': 'вт', 'hours': value[0]['hours']},
                                {'days': 'ср', 'hours': value[0]['hours']}, {'days': 'чт', 'hours': value[0]['hours']},
                                {'days': 'пт', 'hours': value[1]['hours']}, {'days': 'сб', 'hours': value[2]['hours']},
                                {'days': 'вс', 'hours': value[2]['hours']}]
    if value[0]['days'] == 'пн-пт':
        open_hours_dict[key] = [{'days': 'пн', 'hours': value[0]['hours']}, {'days': 'вт', 'hours': value[0]['hours']},
                                {'days': 'ср', 'hours': value[0]['hours']}, {'days': 'чт', 'hours': value[0]['hours']},
                                {'days': 'пт', 'hours': value[0]['hours']}, {'days': 'сб', 'hours': value[1]['hours']},
                                {'days': 'вс', 'hours': value[1]['hours']}]
    if value[0]['days'] == 'Не обслуживает ЮЛ':
        open_hours_dict[key] = [{'days': 'пн', 'hours': 'Нет обслуживания ЮЛ'},
                                {'days': 'вт', 'hours': 'Нет обслуживания ЮЛ'},
                                {'days': 'ср', 'hours': 'Нет обслуживания ЮЛ'},
                                {'days': 'чт', 'hours': 'Нет обслуживания ЮЛ'},
                                {'days': 'пт', 'hours': 'Нет обслуживания ЮЛ'},
                                {'days': 'сб', 'hours': 'Нет обслуживания ЮЛ'},
                                {'days': 'вс', 'hours': 'Нет обслуживания ЮЛ'}]

open_hours_data = []

for key in open_hours_dict:
    day_data = open_hours_dict[key]
    open_hours_data.append(
        [key,
         day_data[0]['hours'],
         day_data[1]['hours'],
         day_data[2]['hours'],
         day_data[3]['hours'],
         day_data[4]['hours'],
         day_data[5]['hours'],
         day_data[6]['hours']])


open_hours_query = """ 
         INSERT INTO offices_hours (
       office_id, monday, tuesday, wednesday, thursday,
    friday, saturday,sunday) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""
with conn.cursor() as cursor:
    cursor.executemany(open_hours_query, open_hours_data)

# заполнение ofiices_hours_individual
open_hoursINDIV_list = []
open_hoursINDIV_dict = {}

for item in data_offices:
    open_hoursINDIV_list.append(item['openHoursIndividual'])

for i in range(len(open_hoursINDIV_list)):
    open_hoursINDIV_dict[i + 1] = open_hoursINDIV_list[i]

for key, value in open_hoursINDIV_dict.items():
    if value[0]['days'] == 'пн-чт':
        open_hoursINDIV_dict[key] = [{'days': 'пн', 'hours': value[0]['hours']},
                                     {'days': 'вт', 'hours': value[0]['hours']},
                                     {'days': 'ср', 'hours': value[0]['hours']},
                                     {'days': 'чт', 'hours': value[0]['hours']},
                                     {'days': 'пт', 'hours': value[1]['hours']},
                                     {'days': 'сб', 'hours': value[2]['hours']},
                                     {'days': 'вс', 'hours': value[2]['hours']}]
    if value[0]['days'] == 'пн-пт':
        open_hoursINDIV_dict[key] = [{'days': 'пн', 'hours': value[0]['hours']},
                                     {'days': 'вт', 'hours': value[0]['hours']},
                                     {'days': 'ср', 'hours': value[0]['hours']},
                                     {'days': 'чт', 'hours': value[0]['hours']},
                                     {'days': 'пт', 'hours': value[0]['hours']},
                                     {'days': 'сб', 'hours': value[1]['hours']},
                                     {'days': 'вс', 'hours': value[1]['hours']}]
    if value[0]['days'] == 'Не обслуживает ФЛ':
        open_hoursINDIV_dict[key] = [{'days': 'пн', 'hours': 'Нет обслуживания ФЛ'},
                                     {'days': 'вт', 'hours': 'Нет обслуживания ФЛ'},
                                     {'days': 'ср', 'hours': 'Нет обслуживания ФЛ'},
                                     {'days': 'чт', 'hours': 'Нет обслуживания ФЛ'},
                                     {'days': 'пт', 'hours': 'Нет обслуживания ФЛ'},
                                     {'days': 'сб', 'hours': 'Нет обслуживания ФЛ'},
                                     {'days': 'вс', 'hours': 'Нет обслуживания ФЛ'}]

open_hoursINDIV_data = []
for key in open_hoursINDIV_dict:
    day_data = open_hoursINDIV_dict[key]
    open_hoursINDIV_data.append(
        [key,
         day_data[0]['hours'],
         day_data[1]['hours'],
         day_data[2]['hours'],
         day_data[3]['hours'],
         day_data[4]['hours'],
         day_data[5]['hours'],
         day_data[6]['hours']])
open_hoursINDIV_query = """
 INSERT INTO offices_hours_individual (
 office_id, monday, tuesday, wednesday, thursday,
 friday, saturday,sunday) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
 """


with conn.cursor() as cursor:
    cursor.executemany(open_hoursINDIV_query, open_hoursINDIV_data)

### заполнение atm и atm_services
atms_data = [(item["address"], item["latitude"], item["longitude"], item["allDay"]) for item in data_atm["atms"]]
atms_query = "INSERT INTO atms (address, latitude, longitude, all_day) VALUES (%s, %s, %s, %s)"
with conn.cursor() as cursor:
    cursor.executemany(atms_query, atms_data)
atms_services_data = []
i = 1
for item in data_atm["atms"]:
    service_data = item["services"]
    atms_services_data.append(
        [i,
         service_data["wheelchair"]["serviceCapability"],
         service_data["wheelchair"]["serviceActivity"],
         service_data["blind"]["serviceCapability"],
         service_data["blind"]["serviceActivity"],
         service_data["nfcForBankCards"]["serviceCapability"],
         service_data["nfcForBankCards"]["serviceActivity"],
         service_data["qrRead"]["serviceCapability"],
         service_data["qrRead"]["serviceActivity"],
         service_data["supportsUsd"]["serviceCapability"],
         service_data["supportsUsd"]["serviceActivity"],
         service_data["supportsChargeRub"]["serviceCapability"],
         service_data["supportsChargeRub"]["serviceActivity"],
         service_data["supportsEur"]["serviceCapability"],
         service_data["supportsEur"]["serviceActivity"],
         service_data["supportsRub"]["serviceCapability"],
         service_data["supportsRub"]["serviceActivity"]])
    i += 1

for i in range(len(atms_services_data)):
    for j in range(1, len(atms_services_data[i])):
        if atms_services_data[i][j] == 'UNKNOWN':
            atms_services_data[i][j] = None
        elif atms_services_data[i][j][:2] == 'UN':
            atms_services_data[i][j] = False
        else:
            atms_services_data[i][j] = True

atms_services_query = """
     INSERT INTO atms_services (
         atm_id, wheelchair_cap, wheelchair_act, blind_cap, blind_act,
         nfc_cap, nfc_act, qr_cap, qr_act, usd_cap, usd_act, chargerub_cap,
         chargerub_act, eur_cap, eur_act, rub_cap, rub_act
     ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
 """
with conn.cursor() as cursor:
    cursor.executemany(atms_services_query, atms_services_data)



cur = conn.cursor()
cur.execute("""
    INSERT INTO atms_load(atm_id, load)
     SELECT id, 0
     FROM atms
""")
cur = conn.cursor()
cur.execute("""
    INSERT INTO offices_load(office_id, load)
    SELECT id, 0
    FROM offices
""")
hours_predict.to_sql('hours_predict', engine, if_exists='replace')
cur.close()
conn.commit()
conn.close()

