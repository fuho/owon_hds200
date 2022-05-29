# HDS200 Info Doc v2022-05-29.01


## Firmware

### FW v5.7.1
- user:            GSR1600
- post:            https://www.eevblog.com/forum/testgear/owon-hds-200-handheld-oscilloscope-w-builtin-dmmawg/msg4030375/#msg4030375
- model:           HDS272S
- hw_version:      3.0
- original fw:     5.3.0
- serial:          2148xxx
- download:        https://www.eevblog.com/forum/testgear/owon-hds-200-handheld-oscilloscope-w-builtin-dmmawg/?action=dlattach;attach=1424170
- MD5:             6DDE63D0EFFCA1B0C4E647D077DBA560
- SHA-1:           9D3922FAD636A00D0A9C866DF32AFF31AD02FDDA


### FW v5.6.3
- user:            rn777
- post:            https://www.eevblog.com/forum/testgear/owon-hds-200-handheld-oscilloscope-w-builtin-dmmawg/msg4013077/#msg4013077
- model:           HDS272S
- hw_version:      3.0
- original fw:     5.3.0
- serial:          2152xxx
- download:        https://www.eevblog.com/forum/testgear/owon-hds-200-handheld-oscilloscope-w-builtin-dmmawg/?action=dlattach;attach=1416373
- MD5:             02FF935625FD1729A1B8CE0B97DFAAF4
- SHA-1:           8E92F62166E19225EC3F67F65FD92DE4D6308E78


### FW v5.6.3
- user:            eti
- post:            https://www.eevblog.com/forum/testgear/owon-hds-200-handheld-oscilloscope-w-builtin-dmmawg/msg4012864/#msg4012864
- model:           HDS272S
- hw_version:      3.0
- download:        https://www.eevblog.com/forum/testgear/owon-hds-200-handheld-oscilloscope-w-builtin-dmmawg/?action=dlattach;attach=1416196
- MD5:             D05A5D23E36E089A6EA952888D019C1B
- SHA-1:           F773BB86256D771494D624813D1C2B79F2A9B980


### FW v5.6.2
- user:            optotester
- post:            https://www.eevblog.com/forum/testgear/owon-hds-200-handheld-oscilloscope-w-builtin-dmmawg/msg3973145/#msg3973145
- model:           HDS272S
- hw_version:      3.0
- download:        https://www.eevblog.com/forum/testgear/owon-hds-200-handheld-oscilloscope-w-builtin-dmmawg/?action=dlattach;attach=1394687
- MD5:             587BE31898848BA7E102EA7C8773A116
- SHA-1:           5130E27FFE62733214DA89225DCFEA7506783D4F


### FW v3.3.3
- user:            tly
- post:            https://www.eevblog.com/forum/testgear/owon-hds-200-handheld-oscilloscope-w-builtin-dmmawg/msg4015513/#msg4015513
- model:           HDS272S
- hw_version:      2.0
- original fw:     3.2.0
- serial:          2128xxx
- download:        https://www.eevblog.com/forum/testgear/owon-hds-200-handheld-oscilloscope-w-builtin-dmmawg/?action=dlattach;attach=1417543
- MD5:             4265D84170607FC7827600E9D35D7319
- SHA-1:           B79C51348F1630828DA1D61A36E247B82CA6F452


### FW v1.4.1
- user:            gtube
- post:            https://www.eevblog.com/forum/testgear/owon-hds-200-handheld-oscilloscope-w-builtin-dmmawg/msg4027384/#msg4027384
- model:           HDS2102S
- hw_version:      1.0
- serial:          2152008
- download:        https://www.eevblog.com/forum/testgear/owon-hds-200-handheld-oscilloscope-w-builtin-dmmawg/?action=dlattach;attach=1423126
- MD5:             40C68BBB4769E3766AAC9F21574547D1
- SHA-1:           2A0F554655BC2A7546DEDD18DE479B6747F3A3B5


### FW v1.7.0
- user:            blurpy
- post:            https://www.eevblog.com/forum/testgear/owon-hds-200-handheld-oscilloscope-w-builtin-dmmawg/msg3639409/#msg3639409
- model:           HDS272S
- download:        https://www.eevblog.com/forum/testgear/owon-hds-200-handheld-oscilloscope-w-builtin-dmmawg/?action=dlattach;attach=1250065
- MD5:             D05A5D23E36E089A6EA952888D019C1B
- SHA-1:           F773BB86256D771494D624813D1C2B79F2A9B980



### FW v1.7.0
- user:            julius.gl
- post:            https://www.eevblog.com/forum/testgear/owon-hds-200-handheld-oscilloscope-w-builtin-dmmawg/msg3624563/#msg3624563
- model:           HDS242S
- original fw:     1.2.0
- serial:          2047xxx
- latest fw:       1.7.0
- download:        https://www.eevblog.com/forum/testgear/owon-hds-200-handheld-oscilloscope-w-builtin-dmmawg/?action=dlattach;attach=1243775
- MD5:             764A75B3580B9BECD3CA5F977B0144FB
- SHA-1:           72E5F744DC524B1B6A92AC9690DC31C055A10B47


## Hardware

At some point flash chip changed from from "Gigadevice" to "Macronix".  The Gigadevice has a type of OTP SecureRom that
is read-only with a hard coded checksum. Those are apparently "NOT upgradable".

#### HDS2102x_main_v1.0
- board date: 2021-09-16
- devices: HDS2102S
- firmware: 1.3.3
- serials: 2152xxx,

#### HW 3.0
- HDS200_MAIN_V3.0
- board date: 2021-09-27
- devices: HDS2102S
- serials: 2148xxx, 2149xxx, 2152xxx,
- firmware: 5.1.1, 5.4.0, 5.7.1,

#### HW 2.2
- board date: 2021-09-09
- devices: HDS242S
- firmware: 4.2.0, 4.6.1
- serials: 2319xxx,

#### HW 2.1
- HDS200_MAIN_V2.1
- board date: 2021-09-09
- devices: HDS242S
- firmware: 4.2.0, 4.6.1
- serials: 2319xxx,

#### HW 2.0
- HDS200_MAIN_V2.0
- board date: 2021-03-24
- devices: HDS272S
- firmware: v3.0.0, v3.1.0, v3.2.0, v3.3.3
- Used for serial numbers 2118xxx -> 2129xxx
- sn 2124274 has gigadevice flash

#### HW 1.0
- HDS200_MAIN_V1.0
- board date: 2020-09-25
- firmware:
- devices: HDS271 (2047221 -TrendX)
- serials: 2047221,