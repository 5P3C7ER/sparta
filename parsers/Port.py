#!/usr/bin/python

__author__ =  'SECFORCE'
__version__=  '0.1'

import sys
import xml.dom.minidom
import Service, Script

class Port:
	portId = ''
	protocol= ''
	state=''

	def __init__( self, PortNode ):
		if not (PortNode is None):
			self.port_node = PortNode
			self.portId = PortNode.getAttribute('portid')
			self.protocol = PortNode.getAttribute('protocol')
			self.state = PortNode.getElementsByTagName('state')[0].getAttribute('state')

	def get_service( self ):

		service_node = self.port_node.getElementsByTagName('service')
		
		if len(service_node) > 0:
			service = Service.Service(service_node[0])
			if self.port_node.getElementsByTagName('service')[0].getAttribute('name') == "http" and self.port_node.getElementsByTagName('service')[0].getAttribute('tunnel') == "ssl":
				service.name = "https"
			return service

		return None

	def get_scripts( self ):

		scripts = [ ]

		for script_node in self.port_node.getElementsByTagName('script'):
			scr = Script.Script(script_node)
			scripts.append(scr)

		return scripts
