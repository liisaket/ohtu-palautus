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

Login After Successful Registration
    Register Succeeds
    Go To Login Page
    Set Username  testaaja
    Set Password  testi123
    Click Button  Login
    Main Page Should Be Open

Login After Failed Registration
    Register Fails
    Go To Login Page
    Set Username  k
    Set Password  kalle123
    Click Button  Login
    Login Should Fail With Message  Invalid username or password

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

Register Succeeds
    Set Username  testaaja
    Set Password  testi123
    Set Password Confirmation  testi123
    Submit Credentials

Register Fails
    Set Username  k
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  Username is too short

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}