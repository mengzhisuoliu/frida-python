# -*- coding: utf-8 -*-
from __future__ import print_function
import frida
from pprint import pformat
from pygments import highlight
from pygments.formatters import Terminal256Formatter
from pygments.lexers import PythonLexer


print("Local parameters:", highlight(pformat(frida.query_system_parameters()), PythonLexer(), Terminal256Formatter()))
print("USB device parameters:", highlight(pformat(frida.get_usb_device().query_system_parameters()), PythonLexer(), Terminal256Formatter()))
