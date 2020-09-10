## happy path               <!-- name of the story - just for debugging -->
* greet              
  - utter_greet
* mood_great               <!-- user utterance, in format _intent[entities] -->
  - utter_happy
* pss_dump
  - utter_pss_dump
* fex_commit
  - utter_fex_commit
* password_recovery
  - utter_password_recovery
* vnc_setup
  - utter_vnc_setup
* sanity_submission
  - utter_sanity_submission
* bat_commit
  - utter_bat_commit
* db_full_error
  - utter_db_full_error
* safec
  - utter_safec
* snmp_debugging
  - utter_snmp_debugging
* service_dependency
  - utter_service_dependency
* core_debug
  - utter_core_debug
  - utter_did_that_help
* 64_bit_compiler_warnings
  - utter_64_bit_compiler_warnings
* lab_case
  - utter_lab_case

## sad path 1               <!-- this is already the start of the next story -->
* greet
  - utter_greet             <!-- action of the bot to execute -->
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* mood_affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* mood_deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye
