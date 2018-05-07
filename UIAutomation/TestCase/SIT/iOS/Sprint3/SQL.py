# -*- coding:utf-8 -*-
# 物品交接
# Author:YueTianzhuang

'''
根据任务表的UKID来查看，当扫码出现在手机上，看状态是否变更；
0，未扫描，5，已扫描，10，该单已交接完成
SELECT status FROM TS_OPERATION WHERE OPERATION_UKID=51763400000007001

--重置任务和卡片，用于重新测试，需要修改OPERATION_UKID和TASK_UKID
UPDATE TS_OPERATION SET STATUS = 0 WHERE OPERATION_UKID = 51763200000008018;

--可以根据任务UKID获取到包裹ID 包裹ID为ITEM_UKID
SELECT * FROM XDW_APP.TS_STOCK_TASK_DETAIL WHERE TASK_UKID=51763200000008018


--STEP 1:
select * from XDW_APP.ts_operation where operation_ukid=51763200000008018

--STEP2:任务和任务明细、卡片的关联关系 找到ITEM_UKID

SELECT TOM.OPERATION_UKID, TOM.OPERATION_NAME, TOM.STATUS,TSTD.*FROM XDW_APP.TS_OPERATION TOM
INNER JOIN XDW_APP.TS_STOCK_TASK_DETAIL TSTD ON TOM.OPERATION_UKID = TSTD.TASK_UKID WHERE TOM.OPERATION_UKID = 51763200000008018

--step3:根据上一步查到的ITEM_UKID然后获在sw_warehouse_service_task获取 CONTRACT_UKID

select * from  XDW_APP.sw_warehouse_service_task where item_ukid=123450

--step4:根据上一步查到的contract_ukid在 dd_warehouse_tracking 表中查相应的记录

SELECT * FROM xdw_app.dd_warehouse_tracking where contract_ukid=12345 and tracking_status=190
'''

'''
--重置任务和卡片，用于重新测试，需要修改OPERATION_UKID和TASK_UKID
UPDATE TS_OPERATION SET STATUS = 0 WHERE OPERATION_UKID = 51763200000008018;

--可以根据任务UKID获取到包裹ID 包裹ID为ITEM_UKID
SELECT * FROM XDW_APP.TS_STOCK_TASK_DETAIL WHERE TASK_UKID=51763200000008018

--STEP 1:
select * from XDW_APP.ts_operation where operation_ukid=51763200000008018

--STEP2:任务和任务明细、卡片的关联关系 找到ITEM_UKID

SELECT TOM.OPERATION_UKID, TOM.OPERATION_NAME, TOM.STATUS,TSTD.*FROM XDW_APP.TS_OPERATION TOM
INNER JOIN XDW_APP.TS_STOCK_TASK_DETAIL TSTD ON TOM.OPERATION_UKID = TSTD.TASK_UKID WHERE TOM.OPERATION_UKID = 51763200000008018

--step3:根据上一步查到的ITEM_UKID然后获在sw_warehouse_service_task获取 CONTRACT_UKID

select * from  XDW_APP.sw_warehouse_service_task where item_ukid=123450

--step4:根据上一步查到的contract_ukid在 dd_warehouse_tracking 表中查相应的记录

select * from xdw_app.dd_contract_tracking where contract_ukid=12345

SELECT * FROM xdw_app.dd_warehouse_tracking where contract_ukid=12345 and tracking_status=190

'''
