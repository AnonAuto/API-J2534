#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
"""
32 Bit Please
AAAAPI Tkinter GUI — J2534 HTTP API client
Tested with Python 3.9+ on Windows.

Usage:
    pip install requests
    python AAAUI.py
"""
import json
import threading
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

try:
    import requests
except ImportError:
    requests = None

APP_TITLE = "AAAAPI — J2534 HTTP API GUI"
DEFAULT_BASE_URL = "http://localhost:5000"

# ----------------------------- HTTP helpers -----------------------------
def _require_requests():
    if requests is None:
        messagebox.showerror("Missing dependency", "The 'requests' package is required.\nRun: pip install requests")
        raise RuntimeError("requests not available")

def http_post(base_url, path, data=None, timeout=10):
    _require_requests()
    url = base_url.rstrip("/") + path
    headers = {"Content-Type": "application/json"}
    r = requests.post(url, data=json.dumps(data or {}), headers=headers, timeout=timeout)
    r.raise_for_status()
    if r.text.strip():
        try:
            return r.json()
        except Exception:
            return r.text
    return None

def http_get(base_url, path, timeout=10):
    _require_requests()
    url = base_url.rstrip("/") + path
    r = requests.get(url, timeout=timeout)
    r.raise_for_status()
    if r.text.strip():
        try:
            return r.json()
        except Exception:
            return r.text
    return None

# ----------------------------- Tk GUI -----------------------------
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(APP_TITLE)
        self.geometry("980x680")
        self.minsize(900, 600)

        self.base_url_var = tk.StringVar(value=DEFAULT_BASE_URL)
        self.vendor_var = tk.StringVar(value="OBDX")
        self.dev_name_var = tk.StringVar(value="Pro")
        self.dll_path_var = tk.StringVar(value=r"C:\Path\To\VendorJ2534.dll")

        self.protocol_var = tk.StringVar(value="CAN")
        self.baud_var = tk.StringVar(value="CAN_500000")
        self.flags_var = tk.StringVar(value="NONE")

        self.hex_var = tk.StringVar(value="02 10 01")
        self.read_num_var = tk.IntVar(value=50)
        self.read_timeout_var = tk.IntVar(value=50)
        self.read_until_timeout_var = tk.BooleanVar(value=True)

        self.filter_type_var = tk.StringVar(value="PASS_FILTER")
        self.filter_mask_var = tk.StringVar(value="")
        self.filter_pattern_var = tk.StringVar(value="")
        self.filter_flow_var = tk.StringVar(value="")
        self.filter_id_var = tk.IntVar(value=0)

        self._build_ui()

    # Layout
    def _build_ui(self):
        # Top bar: base URL + actions
        top = ttk.Frame(self); top.pack(fill="x", padx=8, pady=6)

        ttk.Label(top, text="Base URL:").pack(side="left")
        ttk.Entry(top, textvariable=self.base_url_var, width=40).pack(side="left", padx=4)
        ttk.Button(top, text="State", command=self._async(self.action_state)).pack(side="left", padx=2)
        ttk.Button(top, text="Open Swagger", command=self.open_swagger).pack(side="left", padx=2)

        # Device group
        dev = ttk.LabelFrame(self, text="Device / DLL"); dev.pack(fill="x", padx=8, pady=6)
        row1 = ttk.Frame(dev); row1.pack(fill="x", padx=6, pady=4)
        ttk.Label(row1, text="Vendor:").grid(row=0, column=0, sticky="w")
        ttk.Entry(row1, textvariable=self.vendor_var, width=20).grid(row=0, column=1, sticky="w", padx=4)
        ttk.Label(row1, text="Name:").grid(row=0, column=2, sticky="w")
        ttk.Entry(row1, textvariable=self.dev_name_var, width=20).grid(row=0, column=3, sticky="w", padx=4)
        ttk.Label(row1, text="DLL Path:").grid(row=0, column=4, sticky="w")
        ttk.Entry(row1, textvariable=self.dll_path_var, width=40).grid(row=0, column=5, sticky="we", padx=4)
        ttk.Button(row1, text="Browse", command=self.browse_dll).grid(row=0, column=6, padx=2)

        row2 = ttk.Frame(dev); row2.pack(fill="x", padx=6, pady=2)
        ttk.Button(row2, text="Load DLL", command=self._async(self.action_load)).pack(side="left", padx=2)
        ttk.Button(row2, text="Free DLL", command=self._async(self.action_free)).pack(side="left", padx=2)
        ttk.Separator(row2, orient="vertical").pack(side="left", fill="y", padx=6)
        ttk.Button(row2, text="Open", command=self._async(self.action_open)).pack(side="left", padx=2)
        ttk.Button(row2, text="Close", command=self._async(self.action_close)).pack(side="left", padx=2)

        # Connect group
        conn = ttk.LabelFrame(self, text="Connect"); conn.pack(fill="x", padx=8, pady=6)
        ttk.Label(conn, text="Protocol:").grid(row=0, column=0, sticky="w")
        ttk.Combobox(conn, textvariable=self.protocol_var, values=[
            "CAN","ISO15765","ISO9141","ISO14230","J1850VPW","J1850PWM"
        ], width=14, state="readonly").grid(row=0, column=1, sticky="w", padx=4)

        ttk.Label(conn, text="Baud:").grid(row=0, column=2, sticky="w")
        ttk.Combobox(conn, textvariable=self.baud_var, values=[
            "CAN_500000","CAN_250000","CAN_125000","ISO9141_10400","ISO14230_10400","J1850PWM_41600","J1850VPW_41600"
        ], width=18, state="readonly").grid(row=0, column=3, sticky="w", padx=4)

        ttk.Label(conn, text="Flags:").grid(row=0, column=4, sticky="w")
        ttk.Combobox(conn, textvariable=self.flags_var, values=[
            "NONE","CAN_29BIT_ID","CAN_ID_BOTH","FULL_DUPLEX","ISO9141_NO_CHECKSUM","ISO9141_K_LINE_ONLY"
        ], width=18, state="readonly").grid(row=0, column=5, sticky="w", padx=4)

        ttk.Button(conn, text="Connect", command=self._async(self.action_connect)).grid(row=0, column=6, padx=6)
        ttk.Button(conn, text="Disconnect", command=self._async(self.action_disconnect)).grid(row=0, column=7, padx=2)

        # IO group
        io = ttk.LabelFrame(self, text="I/O"); io.pack(fill="x", padx=8, pady=6)
        ttk.Label(io, text="Hex payload:").grid(row=0, column=0, sticky="w")
        ttk.Entry(io, textvariable=self.hex_var, width=60).grid(row=0, column=1, sticky="we", padx=4)
        ttk.Button(io, text="Send", command=self._async(self.action_write)).grid(row=0, column=2, padx=2)

        ttk.Label(io, text="#Msgs:").grid(row=1, column=0, sticky="e")
        ttk.Entry(io, textvariable=self.read_num_var, width=8).grid(row=1, column=1, sticky="w")
        ttk.Label(io, text="Timeout ms:").grid(row=1, column=1, sticky="e", padx=(110,0))
        ttk.Entry(io, textvariable=self.read_timeout_var, width=8).grid(row=1, column=1, sticky="e", padx=(200,0))
        ttk.Checkbutton(io, text="Until timeout", variable=self.read_until_timeout_var).grid(row=1, column=1, sticky="e", padx=(290,0))
        ttk.Button(io, text="Read", command=self._async(self.action_read)).grid(row=1, column=2, padx=2)

        # Filters/Config/Voltages
        misc = ttk.LabelFrame(self, text="Filters / Config / Voltages"); misc.pack(fill="x", padx=8, pady=6)

        # Filters
        frow = ttk.Frame(misc); frow.pack(fill="x", padx=4, pady=2)
        ttk.Label(frow, text="Filter:").grid(row=0, column=0, sticky="w")
        ttk.Combobox(frow, textvariable=self.filter_type_var, values=["PASS_FILTER","BLOCK_FILTER","FLOW_CONTROL_FILTER"], width=22, state="readonly").grid(row=0, column=1, sticky="w", padx=4)
        ttk.Label(frow, text="Mask:").grid(row=0, column=2); ttk.Entry(frow, textvariable=self.filter_mask_var, width=20).grid(row=0, column=3, padx=2)
        ttk.Label(frow, text="Pattern:").grid(row=0, column=4); ttk.Entry(frow, textvariable=self.filter_pattern_var, width=20).grid(row=0, column=5, padx=2)
        ttk.Label(frow, text="Flow:").grid(row=0, column=6); ttk.Entry(frow, textvariable=self.filter_flow_var, width=20).grid(row=0, column=7, padx=2)
        ttk.Button(frow, text="Start", command=self._async(self.action_filter_start)).grid(row=0, column=8, padx=2)
        ttk.Button(frow, text="Clear All", command=self._async(self.action_filter_clear)).grid(row=0, column=9, padx=2)

        frow2 = ttk.Frame(misc); frow2.pack(fill="x", padx=4, pady=2)
        ttk.Label(frow2, text="Filter Id:").grid(row=0, column=0); ttk.Entry(frow2, textvariable=self.filter_id_var, width=8).grid(row=0, column=1)
        ttk.Button(frow2, text="Stop", command=self._async(self.action_filter_stop)).grid(row=0, column=2, padx=2)
        ttk.Separator(frow2, orient="vertical").grid(row=0, column=3, padx=6, sticky="ns")
        ttk.Button(frow2, text="Clear TX", command=self._async(self.action_clear_tx)).grid(row=0, column=4, padx=2)
        ttk.Button(frow2, text="Clear RX", command=self._async(self.action_clear_rx)).grid(row=0, column=5, padx=2)
        ttk.Button(frow2, text="Clear Periodic", command=self._async(self.action_clear_periodic)).grid(row=0, column=6, padx=2)
        ttk.Separator(frow2, orient="vertical").grid(row=0, column=7, padx=6, sticky="ns")
        ttk.Button(frow2, text="VBatt", command=self._async(self.action_vbatt)).grid(row=0, column=8, padx=2)
        ttk.Button(frow2, text="VProg", command=self._async(self.action_vprog)).grid(row=0, column=9, padx=2)

        # Log
        logf = ttk.LabelFrame(self, text="Log"); logf.pack(fill="both", expand=True, padx=8, pady=6)
        self.log = tk.Text(logf, height=18, wrap="word")
        self.log.pack(fill="both", expand=True)
        self._log("Ready.\n")

        # Status bar
        self.status_var = tk.StringVar(value="Idle")
        status = ttk.Label(self, textvariable=self.status_var, relief="sunken", anchor="w")
        status.pack(fill="x", side="bottom")

    # Utilities
    def _log(self, s):
        self.log.insert("end", s if s.endswith("\n") else s + "\n")
        self.log.see("end")

    def set_status(self, s):
        self.status_var.set(s)
        self.update_idletasks()

    def open_swagger(self):
        import webbrowser
        webbrowser.open(self.base_url_var.get().rstrip("/") + "/swagger")

    def browse_dll(self):
        path = filedialog.askopenfilename(title="Select J2534 DLL", filetypes=[("DLL", "*.dll"), ("All files", "*.*")])
        if path:
            self.dll_path_var.set(path)

    # Async decorator
    def _async(self, fn):
        def wrapper(*args, **kwargs):
            t = threading.Thread(target=self._guard(fn), args=args, kwargs=kwargs, daemon=True)
            t.start()
        return wrapper

    def _guard(self, fn):
        def run(*args, **kwargs):
            try:
                self.set_status("Working...")
                fn(*args, **kwargs)
            except Exception as ex:
                messagebox.showerror("Error", str(ex))
                self._log(f"[ERROR] {ex}")
            finally:
                self.set_status("Idle")
        return run

    # Actions
    def action_state(self):
        base = self.base_url_var.get()
        res = http_get(base, "/j2534/state")
        self._log(json.dumps(res, indent=2))

    def action_load(self):
        base = self.base_url_var.get()
        payload = {
            "device": {
                "vendor": self.vendor_var.get().strip() or "Vendor",
                "name": self.dev_name_var.get().strip() or "Name",
                "functionLibrary": self.dll_path_var.get().strip(),
                "configApplication": None
            }
        }
        self._log(f"POST /j2534/load {payload}")
        res = http_post(base, "/j2534/load", payload)
        self._log(json.dumps(res, indent=2))

    def action_free(self):
        base = self.base_url_var.get()
        self._log("POST /j2534/free")
        res = http_post(base, "/j2534/free")
        self._log(json.dumps(res, indent=2))

    def action_open(self):
        base = self.base_url_var.get()
        self._log("POST /j2534/open")
        res = http_post(base, "/j2534/open")
        self._log(json.dumps(res, indent=2))

    def action_close(self):
        base = self.base_url_var.get()
        self._log("POST /j2534/close")
        res = http_post(base, "/j2534/close")
        self._log(json.dumps(res, indent=2))

    def action_connect(self):
        base = self.base_url_var.get()
        payload = {
            "protocol": self.protocol_var.get(),
            "flags": self.flags_var.get(),
            "baud": self.baud_var.get()
        }
        self._log(f"POST /j2534/connect {payload}")
        res = http_post(base, "/j2534/connect", payload)
        self._log(json.dumps(res, indent=2))

    def action_disconnect(self):
        base = self.base_url_var.get()
        self._log("POST /j2534/disconnect")
        res = http_post(base, "/j2534/disconnect")
        self._log(json.dumps(res, indent=2))

    def action_write(self):
        base = self.base_url_var.get()
        payload = {
            "protocol": self.protocol_var.get(),
            "txFlags": "NONE",
            "hexData": self.hex_var.get(),
            "timeoutMs": 100
        }
        self._log(f"POST /j2534/write {payload}")
        res = http_post(base, "/j2534/write", payload)
        self._log(json.dumps(res, indent=2))

    def action_read(self):
        base = self.base_url_var.get()
        payload = {
            "numMsgs": int(self.read_num_var.get()),
            "timeoutMs": int(self.read_timeout_var.get()),
            "untilTimeout": bool(self.read_until_timeout_var.get())
        }
        self._log(f"POST /j2534/read {payload}")
        res = http_post(base, "/j2534/read", payload)
        self._log(json.dumps(res, indent=2))

    def action_filter_start(self):
        base = self.base_url_var.get()
        payload = {
            "type": self.filter_type_var.get(),
            "maskHex": self.filter_mask_var.get(),
            "patternHex": self.filter_pattern_var.get(),
            "flowHex": self.filter_flow_var.get()
        }
        self._log(f"POST /j2534/filters/start {payload}")
        res = http_post(base, "/j2534/filters/start", payload)
        self._log(json.dumps(res, indent=2))
        if isinstance(res, dict) and "filterId" in res:
            try:
                self.filter_id_var.set(int(res["filterId"]))
            except Exception:
                pass

    def action_filter_stop(self):
        base = self.base_url_var.get()
        payload = { "filterId": int(self.filter_id_var.get()) }
        self._log(f"POST /j2534/filters/stop {payload}")
        res = http_post(base, "/j2534/filters/stop", payload)
        self._log(json.dumps(res, indent=2))

    def action_filter_clear(self):
        base = self.base_url_var.get()
        self._log("POST /j2534/filters/clear")
        res = http_post(base, "/j2534/filters/clear")
        self._log(json.dumps(res, indent=2))

    def action_clear_tx(self):
        base = self.base_url_var.get()
        self._log("POST /j2534/clear-tx")
        res = http_post(base, "/j2534/clear-tx")
        self._log(json.dumps(res, indent=2))

    def action_clear_rx(self):
        base = self.base_url_var.get()
        self._log("POST /j2534/clear-rx")
        res = http_post(base, "/j2534/clear-rx")
        self._log(json.dumps(res, indent=2))

    def action_clear_periodic(self):
        base = self.base_url_var.get()
        self._log("POST /j2534/clear-periodic")
        res = http_post(base, "/j2534/clear-periodic")
        self._log(json.dumps(res, indent=2))

    def action_vbatt(self):
        base = self.base_url_var.get()
        self._log("GET /j2534/vbatt")
        res = http_get(base, "/j2534/vbatt")
        self._log(json.dumps(res, indent=2))

    def action_vprog(self):
        base = self.base_url_var.get()
        self._log("GET /j2534/vprog")
        res = http_get(base, "/j2534/vprog")
        self._log(json.dumps(res, indent=2))


def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()
