movie 'E:\Projects\CNC3\Data\APTBUI~1\034A3~1.0-D\pc\Output\SKIRMI~1\\SKIRMI~1.eaf' &compressed // flash 7, total frames: 13, frame rate: 30 fps, 1024x768 px

  &defineMovieClip 2 // total frames: 1
  &end // of defineMovieClip 2
  
  &exportAssets
    2 &as 'GameMovie'
  &end // of exportAssets

  &frame 0
    &constants 'AptZombieClass', 'DeleteFunctions', 'colorInnerFrameA', '3399FF', 'colorInnerFrameB', 'colorLine', 'colorGadgetBox', 'colorGadgetGameSpeed', 'colorTextDark', '0x57512B', 'colorTextBright', '0x31210F', 'colorSubTextBright', '0xC2F47D', 'colorSubTextDark', '0x57842B', 'colorTitleA', '0xCDE47E', 'tabTextColorDark', '0x123B15', 'tabTextColorBritght', '0x8ac14d', '', '/', '_root', 'GameCode', 'Call ', '(', ')', 'GameCodeNoPrefix', 'Call(NP) ', 'FSCommand:', 'GetExtern', 'GetExtern(', ')=>', 'SetExtern', 'SetExtern(', 'ToggleExtern', 'FindAbsolute', '_parent', 'autoPopPossible', '_global', 'InGame', 'testPalette', '_visible'  
    &function2 onUnload () (r:1='this')
      &pushtrue
      &push r:1      
      &pushbyte 2
      &pushsdbgv 0							//'AptZombieClass'
      &dcallmp 1							// DeleteFunctions()
    &end // of function onUnload

    &pushsdb 2							//'colorInnerFrameA'
    &pushsdb 3							//'3399FF'
    &setVariable
    &pushsdb 4							//'colorInnerFrameB'
    &pushsdb 3							//'3399FF'
    &setVariable
    &pushsdb 5							//'colorLine'
    &pushsdb 3							//'3399FF'
    &setVariable
    &pushsdb 6							//'colorGadgetBox'
    &pushsdb 3							//'3399FF'
    &setVariable
    &pushsdb 7							//'colorGadgetGameSpeed'
    &pushsdb 3							//'3399FF'
    &setVariable
    &pushsdb 8							//'colorTextDark'
    &pushsdb 9							//'0x57512B'
    &setVariable
    &pushsdb 10							//'colorTextBright'
    &pushsdb 11							//'0x31210F'
    &setVariable
    &pushsdb 12							//'colorSubTextBright'
    &pushsdb 13							//'0xC2F47D'
    &setVariable
    &pushsdb 14							//'colorSubTextDark'
    &pushsdb 15							//'0x57842B'
    &setVariable
    &pushsdb 16							//'colorTitleA'
    &pushsdb 17							//'0xCDE47E'
    &setVariable
    &pushsdb 18							//'tabTextColorDark'
    &pushsdb 19							//'0x123B15'
    &setVariable
    &pushsdb 20							//'tabTextColorBritght'
    &pushsdb 21							//'0x8ac14d'
    &setVariable
    &pushsdb 22							//''
    &pushbyte 11
    &getProperty
    &pushsdb 23							//'/'
    &equals
    &not
    &jnz label4    
    &pushsdbgv 24							//'_root'
    &pushsdb 25							//'GameCode'
    &function2  (r:1='func', r:2='params') ()
      &pushsdb 26							//'Call '
      &push r:1      
      &add
      &pushsdb 27							//'('
      &add
      &push r:2      
      &add
      &pushsdb 28							//')'
      &add
      &trace
    &end // of function 

    &setMember
    &pushsdbgv 24							//'_root'
    &pushsdb 29							//'GameCodeNoPrefix'
    &function2  (r:1='func', r:2='params') ()
      &pushsdb 30							//'Call(NP) '
      &push r:1      
      &add
      &pushsdb 27							//'('
      &add
      &push r:2      
      &add
      &pushsdb 28							//')'
      &add
      &trace
      &pushsdb 31							//'FSCommand:'
      &push r:1      
      &concat
      &push r:2      
      &getURL2
    &end // of function 

    &setMember
    &pushsdbgv 24							//'_root'
    &pushsdb 32							//'GetExtern'
    &function2  (r:3='ext', r:4='testDefault') (r:1='_root')
      &pushundef
      &setRegister r:2
      &pop
      &push r:1      
      &push r:3      
      &getMember
      &pushundef
      &equals
      &not
      &jnz label1      
      &push r:4      
      &setRegister r:2
      &pop
      &jmp label2      
     label1:
      &push r:1      
      &push r:3      
      &getMember
      &setRegister r:2
      &pop
     label2:
      &pushsdb 33							//'GetExtern('
      &push r:3      
      &add
      &pushsdb 34							//')=>'
      &add
      &push r:2      
      &add
      &trace
      &push r:2      
      &return
    &end // of function 

    &setMember
    &pushsdbgv 24							//'_root'
    &pushsdb 35							//'SetExtern'
    &function2  (r:3='ext', r:2='to') (r:1='_root')
      &push r:1      
      &push r:3      
      &push r:2      
      &setMember
      &pushsdb 36							//'SetExtern('
      &push r:3      
      &add
      &pushsdb 34							//')=>'
      &add
      &push r:2      
      &add
      &trace
    &end // of function 

    &setMember
    &pushsdbgv 24							//'_root'
    &pushsdb 37							//'ToggleExtern'
    &function2  (r:2='ext') (r:1='_root')
      &push r:1      
      &push r:2      
      &push r:1      
      &push r:2      
      &getMember
      &not
      &setMember
    &end // of function 

    &setMember
    &pushsdbgv 24							//'_root'
    &pushsdb 38							//'FindAbsolute'
    &function2  (r:2='of', r:1='from') ()
      &push r:1      
      &pushsdbgm 39							//'_parent'
      &pushundef
      &equals
      &not
      &jnz label3      
      &push r:1      
      &push r:2      
      &getMember
      &return
     label3:
      &push r:1      
      &pushsdbgm 39							//'_parent'
      &push r:2      
      &pushbyte 2
      &pushsdb 38							//'FindAbsolute'
      &callFunction
      &push r:1      
      &push r:2      
      &getMember
      &add
      &return
    &end // of function 

    &setMember
   label4:
    &pushsdb 40							//'autoPopPossible'
    &pushzerosv
    &pushglobalgv
    &pushsdbgm 42							//'InGame'
    &not
    &jnz label5    
    &pushsdbgv 43							//'testPalette'
    &pushsdb 44							//'_visible'
    &pushzero
    &setMember
   label5:
  &end // of frame 0

  &defineMovieClip 8 // total frames: 0
  &end // of defineMovieClip 8
  
  &exportAssets
    8 &as '__Packages.DebugClass'
  &end // of exportAssets
  
  &initMovieClip 8
    &constants '_global', 'DebugClass', 'prototype', 'InitDebugClass', 'm_codePrefix', ':', 'Enable', 'extern', 'InGame', 'Boolean', 'DoTrace', 'm_enabled', 'Trace', 'Dump', 'Dump:', '\t', ': ', ' : ', '', 'ASSetPropFlags'  
    &pushglobalgv
    &pushsdbgm 1							//'DebugClass'
    &not
    &not
    &jnz label5    
    &pushglobalgv
    &pushsdb 1							//'DebugClass'
    &function  (    )    
    &end // of function 

    &setRegister r:0
    &setMember
    &push r:0    
    &pushsdbgm 2							//'prototype'
    &setRegister r:1
    &pop
    &push r:1    
    &pushsdb 3							//'InitDebugClass'
    &function2  (r:2='codePrefix') (r:1='this')
      &push r:1      
      &pushsdb 4							//'m_codePrefix'
      &push r:2      
      &pushsdb 5							//':'
      &add
      &setMember
      &pushfalse
      &pushone
      &push r:1      
      &dcallmp 6							// Enable()
    &end // of function 

    &setMember
    &push r:1    
    &pushsdb 6							//'Enable'
    &function2  (r:2='enable') (r:1='this')
      &push r:1      
      &pushsdbgm 7							//'extern'
      &pushsdbgm 8							//'InGame'
      &toNumber
      &pushone
      &pushsdb 9							//'Boolean'
      &callFunction
      &not
      &not
      &jnz label1      
      &push r:1      
      &pushsdbgm 7							//'extern'
      &pushsdb 10							//'DoTrace'
      &push r:2      
      &setMember
     label1:
      &push r:1      
      &pushsdb 11							//'m_enabled'
      &push r:1      
      &pushsdbgm 7							//'extern'
      &pushsdbgm 10							//'DoTrace'
      &toNumber
      &pushone
      &pushsdb 9							//'Boolean'
      &callFunction
      &setMember
    &end // of function 

    &setMember
    &push r:1    
    &pushsdb 12							//'Trace'
    &function2  (r:2='show') (r:1='this')
      &push r:1      
      &pushsdbgm 11							//'m_enabled'
      &not
      &jnz label2      
      &push r:1      
      &pushsdbgm 4							//'m_codePrefix'
      &push r:2      
      &add
      &trace
     label2:
    &end // of function 

    &setMember
    &push r:1    
    &pushsdb 13							//'Dump'
    &function2  (r:2='obj', r:4='msg') (r:1='this')
      &push r:1      
      &pushsdbgm 11							//'m_enabled'
      &not
      &jnz label4      
      &pushsdb 14							//'Dump:'
      &push r:4      
      &add
      &pushsdb 5							//':'
      &add
      &push r:2      
      &typeof
      &add
      &trace
      &push r:2      
      &enumerateValue
     label3:
      &setRegister r:0
      &pushnull
      &equals
      &jnz label4      
      &push r:0      
      &setRegister r:3
      &pop
      &pushsdb 15							//'\t'
      &push r:3      
      &add
      &pushsdb 16							//': '
      &add
      &push r:2      
      &push r:3      
      &getMember
      &add
      &pushsdb 17							//' : '
      &add
      &push r:2      
      &push r:3      
      &getMember
      &typeof
      &add
      &trace
      &jmp label3      
     label4:
    &end // of function 

    &setMember
    &push r:1    
    &pushsdb 7							//'extern'
    &pushsdb 10							//'DoTrace'
    &pushone
    &pushsdb 8							//'InGame'
    &pushzero
    &pushbyte 2
    &initObject
    &setMember
    &push r:1    
    &pushsdb 4							//'m_codePrefix'
    &pushsdb 18							//''
    &setMember
    &pushone
    &pushnull
    &pushglobalgv
    &pushsdbgm 1							//'DebugClass'
    &pushsdbgm 2							//'prototype'
    &pushbyte 3
    &pushsdb 19							//'ASSetPropFlags'
    &callFunction
   label5:
    &pop
  &end // of initMovieClip 8

  &defineMovieClip 9 // total frames: 0
  &end // of defineMovieClip 9
  
  &exportAssets
    9 &as '__Packages.AptZombieClass'
  &end // of exportAssets
  
  &initMovieClip 9
    &constants '_global', 'AptZombieClass', '_visible', 'MovieClip', 'prototype', 'AddClass', 's_classes', 'push', 'Object', 'registerClass', 'AddObject', 'AddObject:', 'debug', 'Trace', 's_objects', 'DeleteClass', 'DeleteClass:', 'DeleteFunctions', 'DeleteFunctions:', '_target', '   ', ':', 'movieclip', 'function', 'onUnload', 'length', 'Array', 'AptZombieClass::', 'DebugClass', 'ASSetPropFlags'  
    &pushglobalgv
    &pushsdbgm 1							//'AptZombieClass'
    &not
    &not
    &jnz label9    
    &pushglobalgv
    &pushsdb 1							//'AptZombieClass'
    &function2  () (r:1='this', r:2='super')
      &pushzero
      &push r:2      
      &pushundef
      &callmp
      &push r:1      
      &pushsdb 2							//'_visible'
      &pushfalse
      &setMember
    &end // of function 

    &setRegister r:0
    &setMember
    &pushglobalgv
    &pushsdbgm 1							//'AptZombieClass'
    &pushsdbgv 3							//'MovieClip'
    &extends
    &push r:0    
    &pushsdbgm 4							//'prototype'
    &setRegister r:1
    &pop
    &push r:0    
    &pushsdb 5							//'AddClass'
    &function2  (r:1='linkageIdentifier', r:2='className') ()
      &push r:1      
      &pushone
      &pushsdbgv 1							//'AptZombieClass'
      &pushsdbgm 6							//'s_classes'
      &dcallmp 7							// push()
      &push r:2      
      &push r:1      
      &pushbyte 2
      &pushsdbgv 8							//'Object'
      &dcallmp 9							// registerClass()
    &end // of function 

    &setMember
    &push r:0    
    &pushsdb 10							//'AddObject'
    &function2  (r:1='obj') ()
      &pushsdb 11							//'AddObject:'
      &push r:1      
      &add
      &pushone
      &pushsdbgv 1							//'AptZombieClass'
      &pushsdbgm 12							//'debug'
      &dcallmp 13							// Trace()
      &push r:1      
      &pushone
      &pushsdbgv 1							//'AptZombieClass'
      &pushsdbgm 14							//'s_objects'
      &dcallmp 7							// push()
    &end // of function 

    &setMember
    &push r:0    
    &pushsdb 15							//'DeleteClass'
    &function2  (r:2='className') (r:1='_global')
      &pushsdb 16							//'DeleteClass:'
      &push r:2      
      &add
      &pushone
      &pushsdbgv 1							//'AptZombieClass'
      &pushsdbgm 12							//'debug'
      &dcallmp 13							// Trace()
      &pushnull
      &push r:2      
      &pushbyte 2
      &pushsdbgv 8							//'Object'
      &dcallmp 9							// registerClass()
      &push r:1      
      &push r:2      
      &delete
      &pop
    &end // of function 

    &setMember
    &push r:0    
    &pushsdb 17							//'DeleteFunctions'
    &function2  (r:2='obj') ()
      &pushsdb 18							//'DeleteFunctions:'
      &push r:2      
      &pushsdbgm 19							//'_target'
      &add
      &pushone
      &pushsdbgv 1							//'AptZombieClass'
      &pushsdbgm 12							//'debug'
      &dcallmp 13							// Trace()
      &push r:2      
      &enumerateValue
     label1:
      &setRegister r:0
      &pushnull
      &equals
      &jnz label4      
      &push r:0      
      &setRegister r:3
      &pop
      &push r:2      
      &push r:3      
      &getMember
      &typeof
      &setRegister r:1
      &pop
      &pushsdb 20							//'   '
      &push r:3      
      &add
      &pushsdb 21							//':'
      &add
      &push r:1      
      &add
      &pushone
      &pushsdbgv 1							//'AptZombieClass'
      &pushsdbgm 12							//'debug'
      &dcallmp 13							// Trace()
      &push r:1      
      &pushsdb 22							//'movieclip'
      &stringEq
      &not
      &jnz label2      
      &pushtrue
      &push r:2      
      &push r:3      
      &getMember
      &pushbyte 2
      &pushsdbgv 1							//'AptZombieClass'
      &dcallmp 17							// DeleteFunctions()
      &jmp label3      
     label2:
      &push r:1      
      &pushsdb 23							//'function'
      &stringEq
      &not
      &jnz label3      
      &push r:2      
      &push r:3      
      &delete
      &pop
     label3:
      &jmp label1      
     label4:
    &end // of function 

    &setMember
    &push r:1    
    &pushsdb 24							//'onUnload'
    &function2  () ()
      &pushzero
      &setRegister r:1
      &pop
     label5:
      &push r:1      
      &pushsdbgv 1							//'AptZombieClass'
      &pushsdbgm 14							//'s_objects'
      &pushsdbgm 25							//'length'
      &lessThan
      &not
      &jnz label6      
      &push r:1      
      &increment
      &setRegister r:1
      &pop
      &jmp label5      
     label6:
      &pushzero
      &setRegister r:1
      &pop
     label7:
      &push r:1      
      &pushsdbgv 1							//'AptZombieClass'
      &pushsdbgm 6							//'s_classes'
      &pushsdbgm 25							//'length'
      &lessThan
      &not
      &jnz label8      
      &push r:1      
      &increment
      &setRegister r:1
      &pop
      &jmp label7      
     label8:
    &end // of function 

    &setMember
    &push r:0    
    &pushsdb 6							//'s_classes'
    &pushzero
    &pushsdb 26							//'Array'
    &new
    &setMember
    &push r:0    
    &pushsdb 14							//'s_objects'
    &pushzero
    &pushsdb 26							//'Array'
    &new
    &setMember
    &push r:0    
    &pushsdb 12							//'debug'
    &pushsdb 27							//'AptZombieClass::'
    &pushone
    &pushsdb 28							//'DebugClass'
    &new
    &setMember
    &pushone
    &pushnull
    &pushglobalgv
    &pushsdbgm 1							//'AptZombieClass'
    &pushsdbgm 4							//'prototype'
    &pushbyte 3
    &pushsdb 29							//'ASSetPropFlags'
    &callFunction
   label9:
    &pop
  &end // of initMovieClip 9
  
  &importAssets &from 'MpGameSetup.swf'
    'MpGameSetup_Matrix' &as 3
  &end // of importAssets
  
  &importAssets &from 'MpGameSetup.swf'
    'MpGameSetup_Settings' &as 4
  &end // of importAssets
  
  &exportAssets
    2 &as 'GameMovie'
  &end // of exportAssets

  &defineMovieClip 6 // total frames: 1

    &placeMovieClip 2 &as 'SkirmishSetupMovie'
    
      &onClipEvent &construct
        &constants '_MovieName', 'SkirmishSetupMovie', '_CallOnLastFrame', '', '_Loop', '_UseAlpha', '_HoldLastFrame', '_type', 'GameMovie', '_Init', 'GameMovieInit', '_Load'  
        &pushsdb 0							//'_MovieName'
        &pushsdb 1							//'SkirmishSetupMovie'
        &setVariable
        &pushsdb 2							//'_CallOnLastFrame'
        &pushsdb 3							//''
        &setVariable
        &pushsdb 4							//'_Loop'
        &pushtrue
        &setVariable
        &pushsdb 5							//'_UseAlpha'
        &pushfalse
        &setVariable
        &pushsdb 6							//'_HoldLastFrame'
        &pushfalse
        &setVariable
        &pushsdb 7							//'_type'
        &pushsdb 8							//'GameMovie'
        &setVariable
        &pushsdb 9							//'_Init'
        &pushsdb 10							//'GameMovieInit'
        &setVariable
        &pushsdb 11							//'_Load'
        &pushsdb 8							//'GameMovie'
        &setVariable
      &end
    &end // of placeMovieClip 2
  &end // of defineMovieClip 6

  &defineMovieClip 7 // total frames: 1

    &placeMovieClip 3 
    
      &onClipEvent &construct
        &pushs 'vShowReady'
        &pushfalse
        &setVariable
        &pushs 'vShowKick'
        &pushfalse
        &setVariable
        &pushs 'vShowRank'
        &pushfalse
        &setVariable
      &end
    &end // of placeMovieClip 3

    &placeMovieClip 4 &as 'MpMapAndSettings'
    
      &onClipEvent &load
        &pushs ''
        &pushbyte 13
        &pushs 'MpMapAndSettings'
        &setProperty
      &end
    &end // of placeMovieClip 4
  &end // of defineMovieClip 7

  &frame 5
    &stop
    &pushsgv 'autoPop'
    &not
    &jnz label1    
    &pushs 'open'
    &pushone
    &pushs 'PopUpControl'
    &callfp
   label1:
    &pushbyte -1
    &pushone
    &pushs 'SetProgressBar'
    &callfp
  &end // of frame 5

  &frame 6
    &constants 'whereTo', 'profile', '_close', 'titleGraphic', 'gotoAndPlay', 'patternShell', 'buttonDown', 'Back', '_exit', 'bottomNav', 'StartGame'  
    &pushsdbgv 0							//'whereTo'
    &pushsdb 1							//'profile'
    &equals
    &not
    &not
    &jnz label1    
    &pushsdb 2							//'_close'
    &pushone
    &pushsdbgv 3							//'titleGraphic'
    &dcallmp 4							// gotoAndPlay()
    &pushsdb 2							//'_close'
    &pushone
    &pushsdbgv 5							//'patternShell'
    &dcallmp 4							// gotoAndPlay()
   label1:
    &pushsdbgv 6							//'buttonDown'
    &pushsdb 7							//'Back'
    &equals
    &not
    &jnz label2    
    &pushsdb 8							//'_exit'
    &pushone
    &pushsdbgv 9							//'bottomNav'
    &pushsdbgm 10							//'StartGame'
    &dcallmp 4							// gotoAndPlay()
    &jmp label4    
   label2:
    &pushsdbgv 6							//'buttonDown'
    &pushsdb 10							//'StartGame'
    &equals
    &not
    &jnz label3    
    &pushsdb 8							//'_exit'
    &pushone
    &pushsdbgv 9							//'bottomNav'
    &pushsdbgm 7							//'Back'
    &dcallmp 4							// gotoAndPlay()
    &jmp label4    
   label3:
    &pushsdb 8							//'_exit'
    &pushone
    &pushsdbgv 9							//'bottomNav'
    &pushsdbgm 10							//'StartGame'
    &dcallmp 4							// gotoAndPlay()
    &pushsdb 8							//'_exit'
    &pushone
    &pushsdbgv 9							//'bottomNav'
    &pushsdbgm 7							//'Back'
    &dcallmp 4							// gotoAndPlay()
   label4:
  &end // of frame 6

  &frame 11
    &pushzero
    &pushsgv '_root'
    &pushs 'OnMainMovieComplete'
    &callmp
  &end // of frame 11
&end
