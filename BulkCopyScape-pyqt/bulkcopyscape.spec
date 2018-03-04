# -*- mode: python -*-
import platform

block_cipher = None


a = Analysis(['PyInstallerStub.py'],
             pathex=['/Users/justinvieira/BulkCopyscape/BulkCopyScape-pyqt'],
             binaries=[],
             datas=[('resources/resources.qrc', './resources')],
             hiddenimports=['dataset'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='bulkcopyscape',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='bulkcopyscape')


if platform.system() == 'Darwin':
    info_plist = {'addition_prop': 'additional_value'}
    app = BUNDLE(exe,
                 name='Foobar.app',
                 bundle_identifier=None,
                 info_plist=info_plist
)