import ap

def get_cell(name, i, j):
    return ap.tvm.table_get_number(name + str(i), j)

def set_cell(name, i, j, value):
    ap.tvm.table_set(name + str(i), j, value)

def mat_length(name, i):
    return ap.tvm.length(name + str(i))

m1 = ap.args["m1_id"]
m2 = ap.args["m2_id"]
i = int(ap.args["count"])

m3 = ap.args["m_res"]

m1_length = mat_length(m1, 0)
m2_length = mat_length(m2, 0)

for j in range(m2_length):
    num = get_cell(m1, i, 0) * get_cell(m2, 0, j)
    for n in range(1, m1_length):
        num = num + get_cell(m1, i, n) * get_cell(m2, n, j)
    set_cell(m3, i, j, num)
