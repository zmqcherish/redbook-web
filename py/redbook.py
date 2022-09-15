from mitmproxy.options import Options
from mitmproxy.proxy.config import ProxyConfig
from mitmproxy.proxy.server import ProxyServer
from mitmproxy.tools.dump import DumpMaster
import leancloud
from leancloud import Object, Query
from util import *
from config import *

leancloud.init(lc_app_id, lc_app_key, master_key=lc_master_key)
leancloud.use_master_key(True)

RB_ITEM = Object.extend(lc_class_name)

ids_path = 'file/rbIds.txt'
note_ids = get_txt_file(ids_path)
ids_detail_path = 'file/rbIds-detail.txt'
note_detail_ids = get_txt_file(ids_detail_path)

class MainAddon:
	def __init__(self):
		pass

	
	def request(self, flow):
		pass

	
	@except_decorative
	def insert_one(self, note):
		note_id = note['id']
		print('receive note base', note_id)
		a = RB_ITEM()
		for k, v in note.items():
			if not v:
				continue
			a.set(k, v)
		a.set('has_detail', False)
		a.set('display_order', 0)
		a.save()
		append_txt_file(ids_path, note_id)
		note_ids.append(note_id)


	def import_data(self, notes):
		print('receive note list')
		for note in notes:
			if note['id'] in note_ids:
				continue
			self.insert_one(note)


	@except_decorative
	def update_data(self, note):
		note_id = note['id']
		if note_id in note_detail_ids:
			return
		print('receive note detail', note_id)
		data = Query(RB_ITEM).equal_to('id', note_id).find()
		if len(data) != 1:
			print('error', note_id)
			return
		exist_note = data[0]
		exist_note.set('has_detail', True)
		exist_note.set('detail', note['desc'])
		exist_note.save()
		append_txt_file(ids_detail_path, note_id)
		note_detail_ids.append(note_id)


	@except_decorative
	def update_video(self, data):
		for note in data:
			self.update_data(note)


	def response(self, flow):
		req = flow.request
		res = flow.response
		if 'httpbin.org' in req.url:
			res.text = json.dumps({'success': True})
			return
		if 'api/sns/v4/note/user/posted' in req.url:
			data = json.loads(res.text)
			if data['success']:
				self.import_data(data['data']['notes'])
		if 'api/sns/v2/note/feed' in req.url:
			data = json.loads(res.text)
			if data['success']:
				self.update_data(data['data'][0]['note_list'][0])
		if '/api/sns/v3/note/videofeed' in req.url:
			data = json.loads(res.text)
			if data['success']:
				self.update_video(data['data'])


opts = Options(listen_host=proxy_ip, listen_port=proxy_port)
opts.add_option("body_size_limit", int, 0, "")

m = DumpMaster(opts, with_termlog=False, with_dumper=False)
config = ProxyConfig(opts)
m.server = ProxyServer(config)
m.addons.add(MainAddon())

try:
	print('\nproxy:', proxy_ip, proxy_port)
	m.run()
except KeyboardInterrupt:
	m.shutdown()