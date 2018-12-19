## greet_path
* greet
  - action_get_time
  - slot{"time": "pagi"}
  - utter_greet
* ask_cuti
 - utter_ask_cuti
* tipe_cuti{"tipe_cuti":"tahunan"}
 - utter_tipe_cuti
 - slot{"tipe_cuti":"tahunan"}
* start_date{"start_date":"1 November 2018"}
 - utter_start_date
 - slot{"start_date":"1 November 2018"}
* lama_cuti
 - utter_lama_cuti
 - slot{"lama_cuti":"1 November 2018"}
* alamat{"alamat":"solo"}
 - utter_alamat
 - slot{"alamat" : "solo"}
* telepon{"telepon":"085725629333"}
 - utter_telepon
 - slot{"telepon":"085725629333"}
* alasan{"alasan":"liburan keluarga"}
 - utter_alasan
 - slot{"alasan":"liburan keluarga"}
* ask_trip
 - utter_ask_trip
* trip_berangkat{"trip_berangkat":"2 hari"}
 - utter_trip_berangkat
 - slot{"trip_berangkat":"2 hari"}
* trip_pulang{"trip_pulang":"2 hari"}
 - utter_trip_pulang
 - slot{"trip_pulang":"2 hari"}
* konfirmasi
 - utter_konfirmasi
* thanks
 - utter_thanks
* goodbye
  - utter_goodbye

## ask_cuti_path
* ask_cuti
 - utter_ask_cuti

## story_thanks_path
* thanks
 - utter_thanks

## story_goodbye_path
* goodbye
 - utter_goodbye
