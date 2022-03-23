# %%
import redis


pool = redis.ConnectionPool(
    host='192.168.1.246', port=6379, password='gssx208', decode_responses=True)
r = redis.Redis(host='192.168.1.246', port=6379,
                password='gssx208', decode_responses=True)

r.select(7)
x = r.get('otc-server:object-key:9c7ca9f32ae9cc99ce46a5728d049336')
print(x)

# %%
