
# redis
# from redis.sentinel import Sentinel
# from booking_server.settings import REDIS_SENTINEL, REDIS_SNS_CLUSTER_NAME, REDIS_SENTINEL_DB

# sentinel = None
# _cached_master_client = None
# _cached_slave_client = None


# def get_redis_conn(readonly=False):
#     global sentinel, _cached_master_client, _cached_slave_client
#     if not sentinel:
#         sentinel = Sentinel(REDIS_SENTINEL, socket_timeout=0.1)
#     if not _cached_master_client:
#         _cached_master_client = sentinel.master_for(REDIS_SNS_CLUSTER_NAME, db=REDIS_SENTINEL_DB)
#     if not _cached_slave_client:
#         _cached_slave_client = sentinel.slave_for(REDIS_SNS_CLUSTER_NAME, db=REDIS_SENTINEL_DB)
#     return _cached_slave_client if readonly else _cached_master_client
