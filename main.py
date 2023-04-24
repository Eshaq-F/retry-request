from vgang_job.app import retry_request
from logging import getLogger

if __name__ == "__main__":
    logger = getLogger(__name__)
    print('>>> job started!')
    result = retry_request.apply_async(args=['https://uat.vgang.io/api/vgang-core/v1/common/sample-failing-request'])
    logger.info(result.get())
