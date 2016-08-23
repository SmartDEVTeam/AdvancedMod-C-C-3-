movie 'E:\Projects\CNC3\Data\APTBUI~1\034A3~1.0-D\pc\Output\Skirmish\\Skirmish.eaf' &compressed // flash 7, total frames: 17, frame rate: 30 fps, 1024x768 px

  &frame 0
    &constants 'Call ', 'CodePrefix', '::', '(', ')', 'FSCommand:', 'Call(NP) ', 'Initialized', 'FSCommand:PlaySound', 'extern', 'InGame', 'InBetaDemo', 'InDreamMachineDemo', 'InitFunc', 'EnableComponents:', 'FSCommand:EnableComponents', 'DisableComponents:', 'FSCommand:DisableComponents', 'GetExtern(', ')=>', 'SetExtern(', '_parent', 'FindAbsolute', 'Strategic', 'OpenPlay', 'vScreenName', 'AptMapPreview::GameMapType', 'GetExtern', 'Skirmish', '.swf', 'loadMovie', '_open', 'ProfileMenu', 'gotoAndPlay', 'ProfileButton', 'unloadMovie', 'vShowAddProfile', 'lobby', 'Nav', 'StartGame', 'Enable', 'MainMenu', '_root', 'AptSkirmish', 'colorInnerFrameA', '3399FF', 'colorInnerFrameB', 'colorLine', 'colorGadgetBox', 'colorGadgetGameSpeed', 'colorTextDark', '0x57512B', 'colorTextBright', '0x31210F', 'colorSubTextBright', '0xC2F47D', 'colorSubTextDark', '0x57842B', 'colorTitleA', '0xCDE47E', 'tabTextColorDark', '0x123B15', 'tabTextColorBritght', '0x8ac14d', 'OnInitialized', 'GameCode', 'InitialSetup', 'vShowStatsScreen', '_global', 'testPalette', '_visible'  
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

    &function2 OpenMainMovie () (r:1='_root')
      &pushone
      &jnz label12      
      &pushsdb 23							//'Strategic'
      &jmp label13      
     label12:
      &pushsdb 24							//'OpenPlay'
     label13:
      &setRegister r:2
      &pop
      &pushsdb 25							//'vScreenName'
      &push r:2      
      &pushsdb 26							//'AptMapPreview::GameMapType'
      &pushbyte 2
      &push r:1      
      &dcallmsv 27							// GetExtern()
      &pushsdb 28							//'Skirmish'
      &pushsdbgv 25							//'vScreenName'
      &add
      &pushsdb 29							//'.swf'
      &add
      &setRegister r:3
      &pop
      &push r:3      
      &pushone
      &push r:1      
      &pushsdbgv 25							//'vScreenName'
      &getMember
      &dcallmp 30							// loadMovie()
      &pushsdb 31							//'_open'
      &pushone
      &pushsdbgv 32							//'ProfileMenu'
      &dcallmp 33							// gotoAndPlay()
      &pushsdb 31							//'_open'
      &pushone
      &pushsdbgv 34							//'ProfileButton'
      &dcallmp 33							// gotoAndPlay()
    &end // of function OpenMainMovie

    &function2 OnMainMovieComplete () (r:1='_root')
      &pushzero
      &push r:1      
      &pushsdbgv 25							//'vScreenName'
      &getMember
      &dcallmp 35							// unloadMovie()
      &pushsdb 25							//'vScreenName'
      &pushundef
      &setVariable
      &push r:1      
      &pushsdbgv 25							//'vScreenName'
      &pushundef
      &setMember
    &end // of function OnMainMovieComplete

    &function ShowMain (    )    
      &gotoLabel '_open'
      &play
    &end // of function ShowMain

    &function CloseMain (    )    
      &gotoLabel '_close'
      &play
    &end // of function CloseMain

    &function2 ShowAddProfile () (r:1='_root')
      &push r:1      
      &pushsdb 36							//'vShowAddProfile'
      &pushtrue
      &setMember
    &end // of function ShowAddProfile

    &function ButtonReset (    )    
      &pushzero
      &pushsdbgv 37							//'lobby'
      &pushsdbgm 38							//'Nav'
      &pushsdbgm 39							//'StartGame'
      &dcallmp 40							// Enable()
      &pushzero
      &pushsdbgv 37							//'lobby'
      &pushsdbgm 38							//'Nav'
      &pushsdbgm 41							//'MainMenu'
      &dcallmp 40							// Enable()
    &end // of function ButtonReset

    &function CloseStats (    )    
      &gotoLabel '_close_profile'
      &play
    &end // of function CloseStats

    &pushsdbgv 42							//'_root'
    &pushsdb 1							//'CodePrefix'
    &pushsdb 43							//'AptSkirmish'
    &setMember
    &pushsdb 44							//'colorInnerFrameA'
    &pushsdb 45							//'3399FF'
    &setVariable
    &pushsdb 46							//'colorInnerFrameB'
    &pushsdb 45							//'3399FF'
    &setVariable
    &pushsdb 47							//'colorLine'
    &pushsdb 45							//'3399FF'
    &setVariable
    &pushsdb 48							//'colorGadgetBox'
    &pushsdb 45							//'3399FF'
    &setVariable
    &pushsdb 49							//'colorGadgetGameSpeed'
    &pushsdb 45							//'3399FF'
    &setVariable
    &pushsdb 50							//'colorTextDark'
    &pushsdb 51							//'0x57512B'
    &setVariable
    &pushsdb 52							//'colorTextBright'
    &pushsdb 53							//'0x31210F'
    &setVariable
    &pushsdb 54							//'colorSubTextBright'
    &pushsdb 55							//'0xC2F47D'
    &setVariable
    &pushsdb 56							//'colorSubTextDark'
    &pushsdb 57							//'0x57842B'
    &setVariable
    &pushsdb 58							//'colorTitleA'
    &pushsdb 59							//'0xCDE47E'
    &setVariable
    &pushsdb 60							//'tabTextColorDark'
    &pushsdb 61							//'0x123B15'
    &setVariable
    &pushsdb 62							//'tabTextColorBritght'
    &pushsdb 63							//'0x8ac14d'
    &setVariable
    &pushsdbgv 42							//'_root'
    &pushsdbgm 7							//'Initialized'
    &not
    &not
    &jnz label15    
    &pushsdbgv 42							//'_root'
    &pushsdbgm 13							//'InitFunc'
    &pushundef
    &equals
    &not
    &jnz label14    
    &pushsdbgv 42							//'_root'
    &pushsdb 13							//'InitFunc'
    &function  (    )    
      &pushsdb 64							//'OnInitialized'
      &pushone
      &dcallfp 65							// GameCode()
    &end // of function 

    &setMember
   label14:
    &pushzero
    &dcallfp 66							// InitialSetup()
   label15:
    &pushsdbgv 42							//'_root'
    &pushsdb 67							//'vShowStatsScreen'
    &pushfalse
    &setMember
    &pushsdbgv 42							//'_root'
    &pushsdb 36							//'vShowAddProfile'
    &pushfalse
    &setMember
    &pushglobalgv
    &pushsdbgm 10							//'InGame'
    &not
    &jnz label16    
    &pushsdbgv 69							//'testPalette'
    &pushsdb 70							//'_visible'
    &pushzero
    &setMember
   label16:
  &end // of frame 0

  &defineMovieClip 1 // total frames: 1
  &end // of defineMovieClip 1

  &defineMovieClip 2 // total frames: 1
  &end // of defineMovieClip 2
  
  &importAssets &from 'ShellContent.swf'
    'ShellContent_ShellBackground' &as 3
  &end // of importAssets
  
  &importAssets &from 'ShellButtons.swf'
    'ShellButtons Small' &as 4
  &end // of importAssets

  &defineMovieClip 5 // total frames: 1

    &frame 0
      &constants 'StartGame', 'ShowBttn', 'ReleaseCallback', 'Disabled', 'SetMode', 'MainMenu', 'GameCode'  
      &pushzero
      &pushsdbgv 0							//'StartGame'
      &dcallmp 1							// ShowBttn()
      &pushsdbgv 0							//'StartGame'
      &pushsdb 2							//'ReleaseCallback'
      &function2  () (r:1='_root')
        &pushsdb 3							//'Disabled'
        &pushone
        &pushsdbgv 0							//'StartGame'
        &dcallmp 4							// SetMode()
        &pushsdb 3							//'Disabled'
        &pushone
        &pushsdbgv 5							//'MainMenu'
        &dcallmp 4							// SetMode()
        &pushsdb 0							//'StartGame'
        &pushone
        &push r:1        
        &dcallmp 6							// GameCode()
      &end // of function 

      &setMember
    &end // of frame 0

    &frame 0
      &constants 'MainMenu', 'ShowBttn', 'ReleaseCallback', 'Disabled', 'StartGame', 'SetMode', 'Exit', 'GameCode', 'InGame', '_close', 'gotoAndPlay'  
      &pushzero
      &pushsdbgv 0							//'MainMenu'
      &dcallmp 1							// ShowBttn()
      &pushsdbgv 0							//'MainMenu'
      &pushsdb 2							//'ReleaseCallback'
      &function2  () (r:1='_root', r:2='_global')
        &pushsdb 3							//'Disabled'
        &pushone
        &pushsdbgv 4							//'StartGame'
        &dcallmp 5							// SetMode()
        &pushsdb 6							//'Exit'
        &pushone
        &push r:1        
        &dcallmp 7							// GameCode()
        &push r:2        
        &pushsdbgm 8							//'InGame'
        &not
        &not
        &jnz label1        
        &pushsdb 9							//'_close'
        &pushone
        &push r:1        
        &dcallmp 10							// gotoAndPlay()
       label1:
      &end // of function 

      &setMember
    &end // of frame 0

    &placeMovieClip 4 &as 'StartGame'
    &end // of placeMovieClip 4
  &end // of defineMovieClip 5

  &defineMovieClip 8 // total frames: 1
  &end // of defineMovieClip 8

  &defineMovieClip 11 // total frames: 1
  &end // of defineMovieClip 11

  &defineMovieClip 14 // total frames: 1
  &end // of defineMovieClip 14

  &defineMovieClip 17 // total frames: 7

    &frame 0
      &stop
    &end // of frame 0
  &end // of defineMovieClip 17

  &frame 3
    &pushs 'isClosed'
    &pushfalse
    &setVariable
    &pushzero
    &pushs 'OpenMainMovie'
    &callfp
  &end // of frame 3
  
  &importAssets &from 'Commander.swf'
    'Commander NameFlash' &as 18
  &end // of importAssets

  &placeMovieClip 18 &as 'Difficulty'
  
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
  &end // of placeMovieClip 18

  &defineMovieClip 21 // total frames: 1

    &frame 0
      &pushsgv '_parent'
      &pushsgm 'vScreenName'
      &pushs 'Strategic'
      &equals
      &not
      &jnz label1      
      &pushs 'Title'
      &pushssv '$Strategic'
     label1:
    &end // of frame 0
  &end // of defineMovieClip 21

  &frame 9
    &stop
    &pushs 'isClosed'
    &pushfalse
    &setVariable
  &end // of frame 9

  &frame 10
    &constants '_close', '_root', 'vScreenName', 'gotoAndPlay', 'vShowStatsScreen', 'titleGraphic', 'patternShell', 'buttonDown', 'Back', '_exit', 'bottomNav', 'StartGame'  
    &pushsdb 0							//'_close'
    &pushone
    &pushsdbgv 1							//'_root'
    &pushsdbgv 2							//'vScreenName'
    &getMember
    &dcallmp 3							// gotoAndPlay()
    &pushsdbgv 1							//'_root'
    &pushsdbgm 4							//'vShowStatsScreen'
    &not
    &not
    &jnz label1    
    &pushsdb 0							//'_close'
    &pushone
    &pushsdbgv 5							//'titleGraphic'
    &dcallmp 3							// gotoAndPlay()
    &pushsdb 0							//'_close'
    &pushone
    &pushsdbgv 6							//'patternShell'
    &dcallmp 3							// gotoAndPlay()
   label1:
    &pushsdbgv 7							//'buttonDown'
    &pushsdb 8							//'Back'
    &equals
    &not
    &jnz label2    
    &pushsdb 9							//'_exit'
    &pushone
    &pushsdbgv 10							//'bottomNav'
    &pushsdbgm 11							//'StartGame'
    &dcallmp 3							// gotoAndPlay()
    &jmp label4    
   label2:
    &pushsdbgv 7							//'buttonDown'
    &pushsdb 11							//'StartGame'
    &equals
    &not
    &jnz label3    
    &pushsdb 9							//'_exit'
    &pushone
    &pushsdbgv 10							//'bottomNav'
    &pushsdbgm 8							//'Back'
    &dcallmp 3							// gotoAndPlay()
    &jmp label4    
   label3:
    &pushsdb 9							//'_exit'
    &pushone
    &pushsdbgv 10							//'bottomNav'
    &pushsdbgm 11							//'StartGame'
    &dcallmp 3							// gotoAndPlay()
    &pushsdb 9							//'_exit'
    &pushone
    &pushsdbgv 10							//'bottomNav'
    &pushsdbgm 8							//'Back'
    &dcallmp 3							// gotoAndPlay()
   label4:
  &end // of frame 10

  &frame 16
    &constants '_root', 'vShowStatsScreen', 'isClosed', 'OnClosed', 'GameCode'  
    &pushsdbgv 0							//'_root'
    &pushsdbgm 1							//'vShowStatsScreen'
    &not
    &not
    &jnz label2    
    &stop
    &pushsdbgv 2							//'isClosed'
    &not
    &not
    &jnz label1    
    &pushsdb 3							//'OnClosed'
    &pushone
    &pushsdbgv 0							//'_root'
    &dcallmp 4							// GameCode()
   label1:
    &pushsdb 2							//'isClosed'
    &pushtrue
    &setVariable
   label2:
  &end // of frame 16
&end
