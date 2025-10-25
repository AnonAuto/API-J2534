# AAAAPI — J2534 HTTP API (for .NET Framework 4.8.1)

Self-hosted **Web API 2 (OWIN)** service that exposes **J2534** operations over HTTP.   
A simple single-channel host around your J2534 DLL.  
  
> ⚠️ Process bitness **must** match your vendor DLL (many J2534 DLLs are **x86**). Set the project Platform Target accordingly.

---

## Table of Contents
- [What’s Inside](#whats-inside)
- [Architecture](#architecture)
- [Requirements](#requirements)
- [Project Layout](#project-layout)
- [Install & Build](#install--build)
- [Run](#run)
- [Splash & Console](#splash--console)
- [Quick Start](#quick-start)
- [Endpoints](#endpoints)
- [DTO Schemas](#dto-schemas)
- [Hex Rules](#hex-rules)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Security](#security)
- [Extending](#extending)
- [Version & Bitness](#version--bitness)
- [License](#license)

---

## What’s Inside

- **.NET Framework 4.8.1**, **ASP.NET Web API 2**, **OWIN SelfHost**
- **Swagger UI** for interactive REST docs
- **WinForms splash** on startup (minimum 1.5s on screen)
- **Console banner** even if Output type = Windows app (via `AllocConsole`)
- **C# 7.3 friendly** (no `record`, no nullable refs)
- **Single device/channel** J2534 host to keep runtime state simple & predictable

---

## Architecture

```text
+----------------------+         HTTP (localhost:5000)         +---------------------+
|  Your Client Tools   |  <---------------------------------->  |  OWIN SelfHost      |
|  (curl/Postman/etc.) |                                        |  Web API 2          |
+----------------------+                                        |  /swagger           |
                                                                +----------+----------+
                                                                           |
                                                                App-layer   |  Routes (/j2534/*)
                                                                           v
                                                                +---------------------+
                                                                |   J2534Host         |
                                                                |   - tracks device   |
                                                                |     & channel state |
                                                                +----------+----------+
                                                                           |
                                                          P/Invoke via vendor J2534 DLL
                                                                           v
                                                                +---------------------+
                                                                |  Vendor J2534 DLL   |
                                                                |  (x86/x64 matched)  |
                                                                +---------------------+

```
## Requirements

- Windows with J2534 tool + vendor DLL installed
- Visual Studio 2019/2022 (or MSBuild)

#### NuGet packages:
-Microsoft.AspNet.WebApi.Core
-Microsoft.AspNet.WebApi.Owin
-Microsoft.AspNet.WebApi.OwinSelfHost
-Microsoft.Owin
-Microsoft.Owin.Cors
-Swashbuckle.Core (5.6.0)
-Newtonsoft.Json

## Framework references:
 
-System.Web  
-System.Windows.Forms  
-System.Drawing  
  
Ensure your project Platform target matches the DLL (x86 is common).
  
## Project Layout
`
AAAAPI/
 ├─ Program.cs              // AllocConsole, splash thread, OWIN host start, banners
 ├─ Startup.cs              // OWIN pipeline, CORS, Web API routes, Swagger
 ├─ J2534Controller.cs      // Routes /j2534/* → J2534Host actions
 ├─ J2534Host.cs            // Thin wrapper around IJ2534Extended
 ├─ Splash.cs/.Designer.cs  // WinForms splash screen
 ├─ J2534\*.cs              // J2534 enums, structs, interfaces (IJ2534Extended), P/Invoke shim
 └─ packages.config         // NuGet dependencies
`

## Install & Build
1) Restore packages
Visual Studio will prompt to restore NuGet packages on open.

2) Add framework references (if missing)
System.Web, System.Windows.Forms, System.Drawing

3) Platform target
Project → Properties → Build → Platform target → x86 (if your J2534 DLL is 32-bit)

4) Build
Build solution. Fix any missing references (see Troubleshooting).

## Run
Default base URL: http://localhost:5000

First-run URL ACL (if http.sys complains)
Run as Administrator:

`
netsh http add urlacl url=http://localhost:5000/ user=Everyone
Swagger
Open: http://localhost:5000/swagger
`

## Splash & Console
The splash form is displayed on a dedicated STA thread and remains visible
for ≥ 1500 ms. After the web server binds successfully, the splash closes.

If hosting fails (port/ACL/refs), a MessageBox and console error appear with details.

# Quick Start
Base path for all routes: http://localhost:5000/j2534

### Load vendor DLL
`
curl -X POST http://localhost:5000/j2534/load \
  -H "Content-Type: application/json" \
  -d '{ "device": { "vendor":"OBDX", "name":"Pro", "functionLibrary":"C:\\\\OBDX\\\\J2534.dll" } }'
`
### Open
`
curl -X POST http://localhost:5000/j2534/open
`
### Connect (CAN 500k)
`
curl -X POST http://localhost:5000/j2534/connect \
  -H "Content-Type: application/json" \
  -d '{ "protocol":"CAN", "flags":"NONE", "baud":"CAN_500000" }'
`
### Write (payload)
`
curl -X POST http://localhost:5000/j2534/write \
  -H "Content-Type: application/json" \
  -d '{ "protocol":"CAN", "txFlags":"NONE", "hexData":"02 10 01", "timeoutMs":100 }'
`
### Read
`
curl -X POST http://localhost:5000/j2534/read \
  -H "Content-Type: application/json" \
  -d '{ "numMsgs":50, "timeoutMs":50, "untilTimeout":true }'

`
### Voltages
`
curl http://localhost:5000/j2534/vbatt
curl http://localhost:5000/j2534/vprog
`
### Disconnect / Close / Free
`
curl -X POST http://localhost:5000/j2534/disconnect
curl -X POST http://localhost:5000/j2534/close
curl -X POST http://localhost:5000/j2534/free
`
### State
`
curl http://localhost:5000/j2534/state

`
### Endpoints
All endpoints return JSON. Failures surface as HTTP 500 with messages like:
`"PassThruConnect failed: ERR_INVALID_PROTOCOL_ID".`
  
### Health
`GET /j2534/state` → { dllLoaded, opened, connected, deviceId, channelId, device }
  
### Lifecycle  
`POST /j2534/load — body: LoadReq`
  
`POST /j2534/free`  
  
`POST /j2534/open` 
 
`POST /j2534/close`  
   
`POST /j2534/connect — body: ConnectReq`
  
`POST /j2534/disconnect`  
  
### I/O  
`POST /j2534/write — body: WriteReq → { sent: 1 }`  
  
`POST /j2534/read — body: ReadReq → { frames: ["AA BB CC ...", "..."] }`  
  
### Config
`POST /j2534/set-config — body: ConfigReq`  
  
`POST /j2534/get-config — body: GetConfigReq → { "DATA_RATE": 500000, "ISO15765_BS": 8, ... }`  
  
### Filters & Buffers
`POST /j2534/filters/clear`  
  
`POST /j2534/filters/start — body: StartFilterReq → { filterId: n }`  
    
`POST /j2534/filters/stop — body: StopFilterReq` 
  
`POST /j2534/clear-tx`  
  
`POST /j2534/clear-rx`  
  
`POST /j2534/clear-periodic`  
  
### Voltages  
`GET /j2534/vbatt → { millivolts, volts }`  
  
`GET /j2534/vprog → { millivolts, volts }`  
  
### DTO Schemas
LoadReq
`
{
  "device": {
    "vendor": "OBDX",
    "name": "Pro",
    "functionLibrary": "C:\\Path\\To\\VendorJ2534.dll",
    "configApplication": null
  }
}
`  
### ConnectReq  
`
{
  "protocol": "CAN",
  "flags": "NONE",
  "baud": "CAN_500000"
}
`  
### WriteReq
`
{
  "protocol": "CAN",
  "txFlags": "NONE",
  "hexData": "02 10 01",
  "timeoutMs": 100
}
`  
### ReadReq
`
{
  "numMsgs": 50,
  "timeoutMs": 50,
  "untilTimeout": true
}
`
### ConfigReq  
`
{
  "values": {
    "DATA_RATE": 500000,
    "ISO15765_BS": 8,
    "ISO15765_STMIN": 10
  }
}
`  
### GetConfigReq  
`
{
  "keys": ["DATA_RATE", "ISO15765_BS", "ISO15765_STMIN"]
}
`
### StartFilterReq  
`
{
  "type": "PASS_FILTER",
  "maskHex": "FF FF FF FF FF FF FF FF",
  "patternHex": "07 DF 00 00 00 00 00 00",
  "flowHex": ""
}
`  
### StopFilterReq  
`
{ "filterId": 1 }
`
  
### Hex Rules
Non-hex chars are ignored; remaining hex length must be even.

Valid:
`
"021001"

"02 10 01"

" 02-10-01 " → becomes 02 10 01
`  
If odd after cleaning → error: "Hex length must be even."  
  
## Examples
`$base = "http://localhost:5000/j2534"`

# Load
Invoke-RestMethod "$base/load" -Method Post -ContentType "application/json" -Body (@{
  device = @{ vendor="OBDX"; name="Pro"; functionLibrary="C:\OBDX\J2534.dll" }
} | ConvertTo-Json -Depth 5)

# Open & Connect
Invoke-RestMethod "$base/open" -Method Post
Invoke-RestMethod "$base/connect" -Method Post -ContentType "application/json" -Body (@{
  protocol="CAN"; flags="NONE"; baud="CAN_500000"
} | ConvertTo-Json)

# Write & Read
Invoke-RestMethod "$base/write" -Method Post -ContentType "application/json" -Body (@{
  protocol="CAN"; txFlags="NONE"; hexData="02 10 01"; timeoutMs=100
} | Convert-ToJson)

(Invoke-RestMethod "$base/read" -Method Post -ContentType "application/json" -Body (@{
  numMsgs=50; timeoutMs=50; untilTimeout=$true
} | ConvertTo-Json)).frames
curl (CMD)
bat
Copy code
curl -X POST http://localhost:5000/j2534/open
curl -X POST http://localhost:5000/j2534/connect -H "Content-Type: application/json" -d "{\"protocol\":\"CAN\",\"flags\":\"NONE\",\"baud\":\"CAN_500000\"}"
curl -X POST http://localhost:5000/j2534/write   -H "Content-Type: application/json" -d "{\"protocol\":\"CAN\",\"txFlags\":\"NONE\",\"hexData\":\"02 10 01\",\"timeoutMs\":100}"
curl -X POST http://localhost:5000/j2534/read    -H "Content-Type: application/json" -d "{\"numMsgs\":50,\"timeoutMs\":50,\"untilTimeout\":true}"
Postman (Body → raw → JSON)
json
Copy code
POST http://localhost:5000/j2534/connect
{
  "protocol": "CAN",
  "flags": "NONE",
  "baud": "CAN_500000"
}
Troubleshooting
No console output / window closes

Use Console Application output type or rely on AllocConsole (already present).

Process is kept alive via Thread.Sleep(Timeout.Infinite).

Route is defined in an assembly that is not referenced (System.Web)

Add System.Web reference; ensure Web API 2 OWIN packages are installed.

Server fails to start

Port busy → pick a free port.

ACL → reserve URL:

bat
Copy code
netsh http add urlacl url=http://localhost:5000/ user=Everyone
Bitness mismatch → align process with DLL (likely x86).

Missing DLL exports → ensure vendor J2534 DLL implements expected functions.

Swagger not showing

Confirm Swashbuckle.Core 5.x installed and EnableSwagger(...).EnableSwaggerUi() is executed in Startup.

Splash disappears instantly

The code enforces min 1500 ms visibility. If you still don’t see it, you likely hit a startup exception. Check the MessageBox/console for the error.

Security
Default bind is localhost. If you expose beyond your box, add TLS + auth (reverse proxy, API key, etc.).

CORS is AllowAll for dev. Lock it down for production.

Be careful when exposing ECU operations over a network; restrict access.

Extending
Current design uses a single J2534Host (simple singleton).

For multiple devices/channels: make J2534Service a dictionary keyed by hostId, add {hostId} to routes, or introduce DI with scoped lifetimes.

Add helpers for ISO-TP segmentation, periodic messages, timestamping, persistent logs, etc.

Add POST /j2534/periodic/start|stop and /j2534/ioctl wrappers if you need more of the API surface.

Version & Bitness
Target framework: .NET Framework 4.8.1

Language: C# 7.3 (no record, no nullable refs)

Bitness: set x86 when the vendor DLL is 32-bit (very common); otherwise x64.

J2534: make sure the vendor DLL exports the standard PassThru* symbols used.

License
Preserve all banners and notices. Redistribution requires express written consent of the copyright holder.
Software is provided AS IS without warranties; authors are not liable for any damages.
`
#################################################################################################################################################################################################
#                                                                  
#                                                                                                                                                                                                 
#                                                   .  ..   ....   ...   ..  ...  ....    ........   .........      .  .    ..      ...........    ....                                               
#                                              ..                                                                                                         .                                              
#                                             :                            ...                                             ....                   ....     ..                                            
#                                            :      ?YY!    :YY7   :Y!  .?J!~!J?.  !YY^   ?J  :JJ.  .JJ. .JJY^    ~YJ?   ~J?~~7J!   ?Y.   .Y?  .7J~^~??.    :                                            
#                                           .      ~5~7Y.   :5JJ?  :5!  ?5:   :5J  7Y?Y^  JY   .YJ .YJ.  .YJ75:  ^57YJ  :5?    75~  ?5:   .YJ  ~5?          :                                            
#                                          ..     .Y? .Y?   :5!.JJ :5!  JY.   .YJ  75:^5^ JY    .J?J7    .YJ 7Y.:5~.YJ  :57    !5!  ?Y:   .YJ   :!??7~.     :                                            
#                                          .      ?57^^J5~  :5! .JJ~Y!  JY.   .YJ  75: ^Y~JJ     :YJ     .YJ  ?YY!  YJ  :57    !5~  ?5:   .YJ       .757    :                                            
#                            ...          .      !5!.:.:J5. :5!   ?557  ^Y?^::?Y^  75^  ^YYY     .5J     .YJ   ~^  .YJ   7Y!::~Y?.  :Y?^::?Y~  ^J7:.:7Y^     .    .   .         ...                      
#                  ..                            ::     .:.  :.    ::.    .:::.    .:.   .:.      :.      :.        :.    .::^:.      .:::.     .::::.                                   ..              
#                 :                                                                                                                                                                       ..             
#                .       !?7    77   !7 .!!77!!^ .!7!7!.  !77    !77. .~7!!7: .!!77!!^ !7  !7   .7~ :7!!!!.        !7!    :?^     :?^     :?^    ~??:    ^?7:   7!   ^7!!77^   77!!!!.     :             
#                :      ~Y!Y~   JJ   ?Y    ?Y.  .Y?   ?Y  JJJ7  ~Y?Y. ?Y.  !5.   ?Y.   7Y. :Y^  !Y. ^Y~           ~J~J^   ^Y~     ^5~     ^5~   :5!7Y.   !5?Y:  YJ  ~5~   ^~.  YY.         :             
#               .      .Y! !Y.  JJ   ?Y    ?Y   .57   !5. J?.Y~:5:!Y. JJ   ^5^   ?Y    7Y.  7J .J~  :J7~~~       .J~ !J.  ^Y~     ^Y~     ^Y~   JJ .Y7   ~5:^5^ J?  75.        JJ!~~:     ..             
#               :      7Y7^!Y?  JJ   ?Y    ?Y   .57   ?5. J? :Y5~ 7Y. JY   ~5:   ?Y    7J.  .Y~~J   :Y^          ?J!^!J7  ^Y~     ^Y~     ^Y~  ~Y?~~JY:  ~5: ^Y!J?  75:   .:   JJ          .             
#              .      ^Y^   ~Y: ^J7~!J^    7J    ~J!~!J^  ??  .:  !Y. :?7~~?!    ?J    7J.   !JJ^   :J7~~~:     ~J: . ^J^ :J7~~~^ :J?~!!^ :Y~ .J7   .JJ  ~Y:  :YY?  .7J!~!J7.  JJ!~~!.     :             
#              :                  ...              ..                   ...                                                                                            ...          .      :             
#               .                                                                                                                                                                         .              
#                :                          .             ..:^^~~!!!!!!!!!!!~~^:..        ..........................................................................................     .               
#                :                                  .:^!!!!~^:...           ..:^~!!!!^:.                                                                                                 :               
#               ..      ..................      .:!7!~:.                            ..^~!!^.      ..................................................................................     :               
#               :                            :!7!^.                 .:^^..                :~7!^.             ...............................................                             :               
#               :                         .!?!:                  .!?YYYYYJ?~.                .:!7^.                                                                                      :               
#               :      .............    ^?7:                   ^?YYYYYYYYYYYY?^                  :!7:   .:....::::::::::::::::::::::::::::..........................................     :               
#               :                     ~J!.     :!!.          :JYYYYYYYYYYYYYYYY?:          ^!:     .~7^                                                                                  :               
#               :      ..........   ~J~.     !YY~           ~YYJYYYYYYYYYYYYYYJYY^          .?Y7.     ^7^  ..::::::::::::....        ...............................................     :               
#               :                 :J7.  .!:.JJ~            ^YYYYJ?!~^::::^~7?YYYYY:           ^?Y~ !.   ~?:    .............:::::.                                                       .               
#                :               !J:   :Y~.7^::           .YYJ!:             .:7YYJ           ..:7^.Y!   .7!                   ....:..                                                 ..                
#                 ..           .J7    :Y? .^77.           7Y7.                  .?5^           ~7:. ^Y~    ^?:                       ....                                             .                  
#                     ..      :Y~  .^ ?J.^JJ~            .Y!  :~!!!^      ^!!!~.  ??            :?J~.?J .~  .?^                         ...                                        ..                    
#                     .      :Y^   J: Y?77:              !?        ::    ^.       .J.             :!??Y. J:  .?^                           .:.                                    ..                     
#                    ..     :Y^   !5..J^.::              J:   .:~~:       .^!~:    !~             ^:.^J: ??   .J:                             ..                                  :                      
#                    :     .Y~    JY: .:J!              :?   ^^^~~^.      .^^^::   .J              7?:. .JJ.   :J.                              .::..!.                ...       ..                      
#                   :      7?    .YY..?Y^               ?:            ^.            J:              ~J?..JJ.    !?   ................................^::...                      :                       
#                   .     :5.  .: 7J~Y!.                J.   :      . ?^ .     ..   ~!               .7J^?7 .   .J:                                       ...::...              ..                       
#                  .      7?   ^? .YJ..7.               J:   :?~.   :!7!^.  .^7!    ?^              .~ :JJ. 7:   !7    ......                                    ...:...          ..                     
#                  :      Y^   ~Y~ ~.:Y7                .J.   :^~!~~!7.~!~~~!^~    ^?                7?..! ^Y^   :J         ......                                     ......        .                   
#                  .     :5.   :YY: :YJ.                 :?.   .  .:^^.:~^.. :.   ^7                 .JJ. .JJ.   .J.              ....                                       ...       .                 
#                 ..     :Y.    !Y? JY:                   .!^   .    .Y!    .    ~^                   :Y? ~Y~     J:  .::::::....      ..        ............                    ..     .                
#                 ..     ^Y    . ~Y7Y^ ~              .:^!7??7       :Y7       .7??7!^:.             ~ ~Y~J~ :    J:   ............:.......   :..... .........................   .::.    :               
#                 ..     :Y.   !! .J? :Y:        :~!?JYYYYYYYYJ.     :5!      .JYYYYYYYYJ?!^.       .Y. J?. ~7   .Y.       .^^............  :.                                ...   :.   .               
#                 ..     .Y:   .5?..: 7Y:       ~YYYYYYYYYYYYYY?      :      .JYJJJJJJJJYYYYJ.      ^Y! ^ .7Y:   :J   :....             .^ .:          ..............           ...  ^    :              
#                  :      J7    ~YY~  JY.      .YYYYYYYYYYYYYYYY^    ~??.    7YJJJJJJJJJJJJJY!      :Y?  ^YY~    77    ....::::::::::....   ^                                    : ..~:   .              
#                  :      ~Y     :J5?.!Y..~    ~YYYYYYYYYYYYYYYYY.   .Y?    ~YYYYYYJJJJJJJJJYJ    ~..Y!.?Y?:    .Y.          ...........    ..                                  :.    :    .             
#                  ..      Y~    . :?J7Y. Y~   JYYYYYYYYYYYYYYYYY7   .Y?   .YYYYYJJYJJJJJJJJJY:  !J :J7J7: .    77                           ^     ...................          :     ^    :             
#                   :      ^Y.   ^7: .^?^ ?Y:  !YYYYYYYYYJYYYYYYYY^  7YY:  JYJYJJYYYJJYJYJJYY7. ^Y7 !?^..^7.   ^J.   .:..........             ^                                ^    ..!.   :             
#                    .      7J    :JJ!:.. :YJ   .!YYYYYYYYYYYYYYYYY..YYY7 7YJJJJJJJYYJYJYYJ!.   JY. ..:7J7    .Y:    :::::::::::::::.....     .:                              :.   :: ^    :             
#                    .       ?7     ~JYJ!: ~Y: !^ .!JYYYYYYYYYYJJYY7!YYYJ!YYYYYYJJJJJJYYJ~  ^! ~Y: :7JY7:    .J^   .~                          :.                            .^       ^   ..             
#                     :       ?7      .^7J?^!J  J?.  ^?YYYYYJJYYJJJYYJYYYYYYYYYJYYYYYY?^  :J? :J^^?J7^.     .J^    ^       ..                   ^                           .^       .:   .              
#                      .       7?     .:...::~~  !Y!.  .~7JYYYYYYYYYYYYYYYYYYYYYYYJ?~.  .7J^ .~^::...:.    :?:    ^                 .            :..........................:        ^.   .              
#                     .         ~J:    .~77!^:::. :!J7:    .:~!7?JJJYYYYYJJJJ?7!^:.  .^77^. .:.:^~77~.    !7.     ..............     .:..............................................::   ..             
#                  ..            .?!      .^!?JJJJ7!7?7!:.    ..:::::::::::::.    .:!??777JJJJJ?7~.     :?^                              ..............................................   .              
#                 .                ~J^       ..       ..:~7?JJ7~:^^~!^:~~~^:~7J?7!^:..  .......       .7!.   .................  ...  ....:::::::::::::::::::::::::::.:.........:....     ..              
#                :      .........    !?^      :~!!77?JYYYJ?~.  :!~:      .^!^..:~?JYYYJ?7!!~~^.     .7!.                                                                      .        ..                
#               ..                    .~?~.      ..:^^:..   .!J~.           :77:   .:^^~^^..      ^7!.         ..                                               ...       ...     .                      
#               .                        :!7^.             .?~                :7~              :!7^        ...                                                                 ..                        
#               .      ..............       ^!7~.                                          .:!!^.     .......      .         .............................                    ..    . .                  
#               .                              :~!!~:.                                 .^~!~:                                                                                             ..             
#                :                                 .:~!!~^:.                    ..:^~!~^.                                                                                                   :            
#                 .        .~7?J?J????????????????7~:.  ..:^~~~~~~~^^^^^^~~~~!~~~^:.   .:~!7!~:     .^   ::.  :.  .^   .:.  .^   ::.  .:   ::   ^   .::   ^   .:.  .^   ::.  .^   :.  .::    :           
#                  :      ~YYYYYYYYYYYYYYYYYYYYYYYYY5YY?7~^:......................:~7?JYYYYYYYY?     ?  ^: !  ^^   ?  :~ !.  ?  ^: 7  .7  ! .7  !.  7 ^^  7. .! !.  ?  .~ !. .7   :~  ! ^^   :           
#                  :      JYJJJYYYJJJJYJ?7!!!!!!!!!!!!!777777?JJ??77777777???JJYYYYYYYJJJJJJJJJY^   .7  .^.^  ^~   7.  ~.~   7. .:.~  .7  ::::  !:  ~.^.  !:  ~.~   7.  ~.~  .7   :~  ~.^.   :           
#                  :      JJJJJJJJYJYY!.                      .!YYYYYYYYYYYYYYYYYJJYYJJJJJJJJJJY^                                                                                            :           
#                  :      JYJJJJYYYYY^  ^JJJJJJJJJJJJJJJJJJJ?:  ~YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY^                                                                                            :           
#                  :      JYJJJYYYYY^  !YYYYYYYYYYYYYYYYYYYYYY^  ^YYYYYYYYJJJJJJJJJJJJJJJJJJYYJY^   .7   ^~   !:  .7   .7  .^.~  :!  :::^ ^.::  7.  ~.~. .7  .~.~  .7  .^.^  ^^  ~.^. ~.~.   :           
#                  :      JYJJJYYYJ:  75YYYYYYYYYYYYYYYYYYYYYYY~  ^YYYYYYYY~               .JYJY^    ?   .!   ~^   ?    7  ^: 7  .7  !. ! ! .~  !:  7 ^:  7  .~ !   7  ~. !  :~  ! ^: ! ~:   :           
#                  :      JYJJY7:.    ..........................   ..:!YYYY^                ?YJY^   .:.  .:   ::  .:.   :.  ...  .:   ..   ..   :.  ...   :.  ...  .:.  ..   .:  ...  ...    :           
#                  :      JJJYJ                                        JYYY^      :!        JYYY^                                                                                            :           
#                  :      JYJYJ   ~??7?7~                    ~7????^   ?YYY^  ^..^..... :^  JYYY^   ^:^  .~   ^:  ::^  .~  .^:. .::.  ^:   ^:  ::^  ^:^  .~  .^:: .::: .::. ::^.  ~.  ::^    ^           
#                  :      JJJYJ   !JJYYJ?     :::::::::^.    ?JJJYY~   ?YYY^  ^.  ^.  . .:  ?YJY^  .~ !. .?   ^~  7 :^  7  ~. 7 7  !  :~   :~  7 ^:.! ~.  7  ~. 7 !. 7 7 .! 7 .~  !.  ! ~.   ^           
#                  :      JJJJJ                                        ?YJY^       ..:7^    ?YJY^   ^.^  .!   ^^  :.:  .!. .::. .::.  ^^   :^  :.^  ^.^  .!  .::: .::: .::. :.^.  ~:  :.^    :           
#                  :      JJJYJ                                        ?YJY^                ?YJY^                                                                                            :           
#                  :      JYJYJ       ^^^^^^^^^^^^^^^^^^^^^^^^^^.      ?YYY!...............:JYJY^   ...  .:   ..  .:.   :   ..   ..   ..   ..  ...  .:   ..   ..   :.  .:.   :   ...  ...    :           
#                  :      JJJYJ      .YYYYYYYYYYYYYYYYYYYYYYYYY5^      JYJJYYYYYYYYYYYYYYYYYJJJY^  .! !. .7  7 .~ 7 ^:  7  ^: !  ^^   ^~  ! :^ ! ^:  ?   :!   ^~   ~^  7 :^  ?  .! ! .! !.   :           
#                  :      JJJJY?~^::^?YJJJJJJJJJYJJYJJJYJJJYJJJY?^^^^^7YJJYYYJYYJYJJYJJJYJJJJJJY^   ~.~  .7  ^.:: ~.^.  7. .^.~  ^~   ^~  ~.^. ~.^.  7.  :!   :!   ~^  ~.^.  7.  ~.~  ~.~    :           
#                  :      JYJJJYYYYYYYJJJJJJJJJJYJJJYYJJJJJJJJJJYYYYYYYJJJJYJYYYYJJJJJJJYJJJJJJY:                                                                                            .           
#                  :      :JYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYJ^                                                                                             .           
#                  ..       :~!0x416E6F6E796D6F7573204175746F6D6F7469766520416C6C69616E6365!~:      :!  :::^  7.  ~.~  ~.~ .^.^  ^~  ~.^. .7.  ~.~  :!  :^.^ ::.^  ~:  ^.^. .7   .7  .^.^    .           
#                   ..                                                                              .7  !. !  !: .! ~.:~ ! ~. 7  :~  7 :^  7. .~ !.  7  ~. ! ~. 7  ^^  7 .^  ?    7  ~. 7   ..           
#                     .                                                                             .^   ..   :.  ...  ...  :.   ::  .:.   ^.  ...  .^.  :..  .:.  ::  .::  .^.   ^.  :..   :            
#                       ...                                                                                                                                                               ..             
#                                                                                                                             .  ...   .              .................................         #
#
#
#################################################################################################################################################################################################   
`
