#!python3

import openpyxl
hs = openpyxl.load_workbook('ヒアリングシート.xlsx')
hssheet = hs['Sheet1']

cluster_name = hssheet['E4'].value
cluster_dns = hssheet['E5'].value
cluster_management_lif_ip = hssheet['E6'].value
cluster_management_lif_nm = hssheet['E7'].value
cluster_management_lif_gw = hssheet['E8'].value

dd = openpyxl.load_workbook('詳細設計書.xlsx')
ddsheet_cluster = dd['クラスタ情報']

ddsheet_cluster['D4'].value = cluster_name
ddsheet_cluster['D5'].value = cluster_dns
ddsheet_cluster['D6'].value = cluster_management_lif_ip
ddsheet_cluster['D7'].value = cluster_management_lif_nm
ddsheet_cluster['D8'].value = cluster_management_lif_gw
dd.save('詳細設計書.xlsx')
