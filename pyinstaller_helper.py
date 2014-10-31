__author__ = 'sebnil'

import os, sys

def build_version_file():
    print('Build version file')
    print('Version: ' + version)


    version_tuple = version.split('.')


    f = open('version.py', 'w')
    f.write(u"""# UTF-8
#
# For more details about fixed file info 'ffi' see:
# http://msdn.microsoft.com/en-us/library/ms646997.aspx
VSVersionInfo(
  ffi=FixedFileInfo(
    # filevers and prodvers should be always a tuple with four items: (1, 2, 3, 4)
    # Set not needed items to zero 0.
    filevers="""+'({}, {}, {}, {}),'.format(version_tuple[0], version_tuple[1], version_tuple[2], version_tuple[3])+"""
    prodvers="""+'({}, {}, {}, {}),'.format(version_tuple[0], version_tuple[1], version_tuple[2], version_tuple[3])+"""
    # Contains a bitmask that specifies the valid bits 'flags'
    mask=0x3f,
    # Contains a bitmask that specifies the Boolean attributes of the file.
    flags=0x0,
    # The operating system for which this file was designed.
    # 0x4 - NT and there is no need to change it.
    OS=0x4,
    # The general type of file.
    # 0x1 - the file is an application.
    fileType=0x1,
    # The function of the file.
    # 0x0 - the function is not defined for this fileType
    subtype=0x0,
    # Creation date and time stamp.
    date=(0, 0)
    ),
  kids=[
    StringFileInfo(
      [
      StringTable(
        u'040904b0',
        [StringStruct(u'CompanyName', u'"""+company_name +"""'),
        StringStruct(u'ProductName', u'"""+product_name +"""'),
        StringStruct(u'ProductVersion', u'"""+'{}, {}, {}, {}'.format(version_tuple[0], version_tuple[1], version_tuple[2], version_tuple[3])+"""'),
        StringStruct(u'InternalName', u'"""+internal_name +"""'),
        StringStruct(u'OriginalFilename', u'"""+original_filename +"""'),
        StringStruct(u'FileVersion', u'"""+'{}, {}, {}, {}'.format(version_tuple[0], version_tuple[1], version_tuple[2], version_tuple[3])+"""'),
        StringStruct(u'FileDescription', u'"""+file_description +"""'),
        StringStruct(u'LegalCopyright', u'"""+legal_copyright +"""'),
        StringStruct(u'LegalTrademarks', u'"""+legal_trademark +"""')])
      ]),
    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)""")
    f.close()

def get_platform():
    if sys.platform == "linux" or sys.platform == "linux2":
        return 'linux'
    elif sys.platform == "darwin":
        return 'osx'
    elif sys.platform == "win32":
        return 'win'
    else:
        return sys.platform

def get_architecture():
    return 'x64' if sys.maxsize > 2**32 else 'x32'

def build(options):
    filename = options['application_name'] + ' '+ options['version'] + ' ' + get_platform() + ' ' + get_architecture()

    if get_platform() == 'win':
        build_version_file()
        os.system('pyinstaller -y --windowed --onefile --icon=icon/banana.icns --version-file=version.py --name="' + filename + '" ' + options['script'])
    else:
        os.system('pyinstaller -y --windowed --onefile --icon=icon/banana.icns --name="' + filename + '" ' + options['script'])