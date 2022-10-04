#pip install cx_freeze
import cx_Freeze
import sys
base=None

if sys.platform=="win64":
	base = "win64GUI"

executables = [cx_Freeze.Executable('main.py', base=base, icon='icon.ico')]

cx_Freeze.setup(
	name = "PDF-to-Word-Converter-v1.0",
	options = {"main.exe":{"packages":['tkinter'],
							"include_files":['logo.png']}},
	version = '1.0',
	description = "This app converts PDF files into Word documents",
	executables = executables
	)

