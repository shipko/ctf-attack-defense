__author__ = 'sea-kg'

from functions import Message
import string
import time
import sys
import os.path
import configparser

class ConfigIni:
	db = {}
	settings = {}
	teams = []
	services = []
	loaded = False
	
	def __init__(self, filename):
		if not os.path.isfile(filename):
			self.loaded = False
			Message.fail('File not found: ' + filename)
			return
		self.filename = filename;

		try:
			config = configparser.ConfigParser()
			config.read(filename)
			self.checkSection('settings', config)
			self.checkSection('teams', config)
			self.checkSection('services', config)
			self.settings['time'] = {};
			self.checkParamInSection('settings', 'time_start', config);
			self.settings['time']['start'] = config['settings']['time_start']
			self.checkParamInSection('settings', 'time_end', config);
			self.settings['time']['end'] = config['settings']['time_end']
			self.checkParamInSection('settings', 'name', config);
			self.settings['name'] = config['settings']['name']
			self.checkParamInSection('settings', 'round_length', config);
			self.settings['round_length'] = config['settings']['round_length']
			self.settings['flags'] = {};
			self.checkParamInSection('settings', 'flags_lifetime', config);
			self.settings['flags']['lifetime'] = config['settings']['flags_lifetime']
			self.checkParamInSection('settings', 'flags_port', config);
			self.settings['flags']['port'] = config['settings']['flags_port']
			self.settings['admin'] = {};
			self.checkParamInSection('settings', 'admin_login', config);
			self.settings['admin']['login'] = config['settings']['admin_login']
			self.checkParamInSection('settings', 'admin_pass', config);
			self.settings['admin']['pass'] = config['settings']['admin_pass']
			self.checkParamInSection('settings', 'filename_checkers', config);
			self.settings['filename_checkers'] = config['settings']['filename_checkers']
			self.checkParamInSection('settings', 'path_to_checkers', config);
			self.settings['path_to_checkers'] = config['settings']['path_to_checkers']

			self.checkParamInSection('teams', 'count', config);
			count = int(config['teams']['count'])
			i = 0
			teamfields = ['name', 'network', 'host', 'logo']
			while i < count:
				teampref = 'team' + str(i+1)
				team = {}
				for f in teamfields:
					self.checkParamInSection('teams', teampref + '_' + f, config);
					team[f] = config['teams'][teampref + '_' + f]
				self.teams.append(team);
				i = i + 1

			self.checkParamInSection('services', 'count', config);
			count = int(config['services']['count'])
			i = 0
			servicefields = ['name', 'program']
			while i < count:
				servicepref = 'service' + str(i+1)
				srvc = {}
				for f in servicefields:
					self.checkParamInSection('services', servicepref + '_' + f, config);
					srvc[f] = config['services'][servicepref + '_' + f]
				self.services.append(srvc);
				i = i + 1
			self.loaded = True
		except Exception:
			Message.fail('Invalid format of file: ' + filename)
			self.loaded = False

	def checkSection(self, sectionname, config):
		if sectionname not in config:
			Message.fail("Not found [" + sectionname + "] section in " + self.filename)
			self.loaded = False
			sys.exit(-1);

	def checkParamInSection(self, sectionname, paramname, config):
		if paramname not in config[sectionname]:
			Message.fail("Not found param '" + paramname + "' in [" + sectionname + "] section in " + self.filename)
			self.loaded = False
			sys.exit(-1);
	
	def isLoaded(self):
		return self.loaded
			
'''

{
  "settings":{
	 "time":{
		"start":,
		"end":
	 },
	 "name":"ctfight-0111",
	 "round_length":40,
	 "flags":{
		"lifetime":4,
		"port":2605
	 },
	 "admin":{
		"login":"root",
		"pass":"qwe"
	 }
  },
  "teams":[
	 {
		"name":"Dima",
		"network":"",
		"host":"",
		"logo":""
	 },
	 {
		"name":"Tima",
		"network":"10.53.254.127",
		"host":"10.53.254.127",
		"logo":null
	 },
	 {
		"name":"Dima N.",
		"network":"10.53.254.163",
		"host":"10.53.254.163",
		"logo":null
	 },
	 {
		"name":"Maslyata",
		"network":"10.53.254.138",
		"host":"10.53.254.138",
		"logo":null
	 },
	 {
		"name":"ADS",
		"network":"10.53.254.125",
		"host":"10.53.254.125",
		"logo":null
	 },
	 {
		"name":"Maxim",
		"network":"10.53.254.126",
		"host":"10.53.254.126",
		"logo":null
	 },
	 {
		"name":"Lexa",
		"network":"10.53.254.143",
		"host":"10.53.254.143",
		"logo":null
	 },
	 {
		"name":"Rita",
		"network":"10.53.254.134",
		"host":"10.53.254.134",
		"logo":null
	 }
  ],
  "services":[

  ]
}
'''