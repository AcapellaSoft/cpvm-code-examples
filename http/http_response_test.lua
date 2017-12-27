local ap = require 'ap'

local headers = {
    ["My-Header"] = "XYZ",
    ["Tr-Id"] = ap.transaction.id,
    ["User-Id"] = ap.transaction.user.id,
}

ap.http.respond(201, "hello world!", headers)