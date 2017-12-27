import json
import random

import ap
import math


def rnd_matrix(w, h):
    mtx = []
    for i in range(w):
        row = []
        mtx.append(row)
        for j in range(h):
            row.append(math.floor(random.random() * 10 - 5))
    return mtx

N = 7
m1 = rnd_matrix(N, N)
m2 = rnd_matrix(N, N)

ap.tvm.set("m1", json.dumps(m1))
ap.tvm.set("m2", json.dumps(m2))

io_value_id = ap.new_io('{"command":"kv"}', 'http://api.acapella.ru/astorage/v2/kv/keys/matrix_mult')
ap.call("mult_1.py", {"m1_id": "m1", "m2_id": "m2", "io_value_id": io_value_id})
ap.commit()