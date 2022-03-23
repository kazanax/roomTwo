*** Settings ***
Documentation    Suite description
Library  roomTwo.py

*** Variables ***

${expectedAttach}=    UE-1 on cell=1 attached successful.
${expectedDetach}=    UE-1 detached successfully.
${expectedStopTraffic}=     UE-1 traffic on bearer 1 with id 1 has been stopped
${positive_response}=   UE-1 on cell=1 attached successful.
${negative_response}=   Cell-5 is not supported by the eNB.
*** Test Cases ***

Check comunication between UE-eNB
    Attach ue 1 to cell 1
    Start traffic on ue 1 with speed 10 by bearer 1
    Stop traffic on ue 1 with speed 10 by bearer 1
    Detach ue 1 from cell 1

*** Keywords ***
Attach ue ${ueID} to cell ${cellID}
    ${response}    attach  ${ueID}    ${cellID}
    Should be equal as strings   ${response}  ${expectedAttach}

Start traffic on ue ${ueID} with speed ${mbps} by bearer ${bearerID}
    start_traffic  ${ueID}  ${mbps}  ${bearerID}

    ${response}     show_traffic    ${ueID}
    Should not be equal as strings   ${response}    ${null}

Stop traffic on ue ${ueID} with speed ${ueID} by bearer ${bearerID}
    ${response}     stop_traffic  ${ueID}  ${bearerID}
    Should be equal as strings  ${response}     ${response}

Detach ue ${ueID} from cell ${cellID}
    ${response}    detach   ${cellID}
    Should be equal as strings    ${response}   ${expectedDetach}










