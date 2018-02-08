#!/bin/bash

curl -X POST -H "Content-Type: application/json" \
    -d "@handler_meta.json" -u pavlovma007:7FC808C385EE960D992F1F32219DB8ED2568979E4DCCD108BEDE91920AC62189 \
    http://api.acapella.ru:5678/http/services/handlers/register
