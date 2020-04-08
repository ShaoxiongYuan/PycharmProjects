from redis.sentinel import Sentinel

sentinel = Sentinel([('localhost', 26739)], socket_timeout=0.1)

master = sentinel.master_for('tedu', socket_timeout=0.1)
slave = sentinel.slave_for('tedu', socket_timeout=0.1)

master.set('mymaster', 'yes')

print(slave.get('mymaster'))
