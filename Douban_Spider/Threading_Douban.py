#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: LuZhouheng
# @Date:   2016-05-15 16:51:31
# @Language: Python2.7.8

import urllib2, re, string
import threading, Queue, time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
_DATA = []
FILE_LOCK = threading.Lock()
#构建一个不限制大小的队列
SHARE_Q = Queue.Queue()
#设置线程的个数
_WORKER_THREAD_NUM = 3

class MyThread(threading.Thread):

	def __init__(self, func):
		#调用父类的构造函数
		super(MyThread, self).__init__()
		# 传入线程函数逻辑
		self.func = func

	def run(self):
		self.func()

def worker():
	global SHARE_Q
	while not SHARE_Q.empty():
		# 获得任务
		url = SHARE_Q.get()
		my_page = get_page(url)
		# 获得当前页面的电影名
		find_title(my_page)
		# write_into_file(temp_data)
		time.sleep(1)
		SHARE_Q.task_done()

def get_page(url):

	try:
		my_page = urllib2.urlopen(url).read().decode("utf8")
	except urllib2.URLError, e:
		if hasattr(e, "code"):
			print "The server could not fulfill the request."
			print "Error code: %s" % e.code
		elif hasattr(e, "reason"):
			print "We failed to reach a server. Please check your url and read the Reason."
			print "Reason code: %s" % e.reason
	return my_page

def find_title(my_page):
	temp_data = []
	movie_items = re.findall(r'<span.*?class="title">(.*?)</span>', my_page, re.S)
	for index, item in enumerate(movie_items):
		if item.find("&nbsp") == -1:
			#print item
			temp_data.append(item)
		_DATA.append(temp_data)

def main():
	global SHARE_Q
	threads = []
	douban_url = "http://movie.douban.com/top250?start={page}&filter=&type="
	#向队列中放入任务, 真正使用时, 应该设置为可持续的放入任务
	for index in xrange(10):
		SHARE_Q.put(douban_url.format(page = index * 25))
	for i in xrange(_WORKER_THREAD_NUM):
		thread = MyThread(worker)
		#线程开始处理任务
		thread.start()
		threads.append(thread)
	for thread in threads:
		thread.join()
	SHARE_Q.join()
	with open("movie.json", "w+") as my_file:
		for page in _DATA:
			for movie_name in page:
				my_file.write(movie_name + "\n")
	print "Spider Successfully~"

if __name__ == '__main__':
	main()



