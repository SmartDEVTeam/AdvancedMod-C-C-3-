movie 'E:\Projects\CNC3\Data\APTBUI~1\034A3~1.0-D\pc\Output\Options\\Options.eaf' &compressed // flash 7, total frames: 15, frame rate: 30 fps, 1024x768 px

  &defineMovieClip 3 // total frames: 1
  &end // of defineMovieClip 3

  &defineMovieClip 4 // total frames: 1
  &end // of defineMovieClip 4

  &defineMovieClip 7 // total frames: 1
  &end // of defineMovieClip 7

  &defineMovieClip 10 // total frames: 1
  &end // of defineMovieClip 10
  
  &importAssets &from 'ShellButtons.swf'
    'ScanLine' &as 12
  &end // of importAssets

  &defineMovieClip 15 // total frames: 1
  &end // of defineMovieClip 15

  &defineMovieClip 16 // total frames: 40
  &end // of defineMovieClip 16

  &defineMovieClip 19 // total frames: 1
  &end // of defineMovieClip 19

  &defineMovieClip 20 // total frames: 10

    &frame 0
      &constants 'm_text'  
      &function2 Show () (r:1='_parent')
        &pushsdb 0							//'m_text'
        &push r:1        
        &pushsdbgm 0							//'m_text'
        &setVariable
        &gotoFrame 0
        &play
      &end // of function Show

    &end // of frame 0

    &frame 9
      &pushthisgv
      &pushone
      &pushsgv '_parent'
      &pushs 'EndTransition'
      &callmp
      &stop
    &end // of frame 9
  &end // of defineMovieClip 20

  &defineMovieClip 23 // total frames: 1

    &frame 0
      &constants 'GetMode', 'Disabled', 'Hidden', 'IsHidden', 'ClearMode', 'SetMode', 'IsDisabled', 'TabSelected', 'DisabledBttn', 'HiddenBttn', 'HiddenUpState', 'HiddenText', 'TabSelectedBttn', 'ReleaseTransText', 'vStartMode'  
      &function IsDisabled ('Void'      )      
        &pushzero
        &pushsdb 0							//'GetMode'
        &callFunction
        &pushsdb 1							//'Disabled'
        &equals
        &return
      &end // of function IsDisabled

      &function IsHidden ('Void'      )      
        &pushzero
        &pushsdb 0							//'GetMode'
        &callFunction
        &pushsdb 2							//'Hidden'
        &equals
        &return
      &end // of function IsHidden

      &function Show ('Void'      )      
        &pushzero
        &pushsdb 3							//'IsHidden'
        &callFunction
        &not
        &jnz label1        
        &pushzero
        &dcallfp 4							// ClearMode()
       label1:
      &end // of function Show

      &function Hide ('Void'      )      
        &pushsdb 2							//'Hidden'
        &pushone
        &dcallfp 5							// SetMode()
      &end // of function Hide

      &function Enable ('Void'      )      
        &pushzero
        &pushsdb 6							//'IsDisabled'
        &callFunction
        &not
        &jnz label2        
        &pushzero
        &dcallfp 4							// ClearMode()
       label2:
      &end // of function Enable

      &function Disable ('Void'      )      
        &pushsdb 1							//'Disabled'
        &pushone
        &dcallfp 5							// SetMode()
      &end // of function Disable

      &function TabSelected ('Void'      )      
        &pushsdb 7							//'TabSelected'
        &pushone
        &dcallfp 5							// SetMode()
      &end // of function TabSelected

      &pushsdb 8							//'DisabledBttn'
      &pushfalse
      &setVariable
      &pushsdb 9							//'HiddenBttn'
      &pushfalse
      &setVariable
      &pushsdb 10							//'HiddenUpState'
      &pushfalse
      &setVariable
      &pushsdb 11							//'HiddenText'
      &pushfalse
      &setVariable
      &pushsdb 12							//'TabSelectedBttn'
      &pushfalse
      &setVariable
      &pushsdb 13							//'ReleaseTransText'
      &pushfalse
      &setVariable
      &pushsdbgv 14							//'vStartMode'
      &pushone
      &dcallfp 5							// SetMode()
    &end // of frame 0
  &end // of defineMovieClip 23
  
  &exportAssets
    23 &as 'ShellButtonShort1'
  &end // of exportAssets

  &defineMovieClip 29 // total frames: 1

    &frame 0
      &pushthisgv
      &pushs '_alpha'
      &pushzero
      &setMember
    &end // of frame 0
  &end // of defineMovieClip 29

  &defineMovieClip 33 // total frames: 2

    &frame 1
      &gotoFrame 0
      &play
    &end // of frame 1
  &end // of defineMovieClip 33
  
  &exportAssets
    33 &as 'GraphicsSliderContent2'
  &end // of exportAssets

  &defineMovieClip 39 // total frames: 2

    &frame 1
      &gotoFrame 0
      &play
    &end // of frame 1
  &end // of defineMovieClip 39
  
  &exportAssets
    39 &as 'GraphicsSliderContent1'
  &end // of exportAssets

  &defineMovieClip 42 // total frames: 1
  &end // of defineMovieClip 42

  &defineButton 44
  
    &on     &idleToOverUp
      &gotoLabel '_over'
      &play
      &pushs 'Gui_ShellMapMouseOver'
      &pushone
      &pushsgv '_root'
      &pushs 'PlaySound'
      &callmp
    &end
  
    &on     &overUpToIdle    ,&overDownToOutDown    ,&overDownToIdle
      &gotoLabel '_rollOut'
      &play
      &pushs 'Gui_ShellMapMouseOut'
      &pushone
      &pushsgv '_root'
      &pushs 'PlaySound'
      &callmp
    &end
  
    &on     &overUpToOverDown
      &gotoLabel '_press'
      &play
    &end
  
    &on     &overDownToOverUp
      &constants 'this', '_parent', 'Release', 'Gui_ShellMapSelect', '_root', 'PlaySound'  
      &pushfalse
      &pushthisgv
      &pushbyte 2
      &pushsdbgv 1							//'_parent'
      &pushsdbgm 1							//'_parent'
      &dcallmp 2							// Release()
      &pushsdb 3							//'Gui_ShellMapSelect'
      &pushone
      &pushsdbgv 4							//'_root'
      &dcallmp 5							// PlaySound()
    &end
  &end // of defineButton 44

  &defineMovieClip 47 // total frames: 1
  &end // of defineMovieClip 47

  &defineMovieClip 50 // total frames: 1
  &end // of defineMovieClip 50

  &defineMovieClip 53 // total frames: 1
  &end // of defineMovieClip 53

  &defineMovieClip 54 // total frames: 80

    &frame 0
      &constants '_parent', 'MyButtons', 'MyButtonClip', '', 'split', 'this'  
      &pushsdbgv 0							//'_parent'
      &pushsdbgm 0							//'_parent'
      &pushsdbgm 1							//'MyButtons'
      &pushsdbgv 0							//'_parent'
      &pushsdbgm 0							//'_parent'
      &pushsdbgm 2							//'MyButtonClip'
      &pushone
      &pushsdb 3							//''
      &pushbyte 13
      &getProperty
      &pushsdb 4							//'split'
      &callMethod
      &pushone
      &getMember
      &pushthisgv
      &setMember
      &gotoLabel '_up'
      &play
    &end // of frame 0

    &frame 18
      &stop
    &end // of frame 18

    &frame 28
      &stop
    &end // of frame 28

    &frame 38
      &gotoLabel '_up'
      &play
    &end // of frame 38

    &frame 48
      &stop
    &end // of frame 48

    &frame 49
      &constants 'SettingDefaults', 'this', '_name', '_parent', 'DefaultDoButtonCallBack'  
      &pushsdbgv 0							//'SettingDefaults'
      &pushthisgv
      &pushsdbgm 2							//'_name'
      &pushthisgv
      &pushbyte 3
      &pushsdbgv 3							//'_parent'
      &pushsdbgm 3							//'_parent'
      &dcallmp 4							// DefaultDoButtonCallBack()
    &end // of frame 49

    &frame 58
      &stop
    &end // of frame 58

    &frame 68
      &gotoLabel '_up'
      &play
    &end // of frame 68
  &end // of defineMovieClip 54
  
  &exportAssets
    54 &as 'GraphicsSliderButton2'
  &end // of exportAssets

  &defineMovieClip 57 // total frames: 1
  &end // of defineMovieClip 57

  &defineButton 58
  
    &on     &idleToOverUp
      &gotoLabel '_over'
      &play
      &pushs 'Gui_ShellMapMouseOver'
      &pushone
      &pushsgv '_root'
      &pushs 'PlaySound'
      &callmp
    &end
  
    &on     &overUpToIdle    ,&overDownToOutDown    ,&overDownToIdle
      &gotoLabel '_rollOut'
      &play
      &pushs 'Gui_ShellMapMouseOut'
      &pushone
      &pushsgv '_root'
      &pushs 'PlaySound'
      &callmp
    &end
  
    &on     &overUpToOverDown
      &gotoLabel '_press'
      &play
    &end
  
    &on     &overDownToOverUp
      &constants 'this', '_parent', 'Release', 'Gui_ShellMapSelect', '_root', 'PlaySound'  
      &pushfalse
      &pushthisgv
      &pushbyte 2
      &pushsdbgv 1							//'_parent'
      &pushsdbgm 1							//'_parent'
      &dcallmp 2							// Release()
      &pushsdb 3							//'Gui_ShellMapSelect'
      &pushone
      &pushsdbgv 4							//'_root'
      &dcallmp 5							// PlaySound()
    &end
  &end // of defineButton 58

  &defineMovieClip 61 // total frames: 1
  &end // of defineMovieClip 61

  &defineMovieClip 64 // total frames: 1
  &end // of defineMovieClip 64

  &defineMovieClip 67 // total frames: 1
  &end // of defineMovieClip 67

  &defineMovieClip 68 // total frames: 80

    &frame 0
      &constants '_parent', 'MyButtons', 'MyButtonClip', '', 'split', 'this'  
      &pushsdbgv 0							//'_parent'
      &pushsdbgm 0							//'_parent'
      &pushsdbgm 1							//'MyButtons'
      &pushsdbgv 0							//'_parent'
      &pushsdbgm 0							//'_parent'
      &pushsdbgm 2							//'MyButtonClip'
      &pushone
      &pushsdb 3							//''
      &pushbyte 13
      &getProperty
      &pushsdb 4							//'split'
      &callMethod
      &pushone
      &getMember
      &pushthisgv
      &setMember
      &gotoLabel '_up'
      &play
    &end // of frame 0

    &frame 18
      &stop
    &end // of frame 18

    &frame 28
      &stop
    &end // of frame 28

    &frame 38
      &gotoLabel '_up'
      &play
    &end // of frame 38

    &frame 48
      &stop
    &end // of frame 48

    &frame 49
      &constants 'SettingDefaults', 'this', '_name', '_parent', 'DefaultDoButtonCallBack'  
      &pushsdbgv 0							//'SettingDefaults'
      &pushthisgv
      &pushsdbgm 2							//'_name'
      &pushthisgv
      &pushbyte 3
      &pushsdbgv 3							//'_parent'
      &pushsdbgm 3							//'_parent'
      &dcallmp 4							// DefaultDoButtonCallBack()
    &end // of frame 49

    &frame 58
      &stop
    &end // of frame 58

    &frame 68
      &gotoLabel '_up'
      &play
    &end // of frame 68
  &end // of defineMovieClip 68
  
  &exportAssets
    68 &as 'GraphicsSliderButton1'
  &end // of exportAssets
  
  &importAssets &from 'GameWindowGadgets.swf'
    'CheckBox' &as 72
  &end // of importAssets

  &defineMovieClip 73 // total frames: 20

    &frame 0
      &constants '================WHY ARE WE NOT CHECKING:', '_root', 'Options', 'IsSpecialEdition'  
      &pushsdb 0							//'================WHY ARE WE NOT CHECKING:'
      &pushzero
      &pushsdbgv 1							//'_root'
      &pushsdbgm 2							//'Options'
      &pushsdb 3							//'IsSpecialEdition'
      &callMethod
      &add
      &trace
      &pushzero
      &pushsdbgv 1							//'_root'
      &pushsdbgm 2							//'Options'
      &pushsdb 3							//'IsSpecialEdition'
      &callMethod
      &not
      &not
      &jnz label1      
      &gotoLabel '_hide'
      &play
     label1:
    &end // of frame 0

    &placeMovieClip 72 &as 'Options::EnableSpecialEditionContent'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'CheckBox'
        &pushs '_Load'
        &pushssv 'Apt/CheckBox.wnd'
        &pushs '_Init'
        &pushssv 'AptOptions::InitGadgets'
        &pushs '_CheckBoxString'
        &pushssv ''
      &end
    &end // of placeMovieClip 72

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19
  &end // of defineMovieClip 73

  &defineMovieClip 75 // total frames: 1

    &placeMovieClip 72 &as 'Options::AlternateMouseSetup'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'CheckBox'
        &pushs '_Load'
        &pushssv 'Apt/CheckBox.wnd'
        &pushs '_Init'
        &pushssv 'AptOptions::InitGadgets'
        &pushs '_CheckBoxString'
        &pushssv ''
      &end
    &end // of placeMovieClip 72
  &end // of defineMovieClip 75

  &defineMovieClip 80 // total frames: 1
  &end // of defineMovieClip 80
  
  &importAssets &from 'GameWindowGadgets.swf'
    'HorzSlider' &as 81
  &end // of importAssets

  &defineMovieClip 84 // total frames: 1
  &end // of defineMovieClip 84

  &defineMovieClip 87 // total frames: 1
  &end // of defineMovieClip 87

  &defineMovieClip 92 // total frames: 1

    &frame 0
      &pushzero
      &pushsgv '_root'
      &pushsgm 'Options'
      &pushs 'IsInDemo'
      &callMethod
      &not
      &jnz label1      
      &pushs ''
      &pushbyte 7
      &pushfalse
      &setProperty
     label1:
    &end // of frame 0

    &placeMovieClip 72 &as 'Options::ShowTickerNews'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'CheckBox'
        &pushs '_Load'
        &pushssv 'Apt/CheckBox.wnd'
        &pushs '_Init'
        &pushssv 'AptOptions::InitGadgets'
        &pushs '_CheckBoxString'
        &pushssv ''
      &end
    &end // of placeMovieClip 72

    &placeMovieClip 72 &as 'Options::ShowTickerAds'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'CheckBox'
        &pushs '_Load'
        &pushssv 'Apt/CheckBox.wnd'
        &pushs '_Init'
        &pushssv 'AptOptions::InitGadgets'
        &pushs '_CheckBoxString'
        &pushssv ''
      &end
    &end // of placeMovieClip 72
  &end // of defineMovieClip 92

  &defineMovieClip 93 // total frames: 1

    &frame 0
      &constants 'this', 'Game', '_root', 'Options', 'RegisterTabChange', 'MouseSensitivityFrame', 'm_label', '$MouseSensitivity', 'ToolTipDelayFrame', '$ToolTipDelay'  
      &pushthisgv
      &pushsdb 1							//'Game'
      &pushbyte 2
      &pushsdbgv 2							//'_root'
      &pushsdbgm 3							//'Options'
      &dcallmp 4							// RegisterTabChange()
      &pushsdbgv 5							//'MouseSensitivityFrame'
      &pushsdb 6							//'m_label'
      &pushsdb 7							//'$MouseSensitivity'
      &setMember
      &pushsdbgv 8							//'ToolTipDelayFrame'
      &pushsdb 6							//'m_label'
      &pushsdb 9							//'$ToolTipDelay'
      &setMember
    &end // of frame 0

    &placeMovieClip 81 &as 'Options::MouseSensitivity'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'HorzSlider'
        &pushs '_Init'
        &pushssv 'AptOptions::InitGadgets'
        &pushs '_Load'
        &pushssv 'Apt/HorzSlider.wnd'
      &end
    &end // of placeMovieClip 81

    &placeMovieClip 81 &as 'Options::ToolTipDelay'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'HorzSlider'
        &pushs '_Init'
        &pushssv 'AptOptions::InitGadgets'
        &pushs '_Load'
        &pushssv 'Apt/HorzSlider.wnd'
      &end
    &end // of placeMovieClip 81
  &end // of defineMovieClip 93

  &defineMovieClip 96 // total frames: 1

    &frame 0
      &pushs ''
      &pushbyte 7
      &pushfalse
      &setProperty
    &end // of frame 0
  &end // of defineMovieClip 96

  &defineMovieClip 97 // total frames: 1
  &end // of defineMovieClip 97
  
  &importAssets &from 'ShellButtons.swf'
    'ShellButtons Small' &as 98
  &end // of importAssets

  &defineMovieClip 101 // total frames: 1
  &end // of defineMovieClip 101

  &defineMovieClip 102 // total frames: 1
  &end // of defineMovieClip 102

  &defineMovieClip 105 // total frames: 1
  &end // of defineMovieClip 105

  &defineMovieClip 108 // total frames: 1
  &end // of defineMovieClip 108

  &defineMovieClip 111 // total frames: 1

    &frame 0
      &constants 'Done', 'ReleaseCallback', 'Options', 'OnDonePress', 'Cancel', 'OnCancelPress', 'Defaults', 'SetDefaultTabSettings'  
      &pushsdbgv 0							//'Done'
      &pushsdb 1							//'ReleaseCallback'
      &function2  () (r:1='_root')
        &pushzero
        &push r:1        
        &pushsdbgm 2							//'Options'
        &dcallmp 3							// OnDonePress()
      &end // of function 

      &setMember
      &pushsdbgv 4							//'Cancel'
      &pushsdb 1							//'ReleaseCallback'
      &function2  () (r:1='_root')
        &pushzero
        &push r:1        
        &pushsdbgm 2							//'Options'
        &dcallmp 5							// OnCancelPress()
      &end // of function 

      &setMember
      &pushsdbgv 6							//'Defaults'
      &pushsdb 1							//'ReleaseCallback'
      &function2  () (r:1='_root')
        &pushzero
        &push r:1        
        &pushsdbgm 2							//'Options'
        &dcallmp 7							// SetDefaultTabSettings()
      &end // of function 

      &setMember
    &end // of frame 0

    &placeMovieClip 98 &as 'Defaults'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv ''
      &end
    &end // of placeMovieClip 98

    &placeMovieClip 98 &as 'Cancel'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv ''
      &end
    &end // of placeMovieClip 98

    &placeMovieClip 98 &as 'Done'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv ''
      &end
    &end // of placeMovieClip 98
  &end // of defineMovieClip 111

  &defineMovieClip 112 // total frames: 2

    &frame 0
      &constants 'vCurSelected', 'ClearMode', 'TabSelected', '_name', 'Controls', 'Options', 'SetCustomHotkeysVisibility', 'SetDisableStates >> ', 'm_entryPoint', 'IsInDemo', 'IsSpectatorClient', 'Network', 'Disable', 'Graphics', '$GeneralTab', 'Game', 'SetText', '$HotkeysTab', '$GraphicsTab', '$AudioTab', 'Audio', '$NetworkTab', 'ReleaseCallback', 'SwitchTab', '_game', 'gotoAndPlay', '_controls', '_graphics', '_audio', '_network'  
      &function2 SwitchTab (r:2='to') (r:1='_root')
        &push r:2        
        &pushsdbgv 0							//'vCurSelected'
        &equals
        &not
        &not
        &jnz label2        
        &pushzero
        &pushsdbgv 0							//'vCurSelected'
        &dcallmp 1							// ClearMode()
        &pushsdb 0							//'vCurSelected'
        &push r:2        
        &setVariable
        &pushzero
        &pushsdbgv 0							//'vCurSelected'
        &dcallmp 2							// TabSelected()
        &pushsdbgv 0							//'vCurSelected'
        &pushsdbgm 3							//'_name'
        &pushsdb 4							//'Controls'
        &equals
        &not
        &jnz label1        
        &pushtrue
        &pushone
        &push r:1        
        &pushsdbgm 5							//'Options'
        &dcallmp 6							// SetCustomHotkeysVisibility()
        &jmp label2        
       label1:
        &pushfalse
        &pushone
        &push r:1        
        &pushsdbgm 5							//'Options'
        &dcallmp 6							// SetCustomHotkeysVisibility()
       label2:
      &end // of function SwitchTab

      &function2 SetDisableStates () (r:1='_root')
        &pushsdb 7							//'SetDisableStates >> '
        &push r:1        
        &pushsdbgm 5							//'Options'
        &pushsdbgm 8							//'m_entryPoint'
        &add
        &trace
        &pushzero
        &push r:1        
        &pushsdbgm 5							//'Options'
        &pushsdb 9							//'IsInDemo'
        &callMethod
        &dup
        &jnz label3        
        &pop
        &pushzero
        &push r:1        
        &pushsdbgm 5							//'Options'
        &pushsdb 10							//'IsSpectatorClient'
        &callMethod
       label3:
        &not
        &jnz label4        
        &pushzero
        &pushsdbgv 11							//'Network'
        &dcallmp 12							// Disable()
       label4:
      &end // of function SetDisableStates

      &pushsdb 0							//'vCurSelected'
      &pushsdbgv 13							//'Graphics'
      &varEquals
      &pushsdb 14							//'$GeneralTab'
      &pushone
      &pushsdbgv 15							//'Game'
      &dcallmp 16							// SetText()
      &pushsdb 17							//'$HotkeysTab'
      &pushone
      &pushsdbgv 4							//'Controls'
      &dcallmp 16							// SetText()
      &pushsdb 18							//'$GraphicsTab'
      &pushone
      &pushsdbgv 13							//'Graphics'
      &dcallmp 16							// SetText()
      &pushsdb 19							//'$AudioTab'
      &pushone
      &pushsdbgv 20							//'Audio'
      &dcallmp 16							// SetText()
      &pushsdb 21							//'$NetworkTab'
      &pushone
      &pushsdbgv 11							//'Network'
      &dcallmp 16							// SetText()
      &pushsdbgv 15							//'Game'
      &pushsdb 22							//'ReleaseCallback'
      &function2  () (r:1='this', r:2='_parent')
        &push r:1        
        &pushone
        &dcallfp 23							// SwitchTab()
        &pushsdb 24							//'_game'
        &pushone
        &push r:2        
        &dcallmp 25							// gotoAndPlay()
      &end // of function 

      &setMember
      &pushsdbgv 4							//'Controls'
      &pushsdb 22							//'ReleaseCallback'
      &function2  () (r:1='this', r:2='_parent')
        &push r:1        
        &pushone
        &dcallfp 23							// SwitchTab()
        &pushsdb 26							//'_controls'
        &pushone
        &push r:2        
        &dcallmp 25							// gotoAndPlay()
      &end // of function 

      &setMember
      &pushsdbgv 13							//'Graphics'
      &pushsdb 22							//'ReleaseCallback'
      &function2  () (r:1='this', r:2='_parent')
        &push r:1        
        &pushone
        &dcallfp 23							// SwitchTab()
        &pushsdb 27							//'_graphics'
        &pushone
        &push r:2        
        &dcallmp 25							// gotoAndPlay()
      &end // of function 

      &setMember
      &pushsdbgv 20							//'Audio'
      &pushsdb 22							//'ReleaseCallback'
      &function2  () (r:1='this', r:2='_parent')
        &push r:1        
        &pushone
        &dcallfp 23							// SwitchTab()
        &pushsdb 28							//'_audio'
        &pushone
        &push r:2        
        &dcallmp 25							// gotoAndPlay()
      &end // of function 

      &setMember
      &pushsdbgv 11							//'Network'
      &pushsdb 22							//'ReleaseCallback'
      &function2  () (r:1='this', r:2='_parent')
        &push r:1        
        &pushone
        &dcallfp 23							// SwitchTab()
        &pushsdb 29							//'_network'
        &pushone
        &push r:2        
        &dcallmp 25							// gotoAndPlay()
      &end // of function 

      &setMember
    &end // of frame 0

    &placeMovieClip 98 &as 'Graphics'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv 'TabSelected'
      &end
    &end // of placeMovieClip 98

    &placeMovieClip 98 &as 'Audio'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv ''
      &end
    &end // of placeMovieClip 98

    &placeMovieClip 98 &as 'Controls'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv ''
      &end
    &end // of placeMovieClip 98

    &placeMovieClip 98 &as 'Network'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv ''
      &end
    &end // of placeMovieClip 98

    &placeMovieClip 98 &as 'Game'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv ''
      &end
    &end // of placeMovieClip 98

    &frame 1
      &pushzero
      &pushs 'SetDisableStates'
      &callfp
      &stop
    &end // of frame 1
  &end // of defineMovieClip 112

  &defineMovieClip 119 // total frames: 1

    &frame 0
      &pushthisgv
      &pushs '_visible'
      &pushzero
      &setMember
    &end // of frame 0
  &end // of defineMovieClip 119

  &defineMovieClip 120 // total frames: 20

    &frame 0
      &constants 'MyChildren', 'MyOption', 'Template', 'Current', 'vRootApt', 'GetExtern', 'SetDefault', 'ChildNumber', 'ParentName', 'RollCall', 'SetDefaultOptions', 'MyContentClip', 'CurrentOptionText', '$', '_', 'MyButtonClip', 'Release', 'i', 'length', ',', 'split', 'LastTemplate', 'Custom', '_custom', 'gotoAndPlay', 'SetExtern', 'CurrentTemplate', 'toString', 'TemplateCustom', '_deselect', 'SelectedButton', 'Setting MyContentClip: ', ' OptionName: ', 'OptionNameText', ' CurrentOptionText = $', '_Custom', 'SetToHigh', 'MyButtons', 'Warning', 'PlayWarning', 'SelectedSetting', 'GoToSetting', 'ShadowSlider', 'Invoking Shadow -> Terrain/Shaders rule', 'TerrainSlider', 'RaiseToSetting', 'ShaderSlider', 'Invoking Terrain -> Shadow rule', 'LowerToSetting', 'Invoking Shader -> Shadow rule', '', 'SetCustom', 'SettingDefaults', '_select', '_root', 'Options', 'm_apt', 'Content:', 'this', 'attachMovie', 'CurrentExtern', 'Num', 'ParentSlider1', 'ParentSlider', 'vContent', 'vButtonZone', 'ButtonZone', 'vButton', 'vExternNum', 'vHalfWidth', '_width', '_y', '_x', 'Array', 'RefreshAdvOptions'  
      &function2 RollCall (r:1='Num', r:2='Path') ()
        &pushsdbgv 0							//'MyChildren'
        &push r:1        
        &push r:2        
        &setMember
        &pushsdbgv 1							//'MyOption'
        &pushsdb 2							//'Template'
        &add
        &pushsdbgv 1							//'MyOption'
        &pushsdb 3							//'Current'
        &add
        &pushone
        &pushsdbgv 4							//'vRootApt'
        &pushsdb 5							//'GetExtern'
        &callMethod
        &add
        &pushone
        &pushsdbgv 4							//'vRootApt'
        &pushsdb 5							//'GetExtern'
        &callMethod
        &pushone
        &pushsdbgv 0							//'MyChildren'
        &push r:1        
        &getMember
        &dcallmp 6							// SetDefault()
      &end // of function RollCall

      &function2 StandForRoll () (r:1='this', r:2='_parent')
        &push r:1        
        &pushsdbgv 7							//'ChildNumber'
        &pushbyte 2
        &push r:2        
        &pushsdbgv 8							//'ParentName'
        &getMember
        &dcallmp 9							// RollCall()
      &end // of function StandForRoll

      &function2 SetDefaultOptions () (r:1='this')
        &pushsdb 10							//'SetDefaultOptions'
        &trace
        &pushsdbgv 1							//'MyOption'
        &pushsdb 3							//'Current'
        &add
        &pushone
        &pushsdbgv 4							//'vRootApt'
        &pushsdb 5							//'GetExtern'
        &callMethod
        &setRegister r:2
        &pop
        &push r:1        
        &pushsdbgv 11							//'MyContentClip'
        &getMember
        &pushsdb 12							//'CurrentOptionText'
        &pushsdb 13							//'$'
        &pushsdbgv 1							//'MyOption'
        &add
        &pushsdb 14							//'_'
        &add
        &push r:2        
        &add
        &setMember
        &push r:1        
        &pushsdbgv 11							//'MyContentClip'
        &getMember
        &pushsdbgv 15							//'MyButtonClip'
        &push r:2        
        &add
        &getMember
        &pushone
        &dcallfp 16							// Release()
        &pushsdb 17							//'i'
        &pushzerosv
       label1:
        &pushsdbgv 17							//'i'
        &pushsdbgv 0							//'MyChildren'
        &pushsdbgm 18							//'length'
        &lessThan
        &not
        &jnz label2        
        &pushsdbgv 1							//'MyOption'
        &pushsdb 2							//'Template'
        &add
        &pushsdbgv 1							//'MyOption'
        &pushsdb 3							//'Current'
        &add
        &pushone
        &pushsdbgv 4							//'vRootApt'
        &pushsdb 5							//'GetExtern'
        &callMethod
        &add
        &pushone
        &pushsdbgv 4							//'vRootApt'
        &pushsdb 5							//'GetExtern'
        &callMethod
        &pushone
        &pushsdbgv 0							//'MyChildren'
        &pushsdbgv 17							//'i'
        &getMember
        &dcallmp 6							// SetDefault()
        &pushsdb 17							//'i'
        &pushsdbgv 17							//'i'
        &increment
        &setVariable
        &jmp label1        
       label2:
      &end // of function SetDefaultOptions

      &function2 SetDefault (r:3='MyDefault') (r:1='this')
        &push r:1        
        &pushsdbgv 11							//'MyContentClip'
        &getMember
        &pushsdbgv 15							//'MyButtonClip'
        &pushsdb 19							//','
        &pushone
        &push r:3        
        &pushsdb 20							//'split'
        &callMethod
        &pushsdbgv 7							//'ChildNumber'
        &getMember
        &add
        &getMember
        &setRegister r:2
        &pop
        &pushtrue
        &push r:2        
        &pushbyte 2
        &dcallfp 16							// Release()
      &end // of function SetDefault

      &function2 SetCustom (r:2='Change', r:3='Value') (r:1='this')
        &pushsdb 21							//'LastTemplate'
        &pushsdbgv 1							//'MyOption'
        &pushsdb 2							//'Template'
        &add
        &pushsdbgv 1							//'MyOption'
        &pushsdb 3							//'Current'
        &add
        &pushone
        &pushsdbgv 4							//'vRootApt'
        &pushsdb 5							//'GetExtern'
        &callMethod
        &add
        &pushone
        &pushsdbgv 4							//'vRootApt'
        &dcallmsv 5							// GetExtern()
        &pushsdbgv 1							//'MyOption'
        &pushsdb 3							//'Current'
        &add
        &pushone
        &pushsdbgv 4							//'vRootApt'
        &pushsdb 5							//'GetExtern'
        &callMethod
        &pushsdb 22							//'Custom'
        &equals
        &not
        &not
        &jnz label3        
        &pushsdb 23							//'_custom'
        &pushone
        &push r:1        
        &pushsdbgv 11							//'MyContentClip'
        &getMember
        &dcallmp 24							// gotoAndPlay()
        &pushsdb 22							//'Custom'
        &pushsdbgv 1							//'MyOption'
        &pushsdb 3							//'Current'
        &add
        &pushbyte 2
        &pushsdbgv 4							//'vRootApt'
        &dcallmp 25							// SetExtern()
       label3:
        &pushsdb 26							//'CurrentTemplate'
        &pushsdb 19							//','
        &pushone
        &pushsdbgv 21							//'LastTemplate'
        &dcallmsv 20							// split()
        &pushsdbgv 26							//'CurrentTemplate'
        &push r:2        
        &push r:3        
        &setMember
        &pushzero
        &pushsdbgv 26							//'CurrentTemplate'
        &pushsdb 27							//'toString'
        &callMethod
        &pushsdbgv 1							//'MyOption'
        &pushsdb 28							//'TemplateCustom'
        &add
        &pushbyte 2
        &pushsdbgv 4							//'vRootApt'
        &dcallmp 25							// SetExtern()
        &pushsdb 29							//'_deselect'
        &pushone
        &pushsdbgv 30							//'SelectedButton'
        &dcallmp 24							// gotoAndPlay()
        &pushsdb 31							//'Setting MyContentClip: '
        &pushsdbgv 11							//'MyContentClip'
        &add
        &pushsdb 32							//' OptionName: '
        &add
        &push r:1        
        &pushsdbgv 11							//'MyContentClip'
        &getMember
        &pushsdbgm 33							//'OptionNameText'
        &add
        &pushsdb 34							//' CurrentOptionText = $'
        &add
        &pushsdbgv 1							//'MyOption'
        &add
        &pushsdb 35							//'_Custom'
        &add
        &trace
        &push r:1        
        &pushsdbgv 11							//'MyContentClip'
        &getMember
        &pushsdb 12							//'CurrentOptionText'
        &pushsdb 13							//'$'
        &pushsdbgv 1							//'MyOption'
        &add
        &pushsdb 35							//'_Custom'
        &add
        &setMember
        &pushsdb 30							//'SelectedButton'
        &pushnull
        &setVariable
      &end // of function SetCustom

      &function2 GoToMedium () (r:1='_parent')
        &pushsdbgv 36							//'SetToHigh'
        &not
        &jnz label4        
        &pushfalse
        &pushsdbgv 37							//'MyButtons'
        &pushone
        &getMember
        &pushbyte 2
        &dcallfp 16							// Release()
        &pushsdb 36							//'SetToHigh'
        &pushfalse
        &setVariable
        &pushzero
        &push r:1        
        &pushsdbgm 38							//'Warning'
        &dcallmp 39							// PlayWarning()
       label4:
      &end // of function GoToMedium

      &function2 GoToSetting (r:2='newSetting') (r:1='_parent')
        &pushsdbgv 40							//'SelectedSetting'
        &push r:2        
        &equals
        &not
        &not
        &jnz label5        
        &pushfalse
        &pushsdbgv 37							//'MyButtons'
        &push r:2        
        &getMember
        &pushbyte 2
        &dcallfp 16							// Release()
        &pushsdbgv 40							//'SelectedSetting'
        &push r:2        
        &lessThan
        &not
        &jnz label5        
        &pushzero
        &push r:1        
        &pushsdbgm 38							//'Warning'
        &dcallmp 39							// PlayWarning()
       label5:
      &end // of function GoToSetting

      &function2 LowerToSetting (r:1='newSetting') ()
        &pushsdbgv 40							//'SelectedSetting'
        &push r:1        
        &greaterThan
        &not
        &jnz label6        
        &push r:1        
        &pushone
        &dcallfp 41							// GoToSetting()
       label6:
      &end // of function LowerToSetting

      &function2 RaiseToSetting (r:1='newSetting') ()
        &pushsdbgv 40							//'SelectedSetting'
        &push r:1        
        &lessThan
        &not
        &jnz label7        
        &push r:1        
        &pushone
        &dcallfp 41							// GoToSetting()
       label7:
      &end // of function RaiseToSetting

      &function2 DefaultDoButtonCallBack (r:5='Param', r:3='Name', r:4='SettingDefaults') (r:1='this', r:2='_parent')
        &pushsdb 40							//'SelectedSetting'
        &pushsdbgv 15							//'MyButtonClip'
        &pushone
        &push r:3        
        &pushsdb 20							//'split'
        &callMethod
        &pushone
        &getMember
        &toNumber
        &setVariable
        &push r:5        
        &pushsdbgv 30							//'SelectedButton'
        &equals
        &not
        &not
        &jnz label10        
        &pushsdb 29							//'_deselect'
        &pushone
        &pushsdbgv 30							//'SelectedButton'
        &dcallmp 24							// gotoAndPlay()
        &push r:4        
        &not
        &not
        &jnz label10        
        &push r:1        
        &push r:2        
        &pushsdbgm 42							//'ShadowSlider'
        &equals
        &not
        &jnz label8        
        &pushsdbgv 40							//'SelectedSetting'
        &pushbyte 2
        &lessThan
        &not
        &not
        &jnz label8        
        &pushsdb 43							//'Invoking Shadow -> Terrain/Shaders rule'
        &trace
        &pushone
        &pushone
        &push r:2        
        &pushsdbgm 44							//'TerrainSlider'
        &dcallmp 45							// RaiseToSetting()
        &pushone
        &pushone
        &push r:2        
        &pushsdbgm 46							//'ShaderSlider'
        &dcallmp 45							// RaiseToSetting()
       label8:
        &push r:1        
        &push r:2        
        &pushsdbgm 44							//'TerrainSlider'
        &equals
        &not
        &jnz label9        
        &pushsdbgv 40							//'SelectedSetting'
        &pushone
        &lessThan
        &not
        &jnz label9        
        &pushsdb 47							//'Invoking Terrain -> Shadow rule'
        &trace
        &pushone
        &pushone
        &push r:2        
        &pushsdbgm 42							//'ShadowSlider'
        &dcallmp 48							// LowerToSetting()
       label9:
        &push r:1        
        &push r:2        
        &pushsdbgm 46							//'ShaderSlider'
        &equals
        &not
        &jnz label10        
        &pushsdbgv 40							//'SelectedSetting'
        &pushone
        &lessThan
        &not
        &jnz label10        
        &pushsdb 49							//'Invoking Shader -> Shadow rule'
        &trace
        &pushone
        &pushone
        &push r:2        
        &pushsdbgm 42							//'ShadowSlider'
        &dcallmp 48							// LowerToSetting()
       label10:
        &pushsdb 30							//'SelectedButton'
        &push r:5        
        &setVariable
        &pushsdbgv 7							//'ChildNumber'
        &pushsdb 50							//''
        &equals
        &not
        &jnz label11        
        &pushsdbgv 15							//'MyButtonClip'
        &pushone
        &push r:3        
        &pushsdb 20							//'split'
        &callMethod
        &pushone
        &getMember
        &pushsdbgv 1							//'MyOption'
        &pushsdb 3							//'Current'
        &add
        &pushbyte 2
        &pushsdbgv 4							//'vRootApt'
        &dcallmp 25							// SetExtern()
        &pushzero
        &dcallfp 10							// SetDefaultOptions()
        &jmp label12        
       label11:
        &pushsdb 31							//'Setting MyContentClip: '
        &pushsdbgv 11							//'MyContentClip'
        &add
        &pushsdb 32							//' OptionName: '
        &add
        &push r:1        
        &pushsdbgv 11							//'MyContentClip'
        &getMember
        &pushsdbgm 33							//'OptionNameText'
        &add
        &pushsdb 34							//' CurrentOptionText = $'
        &add
        &pushsdbgv 1							//'MyOption'
        &add
        &pushsdb 14							//'_'
        &add
        &pushsdbgv 15							//'MyButtonClip'
        &pushone
        &push r:3        
        &pushsdb 20							//'split'
        &callMethod
        &pushone
        &getMember
        &add
        &trace
        &push r:1        
        &pushsdbgv 11							//'MyContentClip'
        &getMember
        &pushsdb 12							//'CurrentOptionText'
        &pushsdb 13							//'$'
        &pushsdbgv 1							//'MyOption'
        &add
        &pushsdb 14							//'_'
        &add
        &pushsdbgv 15							//'MyButtonClip'
        &pushone
        &push r:3        
        &pushsdb 20							//'split'
        &callMethod
        &pushone
        &getMember
        &add
        &setMember
        &push r:4        
        &pushfalse
        &equals
        &not
        &jnz label12        
        &pushsdbgv 15							//'MyButtonClip'
        &pushone
        &push r:3        
        &pushsdb 20							//'split'
        &callMethod
        &pushone
        &getMember
        &pushsdbgv 7							//'ChildNumber'
        &pushbyte 2
        &push r:2        
        &pushsdbgv 8							//'ParentName'
        &getMember
        &dcallmp 51							// SetCustom()
       label12:
      &end // of function DefaultDoButtonCallBack

      &function2 Release (r:1='Param', r:2='SettingDefaults') ()
        &push r:1        
        &pushsdb 52							//'SettingDefaults'
        &push r:2        
        &setMember
        &push r:1        
        &pushsdbgv 30							//'SelectedButton'
        &equals
        &not
        &not
        &jnz label13        
        &pushsdb 53							//'_select'
        &pushone
        &push r:1        
        &dcallmp 24							// gotoAndPlay()
       label13:
      &end // of function Release

      &pushsdb 4							//'vRootApt'
      &pushsdbgv 54							//'_root'
      &pushsdbgm 55							//'Options'
      &pushsdbgm 56							//'m_apt'
      &varEquals
      &pushsdb 57							//'Content:'
      &pushsdbgv 11							//'MyContentClip'
      &add
      &trace
      &pushbyte 100
      &pushsdbgv 11							//'MyContentClip'
      &pushsdbgv 11							//'MyContentClip'
      &pushbyte 3
      &pushthisgv
      &dcallmp 59							// attachMovie()
      &pushsdb 60							//'CurrentExtern'
      &pushsdbgv 1							//'MyOption'
      &pushsdb 61							//'Num'
      &add
      &pushone
      &pushsdbgv 4							//'vRootApt'
      &pushsdb 5							//'GetExtern'
      &callMethod
      &toNumber
      &setVariable
      &pushsdb 50							//''
      &pushbyte 13
      &getProperty
      &pushsdb 62							//'ParentSlider1'
      &equals
      &not
      &jnz label14      
      &pushsdbgv 54							//'_root'
      &pushsdb 63							//'ParentSlider'
      &pushthisgv
      &setMember
     label14:
      &pushsdb 17							//'i'
      &pushzerosv
     label15:
      &pushsdbgv 17							//'i'
      &pushsdbgv 60							//'CurrentExtern'
      &lessThan
      &not
      &jnz label18      
      &pushsdb 64							//'vContent'
      &pushthisgv
      &pushsdbgv 11							//'MyContentClip'
      &getMember
      &varEquals
      &pushbyte 100
      &pushsdbgv 17							//'i'
      &add
      &pushsdbgv 15							//'MyButtonClip'
      &pushsdbgv 17							//'i'
      &add
      &pushsdbgv 15							//'MyButtonClip'
      &pushbyte 3
      &pushsdbgv 64							//'vContent'
      &dcallmp 59							// attachMovie()
      &pushsdb 65							//'vButtonZone'
      &pushthisgv
      &pushsdbgv 11							//'MyContentClip'
      &getMember
      &pushsdbgm 66							//'ButtonZone'
      &varEquals
      &pushsdb 67							//'vButton'
      &pushthisgv
      &pushsdbgv 11							//'MyContentClip'
      &getMember
      &pushsdbgv 15							//'MyButtonClip'
      &pushsdbgv 17							//'i'
      &add
      &getMember
      &varEquals
      &pushsdb 68							//'vExternNum'
      &pushsdbgv 60							//'CurrentExtern'
      &pushone
      &greaterThan
      &jnz label16      
      &pushone
      &jmp label17      
     label16:
      &pushsdbgv 60							//'CurrentExtern'
      &pushone
      &subtract
     label17:
      &varEquals
      &pushsdb 69							//'vHalfWidth'
      &pushsdbgv 67							//'vButton'
      &pushsdbgm 70							//'_width'
      &pushbyte 2
      &divide
      &varEquals
      &pushsdbgv 67							//'vButton'
      &pushsdb 71							//'_y'
      &pushsdbgv 65							//'vButtonZone'
      &pushsdbgm 71							//'_y'
      &pushone
      &add
      &setMember
      &pushsdbgv 67							//'vButton'
      &pushsdb 72							//'_x'
      &pushsdbgv 65							//'vButtonZone'
      &pushsdbgm 72							//'_x'
      &pushsdbgv 65							//'vButtonZone'
      &pushsdbgm 70							//'_width'
      &pushsdbgv 68							//'vExternNum'
      &divide
      &pushsdbgv 17							//'i'
      &multiply
      &add
      &pushsdbgv 69							//'vHalfWidth'
      &pushsdbgv 60							//'CurrentExtern'
      &pushone
      &subtract
      &divide
      &pushsdbgv 17							//'i'
      &multiply
      &subtract
      &setMember
      &pushsdbgv 64							//'vContent'
      &pushsdb 33							//'OptionNameText'
      &pushsdb 13							//'$'
      &pushsdbgv 1							//'MyOption'
      &add
      &setMember
      &pushsdb 17							//'i'
      &pushsdbgv 17							//'i'
      &increment
      &setVariable
      &jmp label15      
     label18:
      &pushsdb 0							//'MyChildren'
      &pushzero
      &pushsdb 73							//'Array'
      &new
      &setVariable
      &pushsdb 37							//'MyButtons'
      &pushzero
      &pushsdb 73							//'Array'
      &new
      &setVariable
      &pushsdbgv 54							//'_root'
      &pushsdbgm 74							//'RefreshAdvOptions'
      &pushundef
      &equals
      &not
      &jnz label19      
      &pushsdbgv 54							//'_root'
      &pushsdb 74							//'RefreshAdvOptions'
      &function2  () (r:1='_root')
        &pushzero
        &push r:1        
        &pushsdbgm 63							//'ParentSlider'
        &dcallmp 10							// SetDefaultOptions()
      &end // of function 

      &setMember
     label19:
      &gotoLabel '_active'
      &play
    &end // of frame 0

    &frame 9
      &pushsgv 'ChildNumber'
      &pushs ''
      &equals
      &not
      &not
      &jnz label1      
      &pushzero
      &pushs 'StandForRoll'
      &callfp
      &jmp label2      
     label1:
      &pushzero
      &pushs 'SetDefaultOptions'
      &callfp
     label2:
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19
  &end // of defineMovieClip 120
  
  &importAssets &from 'GameWindowGadgets.swf'
    'ComboBox' &as 122
  &end // of importAssets

  &defineMovieClip 125 // total frames: 20

    &frame 0
      &constants 'this', 'Graphics', '_root', 'Options', 'RegisterTabChange', 'ResolutionFrame', 'm_label', '$Resolution', 'BrightnessFrame', '$Brightness', 'm_entryPoint', 'MainMenu', '_disableSliders'  
      &pushthisgv
      &pushsdb 1							//'Graphics'
      &pushbyte 2
      &pushsdbgv 2							//'_root'
      &pushsdbgm 3							//'Options'
      &dcallmp 4							// RegisterTabChange()
      &pushsdbgv 5							//'ResolutionFrame'
      &pushsdb 6							//'m_label'
      &pushsdb 7							//'$Resolution'
      &setMember
      &pushsdbgv 8							//'BrightnessFrame'
      &pushsdb 6							//'m_label'
      &pushsdb 9							//'$Brightness'
      &setMember
      &pushsdbgv 2							//'_root'
      &pushsdbgm 3							//'Options'
      &pushsdbgm 10							//'m_entryPoint'
      &pushsdb 11							//'MainMenu'
      &equals
      &jnz label1      
      &pushsdb 12							//'_disableSliders'
      &jmp label2      
     label1:
      &pushbyte 2
     label2:
      &gotoAndPlay    &end // of frame 0

    &placeMovieClip 120 
    
      &onClipEvent &construct
        &pushs 'MyOption'
        &pushssv 'AdvancedOption0'
        &pushs 'ParentName'
        &pushssv 'ParentSlider1'
        &pushs 'ChildNumber'
        &pushzerosv
        &pushs 'MyContentClip'
        &pushssv 'GraphicsSliderContent1'
        &pushs 'MyButtonClip'
        &pushssv 'GraphicsSliderButton1'
      &end
    &end // of placeMovieClip 120

    &placeMovieClip 120 &as 'TerrainSlider'
    
      &onClipEvent &construct
        &pushs 'MyOption'
        &pushssv 'AdvancedOption1'
        &pushs 'ParentName'
        &pushssv 'ParentSlider1'
        &pushs 'ChildNumber'
        &pushone
        &setVariable
        &pushs 'MyContentClip'
        &pushssv 'GraphicsSliderContent1'
        &pushs 'MyButtonClip'
        &pushssv 'GraphicsSliderButton1'
      &end
    &end // of placeMovieClip 120

    &placeMovieClip 120 
    
      &onClipEvent &construct
        &pushs 'MyOption'
        &pushssv 'AdvancedOption2'
        &pushs 'ParentName'
        &pushssv 'ParentSlider1'
        &pushs 'ChildNumber'
        &pushbyte 2
        &setVariable
        &pushs 'MyContentClip'
        &pushssv 'GraphicsSliderContent1'
        &pushs 'MyButtonClip'
        &pushssv 'GraphicsSliderButton1'
      &end
    &end // of placeMovieClip 120

    &placeMovieClip 120 
    
      &onClipEvent &construct
        &pushs 'MyOption'
        &pushssv 'AdvancedOption3'
        &pushs 'ParentName'
        &pushssv 'ParentSlider1'
        &pushs 'ChildNumber'
        &pushbyte 3
        &setVariable
        &pushs 'MyContentClip'
        &pushssv 'GraphicsSliderContent1'
        &pushs 'MyButtonClip'
        &pushssv 'GraphicsSliderButton1'
      &end
    &end // of placeMovieClip 120

    &placeMovieClip 120 
    
      &onClipEvent &construct
        &pushs 'MyOption'
        &pushssv 'AdvancedOption4'
        &pushs 'ParentName'
        &pushssv 'ParentSlider1'
        &pushs 'ChildNumber'
        &pushbyte 4
        &setVariable
        &pushs 'MyContentClip'
        &pushssv 'GraphicsSliderContent1'
        &pushs 'MyButtonClip'
        &pushssv 'GraphicsSliderButton1'
      &end
    &end // of placeMovieClip 120

    &placeMovieClip 120 &as 'ShaderSlider'
    
      &onClipEvent &construct
        &pushs 'MyOption'
        &pushssv 'AdvancedOption5'
        &pushs 'ParentName'
        &pushssv 'ParentSlider1'
        &pushs 'ChildNumber'
        &pushbyte 5
        &setVariable
        &pushs 'MyContentClip'
        &pushssv 'GraphicsSliderContent1'
        &pushs 'MyButtonClip'
        &pushssv 'GraphicsSliderButton1'
      &end
    &end // of placeMovieClip 120

    &placeMovieClip 120 
    
      &onClipEvent &construct
        &pushs 'MyOption'
        &pushssv 'AdvancedOption6'
        &pushs 'ParentName'
        &pushssv 'ParentSlider1'
        &pushs 'ChildNumber'
        &pushbyte 6
        &setVariable
        &pushs 'MyContentClip'
        &pushssv 'GraphicsSliderContent1'
        &pushs 'MyButtonClip'
        &pushssv 'GraphicsSliderButton1'
      &end
    &end // of placeMovieClip 120

    &placeMovieClip 120 &as 'ShadowSlider'
    
      &onClipEvent &construct
        &pushs 'MyOption'
        &pushssv 'AdvancedOption7'
        &pushs 'ParentName'
        &pushssv 'ParentSlider1'
        &pushs 'ChildNumber'
        &pushbyte 7
        &setVariable
        &pushs 'MyContentClip'
        &pushssv 'GraphicsSliderContent1'
        &pushs 'MyButtonClip'
        &pushssv 'GraphicsSliderButton1'
      &end
    &end // of placeMovieClip 120

    &placeMovieClip 120 
    
      &onClipEvent &construct
        &pushs 'MyOption'
        &pushssv 'AdvancedOption8'
        &pushs 'ParentName'
        &pushssv 'ParentSlider1'
        &pushs 'ChildNumber'
        &pushbyte 8
        &setVariable
        &pushs 'MyContentClip'
        &pushssv 'GraphicsSliderContent1'
        &pushs 'MyButtonClip'
        &pushssv 'GraphicsSliderButton1'
      &end
    &end // of placeMovieClip 120

    &placeMovieClip 120 &as 'ParentSlider1'
    
      &onClipEvent &construct
        &pushs 'MyOption'
        &pushssv 'MasterOption0'
        &pushs 'ParentName'
        &pushssv 'ParentSlider1'
        &pushs 'ChildNumber'
        &pushssv ''
        &pushs 'MyContentClip'
        &pushssv 'GraphicsSliderContent2'
        &pushs 'MyButtonClip'
        &pushssv 'GraphicsSliderButton2'
      &end
    &end // of placeMovieClip 120

    &placeMovieClip 120 
    
      &onClipEvent &construct
        &pushs 'MyOption'
        &pushssv 'AdvancedOption9'
        &pushs 'ParentName'
        &pushssv 'ParentSlider1'
        &pushs 'ChildNumber'
        &pushbyte 9
        &setVariable
        &pushs 'MyContentClip'
        &pushssv 'GraphicsSliderContent1'
        &pushs 'MyButtonClip'
        &pushssv 'GraphicsSliderButton1'
      &end
    &end // of placeMovieClip 120

    &placeMovieClip 122 &as 'Options::Resolution'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'ComboBox'
        &pushs '_Init'
        &pushssv 'AptOptions::InitGadgets'
        &pushs '_Load'
        &pushssv 'Apt/ComboBox.wnd'
      &end
    &end // of placeMovieClip 122

    &placeMovieClip 81 &as 'Options::Brightness'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'HorzSlider'
        &pushs '_Init'
        &pushssv 'AptOptions::InitGadgets'
        &pushs '_Load'
        &pushssv 'Apt/HorzSlider.wnd'
      &end
    &end // of placeMovieClip 81

    &frame 8
      &stop
    &end // of frame 8

    &frame 19
      &stop
    &end // of frame 19
  &end // of defineMovieClip 125

  &defineMovieClip 136 // total frames: 3

    &frame 0
      &stop
      &pushsgv 'RadioButton'
      &pushs 'onRelease'
      &function2  () (r:1='_parent')
        &pushs 'Choice'
        &pushone
        &pushs ''
        &pushbyte 13
        &getProperty
        &pushs 'split'
        &callMethod
        &pushone
        &getMember
        &pushone
        &push r:1        
        &pushs 'SelectChoice'
        &callmp
      &end // of function 

      &setMember
    &end // of frame 0

    &frame 1
      &stop
    &end // of frame 1

    &frame 2
      &stop
    &end // of frame 2
  &end // of defineMovieClip 136

  &defineMovieClip 140 // total frames: 21

    &frame 8
      &stop
    &end // of frame 8

    &frame 19
      &stop
    &end // of frame 19

    &frame 20
    &end // of frame 20

    &frame 20
      &stop
    &end // of frame 20
  &end // of defineMovieClip 140

  &defineMovieClip 144 // total frames: 21

    &frame 8
      &stop
    &end // of frame 8

    &frame 19
      &stop
    &end // of frame 19

    &frame 20
      &stop
    &end // of frame 20
  &end // of defineMovieClip 144

  &defineMovieClip 145 // total frames: 1

    &frame 0
      &constants 'SelectChoice: ', '', ', ', 'currentChoice', 'VoiceActivated', 'PushToTalk', 'Options', 'SetVoIPActivationMode', 'i', 'Choice', 'Text', '_deselect', '_select', 'enabled', 'Choice disabled', '_disabled', 'gotoAndStop', 'ToggleThresholdSlider', 'ThresholdAdjuster', 'UpdateThresholdButton', 'GetVoIPActivationMode', 'SelectChoice', 'RadioGroupEnable: ', 'UpdateChoice', '_root', 'AreVoIPControlsEnabled'  
      &function2 SelectChoice (r:6='selectedChoice') (r:1='this', r:2='_root')
        &pushsdb 0							//'SelectChoice: '
        &pushsdb 1							//''
        &pushbyte 13
        &getProperty
        &add
        &pushsdb 2							//', '
        &add
        &push r:6        
        &add
        &trace
        &pushsdb 3							//'currentChoice'
        &push r:6        
        &setVariable
        &pushsdbgv 3							//'currentChoice'
        &pushzero
        &equals
        &jnz label1        
        &pushsdb 4							//'VoiceActivated'
        &jmp label2        
       label1:
        &pushsdb 5							//'PushToTalk'
       label2:
        &pushone
        &push r:2        
        &pushsdbgm 6							//'Options'
        &dcallmp 7							// SetVoIPActivationMode()
        &pushsdb 8							//'i'
        &pushzerosv
       label3:
        &push r:1        
        &pushsdb 9							//'Choice'
        &pushsdbgv 8							//'i'
        &add
        &getMember
        &setRegister r:4
        &pop
        &push r:1        
        &pushsdb 9							//'Choice'
        &pushsdbgv 8							//'i'
        &add
        &pushsdb 10							//'Text'
        &add
        &getMember
        &setRegister r:5
        &pop
        &push r:4        
        &pushundef
        &equals
        &not
        &jnz label4        
        &jmp label8        
       label4:
        &pushsdbgv 8							//'i'
        &push r:6        
        &equals
        &jnz label5        
        &pushsdb 11							//'_deselect'
        &jmp label6        
       label5:
        &pushsdb 12							//'_select'
       label6:
        &setRegister r:3
        &pop
        &pushsdbgv 13							//'enabled'
        &not
        &not
        &jnz label7        
        &pushsdb 14							//'Choice disabled'
        &trace
        &pushsdb 15							//'_disabled'
        &setRegister r:3
        &pop
       label7:
        &push r:3        
        &pushone
        &push r:4        
        &dcallmp 16							// gotoAndStop()
        &push r:3        
        &pushone
        &push r:5        
        &dcallmp 16							// gotoAndStop()
        &pushsdb 8							//'i'
        &pushsdbgv 8							//'i'
        &increment
        &setVariable
        &jmp label3        
       label8:
        &pushzero
        &dcallfp 17							// ToggleThresholdSlider()
      &end // of function SelectChoice

      &function2 ToggleThresholdSlider () (r:1='_parent')
        &pushzero
        &push r:1        
        &pushsdbgm 18							//'ThresholdAdjuster'
        &dcallmp 19							// UpdateThresholdButton()
      &end // of function ToggleThresholdSlider

      &function2 UpdateChoice () (r:1='_root')
        &pushzero
        &push r:1        
        &pushsdbgm 6							//'Options'
        &pushsdb 20							//'GetVoIPActivationMode'
        &callMethod
        &pushsdb 5							//'PushToTalk'
        &equals
        &jnz label9        
        &pushone
        &jmp label10        
       label9:
        &pushzero
       label10:
        &pushone
        &dcallfp 21							// SelectChoice()
        &pushzero
        &dcallfp 17							// ToggleThresholdSlider()
      &end // of function UpdateChoice

      &function2 Enable (r:1='enable') ()
        &pushsdb 22							//'RadioGroupEnable: '
        &push r:1        
        &add
        &trace
        &pushsdb 13							//'enabled'
        &push r:1        
        &setVariable
        &pushzero
        &dcallfp 23							// UpdateChoice()
      &end // of function Enable

      &stop
      &pushsdb 3							//'currentChoice'
      &pushzero
      &varEquals
      &pushsdb 13							//'enabled'
      &pushzero
      &pushsdbgv 24							//'_root'
      &pushsdbgm 6							//'Options'
      &pushsdb 25							//'AreVoIPControlsEnabled'
      &callMethod
      &varEquals
      &pushzero
      &dcallfp 23							// UpdateChoice()
    &end // of frame 0
  &end // of defineMovieClip 145

  &defineMovieClip 147 // total frames: 1
  &end // of defineMovieClip 147

  &defineMovieClip 150 // total frames: 2
  &end // of defineMovieClip 150

  &defineMovieClip 151 // total frames: 3

    &frame 0
      &constants 'originalWidth', 'Bar', '_width', '_visible'  
      &pushsdb 0							//'originalWidth'
      &var
      &pushsdbgv 0							//'originalWidth'
      &pushundef
      &equals
      &not
      &jnz label1      
      &pushsdb 0							//'originalWidth'
      &pushsdbgv 1							//'Bar'
      &pushsdbgm 2							//'_width'
      &setVariable
     label1:
      &pushsdbgv 1							//'Bar'
      &pushsdb 2							//'_width'
      &pushzero
      &setMember
      &pushsdbgv 1							//'Bar'
      &pushsdb 3							//'_visible'
      &pushfalse
      &setMember
      &stop
    &end // of frame 0

    &frame 1
      &constants 'currentValue', '_root', 'Options', 'GetCurrentVoiceLevel', 'Bar', '_width', 'originalWidth', '_visible', '_parent', 'thresholdValue', '_notOk', 'gotoAndStop', '_ok'  
      &pushsdb 0							//'currentValue'
      &pushzero
      &pushsdbgv 1							//'_root'
      &pushsdbgm 2							//'Options'
      &pushsdb 3							//'GetCurrentVoiceLevel'
      &callMethod
      &varEquals
      &pushsdbgv 4							//'Bar'
      &pushsdb 5							//'_width'
      &pushsdbgv 6							//'originalWidth'
      &pushsdbgv 0							//'currentValue'
      &multiply
      &setMember
      &pushsdbgv 4							//'Bar'
      &pushsdb 7							//'_visible'
      &pushtrue
      &setMember
      &pushsdbgv 0							//'currentValue'
      &pushsdbgv 8							//'_parent'
      &pushsdbgm 9							//'thresholdValue'
      &lessThan
      &dup
      &jnz label1      
      &pop
      &pushsdbgv 0							//'currentValue'
      &pushfloat 0.949999988079071
      &greaterThan
     label1:
      &not
      &jnz label2      
      &pushsdb 10							//'_notOk'
      &pushone
      &pushsdbgv 4							//'Bar'
      &dcallmp 11							// gotoAndStop()
      &jmp label3      
     label2:
      &pushsdb 12							//'_ok'
      &pushone
      &pushsdbgv 4							//'Bar'
      &dcallmp 11							// gotoAndStop()
     label3:
    &end // of frame 1

    &frame 2
      &gotoLabel '_enabled'
      &play
    &end // of frame 2
  &end // of defineMovieClip 151

  &defineMovieClip 154 // total frames: 1

    &frame 0
      &constants 'isDragging', '', 'minX', 'maxX', 'SetThreshold', 'thresholdValue', 'Options', 'SetVoiceThreshold', 'ThresholdButton', '_x', 'isEnabled', 'UpdateThresholdButton', '_enabled', 'VolumeDisplay', 'gotoAndPlay', '_disabled', '_visible', 'GetVoIPActivationMode', 'VoiceActivated', '_root', 'GetVoiceThreshold', '_width', '-', 'this', 'onMouseMove', 'UpdateThreshold', 'onPress', 'onMouseUp'  
      &function UpdateThreshold (      )      
        &pushsdbgv 0							//'isDragging'
        &not
        &not
        &jnz label1        
        &pushundef
        &return
       label1:
        &pushsdb 1							//''
        &pushbyte 20
        &getProperty
        &pushsdbgv 2							//'minX'
        &subtract
        &pushsdbgv 3							//'maxX'
        &pushsdbgv 2							//'minX'
        &subtract
        &divide
        &pushone
        &dcallfp 4							// SetThreshold()
      &end // of function UpdateThreshold

      &function2 SetThreshold (r:2='newThresholdValue') (r:1='_root')
        &pushsdb 5							//'thresholdValue'
        &push r:2        
        &setVariable
        &pushsdbgv 5							//'thresholdValue'
        &pushzero
        &lessThan
        &not
        &jnz label2        
        &pushsdb 5							//'thresholdValue'
        &pushzerosv
       label2:
        &pushsdbgv 5							//'thresholdValue'
        &pushone
        &greaterThan
        &not
        &jnz label3        
        &pushsdb 5							//'thresholdValue'
        &pushone
        &setVariable
       label3:
        &pushsdbgv 5							//'thresholdValue'
        &pushone
        &push r:1        
        &pushsdbgm 6							//'Options'
        &dcallmp 7							// SetVoiceThreshold()
        &pushsdbgv 8							//'ThresholdButton'
        &pushsdb 9							//'_x'
        &pushsdbgv 5							//'thresholdValue'
        &pushsdbgv 3							//'maxX'
        &pushsdbgv 2							//'minX'
        &subtract
        &multiply
        &pushsdbgv 2							//'minX'
        &add
        &setMember
      &end // of function SetThreshold

      &function2 Enable (r:1='enabled') ()
        &pushsdb 10							//'isEnabled'
        &push r:1        
        &setVariable
        &pushzero
        &dcallfp 11							// UpdateThresholdButton()
        &push r:1        
        &not
        &jnz label4        
        &pushsdb 12							//'_enabled'
        &pushone
        &pushsdbgv 13							//'VolumeDisplay'
        &dcallmp 14							// gotoAndPlay()
        &jmp label5        
       label4:
        &pushsdb 15							//'_disabled'
        &pushone
        &pushsdbgv 13							//'VolumeDisplay'
        &dcallmp 14							// gotoAndPlay()
       label5:
      &end // of function Enable

      &function2 UpdateThresholdButton () (r:1='_root')
        &pushsdbgv 8							//'ThresholdButton'
        &pushsdb 16							//'_visible'
        &pushsdbgv 10							//'isEnabled'
        &dup
        &not
        &jnz label6        
        &pop
        &pushzero
        &push r:1        
        &pushsdbgm 6							//'Options'
        &pushsdb 17							//'GetVoIPActivationMode'
        &callMethod
        &pushsdb 18							//'VoiceActivated'
        &equals
       label6:
        &setMember
      &end // of function UpdateThresholdButton

      &stop
      &pushsdb 5							//'thresholdValue'
      &pushzero
      &pushsdbgv 19							//'_root'
      &pushsdbgm 6							//'Options'
      &pushsdb 20							//'GetVoiceThreshold'
      &callMethod
      &varEquals
      &pushsdb 10							//'isEnabled'
      &pushfalse
      &varEquals
      &pushsdb 0							//'isDragging'
      &pushfalse
      &varEquals
      &pushsdb 2							//'minX'
      &pushsdbgv 13							//'VolumeDisplay'
      &pushsdbgm 9							//'_x'
      &varEquals
      &pushsdb 3							//'maxX'
      &pushsdbgv 2							//'minX'
      &pushsdbgv 13							//'VolumeDisplay'
      &pushsdbgm 9							//'_x'
      &add
      &pushsdbgv 13							//'VolumeDisplay'
      &pushsdbgm 21							//'_width'
      &add
      &varEquals
      &pushsdbgv 2							//'minX'
      &pushsdb 22							//'-'
      &add
      &pushsdbgv 3							//'maxX'
      &add
      &trace
      &pushzero
      &pushsdbgv 19							//'_root'
      &pushsdbgm 6							//'Options'
      &pushsdb 20							//'GetVoiceThreshold'
      &callMethod
      &pushone
      &dcallfp 4							// SetThreshold()
      &pushthisgv
      &pushsdb 24							//'onMouseMove'
      &function  (      )      
        &pushsdbgv 10							//'isEnabled'
        &not
        &jnz label7        
        &pushzero
        &dcallfp 25							// UpdateThreshold()
       label7:
      &end // of function 

      &setMember
      &pushsdbgv 8							//'ThresholdButton'
      &pushsdb 26							//'onPress'
      &function  (      )      
        &pushsdbgv 10							//'isEnabled'
        &not
        &jnz label8        
        &pushsdb 0							//'isDragging'
        &pushtrue
        &setVariable
        &pushzero
        &dcallfp 25							// UpdateThreshold()
       label8:
      &end // of function 

      &setMember
      &pushthisgv
      &pushsdb 27							//'onMouseUp'
      &function  (      )      
        &pushsdb 0							//'isDragging'
        &pushfalse
        &setVariable
      &end // of function 

      &setMember
      &pushzero
      &dcallfp 11							// UpdateThresholdButton()
    &end // of frame 0
  &end // of defineMovieClip 154

  &defineMovieClip 156 // total frames: 3

    &frame 0
      &play
      &pushs 'stopCalibration'
      &pushfalse
      &varEquals
    &end // of frame 0

    &frame 1
      &constants 'Stopper frame 2: ', 'stopCalibration', '_parent', 'Calibrate', 'ReleaseCallback'  
      &pushsdb 0							//'Stopper frame 2: '
      &pushsdbgv 1							//'stopCalibration'
      &add
      &trace
      &pushsdbgv 1							//'stopCalibration'
      &not
      &jnz label1      
      &pushsdb 1							//'stopCalibration'
      &trace
      &pushzero
      &pushsdbgv 2							//'_parent'
      &pushsdbgm 3							//'Calibrate'
      &dcallmp 4							// ReleaseCallback()
      &pushsdb 1							//'stopCalibration'
      &pushfalse
      &setVariable
     label1:
    &end // of frame 1

    &frame 2
      &gotoFrame 1
      &play
    &end // of frame 2
  &end // of defineMovieClip 156

  &defineMovieClip 160 // total frames: 2

    &frame 0
      &constants 'Calibrate', 'Enable', 'currentlyCalibrating', 'VoiceCalibrationStopper', 'stopCalibration', 'Disable', 'this', 'Audio', '_root', 'Options', 'RegisterTabChange', 'MusicFrame', 'm_label', '$Music', 'SfxFrame', '$SoundFx', 'VoiceFrame', '$Voice', 'AmbientFrame', '$Ambient', 'MovieFrame', '$Movie', 'TransmitFrame', '$TransmitVolume', 'ReceiveFrame', '$ReceiveVolume', '$StartTest', 'SetText', 'ReleaseCallback', 'Calibrate.ReleaseCallback', 'OnVoiceCalibration', '_parent', 'ThresholdAdjuster', '$StopTest', 'prevState', 'TestButton', 'onRelease', 'EnableCalibrateButton'  
      &function2 EnableCalibrateButton (r:1='enable') ()
        &push r:1        
        &not
        &jnz label1        
        &pushzero
        &pushsdbgv 0							//'Calibrate'
        &dcallmp 1							// Enable()
        &jmp label3        
       label1:
        &pushsdbgv 2							//'currentlyCalibrating'
        &not
        &jnz label2        
        &pushsdbgv 3							//'VoiceCalibrationStopper'
        &pushsdb 4							//'stopCalibration'
        &pushtrue
        &setMember
       label2:
        &pushzero
        &pushsdbgv 0							//'Calibrate'
        &dcallmp 5							// Disable()
       label3:
      &end // of function EnableCalibrateButton

      &pushthisgv
      &pushsdb 7							//'Audio'
      &pushbyte 2
      &pushsdbgv 8							//'_root'
      &pushsdbgm 9							//'Options'
      &dcallmp 10							// RegisterTabChange()
      &pushsdbgv 11							//'MusicFrame'
      &pushsdb 12							//'m_label'
      &pushsdb 13							//'$Music'
      &setMember
      &pushsdbgv 14							//'SfxFrame'
      &pushsdb 12							//'m_label'
      &pushsdb 15							//'$SoundFx'
      &setMember
      &pushsdbgv 16							//'VoiceFrame'
      &pushsdb 12							//'m_label'
      &pushsdb 17							//'$Voice'
      &setMember
      &pushsdbgv 18							//'AmbientFrame'
      &pushsdb 12							//'m_label'
      &pushsdb 19							//'$Ambient'
      &setMember
      &pushsdbgv 20							//'MovieFrame'
      &pushsdb 12							//'m_label'
      &pushsdb 21							//'$Movie'
      &setMember
      &pushsdbgv 22							//'TransmitFrame'
      &pushsdb 12							//'m_label'
      &pushsdb 23							//'$TransmitVolume'
      &setMember
      &pushsdbgv 24							//'ReceiveFrame'
      &pushsdb 12							//'m_label'
      &pushsdb 25							//'$ReceiveVolume'
      &setMember
      &pushsdb 2							//'currentlyCalibrating'
      &pushfalse
      &varEquals
      &pushsdb 26							//'$StartTest'
      &pushone
      &pushsdbgv 0							//'Calibrate'
      &dcallmp 27							// SetText()
      &pushsdbgv 0							//'Calibrate'
      &pushsdb 28							//'ReleaseCallback'
      &function2  () (r:1='this', r:2='_root')
        &pushsdb 29							//'Calibrate.ReleaseCallback'
        &trace
        &pushsdb 2							//'currentlyCalibrating'
        &pushsdbgv 2							//'currentlyCalibrating'
        &not
        &setVariable
        &pushsdbgv 2							//'currentlyCalibrating'
        &pushone
        &push r:2        
        &pushsdbgm 9							//'Options'
        &dcallmp 30							// OnVoiceCalibration()
        &pushsdbgv 2							//'currentlyCalibrating'
        &pushone
        &push r:1        
        &pushsdbgm 31							//'_parent'
        &pushsdbgm 32							//'ThresholdAdjuster'
        &dcallmp 1							// Enable()
        &pushsdbgv 2							//'currentlyCalibrating'
        &not
        &jnz label4        
        &pushsdb 33							//'$StopTest'
        &pushone
        &push r:1        
        &dcallmp 27							// SetText()
        &jmp label5        
       label4:
        &pushsdb 26							//'$StartTest'
        &pushone
        &push r:1        
        &dcallmp 27							// SetText()
       label5:
      &end // of function 

      &setMember
      &pushsdb 34							//'prevState'
      &pushfalse
      &varEquals
      &pushsdbgv 35							//'TestButton'
      &pushsdb 36							//'onRelease'
      &function  (      )      
        &pushsdbgv 34							//'prevState'
        &trace
        &pushsdb 34							//'prevState'
        &pushsdbgv 34							//'prevState'
        &not
        &setVariable
        &pushsdbgv 34							//'prevState'
        &pushone
        &dcallfp 37							// EnableCalibrateButton()
      &end // of function 

      &setMember
    &end // of frame 0

    &placeMovieClip 72 &as 'Options::BoostMicrophone'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'CheckBox'
        &pushs '_Load'
        &pushssv 'Apt/CheckBox.wnd'
        &pushs '_Init'
        &pushssv 'AptOptions::InitGadgets'
        &pushs '_CheckBoxString'
        &pushssv ''
      &end
    &end // of placeMovieClip 72

    &placeMovieClip 98 &as 'Calibrate'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv ''
      &end
    &end // of placeMovieClip 98

    &placeMovieClip 81 &as 'Options::MusicVolume'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'HorzSlider'
        &pushs '_Init'
        &pushssv 'AptOptions::InitGadgets'
        &pushs '_Load'
        &pushssv 'Apt/HorzSlider.wnd'
      &end
    &end // of placeMovieClip 81

    &placeMovieClip 81 &as 'Options::SoundFxVolume'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'HorzSlider'
        &pushs '_Init'
        &pushssv 'AptOptions::InitGadgets'
        &pushs '_Load'
        &pushssv 'Apt/HorzSlider.wnd'
      &end
    &end // of placeMovieClip 81

    &placeMovieClip 81 &as 'Options::AmbientVolume'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'HorzSlider'
        &pushs '_Init'
        &pushssv 'AptOptions::InitGadgets'
        &pushs '_Load'
        &pushssv 'Apt/HorzSlider.wnd'
      &end
    &end // of placeMovieClip 81

    &placeMovieClip 81 &as 'Options::MovieVolume'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'HorzSlider'
        &pushs '_Init'
        &pushssv 'AptOptions::InitGadgets'
        &pushs '_Load'
        &pushssv 'Apt/HorzSlider.wnd'
      &end
    &end // of placeMovieClip 81

    &placeMovieClip 72 &as 'Options::HighAudioQuality'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'CheckBox'
        &pushs '_Load'
        &pushssv 'Apt/CheckBox.wnd'
        &pushs '_Init'
        &pushssv 'AptOptions::InitGadgets'
        &pushs '_CheckBoxString'
        &pushssv ''
      &end
    &end // of placeMovieClip 72

    &placeMovieClip 72 &as 'Online::EnabledVoIP'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'CheckBox'
        &pushs '_Load'
        &pushssv 'Apt/CheckBox.wnd'
        &pushs '_Init'
        &pushssv 'AptOptions::InitGadgets'
        &pushs '_CheckBoxString'
        &pushssv ''
      &end
    &end // of placeMovieClip 72

    &placeMovieClip 81 &as 'Options::ReceiveVolume'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'HorzSlider'
        &pushs '_Init'
        &pushssv 'AptOptions::InitGadgets'
        &pushs '_Load'
        &pushssv 'Apt/HorzSlider.wnd'
      &end
    &end // of placeMovieClip 81

    &placeMovieClip 81 &as 'Options::TransmitVolume'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'HorzSlider'
        &pushs '_Init'
        &pushssv 'AptOptions::InitGadgets'
        &pushs '_Load'
        &pushssv 'Apt/HorzSlider.wnd'
      &end
    &end // of placeMovieClip 81

    &placeMovieClip 81 &as 'Options::VoiceVolume'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'HorzSlider'
        &pushs '_Init'
        &pushssv 'AptOptions::InitGadgets'
        &pushs '_Load'
        &pushssv 'Apt/HorzSlider.wnd'
      &end
    &end // of placeMovieClip 81

    &frame 1
      &pushzero
      &pushsgv '_root'
      &pushsgm 'Options'
      &pushs '_RefreshEnableVoIPControls'
      &callmp
      &stop
    &end // of frame 1
  &end // of defineMovieClip 160
  
  &importAssets &from 'GameWindowGadgets.swf'
    'TextEntry' &as 165
  &end // of importAssets

  &defineMovieClip 166 // total frames: 2

    &frame 0
      &constants 'this', 'Network', '_root', 'Options', 'RegisterTabChange', 'ConnectionSpeedFrame', 'm_label', '$ConnectionSpeed', 'OnlineIpFrame', '$OnlineIp', 'PortNumberFrame', '$PortNum', 'RefreshNat', 'ReleaseCallback', 'OnRefreshNATPressed'  
      &pushthisgv
      &pushsdb 1							//'Network'
      &pushbyte 2
      &pushsdbgv 2							//'_root'
      &pushsdbgm 3							//'Options'
      &dcallmp 4							// RegisterTabChange()
      &pushsdbgv 5							//'ConnectionSpeedFrame'
      &pushsdb 6							//'m_label'
      &pushsdb 7							//'$ConnectionSpeed'
      &setMember
      &pushsdbgv 8							//'OnlineIpFrame'
      &pushsdb 6							//'m_label'
      &pushsdb 9							//'$OnlineIp'
      &setMember
      &pushsdbgv 10							//'PortNumberFrame'
      &pushsdb 6							//'m_label'
      &pushsdb 11							//'$PortNum'
      &setMember
      &pushsdbgv 12							//'RefreshNat'
      &pushsdb 13							//'ReleaseCallback'
      &function2  () (r:1='_root')
        &pushzero
        &push r:1        
        &pushsdbgm 3							//'Options'
        &dcallmp 14							// OnRefreshNATPressed()
      &end // of function 

      &setMember
    &end // of frame 0

    &placeMovieClip 98 &as 'RefreshNat'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv ''
      &end
    &end // of placeMovieClip 98

    &placeMovieClip 122 &as 'Options::OnlineIp'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'ComboBox'
        &pushs '_Init'
        &pushssv 'AptOptions::InitGadgets'
        &pushs '_Load'
        &pushssv 'Apt/ComboBox.wnd'
      &end
    &end // of placeMovieClip 122

    &placeMovieClip 165 &as 'Options::OnlinePortNum'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'TextEntry'
        &pushs '_Init'
        &pushssv 'AptOptions::InitGadgets'
        &pushs '_Load'
        &pushssv 'Apt/TextEntry.wnd'
      &end
    &end // of placeMovieClip 165

    &placeMovieClip 72 &as 'Options::SendDelay'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'CheckBox'
        &pushs '_Load'
        &pushssv 'Apt/CheckBox.wnd'
        &pushs '_Init'
        &pushssv 'AptOptions::InitGadgets'
        &pushs '_CheckBoxString'
        &pushssv ''
      &end
    &end // of placeMovieClip 72

    &frame 1
      &constants '_root', 'Options', 'm_entryPoint', 'Online', 'RefreshNat', 'Enable', 'Disable'  
      &pushsdbgv 0							//'_root'
      &pushsdbgm 1							//'Options'
      &pushsdbgm 2							//'m_entryPoint'
      &pushsdb 3							//'Online'
      &equals
      &not
      &jnz label1      
      &pushzero
      &pushsdbgv 4							//'RefreshNat'
      &dcallmp 5							// Enable()
      &jmp label2      
     label1:
      &pushzero
      &pushsdbgv 4							//'RefreshNat'
      &dcallmp 6							// Disable()
     label2:
      &stop
    &end // of frame 1
  &end // of defineMovieClip 166

  &defineMovieClip 167 // total frames: 50

    &frame 0
      &constants 'init', 'LoadCustomHotkeys'  
      &pushsdbgv 0							//'init'
      &not
      &not
      &jnz label1      
      &pushzero
      &dcallfp 1							// LoadCustomHotkeys()
      &gotoLabel '_graphics'
      &play
      &pushsdb 0							//'init'
      &pushtrue
      &setVariable
     label1:
    &end // of frame 0

    &frame 0
      &pushsgv 'MessengerBttn'
      &pushs '_visible'
      &pushzero
      &pushsgv '_root'
      &pushsgm 'Options'
      &pushs 'IsInMpGame'
      &callMethod
      &setMember
    &end // of frame 0

    &frame 8
      &stop
    &end // of frame 8

    &frame 18
      &stop
    &end // of frame 18

    &frame 28
      &stop
    &end // of frame 28

    &frame 38
      &stop
    &end // of frame 38

    &frame 49
      &stop
    &end // of frame 49

    &frame 49
      &pushsgv 'MessengerBttn'
      &pushsgm 'Options'
      &pushs '_visible'
      &pushzero
      &pushsgv '_root'
      &pushs 'IsInMpGame'
      &callMethod
      &setMember
    &end // of frame 49
  &end // of defineMovieClip 167
  
  &exportAssets
    167 &as 'OptionsClass'
  &end // of exportAssets

  &frame 0
    &pushsgv '_root'
    &pushs 'CodePrefix'
    &pushssm 'AptOptions'
  &end // of frame 0
  
  &importAssets &from 'ShellContent.swf'
    'ShellContent_ShellBackground' &as 168
  &end // of importAssets

  &placeMovieClip 168 
  
    &onClipEvent &construct
      &pushs 'vHideScreenBehind'
      &pushtrue
      &setVariable
      &pushs 'vAlpha'
      &pushtrue
      &setVariable
      &pushs 'vTitle'
      &pushssv '$Settings'
    &end
  &end // of placeMovieClip 168
  
  &exportAssets
    167 &as 'OptionsClass'
  &end // of exportAssets

  &defineMovieClip 169 // total frames: 0
  &end // of defineMovieClip 169
  
  &exportAssets
    169 &as '__Packages.DebugClass'
  &end // of exportAssets
  
  &initMovieClip 169
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

    &setRegister r:1
    &setMember
    &push r:1    
    &pushsdbgm 2							//'prototype'
    &setRegister r:2
    &pop
    &push r:2    
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
    &push r:2    
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
    &push r:2    
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
    &push r:2    
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
    &push r:2    
    &pushsdb 7							//'extern'
    &pushsdb 10							//'DoTrace'
    &pushone
    &pushsdb 8							//'InGame'
    &pushzero
    &pushbyte 2
    &initObject
    &setMember
    &push r:2    
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
  &end // of initMovieClip 169

  &defineMovieClip 170 // total frames: 0
  &end // of defineMovieClip 170
  
  &exportAssets
    170 &as '__Packages.OptionsClass'
  &end // of exportAssets
  
  &initMovieClip 170
    &constants '_global', 'OptionsClass', 'debug', 'Enable', 'AptApiClass', 'm_apt', 'm_classRoot', 'InGame', '1', 'AllowAdvancedOptions', 'SetExtern', 'MainMenu', 'EntryPoint', 'AllowResolutionChange', 'NetworkEnabled', 'VoIPControlsEnabled', 'MasterOption0Num', 'Custom', 'MasterOption0Current', 'MasterOption0ResetDefault', '0,0,0,0,0,0,0,0,0,0', 'MasterOption0Template0', '2,2,2,2,2,2,2,2,2,2', 'MasterOption0Template1', '3,3,3,3,3,3,3,3,3,3', 'MasterOption0Template2', '4,4,4,4,4,4,4,4,4,4', 'MasterOption0Template3', '0,0,0,2,2,2,2,2,2,2', 'MasterOption0TemplateCustom', 'AdvancedOption0Num', 'AdvancedOption1Num', 'AdvancedOption2Num', 'AdvancedOption3Num', 'AdvancedOption4Num', 'AdvancedOption5Num', 'AdvancedOption6Num', 'AdvancedOption7Num', 'AdvancedOption8Num', 'AdvancedOption9Num', 'VoiceActivated', 'VoIPActivationMode', 'CurrentVoiceLevel', 'VoiceThreshold', 'm_entryPoint', 'GetExtern', 'm_inMpGame', 'Online', 'Network', 'MovieClip', 'prototype', 'onUnload', 'AptZombieClass', 'DeleteFunctions', 'Class', 'DeleteClass', 'OnExitScreen', 'm_exitVar >> ', 'm_exitVar', '', 'Call', 'OnDonePress', '_close', 'gotoAndPlay', 'Save', 'OnCancelPress', 'Cancel', 'LoadCustomHotkeys', 'HotkeyScreen', 'CustomHotkeys.swf', 'Options', 'CustomHotkeyLoader', 'loadMovie', 'SetCustomHotkeysVisibility', '_visible', 'MainButtons', 'Defaults', 'DefaultsButtonFrame', 'RegisterTabChange', 'm_currentTabName', 'm_currentTabClip', 'm_isVoiceCalibrating', 'OnVoiceCalibration', 'CurrentTab', 'SetDefaultTabSettings', 'SetDefault >> ', 'Reset', 'Graphics', 'ParentSlider1', 'SetDefaultOptions', 'Audio', 'TalkModeRadioGroup', 'UpdateChoice', 'GetVoiceThreshold', 'ThresholdAdjuster', 'SetThreshold', '0', 'SetVoiceThreshold', 'm_voiceThreshold', 'GetCurrentVoiceLevel', 'Math', 'random', 'SetVoIPActivationMode', 'GetVoIPActivationMode', 'AreVoIPControlsEnabled', 'AreVoIPControlsEnabled: ', 'IsNetworkEnabled', 'OnRefreshNATPressed', 'RefreshNat', 'IsInMpGame', 'IsInDemo', 'IsCnc3Demo', 'IsSpectatorClient', 'IsSpecialEdition', 'IsSpecialEditionExe', '_RefreshEnableVoIPControls', 'RefreshEnableVoIPControls called', 'AudioOptions', 'EnableCalibrateButton', 'DebugClass', 'ASSetPropFlags'  
    &pushglobalgv
    &pushsdbgm 1							//'OptionsClass'
    &not
    &not
    &jnz label13    
    &pushglobalgv
    &pushsdb 1							//'OptionsClass'
    &function2  () (r:1='this', r:2='super', r:3='_global')
      &pushzero
      &push r:2      
      &pushundef
      &callmp
      &pushtrue
      &pushone
      &pushsdbgv 1							//'OptionsClass'
      &pushsdbgm 2							//'debug'
      &dcallmp 3							// Enable()
      &pushtrue
      &pushone
      &pushsdbgv 4							//'AptApiClass'
      &pushsdbgm 2							//'debug'
      &dcallmp 3							// Enable()
      &push r:1      
      &pushsdb 5							//'m_apt'
      &push r:1      
      &pushsdbgv 1							//'OptionsClass'
      &pushsdbgm 6							//'m_classRoot'
      &pushbyte 2
      &pushsdb 4							//'AptApiClass'
      &new
      &setMember
      &push r:3      
      &pushsdbgm 7							//'InGame'
      &not
      &not
      &jnz label1      
      &pushsdb 8							//'1'
      &pushsdb 9							//'AllowAdvancedOptions'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
      &pushsdb 11							//'MainMenu'
      &pushsdb 12							//'EntryPoint'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
      &pushsdb 8							//'1'
      &pushsdb 13							//'AllowResolutionChange'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
      &pushsdb 8							//'1'
      &pushsdb 14							//'NetworkEnabled'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
      &pushsdb 8							//'1'
      &pushsdb 15							//'VoIPControlsEnabled'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
      &pushbyte 4
      &pushsdb 16							//'MasterOption0Num'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
      &pushsdb 17							//'Custom'
      &pushsdb 18							//'MasterOption0Current'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
      &pushbyte 2
      &pushsdb 19							//'MasterOption0ResetDefault'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
      &pushsdb 20							//'0,0,0,0,0,0,0,0,0,0'
      &pushsdb 21							//'MasterOption0Template0'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
      &pushsdb 22							//'2,2,2,2,2,2,2,2,2,2'
      &pushsdb 23							//'MasterOption0Template1'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
      &pushsdb 24							//'3,3,3,3,3,3,3,3,3,3'
      &pushsdb 25							//'MasterOption0Template2'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
      &pushsdb 26							//'4,4,4,4,4,4,4,4,4,4'
      &pushsdb 27							//'MasterOption0Template3'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
      &pushsdb 28							//'0,0,0,2,2,2,2,2,2,2'
      &pushsdb 29							//'MasterOption0TemplateCustom'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
      &pushbyte 2
      &pushsdb 30							//'AdvancedOption0Num'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
      &pushbyte 3
      &pushsdb 31							//'AdvancedOption1Num'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
      &pushbyte 7
      &pushsdb 32							//'AdvancedOption2Num'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
      &pushbyte 4
      &pushsdb 33							//'AdvancedOption3Num'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
      &pushbyte 3
      &pushsdb 34							//'AdvancedOption4Num'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
      &pushbyte 4
      &pushsdb 35							//'AdvancedOption5Num'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
      &pushbyte 5
      &pushsdb 36							//'AdvancedOption6Num'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
      &pushbyte 5
      &pushsdb 37							//'AdvancedOption7Num'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
      &pushbyte 5
      &pushsdb 38							//'AdvancedOption8Num'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
      &pushbyte 3
      &pushsdb 39							//'AdvancedOption9Num'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
      &pushsdb 40							//'VoiceActivated'
      &pushsdb 41							//'VoIPActivationMode'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
      &pushfloat 0.400000005960464
      &pushsdb 42							//'CurrentVoiceLevel'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
      &pushfloat 0.200000002980232
      &pushsdb 43							//'VoiceThreshold'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
     label1:
      &push r:1      
      &pushsdb 44							//'m_entryPoint'
      &pushsdb 12							//'EntryPoint'
      &pushone
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &pushsdb 45							//'GetExtern'
      &callMethod
      &setMember
      &push r:1      
      &pushsdb 46							//'m_inMpGame'
      &push r:1      
      &pushsdbgm 44							//'m_entryPoint'
      &pushsdb 47							//'Online'
      &equals
      &dup
      &jnz label2      
      &pop
      &push r:1      
      &pushsdbgm 44							//'m_entryPoint'
      &pushsdb 48							//'Network'
      &equals
     label2:
      &setMember
    &end // of function 

    &setRegister r:1
    &setMember
    &pushglobalgv
    &pushsdbgm 1							//'OptionsClass'
    &pushsdbgv 49							//'MovieClip'
    &extends
    &push r:1    
    &pushsdbgm 50							//'prototype'
    &setRegister r:2
    &pop
    &push r:2    
    &pushsdb 51							//'onUnload'
    &function2  () (r:1='this')
      &push r:1      
      &pushsdb 5							//'m_apt'
      &delete
      &pop
      &pushsdbgv 1							//'OptionsClass'
      &pushsdb 2							//'debug'
      &delete
      &pop
      &push r:1      
      &pushone
      &pushsdbgv 52							//'AptZombieClass'
      &dcallmp 53							// DeleteFunctions()
      &pushsdbgv 1							//'OptionsClass'
      &pushsdbgm 6							//'m_classRoot'
      &pushsdb 54							//'Class'
      &add
      &pushone
      &pushsdbgv 52							//'AptZombieClass'
      &dcallmp 55							// DeleteClass()
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 56							//'OnExitScreen'
    &function2  () (r:1='this')
      &pushsdb 57							//'m_exitVar >> '
      &push r:1      
      &pushsdbgm 58							//'m_exitVar'
      &add
      &trace
      &pushsdb 59							//''
      &push r:1      
      &pushsdbgm 58							//'m_exitVar'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 60							// Call()
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 61							//'OnDonePress'
    &function2  () (r:1='this', r:2='_root')
      &pushsdb 62							//'_close'
      &pushone
      &push r:2      
      &dcallmp 63							// gotoAndPlay()
      &push r:1      
      &pushsdb 58							//'m_exitVar'
      &pushsdb 64							//'Save'
      &setMember
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 65							//'OnCancelPress'
    &function2  () (r:1='this', r:2='_root')
      &pushsdb 62							//'_close'
      &pushone
      &push r:2      
      &dcallmp 63							// gotoAndPlay()
      &push r:1      
      &pushsdb 58							//'m_exitVar'
      &pushsdb 66							//'Cancel'
      &setMember
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 67							//'LoadCustomHotkeys'
    &function2  () (r:1='_root')
      &pushsdb 68							//'HotkeyScreen'
      &pushsdb 69							//'CustomHotkeys.swf'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 70							//'Options'
      &pushsdbgm 71							//'CustomHotkeyLoader'
      &dcallmp 72							// loadMovie()
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 73							//'SetCustomHotkeysVisibility'
    &function2  (r:2='vis') (r:1='_root')
      &push r:1      
      &pushsdbgm 70							//'Options'
      &pushsdbgm 71							//'CustomHotkeyLoader'
      &pushsdb 74							//'_visible'
      &push r:2      
      &setMember
      &push r:2      
      &not
      &jnz label3      
      &push r:1      
      &pushsdbgm 70							//'Options'
      &pushsdbgm 75							//'MainButtons'
      &pushsdbgm 76							//'Defaults'
      &pushsdb 74							//'_visible'
      &pushfalse
      &setMember
      &push r:1      
      &pushsdbgm 70							//'Options'
      &pushsdbgm 75							//'MainButtons'
      &pushsdbgm 77							//'DefaultsButtonFrame'
      &pushsdb 74							//'_visible'
      &pushfalse
      &setMember
      &jmp label4      
     label3:
      &push r:1      
      &pushsdbgm 70							//'Options'
      &pushsdbgm 75							//'MainButtons'
      &pushsdbgm 76							//'Defaults'
      &pushsdb 74							//'_visible'
      &pushtrue
      &setMember
      &push r:1      
      &pushsdbgm 70							//'Options'
      &pushsdbgm 75							//'MainButtons'
      &pushsdbgm 77							//'DefaultsButtonFrame'
      &pushsdb 74							//'_visible'
      &pushtrue
      &setMember
     label4:
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 78							//'RegisterTabChange'
    &function2  (r:2='currentTabName', r:3='currentTabClip') (r:1='this')
      &push r:1      
      &pushsdb 79							//'m_currentTabName'
      &push r:2      
      &setMember
      &push r:1      
      &pushsdb 80							//'m_currentTabClip'
      &push r:3      
      &setMember
      &push r:1      
      &pushsdbgm 81							//'m_isVoiceCalibrating'
      &not
      &jnz label5      
      &pushfalse
      &pushone
      &push r:1      
      &dcallmp 82							// OnVoiceCalibration()
     label5:
      &push r:1      
      &pushsdbgm 79							//'m_currentTabName'
      &pushsdb 83							//'CurrentTab'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 84							//'SetDefaultTabSettings'
    &function2  () (r:1='this')
      &pushsdb 85							//'SetDefault >> '
      &push r:1      
      &pushsdbgm 79							//'m_currentTabName'
      &add
      &trace
      &pushsdb 59							//''
      &pushsdb 86							//'Reset'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 60							// Call()
      &push r:1      
      &pushsdbgm 79							//'m_currentTabName'
      &pushsdb 87							//'Graphics'
      &equals
      &not
      &jnz label7      
      &push r:1      
      &pushsdbgm 44							//'m_entryPoint'
      &pushsdb 11							//'MainMenu'
      &equals
      &not
      &jnz label6      
      &pushsdb 19							//'MasterOption0ResetDefault'
      &pushone
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &pushsdb 45							//'GetExtern'
      &callMethod
      &pushsdb 18							//'MasterOption0Current'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
      &pushzero
      &push r:1      
      &pushsdbgm 80							//'m_currentTabClip'
      &pushsdbgm 88							//'ParentSlider1'
      &dcallmp 89							// SetDefaultOptions()
     label6:
      &jmp label8      
     label7:
      &push r:1      
      &pushsdbgm 79							//'m_currentTabName'
      &pushsdb 90							//'Audio'
      &equals
      &not
      &jnz label8      
      &pushzero
      &push r:1      
      &pushsdbgm 80							//'m_currentTabClip'
      &pushsdbgm 91							//'TalkModeRadioGroup'
      &dcallmp 92							// UpdateChoice()
      &pushzero
      &push r:1      
      &pushsdb 93							//'GetVoiceThreshold'
      &callMethod
      &pushone
      &push r:1      
      &pushsdbgm 80							//'m_currentTabClip'
      &pushsdbgm 94							//'ThresholdAdjuster'
      &dcallmp 95							// SetThreshold()
     label8:
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 82							//'OnVoiceCalibration'
    &function2  (r:2='currentlyCalibrating') (r:1='this')
      &push r:1      
      &pushsdb 81							//'m_isVoiceCalibrating'
      &push r:2      
      &setMember
      &push r:2      
      &jnz label9      
      &pushsdb 96							//'0'
      &jmp label10      
     label9:
      &pushsdb 8							//'1'
     label10:
      &pushsdb 82							//'OnVoiceCalibration'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 60							// Call()
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 97							//'SetVoiceThreshold'
    &function2  (r:2='threshold') (r:1='this')
      &push r:1      
      &pushsdb 98							//'m_voiceThreshold'
      &push r:2      
      &setMember
      &push r:1      
      &pushsdbgm 98							//'m_voiceThreshold'
      &pushsdb 43							//'VoiceThreshold'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 93							//'GetVoiceThreshold'
    &function2  () (r:1='this')
      &push r:1      
      &pushsdb 98							//'m_voiceThreshold'
      &pushsdb 43							//'VoiceThreshold'
      &pushone
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &pushsdb 45							//'GetExtern'
      &callMethod
      &setMember
      &push r:1      
      &pushsdbgm 98							//'m_voiceThreshold'
      &return
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 99							//'GetCurrentVoiceLevel'
    &function2  () (r:1='this', r:2='_global')
      &push r:2      
      &pushsdbgm 7							//'InGame'
      &not
      &jnz label11      
      &pushsdb 42							//'CurrentVoiceLevel'
      &pushone
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &pushsdb 45							//'GetExtern'
      &callMethod
      &return
      &jmp label12      
     label11:
      &pushzero
      &pushsdbgv 100							//'Math'
      &pushsdb 101							//'random'
      &callMethod
      &return
     label12:
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 102							//'SetVoIPActivationMode'
    &function2  (r:2='mode') (r:1='this')
      &push r:2      
      &pushsdb 41							//'VoIPActivationMode'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 103							//'GetVoIPActivationMode'
    &function2  () (r:1='this')
      &pushsdb 41							//'VoIPActivationMode'
      &pushone
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &pushsdb 45							//'GetExtern'
      &callMethod
      &return
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 104							//'AreVoIPControlsEnabled'
    &function2  () (r:1='this')
      &pushsdb 105							//'AreVoIPControlsEnabled: '
      &pushsdb 15							//'VoIPControlsEnabled'
      &pushone
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &pushsdb 45							//'GetExtern'
      &callMethod
      &pushsdb 96							//'0'
      &equals
      &not
      &add
      &trace
      &pushsdb 15							//'VoIPControlsEnabled'
      &pushone
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &pushsdb 45							//'GetExtern'
      &callMethod
      &pushsdb 96							//'0'
      &equals
      &not
      &return
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 106							//'IsNetworkEnabled'
    &function2  () (r:1='this')
      &pushsdb 14							//'NetworkEnabled'
      &pushone
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &pushsdb 45							//'GetExtern'
      &callMethod
      &pushsdb 96							//'0'
      &equals
      &not
      &return
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 107							//'OnRefreshNATPressed'
    &function2  () (r:1='this')
      &pushsdb 59							//''
      &pushsdb 108							//'RefreshNat'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 60							// Call()
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 109							//'IsInMpGame'
    &function2  () (r:1='this')
      &push r:1      
      &pushsdbgm 46							//'m_inMpGame'
      &return
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 110							//'IsInDemo'
    &function2  ('Void') (r:1='this')
      &pushfalse
      &pushone
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &pushsdb 111							//'IsCnc3Demo'
      &callMethod
      &return
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 112							//'IsSpectatorClient'
    &function2  ('Void') (r:1='this')
      &pushfalse
      &pushone
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &pushsdb 112							//'IsSpectatorClient'
      &callMethod
      &return
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 113							//'IsSpecialEdition'
    &function2  () (r:1='this')
      &pushzero
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &pushsdb 114							//'IsSpecialEditionExe'
      &callMethod
      &return
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 115							//'_RefreshEnableVoIPControls'
    &function2  ('Void') (r:1='this', r:2='_root')
      &pushsdb 116							//'RefreshEnableVoIPControls called'
      &trace
      &pushzero
      &push r:1      
      &pushsdb 104							//'AreVoIPControlsEnabled'
      &callMethod
      &setRegister r:3
      &pop
      &push r:3      
      &pushone
      &push r:2      
      &pushsdbgm 70							//'Options'
      &pushsdbgm 117							//'AudioOptions'
      &pushsdbgm 91							//'TalkModeRadioGroup'
      &dcallmp 3							// Enable()
      &push r:3      
      &pushone
      &push r:2      
      &pushsdbgm 70							//'Options'
      &pushsdbgm 117							//'AudioOptions'
      &dcallmp 118							// EnableCalibrateButton()
    &end // of function 

    &setMember
    &push r:1    
    &pushsdb 6							//'m_classRoot'
    &pushsdb 70							//'Options'
    &setMember
    &push r:1    
    &pushsdb 2							//'debug'
    &pushsdbgv 1							//'OptionsClass'
    &pushsdbgm 6							//'m_classRoot'
    &pushone
    &pushsdb 119							//'DebugClass'
    &new
    &setMember
    &push r:2    
    &pushsdb 98							//'m_voiceThreshold'
    &pushzero
    &setMember
    &push r:2    
    &pushsdb 81							//'m_isVoiceCalibrating'
    &pushfalse
    &setMember
    &push r:2    
    &pushsdb 44							//'m_entryPoint'
    &pushsdb 11							//'MainMenu'
    &setMember
    &push r:2    
    &pushsdb 46							//'m_inMpGame'
    &pushfalse
    &setMember
    &pushone
    &pushnull
    &pushglobalgv
    &pushsdbgm 1							//'OptionsClass'
    &pushsdbgm 50							//'prototype'
    &pushbyte 3
    &pushsdb 120							//'ASSetPropFlags'
    &callFunction
   label13:
    &pop
  &end // of initMovieClip 170

  &defineMovieClip 171 // total frames: 0
  &end // of defineMovieClip 171
  
  &exportAssets
    171 &as '__Packages.AptApiClass'
  &end // of exportAssets
  
  &initMovieClip 171
    &constants '_global', 'AptApiClass', 'm_codePrefix', 'Apt', '::', 'm_aptActive', 'InGame', '_target', 'RegisterScreen', 'Call', 'prototype', 'extern', 'Boolean', '__get__Active', 'AptCall ', '(', ')', 'debug', 'Trace', 'FSCommand:', 'CallAbs', 'CallAbs ', 'LoadVariables', 'Object', '_loadVariables', 'ConvertObjectMembers', 'LoadVariables:', 'Dump', ',', 'split', 'length', '=', 'Array', 'Number', 'ERROR: AptLoadVariables - Unable to convert : ', 'GetExtern', 'GetExtern(', ')=>', 'SetExtern', 'SetExtern(', 'ToggleExtern', 'PlaySound', 'FSCommand:PlaySound', 'IsCnc3Demo', 'Cnc3PcDemo', '0', 'IsSpecialEdition', '1', 'IsSpecialEditionExe', '============TESTING KANE', 'IsSpectatorClient', 'EnableEngineComponents', 'EnableEngineComponents:', 'FSCommand:EnableComponents', 'DisableEngineComponents', 'DisableEngineComponents:', 'FSCommand:DisableComponents', 'DoTrace', 'AptApiClass::', 'DebugClass', '', 'Active', 'addProperty', 'ASSetPropFlags'  
    &pushglobalgv
    &pushsdbgm 1							//'AptApiClass'
    &not
    &not
    &jnz label25    
    &pushglobalgv
    &pushsdb 1							//'AptApiClass'
    &function2  (r:3='className', r:2='screen') (r:1='this')
      &push r:1      
      &pushsdb 2							//'m_codePrefix'
      &pushsdb 3							//'Apt'
      &push r:3      
      &add
      &pushsdb 4							//'::'
      &add
      &setMember
      &pushsdbgv 1							//'AptApiClass'
      &pushsdb 5							//'m_aptActive'
      &pushzero
      &pushsdbgv 1							//'AptApiClass'
      &pushsdb 6							//'InGame'
      &callMethod
      &setMember
      &push r:2      
      &pushsdbgm 7							//'_target'
      &pushsdb 8							//'RegisterScreen'
      &pushbyte 2
      &push r:1      
      &dcallmp 9							// Call()
    &end // of function 

    &setRegister r:1
    &setMember
    &push r:1    
    &pushsdbgm 10							//'prototype'
    &setRegister r:2
    &pop
    &push r:1    
    &pushsdb 6							//'InGame'
    &function  ('Void'    )    
      &pushsdbgv 1							//'AptApiClass'
      &pushsdbgm 5							//'m_aptActive'
      &pushundef
      &equals
      &not
      &jnz label1      
      &pushsdbgv 1							//'AptApiClass'
      &pushsdb 5							//'m_aptActive'
      &pushsdbgv 1							//'AptApiClass'
      &pushsdbgm 11							//'extern'
      &pushsdbgm 6							//'InGame'
      &toNumber
      &pushone
      &pushsdb 12							//'Boolean'
      &callFunction
      &setMember
     label1:
      &pushsdbgv 1							//'AptApiClass'
      &pushsdbgm 5							//'m_aptActive'
      &return
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 13							//'__get__Active'
    &function  (    )    
      &pushsdbgv 1							//'AptApiClass'
      &pushsdbgm 5							//'m_aptActive'
      &return
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 9							//'Call'
    &function2  (r:2='func', r:3='params') (r:1='this')
      &pushsdb 14							//'AptCall '
      &push r:1      
      &pushsdbgm 2							//'m_codePrefix'
      &add
      &push r:2      
      &add
      &pushsdb 15							//'('
      &add
      &push r:3      
      &add
      &pushsdb 16							//')'
      &add
      &pushone
      &pushsdbgv 1							//'AptApiClass'
      &pushsdbgm 17							//'debug'
      &dcallmp 18							// Trace()
      &pushsdb 19							//'FSCommand:'
      &push r:1      
      &pushsdbgm 2							//'m_codePrefix'
      &push r:2      
      &add
      &concat
      &push r:3      
      &getURL2
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 20							//'CallAbs'
    &function2  (r:1='func', r:2='params') ()
      &pushsdb 16							//')'
      &push r:2      
      &pushsdb 21							//'CallAbs '
      &push r:1      
      &add
      &pushsdb 15							//'('
      &add
      &pushbyte 3
      &pushsdbgv 1							//'AptApiClass'
      &pushsdbgm 17							//'debug'
      &dcallmp 18							// Trace()
      &pushsdb 19							//'FSCommand:'
      &push r:1      
      &concat
      &push r:2      
      &getURL2
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 22							//'LoadVariables'
    &function2  (r:4='varName', r:2='obj', r:3='convertStr') (r:1='this')
      &pushsdbgv 1							//'AptApiClass'
      &pushsdbgm 5							//'m_aptActive'
      &not
      &jnz label2      
      &pushzero
      &pushsdb 23							//'Object'
      &new
      &setRegister r:2
      &pop
      &push r:2      
      &push r:1      
      &pushsdbgm 2							//'m_codePrefix'
      &push r:4      
      &add
      &pushbyte 2
      &pushsdbgv 1							//'AptApiClass'
      &dcallmp 24							// _loadVariables()
     label2:
      &push r:3      
      &pushundef
      &equals
      &not
      &not
      &jnz label3      
      &push r:3      
      &push r:2      
      &pushbyte 2
      &push r:1      
      &dcallmp 25							// ConvertObjectMembers()
     label3:
      &pushsdb 26							//'LoadVariables:'
      &push r:4      
      &add
      &push r:2      
      &pushbyte 2
      &pushsdbgv 1							//'AptApiClass'
      &pushsdbgm 17							//'debug'
      &dcallmp 27							// Dump()
      &push r:2      
      &return
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 25							//'ConvertObjectMembers'
    &function2  (r:3='obj', r:7='convertStr') ()
      &pushsdb 28							//','
      &pushone
      &push r:7      
      &pushsdb 29							//'split'
      &callMethod
      &setRegister r:5
      &pop
      &push r:5      
      &pushsdbgm 30							//'length'
      &setRegister r:6
      &pop
      &pushzero
      &setRegister r:2
      &pop
     label4:
      &push r:2      
      &push r:6      
      &lessThan
      &not
      &jnz label12      
      &pushsdb 31							//'='
      &pushone
      &push r:5      
      &push r:2      
      &getMember
      &pushsdb 29							//'split'
      &callMethod
      &setRegister r:4
      &pop
      &push r:4      
      &pushzero
      &getMember
      &setRegister r:1
      &pop
      &push r:4      
      &pushone
      &getMember
      &setRegister r:0
      &pushsdb 32							//'Array'
      &strictEquals
      &jnz label5      
      &push r:0      
      &pushsdb 12							//'Boolean'
      &strictEquals
      &jnz label6      
      &push r:0      
      &pushsdb 33							//'Number'
      &strictEquals
      &jnz label9      
      &jmp label10      
     label5:
      &push r:3      
      &push r:1      
      &pushsdb 28							//','
      &pushone
      &push r:3      
      &push r:1      
      &getMember
      &pushsdb 29							//'split'
      &callMethod
      &setMember
      &jmp label11      
     label6:
      &push r:3      
      &push r:1      
      &push r:3      
      &push r:1      
      &getMember
      &toNumber
      &jnz label7      
      &pushfalse
      &jmp label8      
     label7:
      &pushtrue
     label8:
      &setMember
      &jmp label11      
     label9:
      &push r:3      
      &push r:1      
      &push r:3      
      &push r:1      
      &getMember
      &toNumber
      &setMember
      &jmp label11      
     label10:
      &pushsdb 34							//'ERROR: AptLoadVariables - Unable to convert : '
      &push r:5      
      &push r:2      
      &getMember
      &add
      &trace
      &jmp label11      
     label11:
      &push r:2      
      &increment
      &setRegister r:2
      &pop
      &jmp label4      
     label12:
    &end // of function 

    &setMember
    &push r:1    
    &pushsdb 24							//'_loadVariables'
    &function2  (r:2='varName', r:1='obj') ()
      &push r:2      
      &push r:1      
      &loadVariables
      &push r:1      
      &return
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 35							//'GetExtern'
    &function2  (r:3='ext', r:4='testDefault') (r:1='this')
      &pushundef
      &setRegister r:2
      &pop
      &push r:1      
      &pushsdbgm 2							//'m_codePrefix'
      &push r:3      
      &add
      &setRegister r:3
      &pop
      &pushsdbgv 1							//'AptApiClass'
      &pushsdbgm 5							//'m_aptActive'
      &not
      &jnz label13      
      &pushsdbgv 1							//'AptApiClass'
      &pushsdbgm 11							//'extern'
      &push r:3      
      &getMember
      &setRegister r:2
      &pop
      &jmp label16      
     label13:
      &pushsdbgv 1							//'AptApiClass'
      &pushsdbgm 11							//'extern'
      &push r:3      
      &getMember
      &pushundef
      &equals
      &not
      &jnz label14      
      &push r:4      
      &setRegister r:2
      &pop
      &jmp label15      
     label14:
      &pushsdbgv 1							//'AptApiClass'
      &pushsdbgm 11							//'extern'
      &push r:3      
      &getMember
      &setRegister r:2
      &pop
     label15:
      &pushsdb 36							//'GetExtern('
      &push r:3      
      &add
      &pushsdb 37							//')=>'
      &add
      &push r:2      
      &add
      &pushone
      &pushsdbgv 1							//'AptApiClass'
      &pushsdbgm 17							//'debug'
      &dcallmp 18							// Trace()
     label16:
      &push r:2      
      &return
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 38							//'SetExtern'
    &function2  (r:2='ext', r:3='to') (r:1='this')
      &push r:1      
      &pushsdbgm 2							//'m_codePrefix'
      &push r:2      
      &add
      &setRegister r:2
      &pop
      &pushsdbgv 1							//'AptApiClass'
      &pushsdbgm 11							//'extern'
      &push r:2      
      &push r:3      
      &setMember
      &pushsdb 39							//'SetExtern('
      &push r:2      
      &add
      &pushsdb 37							//')=>'
      &add
      &push r:3      
      &add
      &pushone
      &pushsdbgv 1							//'AptApiClass'
      &pushsdbgm 17							//'debug'
      &dcallmp 18							// Trace()
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 40							//'ToggleExtern'
    &function2  (r:3='ext') (r:1='this')
      &push r:1      
      &pushsdbgm 2							//'m_codePrefix'
      &push r:3      
      &add
      &setRegister r:3
      &pop
      &pushsdbgv 1							//'AptApiClass'
      &pushsdbgm 11							//'extern'
      &push r:3      
      &getMember
      &toNumber
      &not
      &setRegister r:2
      &pop
      &pushsdbgv 1							//'AptApiClass'
      &pushsdbgm 11							//'extern'
      &push r:3      
      &push r:2      
      &setMember
      &push r:2      
      &return
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 41							//'PlaySound'
    &function2  (r:1='name') ()
      &pushsdb 42							//'FSCommand:PlaySound'
      &push r:1      
      &getURL2
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 43							//'IsCnc3Demo'
    &function2  (r:1='testDefault') ()
      &pushzero
      &pushsdbgv 1							//'AptApiClass'
      &pushsdb 6							//'InGame'
      &callMethod
      &jnz label17      
      &push r:1      
      &jmp label18      
     label17:
      &pushsdbgv 1							//'AptApiClass'
      &pushsdbgm 11							//'extern'
      &pushsdbgm 44							//'Cnc3PcDemo'
      &pushsdb 45							//'0'
      &equals
      &not
     label18:
      &return
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 46							//'IsSpecialEdition'
    &function2  (r:1='testDefault') ()
      &pushzero
      &pushsdbgv 1							//'AptApiClass'
      &pushsdb 6							//'InGame'
      &callMethod
      &jnz label19      
      &push r:1      
      &jmp label20      
     label19:
      &pushsdbgv 1							//'AptApiClass'
      &pushsdbgm 11							//'extern'
      &pushsdbgm 46							//'IsSpecialEdition'
      &pushsdb 47							//'1'
      &equals
     label20:
      &return
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 48							//'IsSpecialEditionExe'
    &function2  (r:1='testDefault') ()
      &pushsdb 49							//'============TESTING KANE'
      &trace
      &pushzero
      &pushsdbgv 1							//'AptApiClass'
      &pushsdb 6							//'InGame'
      &callMethod
      &jnz label21      
      &push r:1      
      &jmp label22      
     label21:
      &pushsdbgv 1							//'AptApiClass'
      &pushsdbgm 11							//'extern'
      &pushsdbgm 48							//'IsSpecialEditionExe'
      &pushsdb 47							//'1'
      &equals
     label22:
      &return
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 50							//'IsSpectatorClient'
    &function2  (r:1='testDefault') ()
      &pushzero
      &pushsdbgv 1							//'AptApiClass'
      &pushsdb 6							//'InGame'
      &callMethod
      &jnz label23      
      &push r:1      
      &jmp label24      
     label23:
      &pushsdbgv 1							//'AptApiClass'
      &pushsdbgm 11							//'extern'
      &pushsdbgm 50							//'IsSpectatorClient'
      &pushsdb 45							//'0'
      &equals
      &not
     label24:
      &return
    &end // of function 

    &setMember
    &push r:1    
    &pushsdb 51							//'EnableEngineComponents'
    &function2  (r:1='path') ()
      &pushsdb 52							//'EnableEngineComponents:'
      &push r:1      
      &add
      &pushone
      &pushsdbgv 1							//'AptApiClass'
      &pushsdbgm 17							//'debug'
      &dcallmp 18							// Trace()
      &pushsdb 53							//'FSCommand:EnableComponents'
      &push r:1      
      &getURL2
    &end // of function 

    &setMember
    &push r:1    
    &pushsdb 54							//'DisableEngineComponents'
    &function2  (r:1='path') ()
      &pushsdb 55							//'DisableEngineComponents:'
      &push r:1      
      &add
      &pushone
      &pushsdbgv 1							//'AptApiClass'
      &pushsdbgm 17							//'debug'
      &dcallmp 18							// Trace()
      &pushsdb 56							//'FSCommand:DisableComponents'
      &push r:1      
      &getURL2
    &end // of function 

    &setMember
    &push r:1    
    &pushsdb 11							//'extern'
    &pushsdb 57							//'DoTrace'
    &pushzero
    &pushsdb 6							//'InGame'
    &pushzero
    &pushsdb 44							//'Cnc3PcDemo'
    &pushzero
    &pushbyte 3
    &initObject
    &setMember
    &push r:1    
    &pushsdb 17							//'debug'
    &pushsdb 58							//'AptApiClass::'
    &pushone
    &pushsdb 59							//'DebugClass'
    &new
    &setMember
    &push r:1    
    &pushsdb 5							//'m_aptActive'
    &pushundef
    &setMember
    &push r:2    
    &pushsdb 2							//'m_codePrefix'
    &pushsdb 60							//''
    &setMember
    &function  (    )    
    &end // of function 

    &push r:2    
    &pushsdbgm 13							//'__get__Active'
    &pushsdb 61							//'Active'
    &pushbyte 3
    &push r:2    
    &pushsdb 62							//'addProperty'
    &callMethod
    &pushone
    &pushnull
    &pushglobalgv
    &pushsdbgm 1							//'AptApiClass'
    &pushsdbgm 10							//'prototype'
    &pushbyte 3
    &pushsdb 63							//'ASSetPropFlags'
    &callFunction
   label25:
    &pop
  &end // of initMovieClip 171

  &defineMovieClip 172 // total frames: 0
  &end // of defineMovieClip 172
  
  &exportAssets
    172 &as '__Packages.AptZombieClass'
  &end // of exportAssets
  
  &initMovieClip 172
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

    &setRegister r:1
    &setMember
    &pushglobalgv
    &pushsdbgm 1							//'AptZombieClass'
    &pushsdbgv 3							//'MovieClip'
    &extends
    &push r:1    
    &pushsdbgm 4							//'prototype'
    &setRegister r:2
    &pop
    &push r:1    
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
    &push r:1    
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
    &push r:1    
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
    &push r:1    
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
    &push r:2    
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
    &push r:1    
    &pushsdb 6							//'s_classes'
    &pushzero
    &pushsdb 26							//'Array'
    &new
    &setMember
    &push r:1    
    &pushsdb 14							//'s_objects'
    &pushzero
    &pushsdb 26							//'Array'
    &new
    &setMember
    &push r:1    
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
  &end // of initMovieClip 172

  &defineMovieClip 173 // total frames: 0
  &end // of defineMovieClip 173
  
  &exportAssets
    173 &as '__Packages.ButtonClass'
  &end // of exportAssets
  
  &initMovieClip 173
    &constants '_global', 'ButtonClass', 'm_text', '$', '_name', 'movieclip', '_visible', 'Show', 'gotoAndPlay', 'Text', 'indexOf', 'State', 'Trans', 'Bttn', 'onPress', '_parent', 'Press', 'onRelease', 'Release', 'onRollOver', 'RollOver', 'onRollOut', 'RollOut', 'onDragOut', 'DragOut', 'onDragOver', 'DragOver', 'WARNING:ButtonClass:', '_target', '/', ' is an unknown movie clip!', 'MovieClip', 'prototype', 'SetText', 'SetSfxClick', 'm_sfxClick', 'SetSfxRollOver', 'm_sfxRollOver', 'SetSfxRollOut', 'm_sfxRollOut', 'SetMode', 'm_mode', 'm_state', 'UpState', 'ChangeState', 'ClearMode', '', 'GetMode', 'onUnload', 'AptZombieClass', 'DeleteFunctions', 'Button::ChangeState(', '):(', ')', '->', ' (', 'm_curStateMc', ':', 'm_curBttnMc', 'm_curTextMc', ')->(', 'm_nextState', 'GetText', 'SwitchObject', 'GetBttn', 'GetStateClip', 'StartTransition', 'EndTransition', 'stop', 'GetObject', 'PressCallback', 'DownState', 'FSCommand:PlaySound', 'ReleaseCallback', 'ReleaseTrans', 'OverState', 'RollOverCallback', 'RollOutCallback', 'RollOutTrans', 'DragOutCallback', 'OutState', 'DragOverCallback', 'debug', 'ButtonClass::', 'DebugClass', '$ClickButton', '$OverButton', '$OutButton', 'ASSetPropFlags'  
    &pushglobalgv
    &pushsdbgm 1							//'ButtonClass'
    &not
    &not
    &jnz label24    
    &pushglobalgv
    &pushsdb 1							//'ButtonClass'
    &function2  () (r:1='this', r:2='super')
      &pushzero
      &push r:2      
      &pushundef
      &callmp
      &push r:1      
      &pushsdb 2							//'m_text'
      &pushsdb 3							//'$'
      &push r:1      
      &pushsdbgm 4							//'_name'
      &add
      &setMember
      &push r:1      
      &enumerateValue
     label1:
      &setRegister r:0
      &pushnull
      &equals
      &jnz label8      
      &push r:0      
      &setRegister r:5
      &pop
      &push r:1      
      &push r:5      
      &getMember
      &pushundef
      &equals
      &not
      &not
      &jnz label7      
      &push r:1      
      &push r:5      
      &getMember
      &setRegister r:3
      &pop
      &push r:3      
      &typeof
      &pushsdb 5							//'movieclip'
      &equals
      &setRegister r:4
      &pop
      &push r:3      
      &pushsdb 6							//'_visible'
      &pushfalse
      &setMember
      &push r:4      
      &not
      &jnz label2      
      &push r:3      
      &pushsdbgm 7							//'Show'
      &pushundef
      &equals
      &not
      &jnz label2      
      &push r:3      
      &pushsdb 7							//'Show'
      &function2  ('previous') (r:1='this')
        &pushone
        &pushone
        &push r:1        
        &dcallmp 8							// gotoAndPlay()
      &end // of function 

      &setMember
     label2:
      &pushsdb 9							//'Text'
      &pushone
      &push r:5      
      &pushsdb 10							//'indexOf'
      &callMethod
      &pushzero
      &lessThan
      &not
      &not
      &jnz label3      
      &jmp label7      
     label3:
      &pushsdb 11							//'State'
      &pushone
      &push r:5      
      &pushsdb 10							//'indexOf'
      &callMethod
      &pushzero
      &lessThan
      &not
      &dup
      &jnz label4      
      &pop
      &pushsdb 12							//'Trans'
      &pushone
      &push r:5      
      &pushsdb 10							//'indexOf'
      &callMethod
      &pushzero
      &lessThan
      &not
     label4:
      &not
      &jnz label5      
      &jmp label7      
     label5:
      &pushsdb 13							//'Bttn'
      &pushone
      &push r:5      
      &pushsdb 10							//'indexOf'
      &callMethod
      &pushzero
      &lessThan
      &not
      &not
      &jnz label6      
      &push r:3      
      &pushsdb 14							//'onPress'
      &function2  () (r:1='this')
        &pushzero
        &push r:1        
        &pushsdbgm 15							//'_parent'
        &dcallmp 16							// Press()
      &end // of function 

      &setMember
      &push r:3      
      &pushsdb 17							//'onRelease'
      &function2  () (r:1='this')
        &pushzero
        &push r:1        
        &pushsdbgm 15							//'_parent'
        &dcallmp 18							// Release()
      &end // of function 

      &setMember
      &push r:3      
      &pushsdb 19							//'onRollOver'
      &function2  () (r:1='this')
        &pushzero
        &push r:1        
        &pushsdbgm 15							//'_parent'
        &dcallmp 20							// RollOver()
      &end // of function 

      &setMember
      &push r:3      
      &pushsdb 21							//'onRollOut'
      &function2  () (r:1='this')
        &pushzero
        &push r:1        
        &pushsdbgm 15							//'_parent'
        &dcallmp 22							// RollOut()
      &end // of function 

      &setMember
      &push r:3      
      &pushsdb 23							//'onDragOut'
      &function2  () (r:1='this')
        &pushzero
        &push r:1        
        &pushsdbgm 15							//'_parent'
        &dcallmp 24							// DragOut()
      &end // of function 

      &setMember
      &push r:3      
      &pushsdb 25							//'onDragOver'
      &function2  () (r:1='this')
        &pushzero
        &push r:1        
        &pushsdbgm 15							//'_parent'
        &dcallmp 26							// DragOver()
      &end // of function 

      &setMember
      &jmp label7      
     label6:
      &push r:4      
      &not
      &jnz label7      
      &pushsdb 27							//'WARNING:ButtonClass:'
      &push r:1      
      &pushsdbgm 28							//'_target'
      &add
      &pushsdb 29							//'/'
      &add
      &push r:5      
      &add
      &pushsdb 30							//' is an unknown movie clip!'
      &add
      &trace
      &push r:3      
      &pushsdb 6							//'_visible'
      &pushtrue
      &setMember
     label7:
      &jmp label1      
     label8:
    &end // of function 

    &setRegister r:1
    &setMember
    &pushglobalgv
    &pushsdbgm 1							//'ButtonClass'
    &pushsdbgv 31							//'MovieClip'
    &extends
    &push r:1    
    &pushsdbgm 32							//'prototype'
    &setRegister r:2
    &pop
    &push r:2    
    &pushsdb 33							//'SetText'
    &function2  (r:2='textString') (r:1='this')
      &push r:1      
      &pushsdb 2							//'m_text'
      &push r:2      
      &setMember
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 34							//'SetSfxClick'
    &function2  (r:2='sfx') (r:1='this')
      &push r:1      
      &pushsdb 35							//'m_sfxClick'
      &push r:2      
      &setMember
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 36							//'SetSfxRollOver'
    &function2  (r:2='sfx') (r:1='this')
      &push r:1      
      &pushsdb 37							//'m_sfxRollOver'
      &push r:2      
      &setMember
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 38							//'SetSfxRollOut'
    &function2  (r:2='sfx') (r:1='this')
      &push r:1      
      &pushsdb 39							//'m_sfxRollOut'
      &push r:2      
      &setMember
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 40							//'SetMode'
    &function2  (r:2='mode') (r:1='this')
      &push r:1      
      &pushsdb 41							//'m_mode'
      &push r:2      
      &setMember
      &push r:1      
      &pushsdbgm 42							//'m_state'
      &pushundef
      &equals
      &not
      &jnz label9      
      &push r:1      
      &pushsdb 42							//'m_state'
      &pushsdb 43							//'UpState'
      &setMember
     label9:
      &push r:1      
      &pushsdbgm 42							//'m_state'
      &pushone
      &push r:1      
      &dcallmp 44							// ChangeState()
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 45							//'ClearMode'
    &function2  ('Void') (r:1='this')
      &pushsdb 46							//''
      &pushone
      &push r:1      
      &dcallmp 40							// SetMode()
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 47							//'GetMode'
    &function2  ('Void') (r:1='this')
      &push r:1      
      &pushsdbgm 41							//'m_mode'
      &return
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 48							//'onUnload'
    &function2  () (r:1='this')
      &push r:1      
      &pushone
      &pushsdbgv 49							//'AptZombieClass'
      &dcallmp 50							// DeleteFunctions()
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 44							//'ChangeState'
    &function2  (r:2='stateStr') (r:1='this')
      &pushsdb 51							//'Button::ChangeState('
      &push r:1      
      &pushsdbgm 4							//'_name'
      &add
      &pushsdb 52							//'):('
      &add
      &push r:1      
      &pushsdbgm 41							//'m_mode'
      &add
      &pushsdb 53							//')'
      &add
      &push r:1      
      &pushsdbgm 42							//'m_state'
      &add
      &pushsdb 54							//'->'
      &add
      &push r:2      
      &add
      &pushsdb 55							//' ('
      &add
      &push r:1      
      &pushsdbgm 56							//'m_curStateMc'
      &pushsdbgm 4							//'_name'
      &add
      &pushsdb 57							//':'
      &add
      &push r:1      
      &pushsdbgm 58							//'m_curBttnMc'
      &pushsdbgm 4							//'_name'
      &add
      &pushsdb 57							//':'
      &add
      &push r:1      
      &pushsdbgm 59							//'m_curTextMc'
      &pushsdbgm 4							//'_name'
      &add
      &pushsdb 60							//')->('
      &add
      &setRegister r:3
      &pop
      &push r:1      
      &pushsdb 42							//'m_state'
      &push r:2      
      &setMember
      &push r:1      
      &pushsdb 61							//'m_nextState'
      &pushundef
      &setMember
      &push r:1      
      &pushsdb 59							//'m_curTextMc'
      &push r:2      
      &pushone
      &push r:1      
      &pushsdb 62							//'GetText'
      &callMethod
      &push r:1      
      &pushsdbgm 59							//'m_curTextMc'
      &pushbyte 2
      &push r:1      
      &pushsdb 63							//'SwitchObject'
      &callMethod
      &setMember
      &push r:1      
      &pushsdb 58							//'m_curBttnMc'
      &push r:2      
      &pushone
      &push r:1      
      &pushsdb 64							//'GetBttn'
      &callMethod
      &push r:1      
      &pushsdbgm 58							//'m_curBttnMc'
      &pushbyte 2
      &push r:1      
      &pushsdb 63							//'SwitchObject'
      &callMethod
      &setMember
      &push r:1      
      &pushsdb 56							//'m_curStateMc'
      &push r:2      
      &pushone
      &push r:1      
      &pushsdb 65							//'GetStateClip'
      &callMethod
      &push r:1      
      &pushsdbgm 56							//'m_curStateMc'
      &pushbyte 2
      &push r:1      
      &pushsdb 63							//'SwitchObject'
      &callMethod
      &setMember
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 66							//'StartTransition'
    &function2  (r:3='transition', r:4='nextState') (r:1='this')
      &push r:3      
      &pushone
      &push r:1      
      &pushsdb 65							//'GetStateClip'
      &callMethod
      &setRegister r:2
      &pop
      &push r:2      
      &pushundef
      &equals
      &not
      &not
      &jnz label10      
      &push r:1      
      &pushsdb 42							//'m_state'
      &push r:3      
      &setMember
      &push r:1      
      &pushsdb 61							//'m_nextState'
      &push r:4      
      &setMember
      &push r:1      
      &pushsdbgm 58							//'m_curBttnMc'
      &pushsdb 6							//'_visible'
      &pushfalse
      &setMember
      &push r:1      
      &pushsdb 58							//'m_curBttnMc'
      &pushundef
      &setMember
      &push r:1      
      &pushsdb 59							//'m_curTextMc'
      &push r:3      
      &pushone
      &push r:1      
      &pushsdb 62							//'GetText'
      &callMethod
      &push r:1      
      &pushsdbgm 59							//'m_curTextMc'
      &pushbyte 2
      &push r:1      
      &pushsdb 63							//'SwitchObject'
      &callMethod
      &setMember
      &push r:1      
      &pushsdb 56							//'m_curStateMc'
      &push r:2      
      &push r:1      
      &pushsdbgm 56							//'m_curStateMc'
      &pushbyte 2
      &push r:1      
      &pushsdb 63							//'SwitchObject'
      &callMethod
      &setMember
      &pushtrue
      &return
     label10:
      &pushfalse
      &return
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 67							//'EndTransition'
    &function2  (r:2='transition') (r:1='this')
      &push r:2      
      &push r:1      
      &pushsdbgm 56							//'m_curStateMc'
      &equals
      &dup
      &not
      &jnz label11      
      &pop
      &push r:1      
      &pushsdbgm 61							//'m_nextState'
      &pushundef
      &equals
      &not
     label11:
      &not
      &jnz label12      
      &push r:1      
      &pushsdbgm 61							//'m_nextState'
      &pushone
      &push r:1      
      &dcallmp 44							// ChangeState()
     label12:
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 63							//'SwitchObject'
    &function2  (r:1='current', r:3='next') ()
      &push r:3      
      &pushundef
      &equals
      &not
      &not
      &jnz label14      
      &push r:1      
      &setRegister r:2
      &pop
      &push r:3      
      &typeof
      &pushsdb 5							//'movieclip'
      &equals
      &setRegister r:4
      &pop
      &push r:1      
      &not
      &jnz label13      
      &push r:1      
      &pushsdb 6							//'_visible'
      &pushfalse
      &setMember
      &pushzero
      &push r:1      
      &dcallmp 68							// stop()
     label13:
      &push r:3      
      &setRegister r:1
      &pop
      &push r:1      
      &pushsdb 6							//'_visible'
      &pushtrue
      &setMember
      &push r:2      
      &pushone
      &push r:1      
      &dcallmp 7							// Show()
     label14:
      &push r:1      
      &return
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 65							//'GetStateClip'
    &function2  (r:3='stateStr') (r:1='this')
      &push r:1      
      &push r:1      
      &pushsdbgm 41							//'m_mode'
      &push r:3      
      &add
      &getMember
      &setRegister r:2
      &pop
      &push r:2      
      &pushundef
      &equals
      &not
      &jnz label15      
      &push r:1      
      &push r:3      
      &getMember
      &setRegister r:2
      &pop
     label15:
      &push r:2      
      &return
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 62							//'GetText'
    &function2  (r:3='stateStr') (r:1='this')
      &pushsdb 9							//'Text'
      &push r:3      
      &pushbyte 2
      &push r:1      
      &pushsdb 69							//'GetObject'
      &callMethod
      &setRegister r:2
      &pop
      &push r:2      
      &return
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 64							//'GetBttn'
    &function2  (r:3='stateStr') (r:1='this')
      &pushsdb 13							//'Bttn'
      &push r:3      
      &pushbyte 2
      &push r:1      
      &pushsdb 69							//'GetObject'
      &callMethod
      &setRegister r:2
      &pop
      &push r:2      
      &return
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 69							//'GetObject'
    &function2  (r:4='stateStr', r:3='postfix') (r:1='this')
      &push r:1      
      &push r:1      
      &pushsdbgm 41							//'m_mode'
      &push r:4      
      &add
      &push r:3      
      &add
      &getMember
      &setRegister r:2
      &pop
      &push r:2      
      &pushundef
      &equals
      &not
      &jnz label16      
      &push r:1      
      &push r:1      
      &pushsdbgm 41							//'m_mode'
      &push r:3      
      &add
      &getMember
      &setRegister r:2
      &pop
      &push r:2      
      &pushundef
      &equals
      &not
      &jnz label16      
      &push r:1      
      &push r:4      
      &push r:3      
      &add
      &getMember
      &setRegister r:2
      &pop
      &push r:2      
      &pushundef
      &equals
      &not
      &jnz label16      
      &push r:1      
      &push r:3      
      &getMember
      &setRegister r:2
      &pop
     label16:
      &push r:2      
      &return
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 16							//'Press'
    &function2  ('Void') (r:1='this')
      &push r:1      
      &pushsdbgm 13							//'Bttn'
      &pushsdbgm 6							//'_visible'
      &not
      &jnz label17      
      &pushzero
      &push r:1      
      &dcallmp 70							// PressCallback()
      &pushsdb 71							//'DownState'
      &pushone
      &push r:1      
      &dcallmp 44							// ChangeState()
      &pushsdb 72							//'FSCommand:PlaySound'
      &push r:1      
      &pushsdbgm 35							//'m_sfxClick'
      &getURL2
     label17:
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 18							//'Release'
    &function2  ('Void') (r:1='this')
      &push r:1      
      &pushsdbgm 13							//'Bttn'
      &pushsdbgm 6							//'_visible'
      &not
      &jnz label18      
      &pushzero
      &push r:1      
      &dcallmp 73							// ReleaseCallback()
      &pushsdb 43							//'UpState'
      &pushsdb 74							//'ReleaseTrans'
      &pushbyte 2
      &push r:1      
      &pushsdb 66							//'StartTransition'
      &callMethod
      &not
      &not
      &jnz label18      
      &pushsdb 75							//'OverState'
      &pushone
      &push r:1      
      &dcallmp 44							// ChangeState()
     label18:
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 20							//'RollOver'
    &function2  ('Void') (r:1='this')
      &push r:1      
      &pushsdbgm 13							//'Bttn'
      &pushsdbgm 6							//'_visible'
      &not
      &jnz label19      
      &pushzero
      &push r:1      
      &dcallmp 76							// RollOverCallback()
      &pushsdb 75							//'OverState'
      &pushone
      &push r:1      
      &dcallmp 44							// ChangeState()
      &pushsdb 72							//'FSCommand:PlaySound'
      &push r:1      
      &pushsdbgm 37							//'m_sfxRollOver'
      &getURL2
     label19:
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 22							//'RollOut'
    &function2  ('Void') (r:1='this')
      &push r:1      
      &pushsdbgm 13							//'Bttn'
      &pushsdbgm 6							//'_visible'
      &not
      &jnz label21      
      &pushzero
      &push r:1      
      &dcallmp 77							// RollOutCallback()
      &pushsdb 43							//'UpState'
      &pushsdb 78							//'RollOutTrans'
      &pushbyte 2
      &push r:1      
      &pushsdb 66							//'StartTransition'
      &callMethod
      &not
      &not
      &jnz label20      
      &pushsdb 43							//'UpState'
      &pushone
      &push r:1      
      &dcallmp 44							// ChangeState()
     label20:
      &pushsdb 72							//'FSCommand:PlaySound'
      &push r:1      
      &pushsdbgm 39							//'m_sfxRollOut'
      &getURL2
     label21:
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 24							//'DragOut'
    &function2  ('Void') (r:1='this')
      &push r:1      
      &pushsdbgm 13							//'Bttn'
      &pushsdbgm 6							//'_visible'
      &not
      &jnz label22      
      &pushzero
      &push r:1      
      &dcallmp 79							// DragOutCallback()
      &pushsdb 43							//'UpState'
      &pushone
      &push r:1      
      &dcallmp 44							// ChangeState()
      &pushsdb 80							//'OutState'
      &pushone
      &push r:1      
      &dcallmp 44							// ChangeState()
     label22:
    &end // of function 

    &setMember
    &push r:2    
    &pushsdb 26							//'DragOver'
    &function2  ('Void') (r:1='this')
      &push r:1      
      &pushsdbgm 13							//'Bttn'
      &pushsdbgm 6							//'_visible'
      &not
      &jnz label23      
      &pushzero
      &push r:1      
      &dcallmp 81							// DragOverCallback()
      &pushsdb 71							//'DownState'
      &pushone
      &push r:1      
      &dcallmp 44							// ChangeState()
     label23:
    &end // of function 

    &setMember
    &push r:1    
    &pushsdb 82							//'debug'
    &pushsdb 83							//'ButtonClass::'
    &pushone
    &pushsdb 84							//'DebugClass'
    &new
    &setMember
    &push r:2    
    &pushsdb 42							//'m_state'
    &pushundef
    &setMember
    &push r:2    
    &pushsdb 41							//'m_mode'
    &pushundef
    &setMember
    &push r:2    
    &pushsdb 61							//'m_nextState'
    &pushundef
    &setMember
    &push r:2    
    &pushsdb 56							//'m_curStateMc'
    &pushundef
    &setMember
    &push r:2    
    &pushsdb 59							//'m_curTextMc'
    &pushundef
    &setMember
    &push r:2    
    &pushsdb 58							//'m_curBttnMc'
    &pushundef
    &setMember
    &push r:2    
    &pushsdb 35							//'m_sfxClick'
    &pushsdb 85							//'$ClickButton'
    &setMember
    &push r:2    
    &pushsdb 37							//'m_sfxRollOver'
    &pushsdb 86							//'$OverButton'
    &setMember
    &push r:2    
    &pushsdb 39							//'m_sfxRollOut'
    &pushsdb 87							//'$OutButton'
    &setMember
    &pushone
    &pushnull
    &pushglobalgv
    &pushsdbgm 1							//'ButtonClass'
    &pushsdbgm 32							//'prototype'
    &pushbyte 3
    &pushsdb 88							//'ASSetPropFlags'
    &callFunction
   label24:
    &pop
  &end // of initMovieClip 173
  
  &initMovieClip 167
    &constants 'OptionsClass', 'Object', 'registerClass'  
    &pushsdbgv 0							//'OptionsClass'
    &pushsdb 0							//'OptionsClass'
    &pushbyte 2
    &pushsdbgv 1							//'Object'
    &dcallmp 2							// registerClass()
  &end // of initMovieClip 167
  
  &initMovieClip 23
    &pushsgv 'ButtonClass'
    &pushs 'ShellButtonShort1'
    &pushbyte 2
    &pushsgv 'Object'
    &pushs 'registerClass'
    &callmp
  &end // of initMovieClip 23
  
  &exportAssets
    167 &as 'OptionsClass'
  &end // of exportAssets
  
  &exportAssets
    167 &as 'OptionsClass'
  &end // of exportAssets

  &frame 3
    &stop
  &end // of frame 3
  
  &exportAssets
    167 &as 'OptionsClass'
  &end // of exportAssets
  
  &exportAssets
    167 &as 'OptionsClass'
  &end // of exportAssets
  
  &exportAssets
    167 &as 'OptionsClass'
  &end // of exportAssets
  
  &exportAssets
    167 &as 'OptionsClass'
  &end // of exportAssets
  
  &exportAssets
    167 &as 'OptionsClass'
  &end // of exportAssets
  
  &exportAssets
    167 &as 'OptionsClass'
  &end // of exportAssets
  
  &exportAssets
    167 &as 'OptionsClass'
  &end // of exportAssets
  
  &exportAssets
    167 &as 'OptionsClass'
  &end // of exportAssets
  
  &exportAssets
    167 &as 'OptionsClass'
  &end // of exportAssets
  
  &exportAssets
    167 &as 'OptionsClass'
  &end // of exportAssets
  
  &exportAssets
    167 &as 'OptionsClass'
  &end // of exportAssets

  &frame 14
    &pushzero
    &pushsgv '_root'
    &pushsgm 'Options'
    &pushs 'OnExitScreen'
    &callmp
    &stop
  &end // of frame 14
  
  &exportAssets
    167 &as 'OptionsClass'
  &end // of exportAssets
&end
