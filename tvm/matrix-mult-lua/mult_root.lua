local ap = require('ap')
local json = require('dkjson')

local function rnd_matrix(w, h)
    local mtx = {}
    for i = 1, w do
        mtx[i] = {}
        for j = 1, h do
            mtx[i][j] = math.floor(math.random() * 10 - 5)
        end
    end
    return mtx
end

local N = 10
local m1 = rnd_matrix(N, N)
local m2 = rnd_matrix(N, N)

ap.tvm.set("m1", json.encode(m1))
ap.tvm.set("m2", json.encode(m2))

local io_value_id = ap.new_io('{"command":"kv"}', 'http://api.acapella.ru/astorage/v2/kv/keys/matrix_mult')
ap.call("mult_1.lua", {"m1", "m2", io_value_id})
ap.commit()