import redis
import threading
import random

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

def add_score(player_id, score):
    redis_client.zadd('game_ranking', {player_id: score})

def get_rank(player_id):
    rank = redis_client.zrevrank('game_ranking', player_id)
    return rank + 1 if rank is not None else None

def simulate_user(player_id):
    for _ in range(10):
        score = random.randint(1, 100)
        add_score(player_id, score)
        rank = get_rank(player_id)
        print(f"Player {player_id}: Score: {score}, Rank: {rank}")

threads = []
for i in range(15):
        player_id = f"player{i}"
        thread = threading.Thread(target=simulate_user, args=(player_id,))
        threads.append(thread)
        thread.start()

for thread in threads:
    thread.join()


