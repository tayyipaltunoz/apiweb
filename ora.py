import subprocess

# Bağlantı parametreleri
username = "BLACKLIST"
password = "Blockchain_frd123"
hostname = "CONSDB3SCAN.TT-TIM.TR"
port = 1461
service = "BCLOG"

# SQL*Plus'ı başlat
sqlplus_process = subprocess.Popen(["sqlplus", "-s", "-l", username, password, "@hostname:port/service"], stdout=subprocess.PIPE)

# Sorguyu çalıştır
sqlplus_process.communicate('SELECT /*+parallel(4)*/ a.*,b.*,c.*,(MOBIL+GENISBANT+SABIT) as TOPLAM from \
(select count(*) as "MOBIL" from DWH_TRANSACTION_QUEUE_HISTORY where PROCESS_TIME > sysdate -1  and transaction_partner_id=511 )a, \
(select count(*) as "GENISBANT" from  DWH_TRANSACTION_QUEUE_HISTORY where PROCESS_TIME > sysdate -1  and transaction_partner_id=510 )b, \
(select count(*) as "SABIT" from DWH_TRANSACTION_QUEUE_HISTORY where PROCESS_TIME > sysdate -1  and transaction_partner_id=500 )c ;')

# Sonuçları alın
results = sqlplus_process.communicate()[0].decode("utf-8").strip()

# Sonuçları yazdır
for row in results.splitlines():
    print(row)

# SQL*Plus'ı kapat
sqlplus_process.terminate()


import cx_Oracle

# Bağlantı parametreleri
dsn = "oracle://username:password@hostname:port/databasename"

# Bağlantı oluştur
conn = cx_Oracle.connect(dsn)

# Sorguyu çalıştır
cursor = conn.cursor()
cursor.execute("SELECT * FROM tablename")

# Sonuçları alın
results = cursor.fetchall()

# Sonuçları yazdırın
for result in results:
    print(result)

# Bağlantıyı kapatın
conn.close()
