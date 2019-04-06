#!/usr/bin/python
# -*- coding: utf-8 -*-
#  05ip.py
#  
#  Copyright 2019 Álvaro Torralba <donfrutosgomez@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import info_table
import markup
import subprocess

def public_ip():
	cmd = ["wget", "-qO-", "ifconfig.me"]
	process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
	out, error = process.communicate()
	
	public_ip_text = markup.text_set_markup(out.strip())
	public_ip_label = markup.label_set_markup("IP pública")
	return public_ip_label, public_ip_text

def local_ip():
	cmd = ["hostname", "-I"]
	process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
	out, error = process.communicate()
	
	private_ip_text = markup.text_set_markup(out.strip())
	private_ip_label = markup.label_set_markup("IP local")
	return private_ip_label, private_ip_text


info_table.add_row_to_table(local_ip()[0], local_ip()[1], 6, "Dirección IP local")
info_table.add_row_to_table(public_ip()[0], public_ip()[1], 7, "Dirección IP pública")
