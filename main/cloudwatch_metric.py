import datetime
import boto3

def put_readytime(brewtime):

   now = datetime.datetime.now()
   cloudwatch = boto3.client('cloudwatch')

   result = cloudwatch.put_metric_data(
       MetricData = [
           {
               'MetricName': 'CoffeeReady',
               'Dimensions': [
                   {
                       'Name': 'CoffeeBrewing',
                       'Value': 'CoffeeReady'
                   },
               ],
			   'Timestamp': now + datetime.timedelta(minutes = brewtime),
               'Unit': 'None', 
               'Value': 300.0
           },
       ],
       Namespace='coffeebot-prod'
   )

   return result