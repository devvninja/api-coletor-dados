
import flask
from flask import request
from datetime import datetime, timedelta
import oracledb

################################################ Configuração ORACLE ########################################################

oracledb.init_oracle_client()
username="SEGREDO :)"
userpwd = "SEGREDO :)"
host = "SEGREDO :)"
port = 1521
service_name = "ORCL"


dsn = f'{username}/{userpwd}@{host}:{port}/{service_name}'

######################################################## INIT ########################################################

#Flask configuration
versao=''
app = flask.Flask(__name__)
app.secret_key = 'key'
#app.secret_key = os.environ['SECRETKEY']
#Flask-Login configuration

#Database configuration
#databaseOBJ=database.postgresDatabase(user=os.environ['DBUSER'], password=os.environ['DBPASSWORD'], host=os.environ['DBHOST'], dbname=os.environ['DBNAME'])
#databaseOBJ=database.postgresDatabase(host='localhost')

######################################################## CRUD RESOURCES ####################################################

@app.route('/api/Machines/Receive', methods=['POST'])
def api():
    dt = datetime.now()
    now = datetime.now()
    tm = datetime.timestamp(now)
    dtstring = dt.strftime ('%Y-%m-%d %H:%M:%S')
    print('acessou')
    if flask.request.method == 'POST':
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json
            print(json)

            pc1=(json['Record'][0][3])
            t1=(json['Record'][1][3])
            pc2=(json['Record'][3][3])
            t2=(json['Record'][4][3])
            pc3=(json['Record'][6][3])
            t3=(json['Record'][7][3])
            pc4=(json['Record'][9][3])
            t4=(json['Record'][10][3])

            tempo1= tm - int(t1/1000)
            tempo2= tm - int(t2/1000)
            tempo3= tm - int(t3/1000)
            tempo4= tm - int(t4/1000)


            dt_fim = datetime.fromtimestamp(tm)
            dt_inicio1 = datetime.fromtimestamp(tempo1)
            dt_inicio2 = datetime.fromtimestamp(tempo2)
            dt_inicio3 = datetime.fromtimestamp(tempo3)
            dt_inicio4 = datetime.fromtimestamp(tempo4)

            if(pc1==1):
                with oracledb.connect(dsn) as connection:
                    with connection.cursor() as cursor:
                #        sql = """select * from sankhya.pecas"""

                        dados_insert = (1, str(dtstring),str(dtstring) )

                        sql = "INSERT INTO SANKHYA.PECAS (ID, ID_MAQUINA, DATA_INICIO, DATA_FIM) \
                        VALUES ((SELECT MAX(ID)+1 FROM SANKHYA.PECAS), :2, TO_DATE(:3, 'YYYY-MM-DD HH24:MI:SS'), TO_DATE(:4, 'YYYY-MM-DD HH24:MI:SS'))"

                        cursor.execute(sql, dados_insert)
                        connection.commit()
            
                #databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dt_inicio1) +"','"+ str(dt_fim) +"', 1)")
                print('Adicionado maquina 1')

            elif(pc2==1):
                with oracledb.connect(dsn) as connection:
                    with connection.cursor() as cursor:
                #        sql = """select * from sankhya.pecas"""

                        dados_insert = (2, str(dtstring),str(dtstring) )

                        sql = "INSERT INTO SANKHYA.PECAS (ID, ID_MAQUINA, DATA_INICIO, DATA_FIM) \
                        VALUES ((SELECT MAX(ID)+1 FROM SANKHYA.PECAS), :2, TO_DATE(:3, 'YYYY-MM-DD HH24:MI:SS'), TO_DATE(:4, 'YYYY-MM-DD HH24:MI:SS'))"

                        cursor.execute(sql, dados_insert)
                        connection.commit()
                #databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dt_inicio2) +"','"+ str(dt_fim) +"', 2)")
                print('Adicionado maquina 2')

            elif(pc3==1):
                with oracledb.connect(dsn) as connection:
                    with connection.cursor() as cursor:
                #        sql = """select * from sankhya.pecas"""

                        dados_insert = (3, str(dtstring),str(dtstring) )
                        print(dados_insert)
                        sql = "INSERT INTO SANKHYA.PECAS (ID, ID_MAQUINA, DATA_INICIO, DATA_FIM) \
                        VALUES ((SELECT MAX(ID)+1 FROM SANKHYA.PECAS), :2, TO_DATE(:3, 'YYYY-MM-DD HH24:MI:SS'), TO_DATE(:4, 'YYYY-MM-DD HH24:MI:SS'))"

                        cursor.execute(sql, dados_insert)
                        connection.commit()
                #databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dt_inicio3) +"','"+ str(dt_fim) +"', 3)")
                print('Adicionado maquina 3')

            elif(pc4==1):
                with oracledb.connect(dsn) as connection:
                    with connection.cursor() as cursor:
                #        sql = """select * from sankhya.pecas"""

                        dados_insert = (4, str(dtstring),str(dtstring) )

                        sql = "INSERT INTO SANKHYA.PECAS (ID, ID_MAQUINA, DATA_INICIO, DATA_FIM) \
                        VALUES ((SELECT MAX(ID)+1 FROM SANKHYA.PECAS), :2, TO_DATE(:3, 'YYYY-MM-DD HH24:MI:SS'), TO_DATE(:4, 'YYYY-MM-DD HH24:MI:SS'))"

                        cursor.execute(sql, dados_insert)
                        connection.commit()
                #databaseOBJ.writeRaw("insert into pecas(data_inicio, data_fim, id_maquina) VALUES('"+ str(dt_inicio4) +"','"+ str(dt_fim) +"', 4)")
                print('Adicionado maquina 4')
            return json
        else:
            return 'Content-Type not supported!'
    else:
        flask.abort(405)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
