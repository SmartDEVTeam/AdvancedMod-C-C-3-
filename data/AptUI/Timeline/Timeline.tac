movie 'E:\Projects\CNC3\Data\APTBUI~1\034A3~1.0-D\pc\Output\Timeline\\Timeline.eaf' &compressed // flash 7, total frames: 18, frame rate: 30 fps, 1024x768 px

  &defineMovieClip 3 // total frames: 1
  &end // of defineMovieClip 3

  &defineMovieClip 4 // total frames: 18

    &frame 0
      &stop
    &end // of frame 0

    &frame 8
      &stop
    &end // of frame 8

    &frame 9
      &play
    &end // of frame 9

    &frame 17
      &stop
    &end // of frame 17
  &end // of defineMovieClip 4
  
  &exportAssets
    4 &as 'Dot'
  &end // of exportAssets

  &defineMovieClip 5 // total frames: 1
  &end // of defineMovieClip 5

  &defineMovieClip 10 // total frames: 65

    &frame 0
      &stop
    &end // of frame 0
  &end // of defineMovieClip 10
  
  &exportAssets
    10 &as 'EventIcon'
  &end // of exportAssets

  &defineMovieClip 13 // total frames: 1
  &end // of defineMovieClip 13

  &defineMovieClip 14 // total frames: 10

    &frame 9
      &pushzero
      &pushthisgv
      &pushs 'unloadMovie'
      &callmp
    &end // of frame 9
  &end // of defineMovieClip 14
  
  &exportAssets
    14 &as 'PlayerCarrotReleaseAnimation'
  &end // of exportAssets

  &defineMovieClip 15 // total frames: 2

    &frame 0
      &constants 'AptTimeLine::GraphFocus:', '_parent', '_name', 'substr', ' = ', 'this', '_alpha', ' currentframe = ', '_currentframe', '_root', 'SetExtern'  
      &pushsdb 0							//'AptTimeLine::GraphFocus:'
      &pushbyte 6
      &pushone
      &pushsdbgv 1							//'_parent'
      &pushsdbgm 1							//'_parent'
      &pushsdbgm 2							//'_name'
      &pushsdb 3							//'substr'
      &callMethod
      &add
      &pushsdb 4							//' = '
      &add
      &pushthisgv
      &pushsdbgm 6							//'_alpha'
      &add
      &pushsdb 7							//' currentframe = '
      &add
      &pushsdbgv 1							//'_parent'
      &pushsdbgm 8							//'_currentframe'
      &add
      &trace
      &pushthisgv
      &pushsdbgm 6							//'_alpha'
      &pushsdb 0							//'AptTimeLine::GraphFocus:'
      &pushbyte 6
      &pushone
      &pushsdbgv 1							//'_parent'
      &pushsdbgm 1							//'_parent'
      &pushsdbgm 2							//'_name'
      &pushsdb 3							//'substr'
      &callMethod
      &add
      &pushbyte 2
      &pushsdbgv 9							//'_root'
      &dcallmp 10							// SetExtern()
    &end // of frame 0

    &frame 1
      &gotoFrame 0
      &play
    &end // of frame 1
  &end // of defineMovieClip 15

  &defineMovieClip 16 // total frames: 14

    &frame 0
      &stop
    &end // of frame 0

    &frame 1
      &play
    &end // of frame 1

    &frame 6
      &stop
    &end // of frame 6

    &frame 7
      &play
    &end // of frame 7

    &frame 13
      &stop
    &end // of frame 13
  &end // of defineMovieClip 16

  &defineMovieClip 19 // total frames: 1
  &end // of defineMovieClip 19

  &defineMovieClip 20 // total frames: 40
  &end // of defineMovieClip 20

  &defineMovieClip 23 // total frames: 1
  &end // of defineMovieClip 23

  &defineMovieClip 26 // total frames: 1
  &end // of defineMovieClip 26

  &defineMovieClip 29 // total frames: 2

    &frame 1
      &constants 'ParentColor: ', '_parent', 'ButtonColor', ' - ', '_name', 'GUIPlayer', 'textColor'  
      &pushsdb 0							//'ParentColor: '
      &pushsdbgv 1							//'_parent'
      &pushsdbgm 2							//'ButtonColor'
      &add
      &pushsdb 3							//' - '
      &add
      &pushsdbgv 1							//'_parent'
      &pushsdbgm 4							//'_name'
      &add
      &trace
      &pushsdbgv 5							//'GUIPlayer'
      &pushsdb 6							//'textColor'
      &pushsdbgv 1							//'_parent'
      &pushsdbgm 2							//'ButtonColor'
      &setMember
      &stop
    &end // of frame 1
  &end // of defineMovieClip 29
  
  &importAssets &from 'ShellButtons.swf'
    'ScanLine' &as 31
  &end // of importAssets

  &defineMovieClip 34 // total frames: 1
  &end // of defineMovieClip 34

  &defineMovieClip 36 // total frames: 40
  &end // of defineMovieClip 36

  &defineMovieClip 38 // total frames: 1
  &end // of defineMovieClip 38

  &defineMovieClip 39 // total frames: 10

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
  &end // of defineMovieClip 39

  &defineMovieClip 44 // total frames: 1
  &end // of defineMovieClip 44

  &defineMovieClip 47 // total frames: 1
  &end // of defineMovieClip 47

  &defineMovieClip 50 // total frames: 1
  &end // of defineMovieClip 50

  &defineMovieClip 51 // total frames: 30

    &frame 1
      &constants 'my_color', 'this', 'Color', '_parent', 'ButtonColor', 'setRGB', '_parent.Faction: ', 'Faction', ' - ', '_name'  
      &pushsdb 0							//'my_color'
      &pushthisgv
      &pushone
      &pushsdb 2							//'Color'
      &new
      &varEquals
      &pushsdbgv 3							//'_parent'
      &pushsdbgm 4							//'ButtonColor'
      &pushone
      &pushsdbgv 0							//'my_color'
      &dcallmp 5							// setRGB()
      &pushsdb 6							//'_parent.Faction: '
      &pushsdbgv 3							//'_parent'
      &pushsdbgm 7							//'Faction'
      &add
      &pushsdb 8							//' - '
      &add
      &pushsdbgv 3							//'_parent'
      &pushsdbgm 9							//'_name'
      &add
      &trace
      &pushsdbgv 3							//'_parent'
      &pushsdbgm 7							//'Faction'
      &gotoAndPlay    &end // of frame 1

    &frame 8
      &stop
    &end // of frame 8

    &frame 18
      &stop
    &end // of frame 18

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 51

  &defineMovieClip 52 // total frames: 1

    &frame 0
      &constants 'GetMode', 'Disabled', 'Hidden', 'IsHidden', 'ClearMode', 'SetMode', 'IsDisabled', 'FactionIcon', '_alpha', 'TabSelected', 'Selected: ', '', '_blur', 'FocusClip', 'gotoAndPlay', 'BLUR: Button', 'FocusPlayer', '_focus', 'Button', 'Param', 'DisabledBttn', 'HiddenBttn', 'HiddenUpState', 'HiddenText', 'TabSelectedBttn', 'ReleaseTransText', 'vStartMode', 'Disable'  
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
        &pushsdbgv 7							//'FactionIcon'
        &pushsdb 8							//'_alpha'
        &pushbyte 100
        &setMember
      &end // of function Enable

      &function Disable ('Void'      )      
        &pushsdb 1							//'Disabled'
        &pushone
        &dcallfp 5							// SetMode()
        &pushsdbgv 7							//'FactionIcon'
        &pushsdb 8							//'_alpha'
        &pushbyte 50
        &setMember
      &end // of function Disable

      &function TabSelected ('Void'      )      
        &pushsdb 9							//'TabSelected'
        &pushone
        &dcallfp 5							// SetMode()
        &pushsdb 10							//'Selected: '
        &pushsdb 11							//''
        &pushbyte 13
        &getProperty
        &add
        &trace
      &end // of function TabSelected

      &function2 Blur ('Void') (r:1='this', r:2='_root')
        &pushsdb 12							//'_blur'
        &pushone
        &pushsdbgv 13							//'FocusClip'
        &dcallmp 14							// gotoAndPlay()
        &pushsdb 15							//'BLUR: Button'
        &push r:2        
        &pushsdbgm 16							//'FocusPlayer'
        &add
        &trace
        &pushsdb 17							//'_focus'
        &pushone
        &push r:1        
        &pushsdb 18							//'Button'
        &pushsdbgv 19							//'Param'
        &add
        &getMember
        &pushsdbgm 13							//'FocusClip'
        &dcallmp 14							// gotoAndPlay()
      &end // of function Blur

      &function Focus ('Void'      )      
        &pushsdb 17							//'_focus'
        &pushone
        &pushsdbgv 13							//'FocusClip'
        &dcallmp 14							// gotoAndPlay()
      &end // of function Focus

      &pushsdb 20							//'DisabledBttn'
      &pushfalse
      &setVariable
      &pushsdb 21							//'HiddenBttn'
      &pushfalse
      &setVariable
      &pushsdb 22							//'HiddenUpState'
      &pushfalse
      &setVariable
      &pushsdb 23							//'HiddenText'
      &pushfalse
      &setVariable
      &pushsdb 24							//'TabSelectedBttn'
      &pushfalse
      &setVariable
      &pushsdb 25							//'ReleaseTransText'
      &pushfalse
      &setVariable
      &pushsdbgv 26							//'vStartMode'
      &pushone
      &dcallfp 5							// SetMode()
      &pushzero
      &dcallfp 27							// Disable()
    &end // of frame 0
  &end // of defineMovieClip 52
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets

  &defineMovieClip 55 // total frames: 1
  &end // of defineMovieClip 55
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets

  &defineMovieClip 58 // total frames: 1
  &end // of defineMovieClip 58

  &defineMovieClip 61 // total frames: 1
  &end // of defineMovieClip 61
  
  &importAssets &from 'ShellButtons.swf'
    'ShellButtons Small' &as 62
  &end // of importAssets

  &defineMovieClip 63 // total frames: 1

    &frame 0
      &constants 'vCurSelected', 'ClearMode', 'TabSelected', 'SWITCH_TAB : ', '_visible', 'ShowAllTabs()', 'vVisIndex', 'length', 'SwitchTab', 'FinalTab', '$UnitsTab', 'Units', 'SetText', '$StructuresTab', 'Structures', '$ResourcesTab', 'Resources', '$StatsTab', 'Stats', 'Array', 'ReleaseCallback', '_units', 'gotoAndPlay', '_structures', '_resources', '_stats'  
      &function2 SwitchTab (r:1='to') ()
        &push r:1        
        &pushsdbgv 0							//'vCurSelected'
        &equals
        &not
        &not
        &jnz label1        
        &pushzero
        &pushsdbgv 0							//'vCurSelected'
        &dcallmp 1							// ClearMode()
        &pushsdb 0							//'vCurSelected'
        &push r:1        
        &setVariable
        &pushzero
        &pushsdbgv 0							//'vCurSelected'
        &dcallmp 2							// TabSelected()
       label1:
        &pushsdb 3							//'SWITCH_TAB : '
        &pushsdbgv 0							//'vCurSelected'
        &pushsdbgm 2							//'TabSelected'
        &add
        &trace
      &end // of function SwitchTab

      &function2 RevealTab (r:1='tab') ()
        &push r:1        
        &pushsdbgm 4							//'_visible'
        &not
        &not
        &jnz label2        
        &push r:1        
        &pushsdb 4							//'_visible'
        &pushtrue
        &setMember
       label2:
      &end // of function RevealTab

      &function2 ShowAllTabs () ()
        &pushsdb 5							//'ShowAllTabs()'
        &trace
        &pushzero
        &setRegister r:1
        &pop
       label3:
        &push r:1        
        &pushsdbgv 6							//'vVisIndex'
        &pushsdbgm 7							//'length'
        &lessThan
        &not
        &jnz label5        
        &pushsdbgv 6							//'vVisIndex'
        &push r:1        
        &getMember
        &pushsdbgm 4							//'_visible'
        &not
        &not
        &jnz label4        
        &pushsdbgv 6							//'vVisIndex'
        &push r:1        
        &getMember
        &pushsdb 4							//'_visible'
        &pushtrue
        &setMember
       label4:
        &push r:1        
        &increment
        &setRegister r:1
        &pop
        &jmp label3        
       label5:
        &pushsdbgv 6							//'vVisIndex'
        &pushsdbgv 6							//'vVisIndex'
        &pushsdbgm 7							//'length'
        &pushone
        &subtract
        &getMember
        &pushone
        &dcallfp 8							// SwitchTab()
        &pushsdb 9							//'FinalTab'
        &pushtrue
        &setVariable
      &end // of function ShowAllTabs

      &pushsdb 0							//'vCurSelected'
      &pushnull
      &varEquals
      &pushsdb 10							//'$UnitsTab'
      &pushone
      &pushsdbgv 11							//'Units'
      &dcallmp 12							// SetText()
      &pushsdb 13							//'$StructuresTab'
      &pushone
      &pushsdbgv 14							//'Structures'
      &dcallmp 12							// SetText()
      &pushsdb 15							//'$ResourcesTab'
      &pushone
      &pushsdbgv 16							//'Resources'
      &dcallmp 12							// SetText()
      &pushsdb 17							//'$StatsTab'
      &pushone
      &pushsdbgv 18							//'Stats'
      &dcallmp 12							// SetText()
      &pushsdb 6							//'vVisIndex'
      &pushzero
      &pushsdb 19							//'Array'
      &new
      &varEquals
      &pushsdbgv 6							//'vVisIndex'
      &pushzero
      &pushsdbgv 14							//'Structures'
      &setMember
      &pushsdbgv 6							//'vVisIndex'
      &pushone
      &pushsdbgv 16							//'Resources'
      &setMember
      &pushsdbgv 6							//'vVisIndex'
      &pushbyte 2
      &pushsdbgv 18							//'Stats'
      &setMember
      &pushsdbgv 11							//'Units'
      &pushsdb 20							//'ReleaseCallback'
      &function2  () (r:1='this', r:2='_parent')
        &push r:1        
        &pushone
        &dcallfp 8							// SwitchTab()
        &pushsdb 21							//'_units'
        &pushone
        &push r:2        
        &dcallmp 22							// gotoAndPlay()
      &end // of function 

      &setMember
      &pushsdbgv 14							//'Structures'
      &pushsdb 20							//'ReleaseCallback'
      &function2  () (r:1='this', r:2='_parent')
        &push r:1        
        &pushone
        &dcallfp 8							// SwitchTab()
        &pushsdb 23							//'_structures'
        &pushone
        &push r:2        
        &dcallmp 22							// gotoAndPlay()
      &end // of function 

      &setMember
      &pushsdbgv 16							//'Resources'
      &pushsdb 20							//'ReleaseCallback'
      &function2  () (r:1='this', r:2='_parent')
        &push r:1        
        &pushone
        &dcallfp 8							// SwitchTab()
        &pushsdb 24							//'_resources'
        &pushone
        &push r:2        
        &dcallmp 22							// gotoAndPlay()
      &end // of function 

      &setMember
      &pushsdbgv 18							//'Stats'
      &pushsdb 20							//'ReleaseCallback'
      &function2  () (r:1='this', r:2='_parent')
        &push r:1        
        &pushone
        &dcallfp 8							// SwitchTab()
        &pushsdb 25							//'_stats'
        &pushone
        &push r:2        
        &dcallmp 22							// gotoAndPlay()
      &end // of function 

      &setMember
      &pushsdbgv 14							//'Structures'
      &pushsdb 4							//'_visible'
      &pushfalse
      &setMember
      &pushsdbgv 16							//'Resources'
      &pushsdb 4							//'_visible'
      &pushfalse
      &setMember
      &pushsdbgv 18							//'Stats'
      &pushsdb 4							//'_visible'
      &pushfalse
      &setMember
      &pushsdbgv 11							//'Units'
      &pushone
      &dcallfp 8							// SwitchTab()
    &end // of frame 0

    &placeMovieClip 62 &as 'Units'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv ''
      &end
    &end // of placeMovieClip 62

    &placeMovieClip 62 &as 'Structures'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv ''
      &end
    &end // of placeMovieClip 62

    &placeMovieClip 62 &as 'Resources'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv ''
      &end
    &end // of placeMovieClip 62

    &placeMovieClip 62 &as 'Stats'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv ''
      &end
    &end // of placeMovieClip 62
  &end // of defineMovieClip 63

  &defineMovieClip 90 // total frames: 1
  &end // of defineMovieClip 90

  &defineMovieClip 92 // total frames: 1
  &end // of defineMovieClip 92

  &defineMovieClip 93 // total frames: 1

    &placeMovieClip 92 &as 'GridRender'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'AptTimeLine::RenderGraph'
        &pushs '_graphMode'
        &pushssv 'Score'
      &end
    &end // of placeMovieClip 92
  &end // of defineMovieClip 93

  &defineMovieClip 94 // total frames: 115

    &frame 49
      &constants '_parent', 'FinalTab', 'EnablePlayerButtons'  
      &pushsdbgv 0							//'_parent'
      &pushsdbgm 1							//'FinalTab'
      &not
      &jnz label1      
      &pushzero
      &pushsdbgv 0							//'_parent'
      &dcallmp 2							// EnablePlayerButtons()
      &stop
     label1:
    &end // of frame 49

    &frame 114
      &pushzero
      &pushsgv '_parent'
      &pushs 'DoGotoNextTab'
      &callmp
      &gotoFrame 0
      &play
    &end // of frame 114
  &end // of defineMovieClip 94

  &defineMovieClip 96 // total frames: 1

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
  &end // of defineMovieClip 96

  &defineMovieClip 99 // total frames: 1
  &end // of defineMovieClip 99

  &defineMovieClip 115 // total frames: 43

    &frame 0
      &pushzero
      &pushsgv '_root'
      &pushsgm 'Timeline'
      &pushs 'GetScreenMode'
      &callMethod
      &gotoAndStop    &end // of frame 0

    &placeMovieClip 99 
    
      &onClipEvent &load
        &pushthisgv
        &pushs '_visible'
        &pushzero
        &setMember
      &end
    &end // of placeMovieClip 99

    &frame 9
      &pushsgv 'Conquered'
      &pushs 'text'
      &pushssm '$RegionUnified'
    &end // of frame 9
  &end // of defineMovieClip 115

  &defineButton 118
  
    &on     &overDownToOverUp
      &constants '_parent', 'DoGotoNextTab', 'Axis', 'gotoAndPlay'  
      &pushzero
      &pushsdbgv 0							//'_parent'
      &dcallmp 1							// DoGotoNextTab()
      &pushone
      &pushone
      &pushsdbgv 0							//'_parent'
      &pushsdbgm 2							//'Axis'
      &dcallmp 3							// gotoAndPlay()
    &end
  &end // of defineButton 118

  &defineMovieClip 119 // total frames: 20

    &frame 8
      &stop
    &end // of frame 8

    &frame 19
      &stop
    &end // of frame 19
  &end // of defineMovieClip 119

  &defineMovieClip 124 // total frames: 1
  &end // of defineMovieClip 124

  &defineMovieClip 129 // total frames: 19

    &frame 0
      &pushsgv '_root'
      &pushsgm 'ShowSaveReplay'
      &not
      &jnz label1      
      &stop
      &jmp label2      
     label1:
      &gotoLabel '_continue'
      &play
     label2:
    &end // of frame 0

    &frame 9
      &stop
    &end // of frame 9
  &end // of defineMovieClip 129

  &defineMovieClip 130 // total frames: 1

    &frame 0
      &constants 'Continue', 'SetText', '$Continue', 'Skip', '$Skip', 'SaveReplay', '$SaveReplay', '_root', 'ShowSaveReplay', '_visible', 'ReleaseCallback', '_stats', 'gotoAndPlay', '_fullyRevealed', 'Axis', 'Disable', 'OnButtonContinue', 'GameCode', 'CloseFrame', 'OnButtonSaveReplay', 'NextMission'  
      &pushsdbgv 0							//'Continue'
      &pushsdb 1							//'SetText'
      &pushsdb 2							//'$Continue'
      &setMember
      &pushsdbgv 3							//'Skip'
      &pushsdb 1							//'SetText'
      &pushsdb 4							//'$Skip'
      &setMember
      &pushsdbgv 5							//'SaveReplay'
      &pushsdb 1							//'SetText'
      &pushsdb 6							//'$SaveReplay'
      &setMember
      &pushsdbgv 7							//'_root'
      &pushsdbgm 8							//'ShowSaveReplay'
      &not
      &not
      &jnz label1      
      &pushsdbgv 5							//'SaveReplay'
      &pushsdb 9							//'_visible'
      &pushfalse
      &setMember
     label1:
      &pushsdbgv 3							//'Skip'
      &pushsdb 10							//'ReleaseCallback'
      &function2  () (r:1='_parent')
        &pushsdb 11							//'_stats'
        &pushone
        &push r:1        
        &dcallmp 12							// gotoAndPlay()
        &pushsdb 13							//'_fullyRevealed'
        &pushone
        &push r:1        
        &pushsdbgm 14							//'Axis'
        &dcallmp 12							// gotoAndPlay()
      &end // of function 

      &setMember
      &pushsdbgv 0							//'Continue'
      &pushsdb 10							//'ReleaseCallback'
      &function2  () (r:1='_root')
        &pushzero
        &pushsdbgv 5							//'SaveReplay'
        &dcallmp 15							// Disable()
        &pushsdb 16							//'OnButtonContinue'
        &pushone
        &push r:1        
        &dcallmp 17							// GameCode()
        &pushzero
        &push r:1        
        &dcallmp 18							// CloseFrame()
      &end // of function 

      &setMember
      &pushsdbgv 5							//'SaveReplay'
      &pushsdb 10							//'ReleaseCallback'
      &function2  () (r:1='_root')
        &pushsdb 19							//'OnButtonSaveReplay'
        &pushone
        &push r:1        
        &dcallmp 17							// GameCode()
        &pushzero
        &pushsdbgv 0							//'Continue'
        &dcallmp 15							// Disable()
        &pushzero
        &pushsdbgv 20							//'NextMission'
        &dcallmp 15							// Disable()
        &pushzero
        &push r:1        
        &dcallmp 18							// CloseFrame()
      &end // of function 

      &setMember
    &end // of frame 0

    &placeMovieClip 62 &as 'Continue'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv ''
      &end
    &end // of placeMovieClip 62

    &placeMovieClip 62 &as 'Skip'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv ''
      &end
    &end // of placeMovieClip 62

    &placeMovieClip 62 &as 'SaveReplay'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv 'Disabled'
      &end
    &end // of placeMovieClip 62
  &end // of defineMovieClip 130
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &importAssets &from 'GameWindowGadgets.swf'
    'ListBox' &as 131
  &end // of importAssets

  &defineMovieClip 134 // total frames: 1
  &end // of defineMovieClip 134

  &defineMovieClip 137 // total frames: 1
  &end // of defineMovieClip 137

  &defineButton 139
  
    &on     &idleToOverUp
      &pushthisgv
      &pushone
      &pushsgv '_parent'
      &pushs 'Over'
      &callmp
    &end
  
    &on     &overUpToIdle    ,&overDownToOutDown    ,&overDownToIdle
      &pushthisgv
      &pushone
      &pushsgv '_parent'
      &pushs 'RollOut'
      &callmp
    &end
  
    &on     &overUpToOverDown
      &pushthisgv
      &pushone
      &pushsgv '_parent'
      &pushs 'Press'
      &callmp
    &end
  
    &on     &overDownToOverUp
      &pushthisgv
      &pushone
      &pushsgv '_parent'
      &pushs 'Release'
      &callmp
    &end
  &end // of defineButton 139

  &defineMovieClip 142 // total frames: 30
  &end // of defineMovieClip 142

  &defineMovieClip 143 // total frames: 70

    &frame 0
      &pushbyte 100
      &pushs 'ReleaseAnimation'
      &pushbyte 2
      &pushthisgv
      &pushs 'createEmptyMovieClip'
      &callmp
      &pushs 'DownCount'
      &pushzerosv
      &pushzero
      &pushsgv '_parent'
      &pushs 'CheckEnable'
      &callmp
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
      &constants 'DownCount', 'Down', 'PlayerCarrotReleaseAnimation', 'ReleaseAnimation', 'attachMovie', 'this', 'ButtonCallBack', '_parent', 'CheckEnable'  
      &pushbyte 100
      &pushsdbgv 0							//'DownCount'
      &add
      &pushsdb 1							//'Down'
      &pushsdbgv 0							//'DownCount'
      &add
      &pushsdb 2							//'PlayerCarrotReleaseAnimation'
      &pushbyte 3
      &pushsdbgv 3							//'ReleaseAnimation'
      &dcallmp 4							// attachMovie()
      &pushsdb 0							//'DownCount'
      &pushsdbgv 0							//'DownCount'
      &pushone
      &add
      &setVariable
      &pushzero
      &pushthisgv
      &dcallmp 6							// ButtonCallBack()
      &pushzero
      &pushsdbgv 7							//'_parent'
      &dcallmp 8							// CheckEnable()
    &end // of frame 49

    &frame 59
      &pushs 'DownCount'
      &pushzerosv
    &end // of frame 59

    &frame 69
      &stop
    &end // of frame 69
  &end // of defineMovieClip 143

  &defineMovieClip 144 // total frames: 1

    &frame 0
      &constants '_root', 'Timeline', 'GetNumStatsColumns', 'this', '_visible', 'Carrot0', 'ButtonCallBack', 'ChangePlayerSlot0Focus', 'Carrot1', 'CheckEnable', 'PlayerSlot0Focus', '_disable', 'gotoAndPlay', '_up', 'Over', 'Gui_ShellMapMouseOver', 'PlaySound', '_over', 'RollOut', 'Gui_ShellMapMouseOut', '_rollOut', 'Press', '_down', 'Release', 'Gui_ShellMapSelect', '_release'  
      &pushzero
      &pushsdbgv 0							//'_root'
      &pushsdbgm 1							//'Timeline'
      &pushsdb 2							//'GetNumStatsColumns'
      &callMethod
      &pushbyte 3
      &greaterThan
      &not
      &jnz label1      
      &pushthisgv
      &pushsdb 4							//'_visible'
      &pushtrue
      &setMember
      &jmp label2      
     label1:
      &pushthisgv
      &pushsdb 4							//'_visible'
      &pushfalse
      &setMember
     label2:
      &pushsdbgv 5							//'Carrot0'
      &pushsdb 6							//'ButtonCallBack'
      &function2  () (r:1='_parent')
        &pushbyte -1
        &pushone
        &push r:1        
        &dcallmp 7							// ChangePlayerSlot0Focus()
      &end // of function 

      &setMember
      &pushsdbgv 8							//'Carrot1'
      &pushsdb 6							//'ButtonCallBack'
      &function2  () (r:1='_parent')
        &pushone
        &pushone
        &push r:1        
        &dcallmp 7							// ChangePlayerSlot0Focus()
      &end // of function 

      &setMember
      &pushsdb 9							//'CheckEnable'
      &function2  () (r:1='_root', r:2='_parent')
        &push r:2        
        &pushsdbgm 10							//'PlayerSlot0Focus'
        &pushone
        &equals
        &not
        &jnz label3        
        &pushsdb 11							//'_disable'
        &pushone
        &pushsdbgv 5							//'Carrot0'
        &dcallmp 12							// gotoAndPlay()
        &jmp label4        
       label3:
        &pushsdb 13							//'_up'
        &pushone
        &pushsdbgv 5							//'Carrot0'
        &dcallmp 12							// gotoAndPlay()
       label4:
        &push r:2        
        &pushsdbgm 10							//'PlayerSlot0Focus'
        &pushzero
        &push r:1        
        &pushsdbgm 1							//'Timeline'
        &pushsdb 2							//'GetNumStatsColumns'
        &callMethod
        &pushbyte 2
        &subtract
        &equals
        &not
        &jnz label5        
        &pushsdb 11							//'_disable'
        &pushone
        &pushsdbgv 8							//'Carrot1'
        &dcallmp 12							// gotoAndPlay()
        &jmp label6        
       label5:
        &pushsdb 13							//'_up'
        &pushone
        &pushsdbgv 8							//'Carrot1'
        &dcallmp 12							// gotoAndPlay()
       label6:
      &end // of function 

      &setVariable
      &pushsdb 14							//'Over'
      &function2  (r:2='Param') (r:1='_root')
        &pushsdb 15							//'Gui_ShellMapMouseOver'
        &pushone
        &push r:1        
        &dcallmp 16							// PlaySound()
        &pushsdb 17							//'_over'
        &pushone
        &push r:2        
        &dcallmp 12							// gotoAndPlay()
      &end // of function 

      &setVariable
      &pushsdb 18							//'RollOut'
      &function2  (r:2='Param') (r:1='_root')
        &pushsdb 19							//'Gui_ShellMapMouseOut'
        &pushone
        &push r:1        
        &dcallmp 16							// PlaySound()
        &pushsdb 20							//'_rollOut'
        &pushone
        &push r:2        
        &dcallmp 12							// gotoAndPlay()
      &end // of function 

      &setVariable
      &pushsdb 21							//'Press'
      &function2  (r:1='Param') ()
        &pushsdb 22							//'_down'
        &pushone
        &push r:1        
        &dcallmp 12							// gotoAndPlay()
      &end // of function 

      &setVariable
      &pushsdb 23							//'Release'
      &function2  (r:2='Param') (r:1='_root')
        &pushsdb 24							//'Gui_ShellMapSelect'
        &pushone
        &push r:1        
        &dcallmp 16							// PlaySound()
        &pushsdb 25							//'_release'
        &pushone
        &push r:2        
        &dcallmp 12							// gotoAndPlay()
      &end // of function 

      &setVariable
    &end // of frame 0
  &end // of defineMovieClip 144
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets

  &defineMovieClip 145 // total frames: 1

    &frame 0
      &constants '_root', 'Timeline', 'GetNumStatsColumns', 'this', '_visible', 'Carrot0', 'ButtonCallBack', 'ChangePlayerSlot0Focus', 'Carrot1', 'CheckEnable', 'PlayerSlot0Focus', '_disable', 'gotoAndPlay', '_up', 'Over', 'Gui_ShellMapMouseOver', 'PlaySound', '_over', 'RollOut', 'Gui_ShellMapMouseOut', '_rollOut', 'Press', '_down', 'Release', 'Gui_ShellMapSelect', '_release'  
      &pushzero
      &pushsdbgv 0							//'_root'
      &pushsdbgm 1							//'Timeline'
      &pushsdb 2							//'GetNumStatsColumns'
      &callMethod
      &pushbyte 3
      &greaterThan
      &not
      &jnz label1      
      &pushthisgv
      &pushsdb 4							//'_visible'
      &pushtrue
      &setMember
      &jmp label2      
     label1:
      &pushthisgv
      &pushsdb 4							//'_visible'
      &pushfalse
      &setMember
     label2:
      &pushsdbgv 5							//'Carrot0'
      &pushsdb 6							//'ButtonCallBack'
      &function2  () (r:1='_parent')
        &pushbyte -1
        &pushone
        &push r:1        
        &dcallmp 7							// ChangePlayerSlot0Focus()
      &end // of function 

      &setMember
      &pushsdbgv 8							//'Carrot1'
      &pushsdb 6							//'ButtonCallBack'
      &function2  () (r:1='_parent')
        &pushone
        &pushone
        &push r:1        
        &dcallmp 7							// ChangePlayerSlot0Focus()
      &end // of function 

      &setMember
      &pushsdb 9							//'CheckEnable'
      &function2  () (r:1='_root', r:2='_parent')
        &push r:2        
        &pushsdbgm 10							//'PlayerSlot0Focus'
        &pushzero
        &equals
        &not
        &jnz label3        
        &pushsdb 11							//'_disable'
        &pushone
        &pushsdbgv 5							//'Carrot0'
        &dcallmp 12							// gotoAndPlay()
        &jmp label4        
       label3:
        &pushsdb 13							//'_up'
        &pushone
        &pushsdbgv 5							//'Carrot0'
        &dcallmp 12							// gotoAndPlay()
       label4:
        &push r:2        
        &pushsdbgm 10							//'PlayerSlot0Focus'
        &pushzero
        &push r:1        
        &pushsdbgm 1							//'Timeline'
        &pushsdb 2							//'GetNumStatsColumns'
        &callMethod
        &pushbyte 3
        &subtract
        &equals
        &not
        &jnz label5        
        &pushsdb 11							//'_disable'
        &pushone
        &pushsdbgv 8							//'Carrot1'
        &dcallmp 12							// gotoAndPlay()
        &jmp label6        
       label5:
        &pushsdb 13							//'_up'
        &pushone
        &pushsdbgv 8							//'Carrot1'
        &dcallmp 12							// gotoAndPlay()
       label6:
      &end // of function 

      &setVariable
      &pushsdb 14							//'Over'
      &function2  (r:2='Param') (r:1='_root')
        &pushsdb 15							//'Gui_ShellMapMouseOver'
        &pushone
        &push r:1        
        &dcallmp 16							// PlaySound()
        &pushsdb 17							//'_over'
        &pushone
        &push r:2        
        &dcallmp 12							// gotoAndPlay()
      &end // of function 

      &setVariable
      &pushsdb 18							//'RollOut'
      &function2  (r:2='Param') (r:1='_root')
        &pushsdb 19							//'Gui_ShellMapMouseOut'
        &pushone
        &push r:1        
        &dcallmp 16							// PlaySound()
        &pushsdb 20							//'_rollOut'
        &pushone
        &push r:2        
        &dcallmp 12							// gotoAndPlay()
      &end // of function 

      &setVariable
      &pushsdb 21							//'Press'
      &function2  (r:1='Param') ()
        &pushsdb 22							//'_down'
        &pushone
        &push r:1        
        &dcallmp 12							// gotoAndPlay()
      &end // of function 

      &setVariable
      &pushsdb 23							//'Release'
      &function2  (r:2='Param') (r:1='_root')
        &pushsdb 24							//'Gui_ShellMapSelect'
        &pushone
        &push r:1        
        &dcallmp 16							// PlaySound()
        &pushsdb 25							//'_release'
        &pushone
        &push r:2        
        &dcallmp 12							// gotoAndPlay()
      &end // of function 

      &setVariable
    &end // of frame 0
  &end // of defineMovieClip 145
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets
  
  &exportAssets
    52 &as 'PlayerButton'
  &end // of exportAssets

  &defineMovieClip 147 // total frames: 70

    &frame 0
      &constants 'CurrentTab', 'Playlist', 'm_playerButtonsEnabled: ', 'm_playerButtonsEnabled', 'Button', 'FocusPlayer', 'Blur', 'BLUR: Button', 'Focus', 'FOCUS: Button', 'vCurSelected', 'ClearMode', 'TabSelected', 'i', 'TotalPlayers', 'Show', '_visible', 'EnablePlayerButtons', 'Enable', 'DoFocusGraph', 'SwitchTab', 'SetSaveReplayEnableState: ', ' at ', 'MainButtons', 'SaveReplay', 'Disable', '_stats', '_resources', '_structures', '_units', 'DoGotoNextTab', 'Skip', 'Continue', '_root', '$TimeLine:PlayerName:', 'SetText', 'SetButtonColor', ': ', 'Timeline', 'GetPlayerColor', 'ButtonColor', 'SetButtonFaction', 'GetPlayerFaction', 'Faction', 'Button0', 'ReleaseCallback', 'Button1', 'Button2', 'Button3', 'Button4', 'Button5', 'Button6', 'Button7'  
      &function DoGotoNextTab (      )      
        &pushsdbgv 0							//'CurrentTab'
        &pushnull
        &equals
        &not
        &jnz label1        
        &pushsdb 0							//'CurrentTab'
        &pushzerosv
        &pushsdbgv 1							//'Playlist'
        &pushsdbgv 0							//'CurrentTab'
        &getMember
        &gotoAndPlay        &jmp label3        
       label1:
        &pushsdbgv 0							//'CurrentTab'
        &pushbyte 2
        &equals
        &not
        &jnz label2        
        &pushsdb 0							//'CurrentTab'
        &pushsdbgv 0							//'CurrentTab'
        &increment
        &setVariable
        &pushsdbgv 1							//'Playlist'
        &pushsdbgv 0							//'CurrentTab'
        &getMember
        &gotoAndPlay       label2:
        &pushsdb 0							//'CurrentTab'
        &pushsdbgv 0							//'CurrentTab'
        &increment
        &setVariable
        &pushsdbgv 1							//'Playlist'
        &pushsdbgv 0							//'CurrentTab'
        &getMember
        &gotoAndPlay       label3:
      &end // of function DoGotoNextTab

      &function2 DoFocusGraph (r:3='Param') (r:1='this', r:2='_root')
        &pushsdb 2							//'m_playerButtonsEnabled: '
        &pushsdbgv 3							//'m_playerButtonsEnabled'
        &add
        &trace
        &pushsdbgv 3							//'m_playerButtonsEnabled'
        &not
        &not
        &jnz label4        
        &pushundef
        &return
       label4:
        &pushzero
        &push r:1        
        &pushsdb 4							//'Button'
        &push r:2        
        &pushsdbgm 5							//'FocusPlayer'
        &add
        &getMember
        &dcallmp 6							// Blur()
        &pushsdb 7							//'BLUR: Button'
        &push r:2        
        &pushsdbgm 5							//'FocusPlayer'
        &add
        &trace
        &pushzero
        &push r:1        
        &pushsdb 4							//'Button'
        &push r:3        
        &add
        &getMember
        &dcallmp 8							// Focus()
        &pushsdb 9							//'FOCUS: Button'
        &push r:3        
        &add
        &trace
        &push r:2        
        &pushsdb 5							//'FocusPlayer'
        &push r:3        
        &setMember
      &end // of function DoFocusGraph

      &function2 SwitchTab (r:1='to') ()
        &push r:1        
        &pushsdbgv 10							//'vCurSelected'
        &equals
        &not
        &not
        &jnz label5        
        &pushzero
        &pushsdbgv 10							//'vCurSelected'
        &dcallmp 11							// ClearMode()
        &pushsdb 10							//'vCurSelected'
        &push r:1        
        &setVariable
        &pushzero
        &pushsdbgv 10							//'vCurSelected'
        &dcallmp 12							// TabSelected()
       label5:
      &end // of function SwitchTab

      &function2 ShowHidePlayButtons (r:3='Param') (r:1='this', r:2='_root')
        &pushsdb 13							//'i'
        &pushzerosv
       label6:
        &pushsdbgv 13							//'i'
        &push r:2        
        &pushsdbgm 14							//'TotalPlayers'
        &lessThan
        &not
        &jnz label9        
        &push r:3        
        &pushsdb 15							//'Show'
        &equals
        &not
        &jnz label7        
        &push r:1        
        &pushsdb 4							//'Button'
        &pushsdbgv 13							//'i'
        &add
        &getMember
        &pushsdb 16							//'_visible'
        &pushtrue
        &setMember
        &jmp label8        
       label7:
        &push r:1        
        &pushsdb 4							//'Button'
        &pushsdbgv 13							//'i'
        &add
        &getMember
        &pushsdb 16							//'_visible'
        &pushfalse
        &setMember
       label8:
        &pushsdb 13							//'i'
        &pushsdbgv 13							//'i'
        &increment
        &setVariable
        &jmp label6        
       label9:
      &end // of function ShowHidePlayButtons

      &function2 EnablePlayerButtons () (r:1='this', r:2='_root')
        &pushsdb 17							//'EnablePlayerButtons'
        &trace
        &pushzero
        &setRegister r:3
        &pop
       label10:
        &push r:3        
        &push r:2        
        &pushsdbgm 14							//'TotalPlayers'
        &lessThan
        &not
        &jnz label11        
        &pushzero
        &push r:1        
        &pushsdb 4							//'Button'
        &push r:3        
        &add
        &getMember
        &dcallmp 18							// Enable()
        &pushzero
        &push r:1        
        &pushsdb 4							//'Button'
        &push r:3        
        &add
        &getMember
        &dcallmp 6							// Blur()
        &push r:3        
        &increment
        &setRegister r:3
        &pop
        &jmp label10        
       label11:
        &pushsdb 3							//'m_playerButtonsEnabled'
        &pushtrue
        &setVariable
        &pushzero
        &pushone
        &dcallfp 19							// DoFocusGraph()
        &push r:1        
        &pushsdb 4							//'Button'
        &push r:2        
        &pushsdbgm 5							//'FocusPlayer'
        &add
        &getMember
        &pushone
        &dcallfp 20							// SwitchTab()
      &end // of function EnablePlayerButtons

      &function2 SetSaveReplayEnableState (r:1='param') ()
        &pushsdb 21							//'SetSaveReplayEnableState: '
        &push r:1        
        &add
        &pushsdb 22							//' at '
        &add
        &pushsdbgv 23							//'MainButtons'
        &pushsdbgm 24							//'SaveReplay'
        &add
        &trace
        &push r:1        
        &not
        &jnz label12        
        &pushzero
        &pushsdbgv 23							//'MainButtons'
        &pushsdbgm 24							//'SaveReplay'
        &dcallmp 18							// Enable()
        &jmp label13        
       label12:
        &pushzero
        &pushsdbgv 23							//'MainButtons'
        &pushsdbgm 24							//'SaveReplay'
        &dcallmp 25							// Disable()
       label13:
      &end // of function SetSaveReplayEnableState

      &pushsdb 1							//'Playlist'
      &pushsdb 26							//'_stats'
      &pushsdb 27							//'_resources'
      &pushsdb 28							//'_structures'
      &pushsdb 29							//'_units'
      &pushbyte 4
      &initArray
      &setVariable
      &pushsdb 3							//'m_playerButtonsEnabled'
      &pushfalse
      &varEquals
      &pushzero
      &dcallfp 30							// DoGotoNextTab()
      &pushsdbgv 23							//'MainButtons'
      &pushsdbgm 31							//'Skip'
      &pushsdb 16							//'_visible'
      &pushtrue
      &setMember
      &pushsdbgv 23							//'MainButtons'
      &pushsdbgm 32							//'Continue'
      &pushsdb 16							//'_visible'
      &pushfalse
      &setMember
      &pushsdb 13							//'i'
      &pushzerosv
     label14:
      &pushsdbgv 13							//'i'
      &pushbyte 8
      &lessThan
      &not
      &jnz label17      
      &pushsdbgv 13							//'i'
      &pushsdbgv 33							//'_root'
      &pushsdbgm 14							//'TotalPlayers'
      &lessThan
      &not
      &jnz label15      
      &pushsdb 34							//'$TimeLine:PlayerName:'
      &pushsdbgv 13							//'i'
      &add
      &pushone
      &pushsdb 4							//'Button'
      &pushsdbgv 13							//'i'
      &add
      &getVariable
      &dcallmp 35							// SetText()
      &pushsdb 36							//'SetButtonColor'
      &pushsdbgv 13							//'i'
      &add
      &pushsdb 37							//': '
      &add
      &pushsdbgv 13							//'i'
      &pushone
      &pushsdbgv 33							//'_root'
      &pushsdbgm 38							//'Timeline'
      &pushsdb 39							//'GetPlayerColor'
      &callMethod
      &add
      &trace
      &pushsdb 4							//'Button'
      &pushsdbgv 13							//'i'
      &add
      &getVariable
      &pushsdb 40							//'ButtonColor'
      &pushsdbgv 13							//'i'
      &pushone
      &pushsdbgv 33							//'_root'
      &pushsdbgm 38							//'Timeline'
      &pushsdb 39							//'GetPlayerColor'
      &callMethod
      &setMember
      &pushsdb 41							//'SetButtonFaction'
      &pushsdbgv 13							//'i'
      &add
      &pushsdb 37							//': '
      &add
      &pushsdbgv 13							//'i'
      &pushone
      &pushsdbgv 33							//'_root'
      &pushsdbgm 38							//'Timeline'
      &pushsdb 42							//'GetPlayerFaction'
      &callMethod
      &add
      &trace
      &pushsdb 4							//'Button'
      &pushsdbgv 13							//'i'
      &add
      &getVariable
      &pushsdb 43							//'Faction'
      &pushsdbgv 13							//'i'
      &pushone
      &pushsdbgv 33							//'_root'
      &pushsdbgm 38							//'Timeline'
      &pushsdb 42							//'GetPlayerFaction'
      &callMethod
      &setMember
      &jmp label16      
     label15:
      &pushsdb 4							//'Button'
      &pushsdbgv 13							//'i'
      &add
      &getVariable
      &pushsdb 16							//'_visible'
      &pushzero
      &setMember
     label16:
      &pushsdb 13							//'i'
      &pushsdbgv 13							//'i'
      &increment
      &setVariable
      &jmp label14      
     label17:
      &pushsdb 10							//'vCurSelected'
      &pushnull
      &varEquals
      &pushsdbgv 44							//'Button0'
      &pushsdb 45							//'ReleaseCallback'
      &function2  () (r:1='this')
        &push r:1        
        &pushone
        &dcallfp 20							// SwitchTab()
        &pushzero
        &pushone
        &dcallfp 19							// DoFocusGraph()
      &end // of function 

      &setMember
      &pushsdbgv 46							//'Button1'
      &pushsdb 45							//'ReleaseCallback'
      &function2  () (r:1='this')
        &push r:1        
        &pushone
        &dcallfp 20							// SwitchTab()
        &pushone
        &pushone
        &dcallfp 19							// DoFocusGraph()
      &end // of function 

      &setMember
      &pushsdbgv 47							//'Button2'
      &pushsdb 45							//'ReleaseCallback'
      &function2  () (r:1='this')
        &push r:1        
        &pushone
        &dcallfp 20							// SwitchTab()
        &pushbyte 2
        &pushone
        &dcallfp 19							// DoFocusGraph()
      &end // of function 

      &setMember
      &pushsdbgv 48							//'Button3'
      &pushsdb 45							//'ReleaseCallback'
      &function2  () (r:1='this')
        &push r:1        
        &pushone
        &dcallfp 20							// SwitchTab()
        &pushbyte 3
        &pushone
        &dcallfp 19							// DoFocusGraph()
      &end // of function 

      &setMember
      &pushsdbgv 49							//'Button4'
      &pushsdb 45							//'ReleaseCallback'
      &function2  () (r:1='this')
        &push r:1        
        &pushone
        &dcallfp 20							// SwitchTab()
        &pushbyte 4
        &pushone
        &dcallfp 19							// DoFocusGraph()
      &end // of function 

      &setMember
      &pushsdbgv 50							//'Button5'
      &pushsdb 45							//'ReleaseCallback'
      &function2  () (r:1='this')
        &push r:1        
        &pushone
        &dcallfp 20							// SwitchTab()
        &pushbyte 5
        &pushone
        &dcallfp 19							// DoFocusGraph()
      &end // of function 

      &setMember
      &pushsdbgv 51							//'Button6'
      &pushsdb 45							//'ReleaseCallback'
      &function2  () (r:1='this')
        &push r:1        
        &pushone
        &dcallfp 20							// SwitchTab()
        &pushbyte 6
        &pushone
        &dcallfp 19							// DoFocusGraph()
      &end // of function 

      &setMember
      &pushsdbgv 52							//'Button7'
      &pushsdb 45							//'ReleaseCallback'
      &function2  () (r:1='this')
        &push r:1        
        &pushone
        &dcallfp 20							// SwitchTab()
        &pushbyte 7
        &pushone
        &dcallfp 19							// DoFocusGraph()
      &end // of function 

      &setMember
    &end // of frame 0

    &placeMovieClip 52 &as 'Button0'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv ''
      &end
    &end // of placeMovieClip 52

    &placeMovieClip 52 &as 'Button1'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv ''
      &end
    &end // of placeMovieClip 52

    &placeMovieClip 52 &as 'Button2'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv ''
      &end
    &end // of placeMovieClip 52

    &placeMovieClip 52 &as 'Button3'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv ''
      &end
    &end // of placeMovieClip 52

    &placeMovieClip 52 &as 'Button4'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv ''
      &end
    &end // of placeMovieClip 52

    &placeMovieClip 52 &as 'Button5'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv ''
      &end
    &end // of placeMovieClip 52

    &placeMovieClip 52 &as 'Button6'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv ''
      &end
    &end // of placeMovieClip 52

    &placeMovieClip 52 &as 'Button7'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv ''
      &end
    &end // of placeMovieClip 52

    &placeMovieClip 115 &as 'HelpBar'
    
      &onClipEvent &load
        &pushthisgv
        &pushs '_visible'
        &pushtrue
        &setMember
      &end
    &end // of placeMovieClip 115

    &frame 9
      &constants 'Units', '_parent', 'DoDrawTimeline', 'FinalTab', 'm_playerButtonsEnabled', 'EnablePlayerButtons', 'Mc', 'this', 'Button', '_root', 'FocusPlayer', 'SwitchTab', 'DoFocusGraph', 'Axis', '_visible', 'HelpBar', 'Show', 'ShowHidePlayButtons', 'SetSaveReplayEnableState', 'ShowSaveReplay'  
      &pushsdb 0							//'Units'
      &pushone
      &pushsdbgv 1							//'_parent'
      &dcallmp 2							// DoDrawTimeline()
      &pushsdbgv 3							//'FinalTab'
      &not
      &jnz label2      
      &pushsdbgv 4							//'m_playerButtonsEnabled'
      &not
      &not
      &jnz label1      
      &pushzero
      &pushsdbgv 1							//'_parent'
      &dcallmp 5							// EnablePlayerButtons()
      &pushsdb 6							//'Mc'
      &pushthisgv
      &pushsdb 8							//'Button'
      &pushsdbgv 9							//'_root'
      &pushsdbgm 10							//'FocusPlayer'
      &add
      &getMember
      &varEquals
      &pushsdbgv 6							//'Mc'
      &pushone
      &dcallfp 11							// SwitchTab()
     label1:
      &pushsdbgv 9							//'_root'
      &pushsdbgm 10							//'FocusPlayer'
      &pushone
      &dcallfp 12							// DoFocusGraph()
      &stop
     label2:
      &pushsdbgv 13							//'Axis'
      &pushsdb 14							//'_visible'
      &pushtrue
      &setMember
      &pushsdbgv 15							//'HelpBar'
      &pushsdb 14							//'_visible'
      &pushtrue
      &setMember
      &pushsdb 16							//'Show'
      &pushone
      &dcallfp 17							// ShowHidePlayButtons()
      &pushsdbgv 3							//'FinalTab'
      &not
      &not
      &jnz label3      
      &pushfalse
      &pushone
      &dcallfp 18							// SetSaveReplayEnableState()
      &jmp label4      
     label3:
      &pushsdbgv 9							//'_root'
      &pushsdbgm 19							//'ShowSaveReplay'
      &pushone
      &dcallfp 18							// SetSaveReplayEnableState()
     label4:
    &end // of frame 9

    &frame 10
      &pushsgv 'FinalTab'
      &not
      &not
      &jnz label1      
      &pushsgv '_root'
      &pushsgm 'FocusPlayer'
      &pushone
      &pushs 'DoFocusGraph'
      &callfp
      &stop
     label1:
      &pushsgv 'Units'
      &pushone
      &pushsgv 'MainTabs'
      &pushs 'SwitchTab'
      &callmp
    &end // of frame 10

    &frame 19
      &constants 'Structures', '_parent', 'DoDrawTimeline', '_root', 'FocusPlayer', 'DoFocusGraph', 'Axis', '_visible', 'HelpBar', 'Show', 'ShowHidePlayButtons', 'FinalTab', 'm_playerButtonsEnabled', 'EnablePlayerButtons', 'Mc', 'this', 'Button', 'SwitchTab', 'MainTabs', 'RevealTab', 'SetSaveReplayEnableState', 'ShowSaveReplay'  
      &pushsdb 0							//'Structures'
      &pushone
      &pushsdbgv 1							//'_parent'
      &dcallmp 2							// DoDrawTimeline()
      &pushsdbgv 3							//'_root'
      &pushsdbgm 4							//'FocusPlayer'
      &pushone
      &dcallfp 5							// DoFocusGraph()
      &pushsdbgv 6							//'Axis'
      &pushsdb 7							//'_visible'
      &pushtrue
      &setMember
      &pushsdbgv 8							//'HelpBar'
      &pushsdb 7							//'_visible'
      &pushtrue
      &setMember
      &pushsdb 9							//'Show'
      &pushone
      &dcallfp 10							// ShowHidePlayButtons()
      &pushsdbgv 11							//'FinalTab'
      &not
      &jnz label2      
      &pushsdbgv 12							//'m_playerButtonsEnabled'
      &not
      &not
      &jnz label1      
      &pushzero
      &pushsdbgv 1							//'_parent'
      &dcallmp 13							// EnablePlayerButtons()
      &pushsdb 14							//'Mc'
      &pushthisgv
      &pushsdb 16							//'Button'
      &pushsdbgv 3							//'_root'
      &pushsdbgm 4							//'FocusPlayer'
      &add
      &getMember
      &varEquals
      &pushsdbgv 14							//'Mc'
      &pushone
      &dcallfp 17							// SwitchTab()
     label1:
      &jmp label3      
     label2:
      &pushsdbgv 18							//'MainTabs'
      &pushsdbgm 0							//'Structures'
      &pushone
      &pushsdbgv 18							//'MainTabs'
      &dcallmp 19							// RevealTab()
     label3:
      &pushsdbgv 11							//'FinalTab'
      &not
      &not
      &jnz label4      
      &pushfalse
      &pushone
      &dcallfp 20							// SetSaveReplayEnableState()
      &jmp label5      
     label4:
      &pushsdbgv 3							//'_root'
      &pushsdbgm 21							//'ShowSaveReplay'
      &pushone
      &dcallfp 20							// SetSaveReplayEnableState()
     label5:
      &stop
    &end // of frame 19

    &frame 29
      &constants 'Resources', '_parent', 'DoDrawTimeline', '_root', 'FocusPlayer', 'DoFocusGraph', 'Axis', '_visible', 'HelpBar', 'Show', 'ShowHidePlayButtons', 'FinalTab', 'm_playerButtonsEnabled', 'EnablePlayerButtons', 'Mc', 'this', 'Button', 'SwitchTab', 'MainTabs', 'RevealTab', 'SetSaveReplayEnableState', 'ShowSaveReplay'  
      &pushsdb 0							//'Resources'
      &pushone
      &pushsdbgv 1							//'_parent'
      &dcallmp 2							// DoDrawTimeline()
      &pushsdbgv 3							//'_root'
      &pushsdbgm 4							//'FocusPlayer'
      &pushone
      &dcallfp 5							// DoFocusGraph()
      &pushsdbgv 6							//'Axis'
      &pushsdb 7							//'_visible'
      &pushtrue
      &setMember
      &pushsdbgv 8							//'HelpBar'
      &pushsdb 7							//'_visible'
      &pushtrue
      &setMember
      &pushsdb 9							//'Show'
      &pushone
      &dcallfp 10							// ShowHidePlayButtons()
      &pushsdbgv 11							//'FinalTab'
      &not
      &jnz label2      
      &pushsdbgv 12							//'m_playerButtonsEnabled'
      &not
      &not
      &jnz label1      
      &pushzero
      &pushsdbgv 1							//'_parent'
      &dcallmp 13							// EnablePlayerButtons()
      &pushsdb 14							//'Mc'
      &pushthisgv
      &pushsdb 16							//'Button'
      &pushsdbgv 3							//'_root'
      &pushsdbgm 4							//'FocusPlayer'
      &add
      &getMember
      &varEquals
      &pushsdbgv 14							//'Mc'
      &pushone
      &dcallfp 17							// SwitchTab()
     label1:
      &jmp label3      
     label2:
      &pushsdbgv 18							//'MainTabs'
      &pushsdbgm 0							//'Resources'
      &pushone
      &pushsdbgv 18							//'MainTabs'
      &dcallmp 19							// RevealTab()
     label3:
      &pushsdbgv 11							//'FinalTab'
      &not
      &not
      &jnz label4      
      &pushfalse
      &pushone
      &dcallfp 20							// SetSaveReplayEnableState()
      &jmp label5      
     label4:
      &pushsdbgv 3							//'_root'
      &pushsdbgm 21							//'ShowSaveReplay'
      &pushone
      &dcallfp 20							// SetSaveReplayEnableState()
     label5:
      &stop
    &end // of frame 29

    &frame 39
      &constants 'Axis', '_visible', 'HelpBar', 'hide', 'ShowHidePlayButtons', 'FinalTab', '_root', 'ShowSaveReplay', 'SetSaveReplayEnableState', 'MainTabs', 'ShowAllTabs', 'MainButtons', 'Continue', 'Skip', '_hide', 'gotoAndPlay', '_fullyRevealed', 'gotoAndStop', 'LocalPlayerSlot', 'textColor', 'Timeline', 'GetStatsColumnColor', 'PlayerSlot0Focus', 'IsLocalPlayerAnObserver', 'ChangePlayerSlot0Focus', 'GetNumStatsColumns', 'PlayerFocus = ', 'PlayerSlot1', 'PlayerCarrots', 'PlayerSlot0', 'PlayerName', '$TimeLine:PlayerName:1', 'PlayerNameText', '$TimeLine:PlayerName:', 'SetPlayerFocus', 'GameCode'  
      &pushsdbgv 0							//'Axis'
      &pushsdb 1							//'_visible'
      &pushfalse
      &setMember
      &pushsdbgv 2							//'HelpBar'
      &pushsdb 1							//'_visible'
      &pushfalse
      &setMember
      &pushsdb 3							//'hide'
      &pushone
      &dcallfp 4							// ShowHidePlayButtons()
      &pushsdbgv 5							//'FinalTab'
      &not
      &not
      &jnz label1      
      &pushsdbgv 6							//'_root'
      &pushsdbgm 7							//'ShowSaveReplay'
      &pushone
      &dcallfp 8							// SetSaveReplayEnableState()
      &pushzero
      &pushsdbgv 9							//'MainTabs'
      &dcallmp 10							// ShowAllTabs()
      &pushsdbgv 11							//'MainButtons'
      &pushsdbgm 12							//'Continue'
      &pushsdb 1							//'_visible'
      &pushtrue
      &setMember
      &pushsdbgv 11							//'MainButtons'
      &pushsdbgm 13							//'Skip'
      &pushsdb 1							//'_visible'
      &pushfalse
      &setMember
      &pushsdb 14							//'_hide'
      &pushone
      &pushsdbgv 13							//'Skip'
      &dcallmp 15							// gotoAndPlay()
      &pushsdb 5							//'FinalTab'
      &pushtrue
      &setVariable
      &pushsdb 16							//'_fullyRevealed'
      &pushone
      &pushsdbgv 0							//'Axis'
      &dcallmp 17							// gotoAndStop()
     label1:
      &pushsdbgv 18							//'LocalPlayerSlot'
      &pushsdb 19							//'textColor'
      &pushzero
      &pushone
      &pushsdbgv 6							//'_root'
      &pushsdbgm 20							//'Timeline'
      &pushsdb 21							//'GetStatsColumnColor'
      &callMethod
      &setMember
      &pushsdbgv 22							//'PlayerSlot0Focus'
      &pushnull
      &equals
      &not
      &jnz label3      
      &pushzero
      &pushsdbgv 6							//'_root'
      &pushsdbgm 20							//'Timeline'
      &pushsdb 23							//'IsLocalPlayerAnObserver'
      &callMethod
      &not
      &jnz label2      
      &pushsdb 22							//'PlayerSlot0Focus'
      &pushzerosv
      &jmp label3      
     label2:
      &pushsdb 22							//'PlayerSlot0Focus'
      &pushone
      &setVariable
     label3:
      &pushsdb 24							//'ChangePlayerSlot0Focus'
      &function2  (r:2='Param') (r:1='_root')
        &pushsdb 22							//'PlayerSlot0Focus'
        &pushsdbgv 22							//'PlayerSlot0Focus'
        &push r:2        
        &add
        &setVariable
        &pushzero
        &push r:1        
        &pushsdbgm 20							//'Timeline'
        &pushsdb 25							//'GetNumStatsColumns'
        &callMethod
        &pushbyte 2
        &lessThan
        &not
        &jnz label4        
        &gotoLabel '_stats1'
        &play
        &jmp label8        
       label4:
        &pushzero
        &push r:1        
        &pushsdbgm 20							//'Timeline'
        &pushsdb 23							//'IsLocalPlayerAnObserver'
        &callMethod
        &not
        &jnz label5        
        &gotoLabel '_statsObserver'
        &play
        &jmp label8        
       label5:
        &pushsdb 26							//'PlayerFocus = '
        &pushsdbgv 22							//'PlayerSlot0Focus'
        &add
        &trace
        &pushzero
        &push r:1        
        &pushsdbgm 6							//'_root'
        &pushsdbgm 20							//'Timeline'
        &pushsdb 25							//'GetNumStatsColumns'
        &callMethod
        &pushbyte 3
        &lessThan
        &not
        &jnz label6        
        &pushsdbgv 27							//'PlayerSlot1'
        &pushsdb 1							//'_visible'
        &pushfalse
        &setMember
        &pushsdbgv 28							//'PlayerCarrots'
        &pushsdb 1							//'_visible'
        &pushfalse
        &setMember
        &pushsdbgv 29							//'PlayerSlot0'
        &pushsdb 30							//'PlayerName'
        &pushsdb 31							//'$TimeLine:PlayerName:1'
        &setMember
        &pushsdbgv 29							//'PlayerSlot0'
        &pushsdbgm 32							//'PlayerNameText'
        &pushsdb 19							//'textColor'
        &pushone
        &pushone
        &push r:1        
        &pushsdbgm 20							//'Timeline'
        &pushsdb 21							//'GetStatsColumnColor'
        &callMethod
        &setMember
        &jmp label7        
       label6:
        &pushsdbgv 29							//'PlayerSlot0'
        &pushsdb 30							//'PlayerName'
        &pushsdb 33							//'$TimeLine:PlayerName:'
        &pushsdbgv 22							//'PlayerSlot0Focus'
        &add
        &setMember
        &pushsdbgv 27							//'PlayerSlot1'
        &pushsdb 30							//'PlayerName'
        &pushsdb 33							//'$TimeLine:PlayerName:'
        &pushsdbgv 22							//'PlayerSlot0Focus'
        &pushone
        &add
        &add
        &setMember
        &pushsdbgv 29							//'PlayerSlot0'
        &pushsdbgm 32							//'PlayerNameText'
        &pushsdb 19							//'textColor'
        &pushsdbgv 22							//'PlayerSlot0Focus'
        &pushone
        &push r:1        
        &pushsdbgm 20							//'Timeline'
        &pushsdb 21							//'GetStatsColumnColor'
        &callMethod
        &setMember
        &pushsdbgv 27							//'PlayerSlot1'
        &pushsdbgm 32							//'PlayerNameText'
        &pushsdb 19							//'textColor'
        &pushsdbgv 22							//'PlayerSlot0Focus'
        &pushone
        &add
        &pushone
        &push r:1        
        &pushsdbgm 20							//'Timeline'
        &pushsdb 21							//'GetStatsColumnColor'
        &callMethod
        &setMember
       label7:
        &pushsdbgv 22							//'PlayerSlot0Focus'
        &pushsdb 34							//'SetPlayerFocus'
        &pushbyte 2
        &push r:1        
        &dcallmp 35							// GameCode()
       label8:
      &end // of function 

      &setVariable
      &pushzero
      &pushone
      &dcallfp 24							// ChangePlayerSlot0Focus()
    &end // of frame 39

    &placeMovieClip 131 &as 'AptTimeLine::StatsList'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'ListBox'
        &pushs '_Init'
        &pushssv 'AptTimeLine::InitGadgets'
        &pushs '_Load'
        &pushssv 'Apt/ListBox.wnd'
      &end
    &end // of placeMovieClip 131

    &frame 44
      &stop
    &end // of frame 44

    &frame 49
      &constants 'ChangePlayerSlot0Focus', 'PlayerSlot0Focus', 'PlayerSlot0', 'PlayerName', '$TimeLine:PlayerName:', 'PlayerNameText', 'textColor', 'Timeline', 'GetStatsColumnColor', 'PlayerSlot1', 'GetNumStatsColumns', 'PlayerSlot2', '_visible', 'PlayerCarrots._visible = ', 'PlayerCarrots', 'SetPlayerFocus', 'GameCode'  
      &pushsdb 0							//'ChangePlayerSlot0Focus'
      &function2  (r:2='Param') (r:1='_root')
        &pushsdb 1							//'PlayerSlot0Focus'
        &pushsdbgv 1							//'PlayerSlot0Focus'
        &push r:2        
        &add
        &setVariable
        &pushsdbgv 2							//'PlayerSlot0'
        &pushsdb 3							//'PlayerName'
        &pushsdb 4							//'$TimeLine:PlayerName:'
        &pushsdbgv 1							//'PlayerSlot0Focus'
        &add
        &setMember
        &pushsdbgv 2							//'PlayerSlot0'
        &pushsdbgm 5							//'PlayerNameText'
        &pushsdb 6							//'textColor'
        &pushsdbgv 1							//'PlayerSlot0Focus'
        &pushone
        &push r:1        
        &pushsdbgm 7							//'Timeline'
        &pushsdb 8							//'GetStatsColumnColor'
        &callMethod
        &setMember
        &pushsdbgv 9							//'PlayerSlot1'
        &pushsdb 3							//'PlayerName'
        &pushsdb 4							//'$TimeLine:PlayerName:'
        &pushsdbgv 1							//'PlayerSlot0Focus'
        &pushone
        &add
        &add
        &setMember
        &pushsdbgv 9							//'PlayerSlot1'
        &pushsdbgm 5							//'PlayerNameText'
        &pushsdb 6							//'textColor'
        &pushsdbgv 1							//'PlayerSlot0Focus'
        &pushone
        &add
        &pushone
        &push r:1        
        &pushsdbgm 7							//'Timeline'
        &pushsdb 8							//'GetStatsColumnColor'
        &callMethod
        &setMember
        &pushzero
        &push r:1        
        &pushsdbgm 7							//'Timeline'
        &pushsdb 10							//'GetNumStatsColumns'
        &callMethod
        &pushbyte 3
        &lessThan
        &not
        &not
        &jnz label1        
        &pushsdbgv 11							//'PlayerSlot2'
        &pushsdb 3							//'PlayerName'
        &pushsdb 4							//'$TimeLine:PlayerName:'
        &pushsdbgv 1							//'PlayerSlot0Focus'
        &pushbyte 2
        &add
        &add
        &setMember
        &pushsdbgv 11							//'PlayerSlot2'
        &pushsdbgm 5							//'PlayerNameText'
        &pushsdb 6							//'textColor'
        &pushsdbgv 1							//'PlayerSlot0Focus'
        &pushbyte 2
        &add
        &pushone
        &push r:1        
        &pushsdbgm 7							//'Timeline'
        &pushsdb 8							//'GetStatsColumnColor'
        &callMethod
        &setMember
        &jmp label2        
       label1:
        &pushsdbgv 11							//'PlayerSlot2'
        &pushsdb 12							//'_visible'
        &pushfalse
        &setMember
       label2:
        &pushsdb 13							//'PlayerCarrots._visible = '
        &pushzero
        &push r:1        
        &pushsdbgm 7							//'Timeline'
        &pushsdb 10							//'GetNumStatsColumns'
        &callMethod
        &pushbyte 4
        &lessThan
        &not
        &add
        &trace
        &pushsdbgv 14							//'PlayerCarrots'
        &pushsdb 12							//'_visible'
        &pushzero
        &push r:1        
        &pushsdbgm 7							//'Timeline'
        &pushsdb 10							//'GetNumStatsColumns'
        &callMethod
        &pushbyte 4
        &lessThan
        &not
        &setMember
        &pushsdbgv 1							//'PlayerSlot0Focus'
        &pushsdb 15							//'SetPlayerFocus'
        &pushbyte 2
        &push r:1        
        &dcallmp 16							// GameCode()
      &end // of function 

      &setVariable
      &pushzero
      &pushone
      &dcallfp 0							// ChangePlayerSlot0Focus()
    &end // of frame 49

    &frame 54
      &stop
    &end // of frame 54

    &frame 59
      &pushsgv 'LocalPlayerSlot1'
      &pushs 'textColor'
      &pushzero
      &pushone
      &pushsgv '_root'
      &pushsgm 'Timeline'
      &pushs 'GetStatsColumnColor'
      &callMethod
      &setMember
    &end // of frame 59

    &frame 64
      &stop
    &end // of frame 64
  &end // of defineMovieClip 147
  
  &exportAssets
    147 &as 'TimelineClass'
  &end // of exportAssets

  &frame 0
    &constants 'Call ', 'CodePrefix', '::', '(', ')', 'FSCommand:', 'Call(NP) ', 'Initialized', 'FSCommand:PlaySound', 'extern', 'InGame', 'InBetaDemo', 'InDreamMachineDemo', 'InitFunc', 'EnableComponents:', 'FSCommand:EnableComponents', 'DisableComponents:', 'FSCommand:DisableComponents', 'GetExtern(', ')=>', 'SetExtern(', '_parent', 'FindAbsolute', 'Timeline', 'Axis', 'GridArea', 'GridRender', '_graphMode', 'graphMode: ', '_root', 'AptTimeLine', 'colorInnerFrameA', '3399FF', 'colorInnerFrameB', 'colorLine', 'colorGadgetBox', 'colorGadgetGameSpeed', 'colorTextDark', '0x57512B', 'colorTextBright', '0x31210F', 'colorSubTextBright', '0xC2F47D', 'colorSubTextDark', '0x57842B', 'colorTitleA', '0xCDE47E', 'tabTextColorDark', '0x123B15', 'tabTextColorBritght', '0x8ac14d', 'OnInitialized', 'GameCode', 'InitialSetup', 'ShowSaveReplay', '1', 'AptTimeLine::ShowSaveReplay', 'GetExtern', '0', 'TotalPlayers', '4', 'AptTimeLine::NumOfPlayers', 'PlayerFaction', 'Array', 'i', 'Aliens', 'AptTimeLine::PlayerFaction:', 'FocusPlayer', 'CloseFrame'  
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

    &function2 DoDrawTimeline (r:2='Tab') (r:1='_root')
      &push r:1      
      &pushsdbgm 23							//'Timeline'
      &pushsdbgm 24							//'Axis'
      &pushsdbgm 25							//'GridArea'
      &pushsdbgm 26							//'GridRender'
      &pushsdb 27							//'_graphMode'
      &push r:2      
      &setMember
      &pushsdb 28							//'graphMode: '
      &push r:1      
      &pushsdbgm 23							//'Timeline'
      &pushsdbgm 24							//'Axis'
      &pushsdbgm 25							//'GridArea'
      &pushsdbgm 26							//'GridRender'
      &pushsdbgm 27							//'_graphMode'
      &add
      &trace
    &end // of function DoDrawTimeline

    &pushsdbgv 29							//'_root'
    &pushsdb 1							//'CodePrefix'
    &pushsdb 30							//'AptTimeLine'
    &setMember
    &pushsdb 31							//'colorInnerFrameA'
    &pushsdb 32							//'3399FF'
    &setVariable
    &pushsdb 33							//'colorInnerFrameB'
    &pushsdb 32							//'3399FF'
    &setVariable
    &pushsdb 34							//'colorLine'
    &pushsdb 32							//'3399FF'
    &setVariable
    &pushsdb 35							//'colorGadgetBox'
    &pushsdb 32							//'3399FF'
    &setVariable
    &pushsdb 36							//'colorGadgetGameSpeed'
    &pushsdb 32							//'3399FF'
    &setVariable
    &pushsdb 37							//'colorTextDark'
    &pushsdb 38							//'0x57512B'
    &setVariable
    &pushsdb 39							//'colorTextBright'
    &pushsdb 40							//'0x31210F'
    &setVariable
    &pushsdb 41							//'colorSubTextBright'
    &pushsdb 42							//'0xC2F47D'
    &setVariable
    &pushsdb 43							//'colorSubTextDark'
    &pushsdb 44							//'0x57842B'
    &setVariable
    &pushsdb 45							//'colorTitleA'
    &pushsdb 46							//'0xCDE47E'
    &setVariable
    &pushsdb 47							//'tabTextColorDark'
    &pushsdb 48							//'0x123B15'
    &setVariable
    &pushsdb 49							//'tabTextColorBritght'
    &pushsdb 50							//'0x8ac14d'
    &setVariable
    &pushsdbgv 29							//'_root'
    &pushsdbgm 7							//'Initialized'
    &not
    &not
    &jnz label13    
    &pushsdbgv 29							//'_root'
    &pushsdbgm 13							//'InitFunc'
    &pushundef
    &equals
    &not
    &jnz label12    
    &pushsdbgv 29							//'_root'
    &pushsdb 13							//'InitFunc'
    &function  (    )    
      &pushsdb 51							//'OnInitialized'
      &pushone
      &dcallfp 52							// GameCode()
    &end // of function 

    &setMember
   label12:
    &pushzero
    &dcallfp 53							// InitialSetup()
   label13:
    &pushsdbgv 29							//'_root'
    &pushsdb 54							//'ShowSaveReplay'
    &pushsdb 55							//'1'
    &pushsdb 56							//'AptTimeLine::ShowSaveReplay'
    &pushbyte 2
    &pushsdbgv 29							//'_root'
    &pushsdb 57							//'GetExtern'
    &callMethod
    &pushsdb 58							//'0'
    &equals
    &not
    &setMember
    &pushsdbgv 29							//'_root'
    &pushsdb 59							//'TotalPlayers'
    &pushsdb 60							//'4'
    &pushsdb 61							//'AptTimeLine::NumOfPlayers'
    &pushbyte 2
    &pushsdbgv 29							//'_root'
    &pushsdb 57							//'GetExtern'
    &callMethod
    &toNumber
    &setMember
    &pushsdbgv 29							//'_root'
    &pushsdb 62							//'PlayerFaction'
    &pushzero
    &pushsdb 63							//'Array'
    &new
    &setMember
    &pushsdb 64							//'i'
    &pushzerosv
   label14:
    &pushsdbgv 64							//'i'
    &pushsdbgv 29							//'_root'
    &pushsdbgm 59							//'TotalPlayers'
    &lessThan
    &not
    &jnz label15    
    &pushsdbgv 29							//'_root'
    &pushsdbgm 62							//'PlayerFaction'
    &pushsdbgv 64							//'i'
    &pushsdb 65							//'Aliens'
    &pushsdb 66							//'AptTimeLine::PlayerFaction:'
    &pushsdbgv 64							//'i'
    &add
    &pushbyte 2
    &pushsdbgv 29							//'_root'
    &pushsdb 57							//'GetExtern'
    &callMethod
    &setMember
    &pushsdb 64							//'i'
    &pushsdbgv 64							//'i'
    &increment
    &setVariable
    &jmp label14    
   label15:
    &pushsdbgv 29							//'_root'
    &pushsdb 67							//'FocusPlayer'
    &pushzero
    &setMember
    &pushsdbgv 29							//'_root'
    &pushsdb 68							//'CloseFrame'
    &function  (    )    
      &gotoLabel '_close'
      &play
    &end // of function 

    &setMember
    &gotoLabel '_open'
    &play
  &end // of frame 0
  
  &importAssets &from 'ShellContent.swf'
    'ShellContent_ShellBackground' &as 148
  &end // of importAssets

  &placeMovieClip 148 &as 'Background'
  
    &onClipEvent &construct
      &pushs 'vHideScreenBehind'
      &pushfalse
      &setVariable
      &pushs 'vAlpha'
      &pushfalse
      &setVariable
      &pushs 'vTitle'
      &pushssv '$TimelineCaps'
    &end
  &end // of placeMovieClip 148

  &defineMovieClip 149 // total frames: 0
  &end // of defineMovieClip 149
  
  &exportAssets
    149 &as '__Packages.DebugClass'
  &end // of exportAssets
  
  &initMovieClip 149
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
  &end // of initMovieClip 149

  &defineMovieClip 150 // total frames: 0
  &end // of defineMovieClip 150
  
  &exportAssets
    150 &as '__Packages.TimelineClass'
  &end // of exportAssets
  
  &initMovieClip 150
    &constants '_global', 'TimelineClass', 'debug', 'Enable', 'AptApiClass', 'm_apt', 'm_classRoot', 'InGame', '0', 'LocalPlayerIsObserver', 'SetExtern', 'OtherOnlineLan', 'ScreenMode', '6', 'NumStatsColumns', '4', 'NumOfPlayers', '0x9a73b6', 'PlayerColor:0', '0x009933', 'PlayerColor:1', '0x6633ff', 'PlayerColor:2', '0xffcc33', 'PlayerColor:3', 'GDI', 'PlayerFaction:0', 'NOD', 'PlayerFaction:1', 'Alien', 'PlayerFaction:2', 'PlayerFaction:3', 'm_numPlayers', 'GetExtern', 'm_numStatsColumns', 'MovieClip', 'prototype', 'onUnload', 'AptZombieClass', 'DeleteFunctions', 'Class', 'DeleteClass', 'IsLocalPlayerAnObserver', 'GetScreenMode', 'GetNumStatsColumns', 'GetPlayerFaction', 'PlayerFaction:', 'GetPlayerColor', 'PlayerColor:', 'GetStatsColumnColor', '0xffffff', 'TimeLine', 'DebugClass', 'ASSetPropFlags'  
    &pushglobalgv
    &pushsdbgm 1							//'TimelineClass'
    &not
    &not
    &jnz label4    
    &pushglobalgv
    &pushsdb 1							//'TimelineClass'
    &function2  () (r:1='this', r:2='super', r:3='_global')
      &pushzero
      &push r:2      
      &pushundef
      &callmp
      &pushtrue
      &pushone
      &pushsdbgv 1							//'TimelineClass'
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
      &pushsdbgv 1							//'TimelineClass'
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
      &pushsdb 8							//'0'
      &pushsdb 9							//'LocalPlayerIsObserver'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
      &pushsdb 11							//'OtherOnlineLan'
      &pushsdb 12							//'ScreenMode'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
      &pushsdb 13							//'6'
      &pushsdb 14							//'NumStatsColumns'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
      &pushsdb 15							//'4'
      &pushsdb 16							//'NumOfPlayers'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
      &pushsdb 17							//'0x9a73b6'
      &pushsdb 18							//'PlayerColor:0'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
      &pushsdb 19							//'0x009933'
      &pushsdb 20							//'PlayerColor:1'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
      &pushsdb 21							//'0x6633ff'
      &pushsdb 22							//'PlayerColor:2'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
      &pushsdb 23							//'0xffcc33'
      &pushsdb 24							//'PlayerColor:3'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
      &pushsdb 25							//'GDI'
      &pushsdb 26							//'PlayerFaction:0'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
      &pushsdb 27							//'NOD'
      &pushsdb 28							//'PlayerFaction:1'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
      &pushsdb 29							//'Alien'
      &pushsdb 30							//'PlayerFaction:2'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
      &pushsdb 27							//'NOD'
      &pushsdb 31							//'PlayerFaction:3'
      &pushbyte 2
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &dcallmp 10							// SetExtern()
     label1:
      &push r:1      
      &pushsdb 32							//'m_numPlayers'
      &pushsdb 16							//'NumOfPlayers'
      &pushone
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &pushsdb 33							//'GetExtern'
      &callMethod
      &toNumber
      &setMember
      &push r:1      
      &pushsdb 34							//'m_numStatsColumns'
      &pushsdb 14							//'NumStatsColumns'
      &pushone
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &pushsdb 33							//'GetExtern'
      &callMethod
      &toNumber
      &setMember
    &end // of function 

    &setRegister r:0
    &setMember
    &pushglobalgv
    &pushsdbgm 1							//'TimelineClass'
    &pushsdbgv 35							//'MovieClip'
    &extends
    &push r:0    
    &pushsdbgm 36							//'prototype'
    &setRegister r:1
    &pop
    &push r:1    
    &pushsdb 37							//'onUnload'
    &function2  () (r:1='this')
      &push r:1      
      &pushsdb 5							//'m_apt'
      &delete
      &pop
      &pushsdbgv 1							//'TimelineClass'
      &pushsdb 2							//'debug'
      &delete
      &pop
      &push r:1      
      &pushone
      &pushsdbgv 38							//'AptZombieClass'
      &dcallmp 39							// DeleteFunctions()
      &pushsdbgv 1							//'TimelineClass'
      &pushsdbgm 6							//'m_classRoot'
      &pushsdb 40							//'Class'
      &add
      &pushone
      &pushsdbgv 38							//'AptZombieClass'
      &dcallmp 41							// DeleteClass()
    &end // of function 

    &setMember
    &push r:1    
    &pushsdb 42							//'IsLocalPlayerAnObserver'
    &function2  () (r:1='this')
      &pushsdb 9							//'LocalPlayerIsObserver'
      &pushone
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &pushsdb 33							//'GetExtern'
      &callMethod
      &pushsdb 8							//'0'
      &equals
      &not
      &return
    &end // of function 

    &setMember
    &push r:1    
    &pushsdb 43							//'GetScreenMode'
    &function2  () (r:1='this')
      &pushsdb 12							//'ScreenMode'
      &pushone
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &pushsdb 33							//'GetExtern'
      &callMethod
      &return
    &end // of function 

    &setMember
    &push r:1    
    &pushsdb 44							//'GetNumStatsColumns'
    &function2  () (r:1='this')
      &push r:1      
      &pushsdbgm 34							//'m_numStatsColumns'
      &return
    &end // of function 

    &setMember
    &push r:1    
    &pushsdb 45							//'GetPlayerFaction'
    &function2  (r:2='playerIndex') (r:1='this')
      &pushsdb 46							//'PlayerFaction:'
      &push r:2      
      &add
      &pushone
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &pushsdb 33							//'GetExtern'
      &callMethod
      &return
    &end // of function 

    &setMember
    &push r:1    
    &pushsdb 47							//'GetPlayerColor'
    &function2  (r:2='playerIndex') (r:1='this')
      &pushsdb 48							//'PlayerColor:'
      &push r:2      
      &add
      &pushone
      &push r:1      
      &pushsdbgm 5							//'m_apt'
      &pushsdb 33							//'GetExtern'
      &callMethod
      &return
    &end // of function 

    &setMember
    &push r:1    
    &pushsdb 49							//'GetStatsColumnColor'
    &function2  (r:2='columnIndex') (r:1='this')
      &push r:2      
      &push r:1      
      &pushsdbgm 32							//'m_numPlayers'
      &lessThan
      &not
      &jnz label2      
      &push r:2      
      &pushone
      &push r:1      
      &pushsdb 47							//'GetPlayerColor'
      &callMethod
      &return
      &jmp label3      
     label2:
      &pushsdb 50							//'0xffffff'
      &return
     label3:
    &end // of function 

    &setMember
    &push r:0    
    &pushsdb 6							//'m_classRoot'
    &pushsdb 51							//'TimeLine'
    &setMember
    &push r:0    
    &pushsdb 2							//'debug'
    &pushsdbgv 1							//'TimelineClass'
    &pushsdbgm 6							//'m_classRoot'
    &pushone
    &pushsdb 52							//'DebugClass'
    &new
    &setMember
    &pushone
    &pushnull
    &pushglobalgv
    &pushsdbgm 1							//'TimelineClass'
    &pushsdbgm 36							//'prototype'
    &pushbyte 3
    &pushsdb 53							//'ASSetPropFlags'
    &callFunction
   label4:
    &pop
  &end // of initMovieClip 150

  &defineMovieClip 151 // total frames: 0
  &end // of defineMovieClip 151
  
  &exportAssets
    151 &as '__Packages.AptApiClass'
  &end // of exportAssets
  
  &initMovieClip 151
    &constants '_global', 'AptApiClass', 'm_codePrefix', 'Apt', '::', 'm_aptActive', 'InGame', '_target', 'RegisterScreen', 'Call', 'prototype', 'extern', 'Boolean', '__get__Active', 'AptCall ', '(', ')', 'debug', 'Trace', 'FSCommand:', 'CallAbs', 'CallAbs ', 'LoadVariables', 'Object', '_loadVariables', 'ConvertObjectMembers', 'LoadVariables:', 'Dump', ',', 'split', 'length', '=', 'Array', 'Number', 'ERROR: AptLoadVariables - Unable to convert : ', 'GetExtern', 'GetExtern(', ')=>', 'SetExtern', 'SetExtern(', 'ToggleExtern', 'PlaySound', 'FSCommand:PlaySound', 'IsCnc3Demo', 'Cnc3PcDemo', '0', 'IsSpecialEdition', '1', 'IsSpecialEditionExe', 'IsSpectatorClient', 'EnableEngineComponents', 'EnableEngineComponents:', 'FSCommand:EnableComponents', 'DisableEngineComponents', 'DisableEngineComponents:', 'FSCommand:DisableComponents', 'DoTrace', 'AptApiClass::', 'DebugClass', '', 'Active', 'addProperty', 'ASSetPropFlags'  
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

    &setRegister r:0
    &setMember
    &push r:0    
    &pushsdbgm 10							//'prototype'
    &setRegister r:1
    &pop
    &push r:0    
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
    &push r:1    
    &pushsdb 13							//'__get__Active'
    &function  (    )    
      &pushsdbgv 1							//'AptApiClass'
      &pushsdbgm 5							//'m_aptActive'
      &return
    &end // of function 

    &setMember
    &push r:1    
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
    &push r:1    
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
    &push r:1    
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
    &push r:1    
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
    &push r:0    
    &pushsdb 24							//'_loadVariables'
    &function2  (r:2='varName', r:1='obj') ()
      &push r:2      
      &push r:1      
      &loadVariables
      &push r:1      
      &return
    &end // of function 

    &setMember
    &push r:1    
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
    &push r:1    
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
    &push r:1    
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
    &push r:1    
    &pushsdb 41							//'PlaySound'
    &function2  (r:1='name') ()
      &pushsdb 42							//'FSCommand:PlaySound'
      &push r:1      
      &getURL2
    &end // of function 

    &setMember
    &push r:1    
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
    &push r:1    
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
    &push r:1    
    &pushsdb 48							//'IsSpecialEditionExe'
    &function2  (r:1='testDefault') ()
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
    &push r:1    
    &pushsdb 49							//'IsSpectatorClient'
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
      &pushsdbgm 49							//'IsSpectatorClient'
      &pushsdb 45							//'0'
      &equals
      &not
     label24:
      &return
    &end // of function 

    &setMember
    &push r:0    
    &pushsdb 50							//'EnableEngineComponents'
    &function2  (r:1='path') ()
      &pushsdb 51							//'EnableEngineComponents:'
      &push r:1      
      &add
      &pushone
      &pushsdbgv 1							//'AptApiClass'
      &pushsdbgm 17							//'debug'
      &dcallmp 18							// Trace()
      &pushsdb 52							//'FSCommand:EnableComponents'
      &push r:1      
      &getURL2
    &end // of function 

    &setMember
    &push r:0    
    &pushsdb 53							//'DisableEngineComponents'
    &function2  (r:1='path') ()
      &pushsdb 54							//'DisableEngineComponents:'
      &push r:1      
      &add
      &pushone
      &pushsdbgv 1							//'AptApiClass'
      &pushsdbgm 17							//'debug'
      &dcallmp 18							// Trace()
      &pushsdb 55							//'FSCommand:DisableComponents'
      &push r:1      
      &getURL2
    &end // of function 

    &setMember
    &push r:0    
    &pushsdb 11							//'extern'
    &pushsdb 56							//'DoTrace'
    &pushzero
    &pushsdb 6							//'InGame'
    &pushzero
    &pushsdb 44							//'Cnc3PcDemo'
    &pushzero
    &pushbyte 3
    &initObject
    &setMember
    &push r:0    
    &pushsdb 17							//'debug'
    &pushsdb 57							//'AptApiClass::'
    &pushone
    &pushsdb 58							//'DebugClass'
    &new
    &setMember
    &push r:0    
    &pushsdb 5							//'m_aptActive'
    &pushundef
    &setMember
    &push r:1    
    &pushsdb 2							//'m_codePrefix'
    &pushsdb 59							//''
    &setMember
    &function  (    )    
    &end // of function 

    &push r:1    
    &pushsdbgm 13							//'__get__Active'
    &pushsdb 60							//'Active'
    &pushbyte 3
    &push r:1    
    &pushsdb 61							//'addProperty'
    &callMethod
    &pushone
    &pushnull
    &pushglobalgv
    &pushsdbgm 1							//'AptApiClass'
    &pushsdbgm 10							//'prototype'
    &pushbyte 3
    &pushsdb 62							//'ASSetPropFlags'
    &callFunction
   label25:
    &pop
  &end // of initMovieClip 151

  &defineMovieClip 152 // total frames: 0
  &end // of defineMovieClip 152
  
  &exportAssets
    152 &as '__Packages.AptZombieClass'
  &end // of exportAssets
  
  &initMovieClip 152
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
  &end // of initMovieClip 152

  &defineMovieClip 153 // total frames: 0
  &end // of defineMovieClip 153
  
  &exportAssets
    153 &as '__Packages.ButtonClass'
  &end // of exportAssets
  
  &initMovieClip 153
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

    &setRegister r:0
    &setMember
    &pushglobalgv
    &pushsdbgm 1							//'ButtonClass'
    &pushsdbgv 31							//'MovieClip'
    &extends
    &push r:0    
    &pushsdbgm 32							//'prototype'
    &setRegister r:1
    &pop
    &push r:1    
    &pushsdb 33							//'SetText'
    &function2  (r:2='textString') (r:1='this')
      &push r:1      
      &pushsdb 2							//'m_text'
      &push r:2      
      &setMember
    &end // of function 

    &setMember
    &push r:1    
    &pushsdb 34							//'SetSfxClick'
    &function2  (r:2='sfx') (r:1='this')
      &push r:1      
      &pushsdb 35							//'m_sfxClick'
      &push r:2      
      &setMember
    &end // of function 

    &setMember
    &push r:1    
    &pushsdb 36							//'SetSfxRollOver'
    &function2  (r:2='sfx') (r:1='this')
      &push r:1      
      &pushsdb 37							//'m_sfxRollOver'
      &push r:2      
      &setMember
    &end // of function 

    &setMember
    &push r:1    
    &pushsdb 38							//'SetSfxRollOut'
    &function2  (r:2='sfx') (r:1='this')
      &push r:1      
      &pushsdb 39							//'m_sfxRollOut'
      &push r:2      
      &setMember
    &end // of function 

    &setMember
    &push r:1    
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
    &push r:1    
    &pushsdb 45							//'ClearMode'
    &function2  ('Void') (r:1='this')
      &pushsdb 46							//''
      &pushone
      &push r:1      
      &dcallmp 40							// SetMode()
    &end // of function 

    &setMember
    &push r:1    
    &pushsdb 47							//'GetMode'
    &function2  ('Void') (r:1='this')
      &push r:1      
      &pushsdbgm 41							//'m_mode'
      &return
    &end // of function 

    &setMember
    &push r:1    
    &pushsdb 48							//'onUnload'
    &function2  () (r:1='this')
      &push r:1      
      &pushone
      &pushsdbgv 49							//'AptZombieClass'
      &dcallmp 50							// DeleteFunctions()
    &end // of function 

    &setMember
    &push r:1    
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
    &push r:1    
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
    &push r:1    
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
    &push r:1    
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
    &push r:1    
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
    &push r:1    
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
    &push r:1    
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
    &push r:1    
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
    &push r:1    
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
    &push r:1    
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
    &push r:1    
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
    &push r:1    
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
    &push r:1    
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
    &push r:1    
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
    &push r:0    
    &pushsdb 82							//'debug'
    &pushsdb 83							//'ButtonClass::'
    &pushone
    &pushsdb 84							//'DebugClass'
    &new
    &setMember
    &push r:1    
    &pushsdb 42							//'m_state'
    &pushundef
    &setMember
    &push r:1    
    &pushsdb 41							//'m_mode'
    &pushundef
    &setMember
    &push r:1    
    &pushsdb 61							//'m_nextState'
    &pushundef
    &setMember
    &push r:1    
    &pushsdb 56							//'m_curStateMc'
    &pushundef
    &setMember
    &push r:1    
    &pushsdb 59							//'m_curTextMc'
    &pushundef
    &setMember
    &push r:1    
    &pushsdb 58							//'m_curBttnMc'
    &pushundef
    &setMember
    &push r:1    
    &pushsdb 35							//'m_sfxClick'
    &pushsdb 85							//'$ClickButton'
    &setMember
    &push r:1    
    &pushsdb 37							//'m_sfxRollOver'
    &pushsdb 86							//'$OverButton'
    &setMember
    &push r:1    
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
  &end // of initMovieClip 153
  
  &initMovieClip 147
    &constants 'TimelineClass', 'Object', 'registerClass'  
    &pushsdbgv 0							//'TimelineClass'
    &pushsdb 0							//'TimelineClass'
    &pushbyte 2
    &pushsdbgv 1							//'Object'
    &dcallmp 2							// registerClass()
  &end // of initMovieClip 147
  
  &initMovieClip 52
    &pushsgv 'ButtonClass'
    &pushs 'PlayerButton'
    &pushbyte 2
    &pushsgv 'Object'
    &pushs 'registerClass'
    &callmp
  &end // of initMovieClip 52
  
  &exportAssets
    147 &as 'TimelineClass'
  &end // of exportAssets
  
  &exportAssets
    147 &as 'TimelineClass'
  &end // of exportAssets
  
  &exportAssets
    147 &as 'TimelineClass'
  &end // of exportAssets
  
  &exportAssets
    147 &as 'TimelineClass'
  &end // of exportAssets

  &frame 13
    &stop
  &end // of frame 13
  
  &exportAssets
    147 &as 'TimelineClass'
  &end // of exportAssets
  
  &exportAssets
    147 &as 'TimelineClass'
  &end // of exportAssets
  
  &exportAssets
    147 &as 'TimelineClass'
  &end // of exportAssets
  
  &exportAssets
    147 &as 'TimelineClass'
  &end // of exportAssets

  &frame 17
    &stop
  &end // of frame 17
  
  &exportAssets
    147 &as 'TimelineClass'
  &end // of exportAssets
&end
