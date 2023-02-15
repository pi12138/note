# snmptrap

- snmptrap 使用

## v1

- 格式 `snmptrap -v 1 -c community destination enterprise-oid agent trap-type specific-type uptime [OID TYPE VALUE]`
- 参数说明
    - `-c community` snmp 配置的 community 
    - `destination` 目的地址
    - `enterprise-oid` 企业 oid， 可以为空，为空时取 1.3.6.1.4.1.3.1.1 (enterprises.cmu.1.1)
    - `agent` 当前发出trap设备的主机名，可以为空，为空时取 hostname
    - `trap-type` 基本 trap 类型
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
- specific-type 企业自定义


## v2 

- 格式 `snmptrap -v 1 -c community destination uptime trapoid [OID TYPE VALUE]`
- 参数说明
    - `-c community` snmp 配置的 community 
    - `destination` 目的地址
    - `uptime` 正常运行时间，可以为空，为空时取当前设备的正常运行时间
    - `trapoid` 
    - `[OID TYPE VALUE]` 一组 【oid 值类型 值】的数据，一次可以传输多组

- trapoid 取值
    - 1.3.6.1.6.3.1.1.5.1  Cold Start Trap