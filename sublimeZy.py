import sublime
import sublime_plugin


class zy1(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "Hello, World111!")

class dpc2(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			line = region
			if line.empty():
				line = self.view.full_line(region)
			line_contents = self.view.substr(line)
			self.view.insert(edit, line.end(), line_contents)


class ushow(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			line = region
			if line.empty():
				line = self.view.full_line(region)
			line_contents = self.view.substr(line)
			# self.view.insert(edit, line.end(), line_contents)
			str=line_contents.encode('utf-8').decode('unicode-escape')
			print(str)

