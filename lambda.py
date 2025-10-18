import json
import boto3
import pymysql 
import csv
from io import StringIO
from datetime import datetime

DB_HOST = "database-1.cd8w4cuu6a79.us-west-1.rds.amazonaws.com"  # host que ves en DBeaver
DB_USER = "admin"  # usuario
DB_PASS = "admin123123"
DB_NAME = "awsdata"  
BUCKET_NAME = "xideralaws-curso-jorge"  
TABLE_NAME = "personas"

s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        # Conexión a la BD
        connection = pymysql.connect(
            host="database-1.cd8w4cuu6a79.us-west-1.rds.amazonaws.com",
            user="admin",
            password="admin123123",
            database="awsdata",
            connect_timeout=10
        )
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(f"SELECT * FROM {"personas"};")
        data = cursor.fetchall()

        if not data:
            return {"statusCode": 200, "body": "No se encontraron registros."}

        # Crear CSV
        csv_buffer = StringIO()
        writer = csv.DictWriter(csv_buffer, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

        # Nombre archivo
        filename = f"personas_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

        # Subir a S3
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=filename,
            Body=csv_buffer.getvalue(),
            ContentType='text/csv'
        )

        cursor.close()
        connection.close()

        return {
            "statusCode": 200,
            "body": json.dumps(f"Archivo {filename} guardado en S3://{BUCKET_NAME}")
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps(f"Error: {str(e)}")
        }
