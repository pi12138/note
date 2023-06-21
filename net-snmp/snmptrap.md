# snmptrap

- snmptrap 使用

## v1

- 格式 `snmptrap -v 1 -c community destination enterprise-oid agent trap-type specific-type uptime [OID TYPE VALUE]`
- 参数说明
    - `-c community` snmp 配置的 community 
    - `destination` 目的地址
    - `enterprise-oid` 企业 oid， 可以为空，为空时取 1.3.6.1.4.1.3.1.1 (enterprises.cmu.1.1)
    - `agent` 当前发出trap设备的主机名，可以为空，为空时取 hostname
    - `trap-type` 基本 trap 类型，又叫 Generic trap type
    - `specific-type` 特殊 trap 类型
    - `uptime` 正常运行时间，可以为空，为空时取当前设备的正常运行时间
    - `[OID TYPE VALUE]` 一组 【oid 值类型 值】的数据，一次可以传输多组

- trap-type 取值
    - 0  Cold Start Trap
    - 1  Warm Start Trap
    - 2  Link Down Trap
    - 3  Link Up Trap
    - 4  Authentication Failure Trap
    - 5  EGP Neighbor Loss Trap
    - 6  Enterprise Specific Trap

|value| type |desc|
|---|---|---|
|0|coldStart|A coldStart trap signifies that the sending protocol entity is reinitializing itself so that the agent’s configuration or the protocol entity implementation can be altered.|
|1|warmStart|A warmStart trap signifies that the sending protocol entity is reinitializing itself so that neither the agent configuration nor the protocol entity implementation can be altered.|
|2|linkDown|A linkDown trap signifies that the sending protocol entity recognizes a failure in one of the communication links represented in the agent’s configuration.<br> A Trap-PDU of type linkDown contains, as the first element of its variable-bindings, the name and value of the ifIndex instance for the affected interface.|
|3|linkUp|	A linkUp trap signifies that the sending protocol entity recognizes that one of the communication links represented in the agent’s configuration has come up.<br> A Trap-PDU of type linkUp contains, as the first element of its variable-bindings, the name and value of the ifIndex instance for the affected interface.|
|4|authenticationFailure|	An authenticationFailure trap signifies that the sending protocol entity is the addressee of a protocol message that is not properly authenticated.|
|5|egpNeighborLoss|An egpNeighborLoss trap signifies that an EGP neighbor for whom the sending protocol entity was an EGP peer has been marked down and the peer relationship no longer exists.<br> The Trap-PDU of the egpNeighborLoss contains, as the first element of its variable-bindings, the name and value of the egpNeighAddr instance for the affected neighbor.|
|6|enterpriseSpecific|An enterpriseSpecific trap signifies that the sending protocol entity recognizes that some Enterprise-specific event has occurred. The specific-trap field identifies the particular trap that occurred.|

- specific-type 企业自定义


## v2c

- 格式 `snmptrap -v 1 -c community destination uptime trapoid [OID TYPE VALUE]`
- 参数说明
    - `-c community` snmp 配置的 community 
    - `destination` 目的地址
    - `uptime` 正常运行时间，可以为空，为空时取当前设备的正常运行时间
    - `trapoid` trap类型，用 oid 表示
    - `[OID TYPE VALUE]` 一组 【oid 值类型 值】的数据，一次可以传输多组

- trapoid 取值
    - 1.3.6.1.6.3.1.1.5.1  SNMPv2-MIB::coldStart
    - 1.3.6.1.6.3.1.1.5.2  SNMPv2-MIB::warmStart 
    - 1.3.6.1.6.3.1.1.5.3  IF-MIB::linkDown
    - 1.3.6.1.6.3.1.1.5.4  IF-MIB::linkUp 
    - 1.3.6.1.6.3.1.1.5.5  SNMPv2-MIB::authenticationFailure

## v3

- 格式 `snmptrap -v 3 -u user -a SHA -A password -x AES -X password -l authPriv destination uptime trapoid [OID TYPE VALUE]`
- 参数说明
    - `-u user` username
    - `-a SHA` 身份验证协议 MD5|SHA|SHA-224|SHA-256|SHA-384|SHA-512
    - `-A password` 身份验证密码
    - `-x AES` 加密协议 DES|AES
    - `-X password` 加密协议密码
    - `-l authPriv` 设置安全级别 (noAuthNoPriv|authNoPriv|authPriv) (无身份验证无加密|有身份验证无加密|有身份验证且有加密)
    - `destination` 目的地址
    - `uptime` 正常运行时间，可以为空，为空时取当前设备的正常运行时间
    - `trapoid` trap类型，用 oid 表示
    - `[OID TYPE VALUE]` 一组 【oid 值类型 值】的数据，一次可以传输多组

## 样例

- 先配置 snmptrapd.conf

```conf
authCommunity log,execute,net public   # for v1 v2c
createUser -e 0x8000000001020304  myuser SHA "password" AES "password"  # for v3
authuser log,execute,net myuser
```

- 执行 `snmptrapd -C -c /root/snmp/snmptrapd.conf -df -Lo` 开启 snmptrapd 的服务，同时可以看到启动log

- v1
```shell
snmptrap -v 1 -c public 10.1.9.3:162 "" "" 1 1 "" 1.3.6.1.9.9.44.1.2.1 i 2`
```

```output
2023-02-16 13:57:33 10.1.9.2 [10.1.9.2] (via UDP: [10.1.9.2]:5919->[10.1.9.3]:162) TRAP, SNMP v1, community public
        SNMPv2-SMI::enterprises.3.1.1 Warm Start Trap (1) Uptime: 1 day, 23:06:33.17
        SNMPv2-SMI::internet.9.9.44.1.2.1 = INTEGER: 2
```

- v2

```shell
snmptrap -v 2c -c public 10.1.9.3:162 "" .1.3.6.1.6.3.1.1.5.6 .1.3.6.1.2.1.1.5.0 s xxx
```

```output
2023-02-16 14:00:27 <UNKNOWN> [UDP: [10.1.9.2]:14261->[10.1.9.3]:162]:
DISMAN-EVENT-MIB::sysUpTimeInstance = Timeticks: (16976791) 1 day, 23:09:27.91  SNMPv2-MIB::snmpTrapOID.0 = OID: SNMPv2-MIB::snmpTraps.6    SNMPv2-MIB::sysName.0 = STRING: xxx
```

- v3

```shell
snmptrap -v 3 -l authPriv -e 0x8000000001020304 -u myuser -a SHA -A password -x AES -X password 10.1.9.3:162 "" .1.3.6.1.6.3.1.1.5.5 .1.3.6.1.2.1.1.5.0 s xxx
```

```output
2023-02-16 14:01:20 master-10.1.9.3 [UDP: [10.1.9.3]:14560->[10.1.9.3]:162]:
DISMAN-EVENT-MIB::sysUpTimeInstance = Timeticks: (381927233) 44 days, 4:54:32.33        SNMPv2-MIB::snmpTrapOID.0 = OID: SNMPv2-MIB::authenticationFailure SNMPv2-MIB::sysName.0 = STRING: xxx
```