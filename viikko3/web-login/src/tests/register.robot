*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page And Click Register

*** Test Cases ***
Register With Valid Username And Password
    Set Username  testaaja
    Set Password  testi123
    Set Password Confirmation  testi123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  Username is too short

Register With Valid Username And Invalid Password
    Set Username  testaaja
    Set Password  kirjaimet
    Set Password Confirmation  kirjaimet
    Submit Credentials
    Register Should Fail With Message  Password is invalid

Register With Nonmatching Password And Password Confirmation
    Set Username  testaaja
    Set Password  salasana123
    Set Password Confirmation  salasana
    Submit Credentials
    Register Should Fail With Message  Passwords do not match

*** Keywords ***
Go To Main Page And Click Register
    Go To Main Page
    Click Link  Register new user

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}