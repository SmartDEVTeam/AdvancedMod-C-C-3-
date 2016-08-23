movie 'E:\Projects\CNC3\Data\APTBUI~1\034A3~1.0-D\pc\Output\SaveLoad\\SaveLoad.eaf' &compressed // flash 7, total frames: 30, frame rate: 30 fps, 1024x768 px

  &frame 0
    &constants 'Call ', 'CodePrefix', '::', '(', ')', 'FSCommand:', 'Call(NP) ', 'Initialized', 'FSCommand:PlaySound', 'extern', 'InGame', 'InBetaDemo', 'InDreamMachineDemo', 'InitFunc', 'EnableComponents:', 'FSCommand:EnableComponents', 'DisableComponents:', 'FSCommand:DisableComponents', 'GetExtern(', ')=>', 'SetExtern(', '_parent', 'FindAbsolute', 'SetCurrentGameType: ', 'CurrentGameType', 'SetExtern', 'callWhenDone', 'Calling SaveButtonEnable:', 'vSaveButtonedEnabled', ', ', '1', '  enable save button', 'MainButtons', 'Save', 'Enable', '  disable save button', 'Disable', 'Calling LoadButtonEnable', 'vLoadButtonedEnabled', '  enable load button', 'Load', '  disable load button', 'Calling DeleteButtonEnable', 'vDeleteButtonedEnabled', '  enable delete button', 'Delete', '  disable delete button', 'LoadBttnEnabled', 'MessageBox', 'ConfirmationMessage', 'CloseRootOnConfirmation', '_open', 'gotoAndPlay', '_root', 'AptSaveLoad', 'colorInnerFrameA', '3399FF', 'colorInnerFrameB', 'colorLine', 'colorGadgetBox', 'colorGadgetGameSpeed', 'colorTextDark', '0x57512B', 'colorTextBright', '0x31210F', 'colorSubTextBright', '0xC2F47D', 'colorSubTextDark', '0x57842B', 'colorTitleA', '0xCDE47E', 'tabTextColorDark', '0x123B15', 'tabTextColorBritght', '0x8ac14d', 'OnInitialized', 'GameCode', 'InitialSetup', 'SaveLoadMode', 'GameTypes', 'CampaignSkirmishWOTRSP', 'SetCurrentGameType'  
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

    &function2 SetCurrentGameType (r:2='type') (r:1='_root')
      &pushsdb 23							//'SetCurrentGameType: '
      &push r:2      
      &add
      &trace
      &push r:1      
      &pushsdb 24							//'CurrentGameType'
      &push r:2      
      &setMember
      &push r:1      
      &pushsdbgm 24							//'CurrentGameType'
      &pushsdb 24							//'CurrentGameType'
      &pushbyte 2
      &push r:1      
      &dcallmp 25							// SetExtern()
    &end // of function SetCurrentGameType

    &function2 closeDelayed (r:2='callWhenDone') (r:1='_root')
      &push r:1      
      &pushsdb 26							//'callWhenDone'
      &push r:2      
      &setMember
      &gotoLabel '_close'
      &play
    &end // of function closeDelayed

    &function2 SaveButtonEnable (r:1='enable') ()
      &pushsdb 27							//'Calling SaveButtonEnable:'
      &pushsdbgv 28							//'vSaveButtonedEnabled'
      &add
      &pushsdb 29							//', '
      &add
      &push r:1      
      &add
      &trace
      &pushsdbgv 28							//'vSaveButtonedEnabled'
      &push r:1      
      &equals
      &not
      &not
      &jnz label14      
      &push r:1      
      &pushsdb 30							//'1'
      &equals
      &not
      &jnz label12      
      &pushsdb 31							//'  enable save button'
      &trace
      &pushzero
      &pushsdbgv 32							//'MainButtons'
      &pushsdbgm 33							//'Save'
      &dcallmp 34							// Enable()
      &jmp label13      
     label12:
      &pushsdb 35							//'  disable save button'
      &trace
      &pushzero
      &pushsdbgv 32							//'MainButtons'
      &pushsdbgm 33							//'Save'
      &dcallmp 36							// Disable()
     label13:
      &pushsdb 28							//'vSaveButtonedEnabled'
      &push r:1      
      &setVariable
     label14:
    &end // of function SaveButtonEnable

    &function2 LoadButtonEnable (r:1='enable') ()
      &pushsdb 37							//'Calling LoadButtonEnable'
      &pushsdbgv 38							//'vLoadButtonedEnabled'
      &add
      &pushsdb 29							//', '
      &add
      &push r:1      
      &add
      &trace
      &pushsdbgv 38							//'vLoadButtonedEnabled'
      &push r:1      
      &equals
      &not
      &not
      &jnz label17      
      &push r:1      
      &pushsdb 30							//'1'
      &equals
      &not
      &jnz label15      
      &pushsdb 39							//'  enable load button'
      &trace
      &pushzero
      &pushsdbgv 32							//'MainButtons'
      &pushsdbgm 40							//'Load'
      &dcallmp 34							// Enable()
      &jmp label16      
     label15:
      &pushsdb 41							//'  disable load button'
      &trace
      &pushzero
      &pushsdbgv 32							//'MainButtons'
      &pushsdbgm 40							//'Load'
      &dcallmp 36							// Disable()
     label16:
      &pushsdb 38							//'vLoadButtonedEnabled'
      &push r:1      
      &setVariable
     label17:
    &end // of function LoadButtonEnable

    &function2 DeleteButtonEnable (r:1='enable') ()
      &pushsdb 42							//'Calling DeleteButtonEnable'
      &pushsdbgv 43							//'vDeleteButtonedEnabled'
      &add
      &pushsdb 29							//', '
      &add
      &push r:1      
      &add
      &trace
      &pushsdbgv 43							//'vDeleteButtonedEnabled'
      &push r:1      
      &equals
      &not
      &not
      &jnz label20      
      &push r:1      
      &pushsdb 30							//'1'
      &equals
      &not
      &jnz label18      
      &pushsdb 44							//'  enable delete button'
      &trace
      &pushzero
      &pushsdbgv 32							//'MainButtons'
      &pushsdbgm 45							//'Delete'
      &dcallmp 34							// Enable()
      &jmp label19      
     label18:
      &pushsdb 46							//'  disable delete button'
      &trace
      &pushzero
      &pushsdbgv 32							//'MainButtons'
      &pushsdbgm 45							//'Delete'
      &dcallmp 36							// Disable()
     label19:
      &pushsdb 43							//'vDeleteButtonedEnabled'
      &push r:1      
      &setVariable
     label20:
    &end // of function DeleteButtonEnable

    &function OnFileSelected (    )    
      &pushsdbgv 47							//'LoadBttnEnabled'
      &pushtrue
      &equals
      &not
      &not
      &jnz label21      
      &pushzero
      &pushsdbgv 32							//'MainButtons'
      &pushsdbgm 40							//'Load'
      &dcallmp 34							// Enable()
      &pushsdb 47							//'LoadBttnEnabled'
      &pushtrue
      &setVariable
     label21:
    &end // of function OnFileSelected

    &function OnNoFileSelected (    )    
      &pushsdbgv 47							//'LoadBttnEnabled'
      &pushfalse
      &equals
      &not
      &not
      &jnz label22      
      &pushzero
      &pushsdbgv 32							//'MainButtons'
      &pushsdbgm 40							//'Load'
      &dcallmp 34							// Enable()
      &pushzero
      &pushsdbgv 32							//'MainButtons'
      &pushsdbgm 45							//'Delete'
      &dcallmp 36							// Disable()
      &pushsdb 47							//'LoadBttnEnabled'
      &pushfalse
      &setVariable
     label22:
    &end // of function OnNoFileSelected

    &function2 showMessageBox (r:1='Text') ()
      &pushsdbgv 48							//'MessageBox'
      &pushsdb 49							//'ConfirmationMessage'
      &push r:1      
      &setMember
      &pushsdbgv 48							//'MessageBox'
      &pushsdb 50							//'CloseRootOnConfirmation'
      &pushfalse
      &setMember
      &pushsdb 51							//'_open'
      &pushone
      &pushsdbgv 48							//'MessageBox'
      &dcallmp 52							// gotoAndPlay()
    &end // of function showMessageBox

    &pushsdbgv 53							//'_root'
    &pushsdb 1							//'CodePrefix'
    &pushsdb 54							//'AptSaveLoad'
    &setMember
    &pushsdb 55							//'colorInnerFrameA'
    &pushsdb 56							//'3399FF'
    &setVariable
    &pushsdb 57							//'colorInnerFrameB'
    &pushsdb 56							//'3399FF'
    &setVariable
    &pushsdb 58							//'colorLine'
    &pushsdb 56							//'3399FF'
    &setVariable
    &pushsdb 59							//'colorGadgetBox'
    &pushsdb 56							//'3399FF'
    &setVariable
    &pushsdb 60							//'colorGadgetGameSpeed'
    &pushsdb 56							//'3399FF'
    &setVariable
    &pushsdb 61							//'colorTextDark'
    &pushsdb 62							//'0x57512B'
    &setVariable
    &pushsdb 63							//'colorTextBright'
    &pushsdb 64							//'0x31210F'
    &setVariable
    &pushsdb 65							//'colorSubTextBright'
    &pushsdb 66							//'0xC2F47D'
    &setVariable
    &pushsdb 67							//'colorSubTextDark'
    &pushsdb 68							//'0x57842B'
    &setVariable
    &pushsdb 69							//'colorTitleA'
    &pushsdb 70							//'0xCDE47E'
    &setVariable
    &pushsdb 71							//'tabTextColorDark'
    &pushsdb 72							//'0x123B15'
    &setVariable
    &pushsdb 73							//'tabTextColorBritght'
    &pushsdb 74							//'0x8ac14d'
    &setVariable
    &pushsdbgv 53							//'_root'
    &pushsdbgm 7							//'Initialized'
    &not
    &not
    &jnz label24    
    &pushsdbgv 53							//'_root'
    &pushsdbgm 13							//'InitFunc'
    &pushundef
    &equals
    &not
    &jnz label23    
    &pushsdbgv 53							//'_root'
    &pushsdb 13							//'InitFunc'
    &function  (    )    
      &pushsdb 75							//'OnInitialized'
      &pushone
      &dcallfp 76							// GameCode()
    &end // of function 

    &setMember
   label23:
    &pushzero
    &dcallfp 77							// InitialSetup()
   label24:
    &pushsdbgv 9							//'extern'
    &pushsdbgm 10							//'InGame'
    &not
    &jnz label25    
    &pushsdbgv 53							//'_root'
    &pushsdb 78							//'SaveLoadMode'
    &pushsdbgv 9							//'extern'
    &pushsdbgm 78							//'SaveLoadMode'
    &setMember
    &pushsdbgv 53							//'_root'
    &pushsdb 79							//'GameTypes'
    &pushsdbgv 9							//'extern'
    &pushsdbgm 79							//'GameTypes'
    &setMember
    &jmp label26    
   label25:
    &pushsdbgv 53							//'_root'
    &pushsdb 78							//'SaveLoadMode'
    &pushsdb 40							//'Load'
    &setMember
    &pushsdbgv 53							//'_root'
    &pushsdb 79							//'GameTypes'
    &pushsdb 80							//'CampaignSkirmishWOTRSP'
    &setMember
   label26:
    &pushsdbgv 53							//'_root'
    &pushsdbgm 79							//'GameTypes'
    &pushsdb 80							//'CampaignSkirmishWOTRSP'
    &equals
    &not
    &not
    &jnz label27    
    &pushsdbgv 53							//'_root'
    &pushsdbgm 79							//'GameTypes'
    &pushone
    &pushsdbgv 53							//'_root'
    &dcallmp 81							// SetCurrentGameType()
   label27:
    &gotoLabel '_open'
    &play
  &end // of frame 0
  
  &importAssets &from 'ShellContent.swf'
    'ShellContent_ShellBackground' &as 1
  &end // of importAssets

  &placeMovieClip 1 &as 'Background'
  
    &onClipEvent &construct
      &pushs 'vHideScreenBehind'
      &pushtrue
      &setVariable
      &pushs 'vAlpha'
      &pushtrue
      &setVariable
      &pushs 'vTitle'
      &pushssv '$TheTitle'
    &end
  &end // of placeMovieClip 1
  
  &importAssets &from 'ShellContent.swf'
    'ShellContent_HideWideScreen' &as 2
  &end // of importAssets

  &defineMovieClip 5 // total frames: 1
  &end // of defineMovieClip 5

  &defineMovieClip 6 // total frames: 15

    &placeMovieClip 2 
    
      &onClipEvent &construct
        &pushs 'vAlpha'
        &pushtrue
        &setVariable
      &end
    &end // of placeMovieClip 2

    &frame 14
      &stop
    &end // of frame 14
  &end // of defineMovieClip 6

  &defineMovieClip 13 // total frames: 1
  &end // of defineMovieClip 13
  
  &importAssets &from 'ShellButtons.swf'
    'ShellButtons Small' &as 14
  &end // of importAssets

  &defineMovieClip 15 // total frames: 30

    &frame 0
      &pushs 'ConfirmationMessage'
      &pushssv ''
      &pushs 'CloseRootOnConfirmation'
      &pushfalse
      &setVariable
      &stop
    &end // of frame 0

    &placeMovieClip 6 
    
      &onClipEvent &load
        &pushthisgv
        &pushs '_visible'
        &pushzero
        &setMember
      &end
    &end // of placeMovieClip 6

    &frame 9
      &constants 'ConfirmationMessage:  ', 'ConfirmationMessage', 'Save', 'this', 'ConfirmationText', '$OverwriteSaveConfirmation', 'ConfirmationOk', '_visible', 'Load', '$LoadGameConfirmation', 'Delete', '$DeleteGameConfirmation', 'ReplayVersionMismatch', '$OlderReplayVersion', 'ConfirmationYes', 'ConfirmationNo', 'Bad ConfirmationMessage: ', '_root', 'DisableComponents', '$MessageBoxYes', 'SetText', '$MessageBoxNo', '$MessageBoxOk', '', 'SetMode', 'ReleaseCallback', 'HELLO!!!', 'DownButton', ' ', 'callWhenDone', 'ConfirmationCancel'  
      &pushsdb 0							//'ConfirmationMessage:  '
      &pushsdbgv 1							//'ConfirmationMessage'
      &add
      &trace
      &pushsdbgv 1							//'ConfirmationMessage'
      &pushsdb 2							//'Save'
      &equals
      &not
      &jnz label1      
      &pushthisgv
      &pushsdb 4							//'ConfirmationText'
      &pushsdb 5							//'$OverwriteSaveConfirmation'
      &setMember
      &pushsdbgv 6							//'ConfirmationOk'
      &pushsdb 7							//'_visible'
      &pushfalse
      &setMember
      &jmp label5      
     label1:
      &pushsdbgv 1							//'ConfirmationMessage'
      &pushsdb 8							//'Load'
      &equals
      &not
      &jnz label2      
      &pushthisgv
      &pushsdb 4							//'ConfirmationText'
      &pushsdb 9							//'$LoadGameConfirmation'
      &setMember
      &pushsdbgv 6							//'ConfirmationOk'
      &pushsdb 7							//'_visible'
      &pushfalse
      &setMember
      &jmp label5      
     label2:
      &pushsdbgv 1							//'ConfirmationMessage'
      &pushsdb 10							//'Delete'
      &equals
      &not
      &jnz label3      
      &pushthisgv
      &pushsdb 4							//'ConfirmationText'
      &pushsdb 11							//'$DeleteGameConfirmation'
      &setMember
      &pushsdbgv 6							//'ConfirmationOk'
      &pushsdb 7							//'_visible'
      &pushfalse
      &setMember
      &jmp label5      
     label3:
      &pushsdbgv 1							//'ConfirmationMessage'
      &pushsdb 12							//'ReplayVersionMismatch'
      &equals
      &not
      &jnz label4      
      &pushthisgv
      &pushsdb 4							//'ConfirmationText'
      &pushsdb 13							//'$OlderReplayVersion'
      &setMember
      &pushsdbgv 14							//'ConfirmationYes'
      &pushsdb 7							//'_visible'
      &pushfalse
      &setMember
      &pushsdbgv 15							//'ConfirmationNo'
      &pushsdb 7							//'_visible'
      &pushfalse
      &setMember
      &jmp label5      
     label4:
      &pushsdb 16							//'Bad ConfirmationMessage: '
      &pushsdbgv 1							//'ConfirmationMessage'
      &add
      &trace
     label5:
      &pushzero
      &pushsdbgv 17							//'_root'
      &dcallmp 18							// DisableComponents()
      &pushsdb 19							//'$MessageBoxYes'
      &pushone
      &pushsdbgv 14							//'ConfirmationYes'
      &dcallmp 20							// SetText()
      &pushsdb 21							//'$MessageBoxNo'
      &pushone
      &pushsdbgv 15							//'ConfirmationNo'
      &dcallmp 20							// SetText()
      &pushsdb 22							//'$MessageBoxOk'
      &pushone
      &pushsdbgv 6							//'ConfirmationOk'
      &dcallmp 20							// SetText()
      &pushsdb 23							//''
      &pushone
      &pushsdbgv 14							//'ConfirmationYes'
      &dcallmp 24							// SetMode()
      &pushsdb 23							//''
      &pushone
      &pushsdbgv 15							//'ConfirmationNo'
      &dcallmp 24							// SetMode()
      &pushsdb 23							//''
      &pushone
      &pushsdbgv 6							//'ConfirmationOk'
      &dcallmp 24							// SetMode()
      &pushsdbgv 14							//'ConfirmationYes'
      &pushsdb 25							//'ReleaseCallback'
      &function2  () (r:1='_root')
        &pushsdb 26							//'HELLO!!!'
        &trace
        &push r:1        
        &pushsdb 27							//'DownButton'
        &pushsdb 28							//' '
        &setMember
        &pushsdb 29							//'callWhenDone'
        &pushsdb 6							//'ConfirmationOk'
        &setVariable
        &gotoLabel '_close'
        &play
      &end // of function 

      &setMember
      &pushsdbgv 15							//'ConfirmationNo'
      &pushsdb 25							//'ReleaseCallback'
      &function2  () (r:1='_root')
        &push r:1        
        &pushsdb 27							//'DownButton'
        &pushsdb 28							//' '
        &setMember
        &pushsdb 29							//'callWhenDone'
        &pushsdb 30							//'ConfirmationCancel'
        &setVariable
        &gotoLabel '_close'
        &play
      &end // of function 

      &setMember
      &pushsdbgv 6							//'ConfirmationOk'
      &pushsdb 25							//'ReleaseCallback'
      &pushsdbgv 15							//'ConfirmationNo'
      &pushsdbgm 25							//'ReleaseCallback'
      &setMember
    &end // of frame 9

    &placeMovieClip 14 &as 'ConfirmationOk'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv ''
      &end
    &end // of placeMovieClip 14

    &placeMovieClip 14 &as 'ConfirmationNo'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv ''
      &end
    &end // of placeMovieClip 14

    &placeMovieClip 14 &as 'ConfirmationYes'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv ''
      &end
    &end // of placeMovieClip 14

    &frame 13
      &stop
    &end // of frame 13

    &frame 19
      &constants '_exit', 'ConfirmationYes', 'gotoAndPlay', 'ConfirmationNo', 'ConfirmationOk'  
      &pushsdb 0							//'_exit'
      &pushone
      &pushsdbgv 1							//'ConfirmationYes'
      &dcallmp 2							// gotoAndPlay()
      &pushsdb 0							//'_exit'
      &pushone
      &pushsdbgv 3							//'ConfirmationNo'
      &dcallmp 2							// gotoAndPlay()
      &pushsdb 0							//'_exit'
      &pushone
      &pushsdbgv 4							//'ConfirmationOk'
      &dcallmp 2							// gotoAndPlay()
    &end // of frame 19

    &frame 23
      &constants '_root', 'EnableComponents', 'callWhenDone', 'GameCode'  
      &pushzero
      &pushsdbgv 0							//'_root'
      &dcallmp 1							// EnableComponents()
      &pushsdbgv 2							//'callWhenDone'
      &pushundef
      &equals
      &not
      &not
      &jnz label1      
      &pushsdbgv 2							//'callWhenDone'
      &pushone
      &pushsdbgv 0							//'_root'
      &dcallmp 3							// GameCode()
     label1:
      &gotoLabel '_init'
    &end // of frame 23
  &end // of defineMovieClip 15
  
  &importAssets &from 'GameWindowGadgets.swf'
    'ListBox' &as 16
  &end // of importAssets
  
  &importAssets &from 'GameWindowGadgets.swf'
    'TextEntry' &as 17
  &end // of importAssets

  &defineMovieClip 18 // total frames: 1

    &placeMovieClip 16 &as '4~GameList'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'ListBox'
        &pushs '_Init'
        &pushssv 'AptSaveLoad::InitGadgets'
        &pushs '_Load'
        &pushssv 'Apt/ListBox.wnd'
      &end
    &end // of placeMovieClip 16

    &placeMovieClip 17 &as '4~FileNameTextEntry'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'TextEntry'
        &pushs '_Init'
        &pushssv 'AptSaveLoad::InitGadgets'
        &pushs '_Load'
        &pushssv 'Apt/TextEntry.wnd'
      &end
    &end // of placeMovieClip 17

    &placeMovieClip 16 &as '2~AutoSaveList'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'ListBox'
        &pushs '_Init'
        &pushssv 'AptSaveLoad::InitGadgets'
        &pushs '_Load'
        &pushssv 'Apt/ListBox.wnd'
      &end
    &end // of placeMovieClip 16

    &placeMovieClip 16 &as '3~GameList'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'ListBox'
        &pushs '_Init'
        &pushssv 'AptSaveLoad::InitGadgets'
        &pushs '_Load'
        &pushssv 'Apt/ListBox.wnd'
      &end
    &end // of placeMovieClip 16

    &placeMovieClip 16 &as '2~GameList'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'ListBox'
        &pushs '_Init'
        &pushssv 'AptSaveLoad::InitGadgets'
        &pushs '_Load'
        &pushssv 'Apt/ListBox.wnd'
      &end
    &end // of placeMovieClip 16

    &placeMovieClip 16 &as '3~AutoSaveList'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'ListBox'
        &pushs '_Init'
        &pushssv 'AptSaveLoad::InitGadgets'
        &pushs '_Load'
        &pushssv 'Apt/ListBox.wnd'
      &end
    &end // of placeMovieClip 16
  &end // of defineMovieClip 18
  
  &importAssets &from 'Commander.swf'
    'Commander NameFlash' &as 19
  &end // of importAssets

  &placeMovieClip 19 &as 'Difficulty'
  
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
  &end // of placeMovieClip 19

  &frame 9
    &pushsgv '_root'
    &pushsgm 'GameTypes'
    &pushs 'WOTRMP'
    &equals
    &not
    &not
    &jnz label1    
    &pushsgv 'MessengerButton'
    &pushs '_visible'
    &pushzero
    &setMember
   label1:
  &end // of frame 9

  &defineMovieClip 26 // total frames: 1

    &frame 0
      &constants 'colorInnerB', 'this', 'Color', '0x', '_root', 'colorInnerFrameB', 'setRGB'  
      &pushsdb 0							//'colorInnerB'
      &pushthisgv
      &pushone
      &pushsdb 2							//'Color'
      &new
      &setVariable
      &pushsdb 3							//'0x'
      &pushsdbgv 4							//'_root'
      &pushsdbgm 5							//'colorInnerFrameB'
      &add
      &pushone
      &pushsdbgv 0							//'colorInnerB'
      &dcallmp 6							// setRGB()
    &end // of frame 0
  &end // of defineMovieClip 26

  &defineMovieClip 29 // total frames: 1
  &end // of defineMovieClip 29

  &defineMovieClip 40 // total frames: 1

    &frame 0
      &constants 'colorInnerB', 'this', 'Color', '0x', '_root', 'colorInnerFrameB', 'setRGB'  
      &pushsdb 0							//'colorInnerB'
      &pushthisgv
      &pushone
      &pushsdb 2							//'Color'
      &new
      &setVariable
      &pushsdb 3							//'0x'
      &pushsdbgv 4							//'_root'
      &pushsdbgm 5							//'colorInnerFrameB'
      &add
      &pushone
      &pushsdbgv 0							//'colorInnerB'
      &dcallmp 6							// setRGB()
    &end // of frame 0
  &end // of defineMovieClip 40

  &defineMovieClip 48 // total frames: 1

    &frame 0
      &constants 'colorInnerB', 'this', 'Color', '0x', '_root', 'colorInnerFrameB', 'setRGB'  
      &pushsdb 0							//'colorInnerB'
      &pushthisgv
      &pushone
      &pushsdb 2							//'Color'
      &new
      &setVariable
      &pushsdb 3							//'0x'
      &pushsdbgv 4							//'_root'
      &pushsdbgm 5							//'colorInnerFrameB'
      &add
      &pushone
      &pushsdbgv 0							//'colorInnerB'
      &dcallmp 6							// setRGB()
    &end // of frame 0
  &end // of defineMovieClip 48
  
  &importAssets &from 'GameWindowGadgets.swf'
    'CheckBox' &as 49
  &end // of importAssets

  &defineMovieClip 64 // total frames: 1

    &frame 0
      &constants 'colorInnerB', 'this', 'Color', '0x', '_root', 'colorInnerFrameB', 'setRGB'  
      &pushsdb 0							//'colorInnerB'
      &pushthisgv
      &pushone
      &pushsdb 2							//'Color'
      &new
      &setVariable
      &pushsdb 3							//'0x'
      &pushsdbgv 4							//'_root'
      &pushsdbgm 5							//'colorInnerFrameB'
      &add
      &pushone
      &pushsdbgv 0							//'colorInnerB'
      &dcallmp 6							// setRGB()
    &end // of frame 0
  &end // of defineMovieClip 64
  
  &importAssets &from 'ShellButtons.swf'
    'Button_Reg_Over_mc' &as 78
  &end // of importAssets
  
  &importAssets &from 'ShellButtons.swf'
    'Button_Reg_Down' &as 79
  &end // of importAssets
  
  &importAssets &from 'ShellButtons.swf'
    'Bttn1Label_dark' &as 80
  &end // of importAssets

  &defineMovieClip 83 // total frames: 1

    &frame 0
      &pushs 'm_text'
      &pushs '$'
      &pushs ''
      &pushbyte 13
      &getProperty
      &add
      &setVariable
    &end // of frame 0
  &end // of defineMovieClip 83

  &defineMovieClip 84 // total frames: 20

    &frame 0
      &constants '$TabSkirmish', 'SkirmishTab', 'SetText', '', 'SetMode', 'ReleaseCallback', 'Skirmish', 'ToggleTabs'  
      &pushsdb 0							//'$TabSkirmish'
      &pushone
      &pushsdbgv 1							//'SkirmishTab'
      &dcallmp 2							// SetText()
      &pushsdb 3							//''
      &pushone
      &pushsdbgv 1							//'SkirmishTab'
      &dcallmp 4							// SetMode()
      &pushsdbgv 1							//'SkirmishTab'
      &pushsdb 5							//'ReleaseCallback'
      &function2  () (r:1='_parent')
        &pushsdb 6							//'Skirmish'
        &pushone
        &push r:1        
        &dcallmp 7							// ToggleTabs()
      &end // of function 

      &setMember
    &end // of frame 0

    &placeMovieClip 14 &as 'SkirmishTab'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv ''
      &end
    &end // of placeMovieClip 14

    &frame 8
      &stop
    &end // of frame 8

    &frame 9
      &constants '$TabCampaign', 'CampaignTab', 'SetText', '', 'SetMode', 'ReleaseCallback', 'Campaign', 'ToggleTabs'  
      &pushsdb 0							//'$TabCampaign'
      &pushone
      &pushsdbgv 1							//'CampaignTab'
      &dcallmp 2							// SetText()
      &pushsdb 3							//''
      &pushone
      &pushsdbgv 1							//'CampaignTab'
      &dcallmp 4							// SetMode()
      &pushsdbgv 1							//'CampaignTab'
      &pushsdb 5							//'ReleaseCallback'
      &function2  () (r:1='_parent')
        &pushsdb 6							//'Campaign'
        &pushone
        &push r:1        
        &dcallmp 7							// ToggleTabs()
      &end // of function 

      &setMember
    &end // of frame 9

    &placeMovieClip 14 &as 'CampaignTab'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv ''
      &end
    &end // of placeMovieClip 14

    &frame 19
      &stop
    &end // of frame 19
  &end // of defineMovieClip 84

  &defineMovieClip 94 // total frames: 1

    &frame 0
      &constants 'colorInnerB', 'this', 'Color', '0x', '_root', 'colorInnerFrameB', 'setRGB'  
      &pushsdb 0							//'colorInnerB'
      &pushthisgv
      &pushone
      &pushsdb 2							//'Color'
      &new
      &setVariable
      &pushsdb 3							//'0x'
      &pushsdbgv 4							//'_root'
      &pushsdbgm 5							//'colorInnerFrameB'
      &add
      &pushone
      &pushsdbgv 0							//'colorInnerB'
      &dcallmp 6							// setRGB()
    &end // of frame 0
  &end // of defineMovieClip 94

  &defineMovieClip 100 // total frames: 88

    &frame 0
      &constants 'DoAssignColumnHeaderNames', 'OnUnload', 'CurrentGameType', 'WOTRSP', 'Column0', '$Name', 'Column1', ' ', 'WOTRMP', '$Players', 'Skirmish', 'Replay', '$Map', '$Mission', 'Campaign', 'Column2', '$Hero', 'Column3', '$Time', 'Column4', '$Date', '_root', 'SaveLoadMode', 'Load', 'ScreenHeader', 'text', '$HeaderLoadSavedGame', 'GameTypes', 'CampaignSkirmishWOTRSP', 'Background', 'SetTitle', '$HeaderLoadSavedReplay', 'Save', '$HeaderSaveReplay', '$HeaderSaveGame'  
      &function onUnload (      )      
        &pushsdb 0							//'DoAssignColumnHeaderNames'
        &delete2
        &pop
        &pushsdb 1							//'OnUnload'
        &delete2
        &pop
      &end // of function onUnload

      &function2 DoAssignColumnHeaderNames () (r:1='_root')
        &push r:1        
        &pushsdbgm 2							//'CurrentGameType'
        &pushsdb 3							//'WOTRSP'
        &equals
        &not
        &jnz label1        
        &pushsdb 4							//'Column0'
        &pushsdb 5							//'$Name'
        &setVariable
        &pushsdb 6							//'Column1'
        &pushsdb 7							//' '
        &setVariable
        &jmp label6        
       label1:
        &push r:1        
        &pushsdbgm 2							//'CurrentGameType'
        &pushsdb 8							//'WOTRMP'
        &equals
        &not
        &jnz label2        
        &pushsdb 4							//'Column0'
        &pushsdb 5							//'$Name'
        &setVariable
        &pushsdb 6							//'Column1'
        &pushsdb 9							//'$Players'
        &setVariable
        &jmp label6        
       label2:
        &push r:1        
        &pushsdbgm 2							//'CurrentGameType'
        &pushsdb 10							//'Skirmish'
        &equals
        &dup
        &jnz label3        
        &pop
        &push r:1        
        &pushsdbgm 2							//'CurrentGameType'
        &pushsdb 11							//'Replay'
        &equals
       label3:
        &not
        &jnz label4        
        &pushsdb 4							//'Column0'
        &pushsdb 12							//'$Map'
        &setVariable
        &jmp label5        
       label4:
        &pushsdb 4							//'Column0'
        &pushsdb 13							//'$Mission'
        &setVariable
       label5:
        &pushsdb 6							//'Column1'
        &pushsdb 5							//'$Name'
        &setVariable
       label6:
        &push r:1        
        &pushsdbgm 2							//'CurrentGameType'
        &pushsdb 14							//'Campaign'
        &equals
        &not
        &jnz label7        
        &pushsdb 15							//'Column2'
        &pushsdb 7							//' '
        &setVariable
        &jmp label8        
       label7:
        &pushsdb 15							//'Column2'
        &pushsdb 16							//'$Hero'
        &setVariable
       label8:
        &pushsdb 17							//'Column3'
        &pushsdb 18							//'$Time'
        &setVariable
        &pushsdb 19							//'Column4'
        &pushsdb 20							//'$Date'
        &setVariable
      &end // of function DoAssignColumnHeaderNames

      &pushsdbgv 21							//'_root'
      &pushsdbgm 22							//'SaveLoadMode'
      &pushsdb 23							//'Load'
      &equals
      &not
      &jnz label13      
      &pushsdbgv 24							//'ScreenHeader'
      &pushsdb 25							//'text'
      &pushsdb 26							//'$HeaderLoadSavedGame'
      &setMember
      &pushsdbgv 21							//'_root'
      &pushsdbgm 27							//'GameTypes'
      &pushsdb 28							//'CampaignSkirmishWOTRSP'
      &equals
      &not
      &jnz label9      
      &pushsdb 26							//'$HeaderLoadSavedGame'
      &pushone
      &pushsdbgv 21							//'_root'
      &pushsdbgm 29							//'Background'
      &dcallmp 30							// SetTitle()
      &gotoLabel '_loadCampaign'
      &jmp label12      
     label9:
      &pushsdbgv 21							//'_root'
      &pushsdbgm 27							//'GameTypes'
      &pushsdb 11							//'Replay'
      &equals
      &not
      &jnz label10      
      &pushsdb 31							//'$HeaderLoadSavedReplay'
      &pushone
      &pushsdbgv 21							//'_root'
      &pushsdbgm 29							//'Background'
      &dcallmp 30							// SetTitle()
      &gotoLabel '_loadReplayGame'
      &jmp label12      
     label10:
      &pushsdbgv 21							//'_root'
      &pushsdbgm 27							//'GameTypes'
      &pushsdb 14							//'Campaign'
      &equals
      &not
      &jnz label11      
      &pushsdb 26							//'$HeaderLoadSavedGame'
      &pushone
      &pushsdbgv 21							//'_root'
      &pushsdbgm 29							//'Background'
      &dcallmp 30							// SetTitle()
      &gotoLabel '_loadGameCampaign'
      &jmp label12      
     label11:
      &pushsdb 26							//'$HeaderLoadSavedGame'
      &pushone
      &pushsdbgv 21							//'_root'
      &pushsdbgm 29							//'Background'
      &dcallmp 30							// SetTitle()
      &gotoLabel '_loadGame'
     label12:
      &jmp label16      
     label13:
      &pushsdbgv 21							//'_root'
      &pushsdbgm 22							//'SaveLoadMode'
      &pushsdb 32							//'Save'
      &equals
      &not
      &jnz label16      
      &pushsdbgv 21							//'_root'
      &pushsdbgm 27							//'GameTypes'
      &pushsdb 11							//'Replay'
      &equals
      &not
      &jnz label14      
      &pushsdb 33							//'$HeaderSaveReplay'
      &pushone
      &pushsdbgv 21							//'_root'
      &pushsdbgm 29							//'Background'
      &dcallmp 30							// SetTitle()
      &jmp label15      
     label14:
      &pushsdb 34							//'$HeaderSaveGame'
      &pushone
      &pushsdbgv 21							//'_root'
      &pushsdbgm 29							//'Background'
      &dcallmp 30							// SetTitle()
     label15:
      &gotoLabel '_saveGame'
     label16:
    &end // of frame 0

    &frame 9
      &pushzero
      &pushs 'DoAssignColumnHeaderNames'
      &callfp
    &end // of frame 9

    &placeMovieClip 16 &as '4~GameList'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'ListBox'
        &pushs '_Init'
        &pushssv 'AptSaveLoad::InitGadgets'
        &pushs '_Load'
        &pushssv 'Apt/ListBox.wnd'
      &end
    &end // of placeMovieClip 16

    &placeMovieClip 17 &as '4~FileNameTextEntry'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'TextEntry'
        &pushs '_Init'
        &pushssv 'AptSaveLoad::InitGadgets'
        &pushs '_Load'
        &pushssv 'Apt/TextEntry.wnd'
      &end
    &end // of placeMovieClip 17

    &frame 19
      &pushzero
      &pushs 'DoAssignColumnHeaderNames'
      &callfp
    &end // of frame 19

    &placeMovieClip 16 &as '2~GameList'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'ListBox'
        &pushs '_Init'
        &pushssv 'AptSaveLoad::InitGadgets'
        &pushs '_Load'
        &pushssv 'Apt/ListBox.wnd'
      &end
    &end // of placeMovieClip 16

    &frame 30
      &pushzero
      &pushs 'DoAssignColumnHeaderNames'
      &callfp
    &end // of frame 30

    &placeMovieClip 49 &as 'AddCommentary'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'CheckBox'
        &pushs '_Load'
        &pushssv 'Apt/CheckBox.wnd'
        &pushs '_Init'
        &pushssv 'AptSaveLoad::InitGadgets'
        &pushs '_CheckBoxString'
        &pushssv ''
      &end
    &end // of placeMovieClip 49

    &placeMovieClip 16 &as '2~AutoSaveList'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'ListBox'
        &pushs '_Init'
        &pushssv 'AptSaveLoad::InitGadgets'
        &pushs '_Load'
        &pushssv 'Apt/ListBox.wnd'
      &end
    &end // of placeMovieClip 16

    &frame 42
      &pushzero
      &pushs 'DoAssignColumnHeaderNames'
      &callfp
    &end // of frame 42

    &frame 57
      &constants 'Campaign', '_campaign', 'Tabs', 'gotoAndPlay', '_skirmish', '_root', 'SetCurrentGameType', 'DoAssignColumnHeaderNames'  
      &function2 ToggleTabs (r:1='newTab') ()
        &push r:1        
        &pushsdb 0							//'Campaign'
        &equals
        &not
        &jnz label1        
        &gotoLabel '_loadCampaign'
        &pushsdb 1							//'_campaign'
        &pushone
        &pushsdbgv 2							//'Tabs'
        &dcallmp 3							// gotoAndPlay()
        &jmp label2        
       label1:
        &gotoLabel '_loadSkirmish'
        &pushsdb 4							//'_skirmish'
        &pushone
        &pushsdbgv 2							//'Tabs'
        &dcallmp 3							// gotoAndPlay()
       label2:
      &end // of function ToggleTabs

      &pushsdb 0							//'Campaign'
      &pushone
      &pushsdbgv 5							//'_root'
      &dcallmp 6							// SetCurrentGameType()
      &pushzero
      &dcallfp 7							// DoAssignColumnHeaderNames()
    &end // of frame 57

    &placeMovieClip 16 &as '3~GameList'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'ListBox'
        &pushs '_Init'
        &pushssv 'AptSaveLoad::InitGadgets'
        &pushs '_Load'
        &pushssv 'Apt/ListBox.wnd'
      &end
    &end // of placeMovieClip 16

    &placeMovieClip 16 &as '3~AutoSaveList'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'ListBox'
        &pushs '_Init'
        &pushssv 'AptSaveLoad::InitGadgets'
        &pushs '_Load'
        &pushssv 'Apt/ListBox.wnd'
      &end
    &end // of placeMovieClip 16

    &frame 67
      &constants 'Skirmish', '_root', 'SetCurrentGameType', 'DoAssignColumnHeaderNames', 'DoAssignTabButtonNames', 'TabButtons', 'Campaign', '_visible', 'WOTR'  
      &pushsdb 0							//'Skirmish'
      &pushone
      &pushsdbgv 1							//'_root'
      &dcallmp 2							// SetCurrentGameType()
      &pushzero
      &dcallfp 3							// DoAssignColumnHeaderNames()
      &pushzero
      &dcallfp 4							// DoAssignTabButtonNames()
      &pushsdbgv 5							//'TabButtons'
      &pushsdbgm 6							//'Campaign'
      &pushsdb 7							//'_visible'
      &pushbyte 100
      &setMember
      &pushsdbgv 5							//'TabButtons'
      &pushsdbgm 0							//'Skirmish'
      &pushsdb 7							//'_visible'
      &pushzero
      &setMember
      &pushsdbgv 5							//'TabButtons'
      &pushsdbgm 8							//'WOTR'
      &pushsdb 7							//'_visible'
      &pushbyte 100
      &setMember
    &end // of frame 67

    &frame 77
    &end // of frame 77
  &end // of defineMovieClip 100

  &defineMovieClip 106 // total frames: 30

    &frame 0
      &pushsgv '_root'
      &pushsgm 'SaveLoadMode'
      &pushs 'Save'
      &equals
      &not
      &jnz label1      
      &gotoLabel '_save'
      &play
      &jmp label2      
     label1:
      &gotoLabel '_load'
      &play
     label2:
    &end // of frame 0

    &frame 9
      &constants '$Cancel', 'Cancel', 'SetText', '$Save', 'Save', '$Delete', 'Delete', '', 'SetMode', 'ReleaseCallback', '_close', 'gotoAndPlay', 'callWhenDone', 'GameCode'  
      &pushsdb 0							//'$Cancel'
      &pushone
      &pushsdbgv 1							//'Cancel'
      &dcallmp 2							// SetText()
      &pushsdb 3							//'$Save'
      &pushone
      &pushsdbgv 4							//'Save'
      &dcallmp 2							// SetText()
      &pushsdb 5							//'$Delete'
      &pushone
      &pushsdbgv 6							//'Delete'
      &dcallmp 2							// SetText()
      &pushsdb 7							//''
      &pushone
      &pushsdbgv 1							//'Cancel'
      &dcallmp 8							// SetMode()
      &pushsdb 7							//''
      &pushone
      &pushsdbgv 4							//'Save'
      &dcallmp 8							// SetMode()
      &pushsdb 7							//''
      &pushone
      &pushsdbgv 6							//'Delete'
      &dcallmp 8							// SetMode()
      &pushsdbgv 1							//'Cancel'
      &pushsdb 9							//'ReleaseCallback'
      &function2  () (r:1='_root')
        &pushsdb 10							//'_close'
        &pushone
        &push r:1        
        &dcallmp 11							// gotoAndPlay()
        &push r:1        
        &pushsdb 12							//'callWhenDone'
        &pushsdb 1							//'Cancel'
        &setMember
      &end // of function 

      &setMember
      &pushsdbgv 4							//'Save'
      &pushsdb 9							//'ReleaseCallback'
      &function2  () (r:1='_root')
        &pushsdb 4							//'Save'
        &pushone
        &push r:1        
        &dcallmp 13							// GameCode()
      &end // of function 

      &setMember
      &pushsdbgv 6							//'Delete'
      &pushsdb 9							//'ReleaseCallback'
      &function2  () (r:1='_root')
        &pushsdb 6							//'Delete'
        &pushone
        &push r:1        
        &dcallmp 13							// GameCode()
      &end // of function 

      &setMember
      &stop
    &end // of frame 9

    &placeMovieClip 14 &as 'Cancel'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv ''
      &end
    &end // of placeMovieClip 14

    &placeMovieClip 14 &as 'Save'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv ''
      &end
    &end // of placeMovieClip 14

    &placeMovieClip 14 &as 'Delete'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv ''
      &end
    &end // of placeMovieClip 14

    &frame 19
      &constants '$Cancel', 'Cancel', 'SetText', '$Load', 'Load', '$Delete', 'Delete', '', 'SetMode', 'ReleaseCallback', '_close', 'gotoAndPlay', 'callWhenDone', 'GameCode'  
      &pushsdb 0							//'$Cancel'
      &pushone
      &pushsdbgv 1							//'Cancel'
      &dcallmp 2							// SetText()
      &pushsdb 3							//'$Load'
      &pushone
      &pushsdbgv 4							//'Load'
      &dcallmp 2							// SetText()
      &pushsdb 5							//'$Delete'
      &pushone
      &pushsdbgv 6							//'Delete'
      &dcallmp 2							// SetText()
      &pushsdb 7							//''
      &pushone
      &pushsdbgv 1							//'Cancel'
      &dcallmp 8							// SetMode()
      &pushsdb 7							//''
      &pushone
      &pushsdbgv 4							//'Load'
      &dcallmp 8							// SetMode()
      &pushsdb 7							//''
      &pushone
      &pushsdbgv 6							//'Delete'
      &dcallmp 8							// SetMode()
      &pushsdbgv 1							//'Cancel'
      &pushsdb 9							//'ReleaseCallback'
      &function2  () (r:1='_root')
        &pushsdb 10							//'_close'
        &pushone
        &push r:1        
        &dcallmp 11							// gotoAndPlay()
        &push r:1        
        &pushsdb 12							//'callWhenDone'
        &pushsdb 1							//'Cancel'
        &setMember
      &end // of function 

      &setMember
      &pushsdbgv 4							//'Load'
      &pushsdb 9							//'ReleaseCallback'
      &function2  () (r:1='_root')
        &pushsdb 4							//'Load'
        &pushone
        &push r:1        
        &dcallmp 13							// GameCode()
      &end // of function 

      &setMember
      &pushsdbgv 6							//'Delete'
      &pushsdb 9							//'ReleaseCallback'
      &function2  () (r:1='_root')
        &pushsdb 6							//'Delete'
        &pushone
        &push r:1        
        &dcallmp 13							// GameCode()
      &end // of function 

      &setMember
      &stop
    &end // of frame 19

    &placeMovieClip 14 &as 'Cancel'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv ''
      &end
    &end // of placeMovieClip 14

    &placeMovieClip 14 &as 'Delete'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv 'Disabled'
      &end
    &end // of placeMovieClip 14

    &placeMovieClip 14 &as 'Load'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv 'Disabled'
      &end
    &end // of placeMovieClip 14
  &end // of defineMovieClip 106

  &frame 18
    &stop
  &end // of frame 18

  &frame 19
    &constants '_root', 'callWhenDone', 'GameCode'  
    &pushsdbgv 0							//'_root'
    &pushsdbgm 1							//'callWhenDone'
    &pushundef
    &equals
    &not
    &not
    &jnz label1    
    &pushsdbgv 0							//'_root'
    &pushsdbgm 1							//'callWhenDone'
    &pushone
    &pushsdbgv 0							//'_root'
    &dcallmp 2							// GameCode()
   label1:
    &stop
  &end // of frame 19
&end
