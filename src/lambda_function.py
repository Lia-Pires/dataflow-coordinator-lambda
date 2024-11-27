import logging
import os
from utils import Utils


def lambda_handler(event, context):
    logging.info(f"Starting execution...")

    if event:
        print("Received event:", event)
        utils = Utils(event)
        queries = utils.process_data()
        data = utils.update_db(queries)

        return data

    return {"message: No event was received"}
