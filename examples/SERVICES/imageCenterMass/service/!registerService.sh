#!/bin/bash

curl -X POST -H "Content-Type: application/json" \
    -d "@handler_meta.json" -u pavlovma007:A5333EE5844AA9F0CE144D7352F507817C58D835EA7F894C98D9103B416C337A \
    http://api.acapella.ru:5678/http/services/handlers/register
