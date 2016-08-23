movie 'E:\Projects\CNC3\Data\APTBUI~1\034A3~1.0-D\pc\Output\LOADSC~1\\LOADSC~1.eaf' &compressed // flash 7, total frames: 11, frame rate: 30 fps, 1024x768 px

  &frame 0
    &constants 'Call ', 'CodePrefix', '::', '(', ')', 'FSCommand:', 'Call(NP) ', 'Initialized', 'FSCommand:PlaySound', 'extern', 'InGame', 'InBetaDemo', 'InDreamMachineDemo', 'InitFunc', 'EnableComponents:', 'FSCommand:EnableComponents', 'DisableComponents:', 'FSCommand:DisableComponents', 'GetExtern(', ')=>', 'SetExtern(', '_parent', 'FindAbsolute', 'UIClip', 'ProgressBars', 'SetBarTo', 'frames', 'gotoAndPlay', 'screen', 'textAnim', 'pageTitle', '_root', 'AptGameLoading', 'colorInnerFrameA', '3399FF', 'colorInnerFrameB', 'colorLine', 'colorGadgetBox', 'colorGadgetGameSpeed', 'colorTextDark', '0x57512B', 'colorTextBright', '0x31210F', 'colorSubTextBright', '0xC2F47D', 'colorSubTextDark', '0x57842B', 'colorTitleA', '0xCDE47E', 'tabTextColorDark', '0x123B15', 'tabTextColorBritght', '0x8ac14d', 'OnInitialized', 'GameCode', 'InitialSetup'  
    &function2 GameCode (r:2='func', r:3='params') (r:1='_root')
      &pushsdb 0							//'Call '
      &push r:1      
      &pushsdbgm 1							//'CodePrefix'
      &add
      &pushsdb 2							//'::'
      &add
      &push r:2      
      &add
      &pushsdb 3							//'('
      &add
      &push r:3      
      &add
      &pushsdb 4							//')'
      &add
      &trace
      &pushsdb 5							//'FSCommand:'
      &push r:1      
      &pushsdbgm 1							//'CodePrefix'
      &pushsdb 2							//'::'
      &add
      &push r:2      
      &add
      &concat
      &push r:3      
      &getURL2
    &end // of function GameCode

    &function2 GameCodeNoPrefix (r:1='func', r:2='params') ()
      &pushsdb 6							//'Call(NP) '
      &push r:1      
      &add
      &pushsdb 3							//'('
      &add
      &push r:2      
      &add
      &pushsdb 4							//')'
      &add
      &trace
      &pushsdb 5							//'FSCommand:'
      &push r:1      
      &concat
      &push r:2      
      &getURL2
    &end // of function GameCodeNoPrefix

    &function2 PlaySound (r:2='name') (r:1='_root')
      &push r:1      
      &pushsdbgm 7							//'Initialized'
      &not
      &not
      &jnz label1      
      &pushundef
      &return
     label1:
      &pushsdb 8							//'FSCommand:PlaySound'
      &push r:2      
      &getURL2
    &end // of function PlaySound

    &function2 InitialSetup () (r:1='_root', r:2='_global')
      &push r:1      
      &pushsdb 7							//'Initialized'
      &pushfalse
      &setMember
      &pushsdbgv 9							//'extern'
      &pushsdbgm 10							//'InGame'
      &not
      &jnz label2      
      &push r:2      
      &pushsdb 10							//'InGame'
      &pushtrue
      &setMember
      &push r:2      
      &pushsdb 11							//'InBetaDemo'
      &pushundef
      &setMember
      &push r:2      
      &pushsdb 12							//'InDreamMachineDemo'
      &pushundef
      &setMember
     label2:
      &pushzero
      &push r:1      
      &dcallmp 13							// InitFunc()
      &push r:1      
      &pushsdb 7							//'Initialized'
      &pushtrue
      &setMember
    &end // of function InitialSetup

    &function2 EnableComponents (r:1='path') ()
      &pushsdb 14							//'EnableComponents:'
      &push r:1      
      &add
      &trace
      &pushsdb 15							//'FSCommand:EnableComponents'
      &push r:1      
      &getURL2
    &end // of function EnableComponents

    &function2 DisableComponents (r:1='path') ()
      &pushsdb 16							//'DisableComponents:'
      &push r:1      
      &add
      &trace
      &pushsdb 17							//'FSCommand:DisableComponents'
      &push r:1      
      &getURL2
    &end // of function DisableComponents

    &function2 GetExtern (r:4='ext', r:5='testDefault') (r:1='_root', r:2='_global')
      &pushundef
      &setRegister r:3
      &pop
      &push r:2      
      &pushsdbgm 10							//'InGame'
      &not
      &jnz label3      
      &pushsdbgv 9							//'extern'
      &push r:4      
      &getMember
      &setRegister r:3
      &pop
      &jmp label6      
     label3:
      &push r:1      
      &push r:4      
      &getMember
      &pushundef
      &equals
      &not
      &jnz label4      
      &push r:5      
      &setRegister r:3
      &pop
      &jmp label5      
     label4:
      &push r:1      
      &push r:4      
      &getMember
      &setRegister r:3
      &pop
     label5:
      &pushsdb 18							//'GetExtern('
      &push r:4      
      &add
      &pushsdb 19							//')=>'
      &add
      &push r:3      
      &add
      &trace
     label6:
      &push r:3      
      &return
    &end // of function GetExtern

    &function2 SetExtern (r:4='ext', r:3='to') (r:1='_root', r:2='_global')
      &push r:2      
      &pushsdbgm 10							//'InGame'
      &not
      &jnz label7      
      &pushsdbgv 9							//'extern'
      &push r:4      
      &push r:3      
      &setMember
      &jmp label8      
     label7:
      &push r:1      
      &push r:4      
      &push r:3      
      &setMember
      &pushsdb 20							//'SetExtern('
      &push r:4      
      &add
      &pushsdb 19							//')=>'
      &add
      &push r:3      
      &add
      &trace
     label8:
    &end // of function SetExtern

    &function2 ToggleExtern (r:4='ext') (r:1='_root', r:2='_global')
      &pushundef
      &setRegister r:3
      &pop
      &push r:2      
      &pushsdbgm 10							//'InGame'
      &not
      &jnz label9      
      &pushsdbgv 9							//'extern'
      &push r:4      
      &getMember
      &toNumber
      &not
      &setRegister r:3
      &pop
      &pushsdbgv 9							//'extern'
      &push r:4      
      &push r:3      
      &setMember
      &jmp label10      
     label9:
      &push r:1      
      &push r:4      
      &getMember
      &not
      &setRegister r:3
      &pop
      &push r:1      
      &push r:4      
      &push r:3      
      &setMember
     label10:
      &push r:3      
      &return
    &end // of function ToggleExtern

    &function StopBackground (    )    
      &getURL 'FSCommand:SetBackground'       'off'      
    &end // of function StopBackground

    &function FadeInBackground (    )    
      &getURL 'FSCommand:SetBackground'       'fadein'      
    &end // of function FadeInBackground

    &function FadeOutBackground (    )    
      &getURL 'FSCommand:SetBackground'       'fadeout'      
    &end // of function FadeOutBackground

    &function2 FindAbsolute (r:2='of', r:1='from') ()
      &push r:1      
      &pushsdbgm 21							//'_parent'
      &pushundef
      &equals
      &not
      &jnz label11      
      &push r:1      
      &push r:2      
      &getMember
      &return
     label11:
      &push r:1      
      &pushsdbgm 21							//'_parent'
      &push r:2      
      &pushbyte 2
      &pushsdb 22							//'FindAbsolute'
      &callFunction
      &push r:1      
      &push r:2      
      &getMember
      &add
      &return
    &end // of function FindAbsolute

    &function2 SetBarTo (r:3='index', r:2='percent') (r:1='_root')
      &push r:2      
      &push r:3      
      &pushbyte 2
      &push r:1      
      &pushsdbgm 23							//'UIClip'
      &pushsdbgm 24							//'ProgressBars'
      &dcallmp 25							// SetBarTo()
    &end // of function SetBarTo

    &function AnimsOpen (    )    
      &pushone
      &pushone
      &pushsdbgv 26							//'frames'
      &dcallmp 27							// gotoAndPlay()
      &pushone
      &pushone
      &pushsdbgv 28							//'screen'
      &dcallmp 27							// gotoAndPlay()
      &pushone
      &pushone
      &pushsdbgv 29							//'textAnim'
      &dcallmp 27							// gotoAndPlay()
      &pushone
      &pushone
      &pushsdbgv 30							//'pageTitle'
      &dcallmp 27							// gotoAndPlay()
    &end // of function AnimsOpen

    &pushsdbgv 31							//'_root'
    &pushsdb 1							//'CodePrefix'
    &pushsdb 32							//'AptGameLoading'
    &setMember
    &pushsdb 33							//'colorInnerFrameA'
    &pushsdb 34							//'3399FF'
    &setVariable
    &pushsdb 35							//'colorInnerFrameB'
    &pushsdb 34							//'3399FF'
    &setVariable
    &pushsdb 36							//'colorLine'
    &pushsdb 34							//'3399FF'
    &setVariable
    &pushsdb 37							//'colorGadgetBox'
    &pushsdb 34							//'3399FF'
    &setVariable
    &pushsdb 38							//'colorGadgetGameSpeed'
    &pushsdb 34							//'3399FF'
    &setVariable
    &pushsdb 39							//'colorTextDark'
    &pushsdb 40							//'0x57512B'
    &setVariable
    &pushsdb 41							//'colorTextBright'
    &pushsdb 42							//'0x31210F'
    &setVariable
    &pushsdb 43							//'colorSubTextBright'
    &pushsdb 44							//'0xC2F47D'
    &setVariable
    &pushsdb 45							//'colorSubTextDark'
    &pushsdb 46							//'0x57842B'
    &setVariable
    &pushsdb 47							//'colorTitleA'
    &pushsdb 48							//'0xCDE47E'
    &setVariable
    &pushsdb 49							//'tabTextColorDark'
    &pushsdb 50							//'0x123B15'
    &setVariable
    &pushsdb 51							//'tabTextColorBritght'
    &pushsdb 52							//'0x8ac14d'
    &setVariable
    &pushsdbgv 31							//'_root'
    &pushsdbgm 7							//'Initialized'
    &not
    &not
    &jnz label13    
    &pushsdbgv 31							//'_root'
    &pushsdbgm 13							//'InitFunc'
    &pushundef
    &equals
    &not
    &jnz label12    
    &pushsdbgv 31							//'_root'
    &pushsdb 13							//'InitFunc'
    &function  (    )    
      &pushsdb 53							//'OnInitialized'
      &pushone
      &dcallfp 54							// GameCode()
    &end // of function 

    &setMember
   label12:
    &pushzero
    &dcallfp 55							// InitialSetup()
   label13:
  &end // of frame 0

  &frame 0
  &end // of frame 0
  
  &importAssets &from 'GameWindowGadgets.swf'
    'ListBox' &as 1
  &end // of importAssets

  &placeMovieClip 1 &as 'MapInfo'
  
    &onClipEvent &construct
      &pushs '_type'
      &pushssv 'ListBox'
      &pushs '_Init'
      &pushssv 'AptMapPreview::MapGadgetInit'
      &pushs '_Load'
      &pushssv 'Apt/ListBox.wnd'
    &end
  &end // of placeMovieClip 1
  
  &importAssets &from 'ShellContent.swf'
    'ShellContent_HideWideScreen' &as 2
  &end // of importAssets

  &placeMovieClip 2 
  
    &onClipEvent &construct
      &pushs 'vAlpha'
      &pushfalse
      &setVariable
    &end
  &end // of placeMovieClip 2
  
  &importAssets &from 'Commander.swf'
    'Commander NameFlash' &as 5
  &end // of importAssets

  &placeMovieClip 5 &as 'Difficulty'
  
    &onClipEvent &construct
      &pushs 'vFlashCommander'
      &pushfalse
      &setVariable
      &pushs 'vFlashOnlineId'
      &pushfalse
      &setVariable
      &pushs 'vShowOnlineId'
      &pushfalse
      &setVariable
    &end
  &end // of placeMovieClip 5

  &defineMovieClip 8 // total frames: 1
  &end // of defineMovieClip 8
  
  &importAssets &from 'MpGameSetup.swf'
    'CurrentMapWin' &as 11
  &end // of importAssets

  &defineMovieClip 12 // total frames: 1

    &placeMovieClip 11 &as 'CurrentMap'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'GameWindow'
        &pushs '_Init'
        &pushssv 'AptMapPreview::MapGadgetInit'
        &pushs '_Load'
        &pushssv 'Apt/MpMapWindow.wnd'
      &end
    &end // of placeMovieClip 11
  &end // of defineMovieClip 12

  &defineMovieClip 14 // total frames: 1
  &end // of defineMovieClip 14

  &defineMovieClip 15 // total frames: 1

    &placeMovieClip 14 &as 'StringInst'
    
      &onClipEvent &load
        &constants 'component', '_parent', 'this', 'stringValue', '$', 'stringName', '_name', 'TheString', '_width', 'stringWidth', 'color', 'Color', 'externName', 'GameLoading:PlayerColor:', 'colorVal', '_root', 'GetExtern', 'setRGB'  
        &pushsdb 0							//'component'
        &pushsdbgv 1							//'_parent'
        &pushsdbgm 1							//'_parent'
        &varEquals
        &pushthisgv
        &pushsdb 3							//'stringValue'
        &pushsdb 4							//'$'
        &pushsdbgv 0							//'component'
        &pushsdbgm 5							//'stringName'
        &add
        &pushsdbgv 1							//'_parent'
        &pushsdbgm 6							//'_name'
        &add
        &setMember
        &pushthisgv
        &pushsdbgm 7							//'TheString'
        &pushsdb 8							//'_width'
        &pushsdbgv 0							//'component'
        &pushsdbgm 9							//'stringWidth'
        &setMember
        &pushsdb 10							//'color'
        &pushsdbgv 7							//'TheString'
        &pushone
        &pushsdb 11							//'Color'
        &new
        &varEquals
        &pushsdb 12							//'externName'
        &pushsdb 13							//'GameLoading:PlayerColor:'
        &pushsdbgv 1							//'_parent'
        &pushsdbgm 6							//'_name'
        &add
        &varEquals
        &pushsdb 14							//'colorVal'
        &pushsdbgv 12							//'externName'
        &pushone
        &pushsdbgv 15							//'_root'
        &pushsdb 16							//'GetExtern'
        &callMethod
        &varEquals
        &pushsdbgv 14							//'colorVal'
        &pushundef
        &equals
        &not
        &jnz label1        
        &pushsdb 14							//'colorVal'
        &pushfloat 4280283648.000000000000000
        &pushsdbgv 1							//'_parent'
        &pushsdbgm 6							//'_name'
        &toNumber
        &pushone
        &add
        &multiply
        &setVariable
       label1:
        &pushsdbgv 14							//'colorVal'
        &toNumber
        &pushone
        &pushsdbgv 10							//'color'
        &dcallmp 17							// setRGB()
      &end
    &end // of placeMovieClip 14
  &end // of defineMovieClip 15

  &defineMovieClip 16 // total frames: 1
  &end // of defineMovieClip 16

  &defineMovieClip 19 // total frames: 1
  &end // of defineMovieClip 19

  &defineMovieClip 22 // total frames: 1
  &end // of defineMovieClip 22

  &defineMovieClip 23 // total frames: 1

    &frame 0
      &constants '_x', 'vSpacingX', 'vDepth', '_name', '_', 'duplicateMovieClip', 'vCurPercent:', 'vCurPercent', ' ,', 'vNumSegments', 'Math', 'round', 'ProgressFull', 'AddSegment', 'vIntervalId', 'clearInterval', 'seg', 'ProgressEmpty', 'FrameUpdate', 'setInterval'  
      &function2 AddSegment (r:1='from', r:5='seg') ()
        &push r:1        
        &pushsdbgm 0							//'_x'
        &push r:5        
        &pushsdbgv 1							//'vSpacingX'
        &multiply
        &add
        &setRegister r:2
        &pop
        &pushsdb 0							//'_x'
        &push r:2        
        &pushone
        &initObject
        &pushsdbgv 2							//'vDepth'
        &pushsdb 2							//'vDepth'
        &pushsdbgv 2							//'vDepth'
        &increment
        &setVariable
        &push r:1        
        &pushsdbgm 3							//'_name'
        &pushsdb 4							//'_'
        &add
        &push r:5        
        &add
        &pushbyte 3
        &push r:1        
        &pushsdb 5							//'duplicateMovieClip'
        &callMethod
        &setRegister r:3
        &pop
      &end // of function AddSegment

      &function2 SetPercent (r:4='newPercent') ()
        &pushfalse
        &setRegister r:2
        &pop
       label1:
        &push r:2        
        &not
        &not
        &jnz label6        
        &pushtrue
        &setRegister r:2
        &pop
        &pushsdb 6							//'vCurPercent:'
        &pushsdbgv 7							//'vCurPercent'
        &add
        &pushsdb 8							//' ,'
        &add
        &push r:4        
        &add
        &trace
        &pushsdbgv 7							//'vCurPercent'
        &push r:4        
        &lessThan
        &dup
        &not
        &jnz label2        
        &pop
        &pushsdbgv 7							//'vCurPercent'
        &pushbyte 100
        &lessThan
       label2:
        &not
        &jnz label5        
        &pushsdbgv 9							//'vNumSegments'
        &pushsdbgv 7							//'vCurPercent'
        &multiply
        &pushbyte 100
        &divide
        &pushone
        &pushsdbgv 10							//'Math'
        &pushsdb 11							//'round'
        &callMethod
        &setRegister r:3
        &pop
        &pushsdb 7							//'vCurPercent'
        &pushsdbgv 7							//'vCurPercent'
        &increment
        &setVariable
        &pushsdb 6							//'vCurPercent:'
        &pushsdbgv 7							//'vCurPercent'
        &add
        &trace
        &pushsdbgv 9							//'vNumSegments'
        &pushsdbgv 7							//'vCurPercent'
        &multiply
        &pushbyte 100
        &divide
        &pushone
        &pushsdbgv 10							//'Math'
        &pushsdb 11							//'round'
        &callMethod
        &setRegister r:1
        &pop
        &push r:3        
        &push r:1        
        &equals
        &not
        &not
        &jnz label3        
        &push r:1        
        &pushsdbgv 12							//'ProgressFull'
        &pushbyte 2
        &dcallfp 13							// AddSegment()
       label3:
        &pushsdbgv 7							//'vCurPercent'
        &pushbyte 100
        &equals
        &not
        &jnz label4        
        &pushsdbgv 14							//'vIntervalId'
        &pushone
        &dcallfp 15							// clearInterval()
        &jmp label5        
       label4:
        &pushsdbgv 7							//'vCurPercent'
        &push r:4        
        &lessThan
        &not
        &setRegister r:2
        &pop
       label5:
        &jmp label1        
       label6:
      &end // of function SetPercent

      &pushsdb 7							//'vCurPercent'
      &pushzero
      &varEquals
      &pushsdb 9							//'vNumSegments'
      &pushbyte 25
      &varEquals
      &pushsdb 1							//'vSpacingX'
      &pushbyte 11
      &varEquals
      &pushsdb 2							//'vDepth'
      &pushbyte 100
      &varEquals
      &pushsdb 16							//'seg'
      &pushone
      &varEquals
     label7:
      &pushsdbgv 16							//'seg'
      &pushsdbgv 9							//'vNumSegments'
      &greaterThan
      &not
      &not
      &jnz label8      
      &pushsdbgv 16							//'seg'
      &pushsdbgv 17							//'ProgressEmpty'
      &pushbyte 2
      &dcallfp 13							// AddSegment()
      &pushsdb 16							//'seg'
      &pushsdbgv 16							//'seg'
      &increment
      &setVariable
      &jmp label7      
     label8:
      &pushsdb 14							//'vIntervalId'
      &pushbyte 100
      &pushsdbgv 18							//'FrameUpdate'
      &pushbyte 2
      &pushsdb 19							//'setInterval'
      &callFunction
      &varEquals
    &end // of frame 0
  &end // of defineMovieClip 23

  &defineMovieClip 25 // total frames: 1

    &frame 0
      &constants 'vCurrentPrecent', '', 'Text', 'text', '%', '&dropShadow', 'Bar', 'SetPercent'  
      &function2 SetPercent (r:1='to') ()
        &push r:1        
        &pushsdbgv 0							//'vCurrentPrecent'
        &lessThan
        &not
        &not
        &jnz label3        
        &pushsdb 0							//'vCurrentPrecent'
        &push r:1        
        &setVariable
        &push r:1        
        &pushzero
        &greaterThan
        &not
        &not
        &jnz label1        
        &pushsdb 1							//''
        &pushbyte 7
        &pushfalse
        &setProperty
        &pushsdbgv 2							//'Text'
        &pushsdb 3							//'text'
        &pushsdb 1							//''
        &setMember
        &jmp label2        
       label1:
        &pushsdb 1							//''
        &pushbyte 7
        &pushtrue
        &setProperty
        &pushsdbgv 2							//'Text'
        &pushsdb 3							//'text'
        &pushsdbgv 0							//'vCurrentPrecent'
        &toString
        &pushsdb 4							//'%'
        &add
        &pushsdb 5							//'&dropShadow'
        &add
        &setMember
       label2:
        &push r:1        
        &pushone
        &pushsdbgv 6							//'Bar'
        &dcallmp 7							// SetPercent()
       label3:
      &end // of function SetPercent

      &pushsdb 0							//'vCurrentPrecent'
      &pushbyte -1
      &varEquals
      &pushbyte -1
      &pushone
      &dcallfp 7							// SetPercent()
    &end // of frame 0
  &end // of defineMovieClip 25

  &defineMovieClip 26 // total frames: 1

    &frame 0
      &function2 SetBarTo (r:4='index', r:3='percent') (r:1='this')
        &pushs 'Bar'
        &push r:4        
        &add
        &setRegister r:2
        &pop
        &push r:3        
        &pushone
        &push r:1        
        &push r:2        
        &getMember
        &pushs 'SetPercent'
        &callmp
      &end // of function SetBarTo

    &end // of frame 0
  &end // of defineMovieClip 26

  &defineMovieClip 28 // total frames: 1
  &end // of defineMovieClip 28

  &defineMovieClip 29 // total frames: 1

    &placeMovieClip 28 &as '6'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'RenderImage'
        &pushs '_imageMap'
        &pushssv 'RankIcon_6'
        &pushs '_mode'
        &pushssv 'SOLID'
      &end
    &end // of placeMovieClip 28

    &placeMovieClip 28 &as '5'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'RenderImage'
        &pushs '_imageMap'
        &pushssv 'RankIcon_5'
        &pushs '_mode'
        &pushssv 'SOLID'
      &end
    &end // of placeMovieClip 28

    &placeMovieClip 28 &as '4'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'RenderImage'
        &pushs '_imageMap'
        &pushssv 'RankIcon_4'
        &pushs '_mode'
        &pushssv 'SOLID'
      &end
    &end // of placeMovieClip 28

    &placeMovieClip 28 &as '3'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'RenderImage'
        &pushs '_imageMap'
        &pushssv 'RankIcon_3'
        &pushs '_mode'
        &pushssv 'SOLID'
      &end
    &end // of placeMovieClip 28

    &placeMovieClip 28 &as '2'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'RenderImage'
        &pushs '_imageMap'
        &pushssv 'RankIcon_2'
        &pushs '_mode'
        &pushssv 'SOLID'
      &end
    &end // of placeMovieClip 28

    &placeMovieClip 28 &as '1'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'RenderImage'
        &pushs '_imageMap'
        &pushssv 'RankIcon_1'
        &pushs '_mode'
        &pushssv 'SOLID'
      &end
    &end // of placeMovieClip 28

    &placeMovieClip 28 &as '0'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'RenderImage'
        &pushs '_imageMap'
        &pushssv 'RankIcon_0'
        &pushs '_mode'
        &pushssv 'SOLID'
      &end
    &end // of placeMovieClip 28

    &placeMovieClip 28 &as '7'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'RenderImage'
        &pushs '_imageMap'
        &pushssv 'RankIcon_7'
        &pushs '_mode'
        &pushssv 'SOLID'
      &end
    &end // of placeMovieClip 28
  &end // of defineMovieClip 29

  &defineMovieClip 30 // total frames: 1

    &placeMovieClip 16 &as 'PlayerName'
    
      &onClipEvent &construct
        &pushs 'stringWidth'
        &pushshort 320
        &setVariable
        &pushs 'stringName'
        &pushssv 'LoadingScreen::PlayerName'
      &end
    &end // of placeMovieClip 16

    &placeMovieClip 16 &as 'TeamNumber'
    
      &onClipEvent &construct
        &pushs 'stringWidth'
        &pushbyte 60
        &setVariable
        &pushs 'stringName'
        &pushssv 'LoadingScreen::TeamNumber'
      &end
    &end // of placeMovieClip 16

    &placeMovieClip 16 &as 'ArmyName'
    
      &onClipEvent &construct
        &pushs 'stringWidth'
        &pushbyte 70
        &setVariable
        &pushs 'stringName'
        &pushssv 'LoadingScreen::ArmyName'
      &end
    &end // of placeMovieClip 16
  &end // of defineMovieClip 30

  &defineMovieClip 32 // total frames: 1
  &end // of defineMovieClip 32

  &placeMovieClip 32 &as 'AptMapPreview::Picture'
  
    &onClipEvent &construct
      &pushs '_type'
      &pushssv 'AptMapPreview::Picture'
    &end
  &end // of placeMovieClip 32

  &frame 1
    &pushzero
    &pushs 'AnimsOpen'
    &callfp
  &end // of frame 1

  &defineMovieClip 34 // total frames: 1

    &frame 0
      &pushsgv 'title'
      &pushs 'text'
      &pushsgv '$Loading'
      &pushs '&dropShadow'
      &add
      &setMember
    &end // of frame 0
  &end // of defineMovieClip 34

  &defineMovieClip 35 // total frames: 1

    &frame 0
      &stop
    &end // of frame 0
  &end // of defineMovieClip 35

  &defineMovieClip 36 // total frames: 1

    &frame 0
    &end // of frame 0
  &end // of defineMovieClip 36

  &defineMovieClip 38 // total frames: 1

    &frame 0
    &end // of frame 0
  &end // of defineMovieClip 38

  &defineMovieClip 40 // total frames: 1

    &frame 0
    &end // of frame 0
  &end // of defineMovieClip 40

  &defineMovieClip 42 // total frames: 1

    &frame 0
    &end // of frame 0
  &end // of defineMovieClip 42

  &defineMovieClip 43 // total frames: 1

    &placeMovieClip 36 
    
      &onClipEvent &load
        &pushthisgv
        &pushs 'stringName'
        &pushssm '$GUI:PlayerName'
      &end
    &end // of placeMovieClip 36

    &placeMovieClip 38 
    
      &onClipEvent &load
        &pushthisgv
        &pushs 'stringName'
        &pushssm '$GUI:TeamNumber'
      &end
    &end // of placeMovieClip 38

    &placeMovieClip 40 
    
      &onClipEvent &load
        &pushthisgv
        &pushs 'stringName'
        &pushssm '$GUI:ArmyName'
      &end
    &end // of placeMovieClip 40

    &placeMovieClip 42 
    
      &onClipEvent &load
        &pushthisgv
        &pushs 'stringName'
        &pushssm '$GUI:PlayerProgress'
      &end
    &end // of placeMovieClip 42
  &end // of defineMovieClip 43

  &defineMovieClip 44 // total frames: 1

    &frame 0
      &stop
    &end // of frame 0
  &end // of defineMovieClip 44

  &frame 10
    &stop
  &end // of frame 10
&end
