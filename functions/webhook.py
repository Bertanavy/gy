import json

def handler(event, context):
    try:
        data = json.loads(event['body'])
        print("Пришёл сигнал:", data)  # Можно смотреть в логах Netlify

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Сигнал получен'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
