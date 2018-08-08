import slack
import logging
import os
import time
import uuid
from decimal import Decimal

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # 'SINGLE', 'DOUBLE', 'LONG'
    click_type = event.get('clickType', 'SINGLE')

    if click_type == 'SINGLE':
        coffee_brewing(event, context)
    elif click_type == 'DOUBLE':
        coffee_needed(event, context)
    elif click_type == 'LONG':
        coffee_ready(event, context)

    return

def coffee_brewing(event, context):
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
    slack_post = 'Coffee is brewing'
    # Post to slack
    slack.post_text_message(slack_token, slack_channel, slack_post)

    return

def coffee_needed(event, context):
    ## Environment
    #
    # Required
    slack_token = os.environ['SLACK_TOKEN']
    aws_region = os.environ['AWS_REGION']
    slack_channel = os.environ.get('SLACK_CHANNEL', 'general')
    #
    ## End Environment

    #session = boto3.Session(region_name=aws_region)
    slack_post = 'Please make coffee!!!'
    # Post to slack
    slack.post_text_message(slack_token, slack_channel, slack_post)

    return

def coffee_ready(event, context):
    ## Environment
    #
    # Required
    slack_token = os.environ['SLACK_TOKEN']
    aws_region = os.environ['AWS_REGION']
    slack_channel = os.environ.get('SLACK_CHANNEL', 'general')
    #
    ## End Environment

    #session = boto3.Session(region_name=aws_region)
    slack_post = 'Is coffee ready?'
    # Post to slack
    slack.post_text_message(slack_token, slack_channel, slack_post)

    return