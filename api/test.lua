-- Set the content type
wrk.headers["Content-Type"] = "application/json"

-- Define the JSON payload
local json_payload = [[
{   
   "dia":16.00
   ,"mes":9.00
   ,"km_ovsd":1086.84
   ,"t_media":21.00
   ,"v_media_viento":6.10
   ,"presion_media":1015.50
   ,"cantidad_de_lluvia_mm":13.70
   ,"nubosidad_perc":53.50
   ,"temporada_alta":1.00
}
]]

-- Define the request function
request = function()
   return wrk.format("POST", "/predict", nil, json_payload)
end

function response(status, headers, body)
   print("Status:", status)
   print("Headers:")
   for key, value in pairs(headers) do
      print(key, value)
   end
end
