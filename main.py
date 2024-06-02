import ctypes
import os
import tools
import simplejson
import start
import jpype
import jpype.imports
from jpype.types import *
from pathlib import Path
cpp = tools.Cpp_tools()
java = tools.Cpp_tools()
folder = Path(__file__).parent.resolve()
def main():
    with open('./config.json','r') as f:
        data = simplejson.loads(f.read())
    for i in os.listdir('.\\c'):
        if i.endswith('c'):
            if not os.path.exists(f'.\\cppws\\{i[:-2]}.dll'):
                os.system(data['c_code'].format(i[:-2],i))
            cpp.append(ctypes.cdll.LoadLibrary(f'.\\cppws\\{i[:-2]}.dll'),i[:-2])
    for i in os.listdir('.\\cpp'):
        if i.endswith('cpp'):
            if not os.path.exists(f'.\\cppws\\{i[:-4]}.dll'):
                os.system(data['cpp_code'].format(i[:-4],i))
            cpp.append(ctypes.cdll.LoadLibrary(f'.\\cppws\\{i[:-4]}.dll'),i[:-5])
    for i in os.listdir('.\\java'):
        if i.endswith('java'):
            if not os.path.exists(f'.\\java\\{i[:-5]}.class'):
                os.system(data['java_code'].format(i))
    jpype.startJVM(classpath=[os.path.join(folder,'javaws')])
    for i in os.listdir('.\\java'):
        if i.endswith('java'):
            class_name = i[:-5]
            java_class = jpype.JClass(class_name)
            java.append(java_class(), class_name)
    for i in os.listdir('.\\mods'):
        if i.endswith('.py'):
            mod = __import__(i[:-3])
            mod.main()
if __name__ == '__main__':
    main()
    start.main()