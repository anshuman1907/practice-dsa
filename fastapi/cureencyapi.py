from fastapi import FastAPI,HTTPException
import psycopg2 
import uvicorn


from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  
    allow_methods=["*"],
    allow_headers=["*"],
)










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

def get_data(query):
    conn = get_db_con()
    cursor=conn.cursor()
    cursor.execute(query=query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data


@app.get("/ans")
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
        raise HTTPException(status_code=404,detail="cuureeccny not found")
    

    from_code,from_name,from_symbol,from_factor=  from_data
    to_code,to_name,to_symbol,to_factor=to_data


    rate = from_factor/to_factor

    return{
            "from": {"code":from_code,"name":from_name,"symbol":from_symbol,}
            ,

            
            "to":{"code":to_code,"name":to_name,"symbol":to_symbol},
            "rate":rate
        }
    


@app.get("/list-currencies")
def list_cur():


    if __name__ == "__main__":
        uvicorn.run("cureencyapi:app", host="127.0.0.1", port=8000, reload=True)




