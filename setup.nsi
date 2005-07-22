; $Id: setup.nsi 110 2005-07-22 10:24:48Z xiphux $

!define py2exeOutputDir 'dist' 
!define exe             'soulforge.exe' 
!define icon            'C:\python24\py.ico' 
!define compressor      'lzma'  ;one of 'zlib', 'bzip2', 'lzma' 
 
!ifdef compressor 
    SetCompressor ${compressor} 
!else 
    SetCompress Off 
!endif 
Name ${exe} 
OutFile ${exe} 
SilentInstall silent 
!ifdef icon 
    Icon ${icon} 
!endif 
	      
Section 
    InitPluginsDir 
    SetOutPath '$PLUGINSDIR' 
    File /r '${py2exeOutputDir}\*.*' 
    SetOutPath '$EXEDIR'        ; uncomment this line to start the exe in the PLUGINSDIR 
    nsExec::Exec $PLUGINSDIR\${exe} 
SectionEnd 
