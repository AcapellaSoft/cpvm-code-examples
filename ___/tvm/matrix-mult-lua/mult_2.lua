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

local m1 = ap.args[1]
local m2 = ap.args[2]
local i = tonumber(ap.args[3])

local m3 = ap.args[4]

local m1_length = length(m1, 1)
local m2_length = length(m2, 1)
for j = 1, m2_length do
    local num = get_cell(m1, i, 1) * get_cell(m2, 1, j)
    for n = 2, m1_length do
        num = num + get_cell(m1, i, n) * get_cell(m2, n, j)
    end
    set_cell(m3, i, j, num)
end
