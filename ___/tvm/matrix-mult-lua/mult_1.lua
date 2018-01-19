local ap = require('ap')

local function get_cell(name, i, j)
    return ap.tvm.table_get_number(name .. tostring(i), j)
end

local function set_cell(name, i, j, value)
    ap.tvm.table_set(name .. tostring(i), j, value)
end

local function length(name, i)
    return ap.tvm.length(name .. tostring(i))
end

local function write_matrix_to_tvm(name, matrix_prototype)
    for i = 1,#matrix_prototype do
        for j = 1,#(matrix_prototype[i]) do
            set_cell(name, i, j, matrix_prototype[i][j])
        end
    end
end

local function read_matrix_from_tvm(name, w, h)
    local res = {}
    for i = 1,w do
        res[i] = {}
        for j = 1,h do
            res[i][j] = get_cell(name, i, j)
        end
    end
    return res
end

local function print_matrix(mat)
    for k, v in pairs(mat) do
        for k1, v1 in pairs(v) do
            io.write(v1, "\t ")
        end
        io.write("\n")
    end
end

local json = require('dkjson')
local m1 = json.decode(ap.tvm.get_number(ap.args[1]))
local m2 = json.decode(ap.tvm.get_number(ap.args[2]))

assert(m1 ~= nil)
assert(m2 ~= nil)

write_matrix_to_tvm("m1", m1)
write_matrix_to_tvm("m2", m2)

for i = 1,#m1 do
    ap.call("mult_2.lua", {"m1", "m2", tostring(i), "m3"})
end

print("async workers supplied")

ap.await_all()

local m3 = read_matrix_from_tvm("m3", #m1, #m2)
ap.tvm.set(ap.args[3], json.encode(m3))