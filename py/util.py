import os
import json
import logging

abs_file_path = os.path.dirname(os.path.abspath(__file__))

def except_decorative(func):
	def decorator(*args, **keyargs):
		try:
			return func(*args, **keyargs)
		except Exception as e:
			logging.error(f'handle {func.__name__} error: {e}')
	return decorator


def get_json_file(file_path):
	file_path = os.path.join(abs_file_path, file_path)
	with open(file_path, 'r', encoding='utf-8') as json_file:
		return json.load(json_file)


def get_txt_file(file_path='1.txt'):
	file_path = os.path.join(abs_file_path, file_path)
	content = ''
	with open(file_path, encoding='utf8') as txt_file:
		content = txt_file.readlines()
	return [c.strip('\n') for c in content]


def append_txt_file(file_path, save_item, end='\n'):
	file_path = os.path.join(abs_file_path, file_path)
	with open(file_path, 'a', encoding='utf-8') as txt_file:
		txt_file.write(save_item + end)