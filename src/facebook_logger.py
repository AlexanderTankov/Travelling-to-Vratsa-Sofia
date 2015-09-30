# -*- coding: utf-8 -*-

class Facebook_Logger():

	def __init__(self, fbAPI, travel):
		self.fbAPI = fbAPI
		self.travel = travel
		self.post_to_group(fbAPI, travel)

	def post_to_group(self, fbAPI, travel):
		fbAPI.put_wall_post("В {}({}.{}) към {} часа пътувам за {}.\
							 Имам {} свободни места :)".format(
							 							self.travel.weekday, 
							 							self.travel.day, 
							 							self.travel.month, 
							 							self.travel.hour, 
							 							self.travel.destination, 
							 							self.travel.free_spots
							 							),
							 attachment={},
							 profile_id="1710362275850068"
							 )
