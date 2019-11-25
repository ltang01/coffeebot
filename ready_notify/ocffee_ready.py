import slack
import logging
import os
#import time
#import uuid
#import cloudwatch_metric
#from decimal import Decimal

#logger = logging.getLogger()
#logger.setLevel(logging.INFO)



def coffee_ready_handler(event, context):
    
    coffee_ready(event, context)
		
    return

def coffee_ready(event, context):
    ## Environment
    #
    # Required
    slack_token = os.environ['SLACK_TOKEN']
    aws_region = os.environ['AWS_REGION']
    #
    # Optional
    slack_channel = os.environ.get('SLACK_CHANNEL', 'general')
    #
    ## End Environment

    #session = boto3.Session(region_name=aws_region)
    slack_post = '@here Coffee is ready!'
    # Post to slack
    slack.post_text_message(slack_token, slack_channel, slack_post)

    return

