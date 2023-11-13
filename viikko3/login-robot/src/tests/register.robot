*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  testaaja  toimii123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  root  validpassword1
    Output Should Contain  Username is taken

Register With Too Short Username And Valid Password
    Input Credentials  xx  validpassword1
    Output Should Contain  Username is too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  @+!  validpassword1
    Output Should Contain  Username invalid

Register With Valid Username And Too Short Password
    Input Credentials  validuser  pw1
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  validuser  passwordd
    Output Should Contain  Password has to contain letters and numbers

*** Keywords ***
Input New Command And Create User
    Input New Command
    Input Credentials  root  salasana123
    Input New Command