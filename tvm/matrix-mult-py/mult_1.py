import ap

def get_cell(name, i, j):
    return ap.tvm.table_get(name + str(i), j)

def set_cell(name, i, j, value):
    ap.tvm.table_set(name + str(i), j, value)

def length(name, i):
    return ap.tvm.length(name + str(i))

def write_matrix_to_tvm(name, matrix_prototype):
    for i in range(len(matrix_prototype)):
        for j in range(len(matrix_prototype[i])):
            set_cell(name, i, j, matrix_prototype[i][j])

def read_matrix_from_tvm(name, w, h):
    res = []
    for i in range(w):
        row = []
        res.append(row)
        for j in range(h):
            row.append(get_cell(name, i, j))
    return res

def print_matrix(mat):
    for i in mat:
        for j in i:
            print('%5s' % j, end="")
        print()

import json
m1 = json.loads(ap.tvm.get(ap.args["m1_id"]))
m2 = json.loads(ap.tvm.get(ap.args["m2_id"]))

write_matrix_to_tvm("m1", m1)
write_matrix_to_tvm("m2", m2)

for i in range(0,len(m1)):
    ap.call_async("mult_2.py", {"m1_id": "m1", "m2_id": "m2", "count": str(i), "m_res": "m3"})

print("async workers supplied")

ap.await_all()

m3 = read_matrix_from_tvm("m3", len(m1), len(m2))
ap.tvm.set(ap.args["io_value_id"], json.dumps(m3))

print_matrix(m3)