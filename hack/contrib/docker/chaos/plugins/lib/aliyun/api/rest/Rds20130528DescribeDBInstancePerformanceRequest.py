'''
Created by auto_sdk on 2015.04.21
'''
from aliyun.api.base import RestApi
class Rds20130528DescribeDBInstancePerformanceRequest(RestApi):
	def __init__(self,domain='rds.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.DBInstanceId = None
		self.EndTime = None
		self.Key = None
		self.StartTime = None

	def getapiname(self):
		return 'rds.aliyuncs.com.DescribeDBInstancePerformance.2013-05-28'
