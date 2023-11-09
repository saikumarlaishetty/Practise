
content = '{"items":[{"hostId":"c3093580-5c4a-11ee-a628-005056b2d540","displayName":"podC-Ise1","hostName":"podC-Ise1","fqdn":"podC-Ise1.sta-lab.com","ipAddress":"9.132.1.31","gateway":"9.132.1.1","iseNodeType":"ISE","iseNodeTypeLongName":"Identity Services Engine (ISE)","nodeTypes":"Administration, Monitoring","nodePersonas":"Administration, Monitoring","services":"NONE","nodeRoleStatus":"PRIMARY","mntHARole":"STANDBY","combinedRole":"PRI(A), SEC(M)","nicInterface1Id":"c3095c90-5c4a-11ee-a628-005056b2d540","nicInterface1IpAddress":"9.132.1.31","nicInterface1MacAddress":"00-50-56-b2-d5-40","nicInterface1SubNetMask":"255.255.255.0","nicInterface1NicCards":"eth0","enablePAP":"on","enableMNT":"on","enableDedicatedMNT":"off","enablePDP":"off","enableInlinePEP":"off","enableSessionServices":"off","enableProfilerServices":"off","enableSXPServices":"off","enableDeviceAdminServices":"off","enableIdentityMappingServices":"off","sxpInterface":"eth0","enableXGridServices":"off","enablePxCloudServices":"off","enableSecurityAssessmentService":"off","sasLicense":false,"replicationStatus":"Not Applicable","syncStatus":"Not Applicable","repStatus":"CONNECTED","id":"c3093580-5c4a-11ee-a628-005056b2d540","promptCertDetails":false,"certImportConfirmed":false,"version":0,"keylength":0,"isDHCP":false,"isHaEnabled":false,"radiusDescription":"","nmapDescription":"","httpDescription":"","netflowDescription":"","dhcpspanDescription":"","dhcpDescription":"","dnsDescription":"","snmptrapDescription":"","snmpqueryDescription":"","activedirDescription":"","pxgridDescription":"","nmapSubnet":"","dhcpPort":0,"snmptrapPort":0,"netflowPort":0,"dhcpspanDevice":"","dhcpDevice":"","httpDevice":"","snmptrapDevice":"","netflowDevice":"","snmpqueryTimeout":100,"dnsTimeout":2,"snmpqueryRetries":1,"snmpqueryEventTimeout":30,"linkTrapQuery":false,"macTrapQuery":false,"activedirRescanDays":0,"snmptrapId":"","snmpqueryId":"","dhcpId":"","dhcpspanId":"","dnsId":"","netflowId":"","radiusId":"","nmapId":"","httpId":"","activedirId":"","pxgridId":"","snmptrapEnable":false,"snmpqueryEnable":false,"dhcpEnable":false,"dhcpspanEnable":false,"dnsEnable":false,"netflowEnable":false,"radiusEnable":false,"nmapEnable":false,"nmapRunning":false,"httpEnable":false,"activedirEnable":false,"pxgridEnable":false,"isPIC":false}]'

import json


content = json.loads(content)
print(content)





























"""
import re


builds_present = ['-rw-r--r--   1 root     root               84 Jul  4 04:43 .lck-67070b0000000000',
                  '-rw-rw-rw-   1 administrator users       127513421 Jul  7 07:04 config-CFG10-230707-1224.tar.gpg',
                  '-rw-rw-rw-   1 administrator users       128089140 Jul 10 05:01 config-CFG10-230710-1018.tar.gpg',
                  '-rw-r--r--   1 root     root         23029195 Jul  4 04:43 dist.tar.gz',
                  '-rw-r--r--   1 root     root              774 Jul  4 04:43 download.txt',
                  '-rw-r--r--   1 root     root      13497010176 Jul  4 05:21 ise-3.3.0.430.SPA.x86_64.iso',
                  '-rw-r--r--   1 root     root      13497010176 Jul  4 05:21 ise-3.3.0.430.vmserial.SPA.x86_64.iso',
                  '-rw-r--r--   1 root     root      15079276653 Jul  4 05:23 ise-upgradebundle-3.0.x-3.2.x-to-3.3.0.430.SPA.x86_64.tar.gz',
                  '-rw-r--r--   1 root     root       8538528764 Jul  4 05:11 ise-upgradebundle-3.3.0.430.SPA.x86_64.tar.gz',
                  '-rw-r--r--   1 root     root        983695631 Jul  4 04:48 ise-urtbundle-3.3.0.430-1.0.0.SPA.x86_64.tar.gz'
                  '-rw-r--r--   1 root     root      13497010176 Jul  4 05:23 pic-3.3.0.430.vmserial.SPA.x86_64.iso',
                  '-rw-rw-rw-   1 administrator users       861436098 Sep 13 06:41 waste-backup-CFG10-230913-1154.tar.gpg']

current_ver = '3.2.0.542'

upgrade_path = '3.2'  # this is extracted from the current version like upgrade_path.group(1)

build_id = '3.3.0.430'






def fun():
    version = '.'.join(build_id.split('.')[:2])
    if float(version) > float(upgrade_path):
        
    
        print("pattern")
        #pattern = r"ise-upgradebundle-3\.0\.x-3\.2\.x-to-3\.3\.0\.430\.SPA\.x86_64\.tar\.gz"
        pattern = r"ise-upgradebundle-[\d\.{2}x-]+-to-[\d\.]+\.SPA\.x86_64\.tar\.gz"
        #pattern = r"ise-upgradebundle-.*-to-[\d\.]+\.SPA\.x86_64\.tar\.gz"
        for build in builds_present:
            #print(build)
            match = re.search(pattern, build)
            #print(match)
            if match:
                print(match.group())
                
        
        for upgrade in builds_present:
            if re.match(r'.*(ise-upgradebundle-{0}.*)'.format(build_id), upgrade, re.M | re.I):
                re_build = re.match(r'.*\s+(\d\d\d\d+).*(ise-upgradebundle-{0}.*)'.format(build_id), upgrade,
                                    re.M | re.I)
                build_size = re_build.group(1)
                build_name = re_build.group(2)
                return build_size, build_name
            else:
                if re.match(r'.*(ise-upgradebundle-2\.\d\.x.*-to-.*)', upgrade, re.M | re.I):
                    re_build = re.match(r'.*\s+(\d\d\d\d+).*(ise-upgradebundle-2\.\d\.x.*-to-.*\..*)', upgrade,
                                        re.M | re.I)
                    build_size = re_build.group(1)
                    build_name = re_build.group(2)
                    return build_size, build_name

   
    for upgrade in builds_present:

        if build_id.startswith(upgrade_path):
            if re.match(r'.*(ise-upgradebundle-{0}.*)'.format(build_id), upgrade, re.M | re.I):
                re_build = re.match(r'.*\s+(\d\d\d\d+).*(ise-upgradebundle-{0}.*)'.format(build_id),
                                    upgrade, re.M | re.I)
                build_size = re_build.group(1)
                build_name = re_build.group(2)
                return build_size, build_name
        else:
            if re.match(r'.*(ise-upgradebundle-2\.\d\.x.*-to-.*)', upgrade, re.M | re.I):
                re_build = re.match(r'.*\s+(\d\d\d\d+).*(ise-upgradebundle-2\.\d\.x.*-to-.*\..*)', upgrade,
                                    re.M | re.I)
                build_size = re_build.group(1)
                build_name = re_build.group(2)
                return build_size, build_name
    return False
"""


"""
res,res1 = fun()
print(res)
print(res1)

"""
