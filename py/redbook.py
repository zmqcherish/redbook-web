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


class MainAddon:
	def __init__(self):
		pass

	
	def request(self, flow):
		pass

	
	def insert_one(self, note):
		note_id = note['id']
		print(note_id)
		a = RB_ITEM()
		for k, v in note.items():
			if not v:
				continue
			a.set(k, v)
		a.save()
		append_txt_file(ids_path, note_id)
		note_ids.append(note_id)


	def import_data(self, notes):
		for note in notes:
			if note['id'] in note_ids:
				continue
			note['display_order'] = 0
			self.insert_one(note)


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
			# res.text = json.dumps(data)


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