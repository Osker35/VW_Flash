# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['VW_Flash_GUI.py'],
    pathex=[],
    binaries=[('lib/lzss/lzss', 'lzss/')],
    datas=[('data', 'data'), ('logging.conf', '.'), ('logs', 'logs'), ('docs', 'docs')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='VW_Flash_GUI',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name='VW_Flash_GUI',
)

app = BUNDLE(
    coll,
    name='VW_Flash_GUI.app',
    icon=None,
    bundle_identifier='com.vwflash.gui',
    version='0.7.3',
    info_plist={
        'NSHighResolutionCapable': True,
        'CFBundleShortVersionString': '0.7.3',
    },
)
