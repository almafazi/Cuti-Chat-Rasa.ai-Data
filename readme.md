Rasa.ai cuti with mongo & mongo-express for store tracker.

=========================
|| Run without docker: ||
=========================
Note: make sure rasa_core, rasa_ai, and rasa_core_sdk already installed.

******** Train Core: **********

python3 -m rasa_core.train -d domain.yml -s data/stories.md -o models/current/dialogue

******** Train NLU ************

python3 -m rasa_nlu.train -c config.yml --data data/nlu.md -o models --fixed_model_name nlu --project current --verbose

******* Run Actions ***********

python3 -m rasa_core_sdk.endpoint --actions actions.actions

******* Run Server and test on cmdline ************

python3 -m rasa_core.run -d models/current/dialogue -u models/current/nlu --enable_api

==========================
||   Run with docker:   ||
==========================

******** Train Core: **********

(sudo) docker run -v $(pwd):/app/project -v $(pwd)/models/rasa_core:/app/models rasa/rasa_core:latest train --domain project/domain.yml --stories project/data/stories.md --out models

******** Train NLU ************

(sudo) docker run -v $(pwd):/app/project -v $(pwd)/models/rasa_nlu:/app/models -v $(pwd)/config:/app/config  rasa/rasa_nlu:latest-full run python -m rasa_nlu.train -c config/nlu_config.yml -d project/data/nlu.md -o models --project current

******** Train NLU ************

(sudo) docker-compose up

Note: Jika python mysql.connector belum terinstall di rasa core.sdk untuk action, run dockerfile :
=========================================
// docker build . -t rasa_mysql:latest //
========================================
dan ganti image di docker-compose.yml.

******** Testing ************

curl --request POST --url http://localhost:5005/webhooks/rest/webhook --header 'content-type: application/json' --data '{"message": "hello"}'

