#import multiprocessing
#workers = multiprocessing.cpu_count() * 2 + 1

worker_class = 'aiohttp.worker.GunicornWebWorker'
forwarded_allow_ips = '*'
secure_scheme_headers = {'X-FORWARDED-PROTO': 'https'}
