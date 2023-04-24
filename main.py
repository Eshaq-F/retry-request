from os import system
from vgang_job.app import retry_request
from logging import getLogger

if __name__ == "__main__":
    system('celery worker -A vgang_job.app.app -l info --pool solo')
    logger = getLogger(__name__)
    result = retry_request.apply_async(args=['https://uat.vgang.io/api/vgang-core/v1/common/sample-failing-request'])
    logger.info(result.get())
