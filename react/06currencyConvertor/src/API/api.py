from fastapi import FastAPI,HTTPException
import psycopg2
import json



app = FastAPI()


db_host= "127.0.0.1"
db_name="ornaz"
db_user="ornaz"
db_pass="ornaz"


def get_db_con():
    conn= psycopg2.connect(
        host= db_host,
        database= db_name,
        user= db_user,
        password= db_pass
    )
    return conn

@app.get("/")
def convert_curr(from_code:str,to_code:str):
    conn =get_db_con()
    cursor=conn.cursor()
    query="Select code ,name ,symbol ,factor from currencies_currency where code= %s and is_active=true "

    cursor.execute(query,(from_code.upper(),))

    from_data= cursor.fetchone()
    

    cursor.execute(query,(to_code.upper(),))
    to_data= cursor.fetchone()
    
    cursor.close()
    conn.close()


    if not from_data or not to_data:
        raise HTTPException(status_code=404,detail="cuureeccn not ffound")
    

        from_code,from_name,from_symbol,from_factor= from_data,to_data,to_name,to_symbol,to_factor=to_data


        rate = from_factor/to_factor

        return{
            "from": {"code":from_code,"name":from_name,"symbol":from_symbol,},"to":{"code":to_code,"name":to_name,"symbol":to_symbol},"rate":rate
        }