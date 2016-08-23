movie 'E:\Projects\CNC3\Data\APTBUI~1\034A3~1.0-D\pc\Output\TA87E3~1\\TACTIC~1.eaf' &compressed // flash 7, total frames: 59, frame rate: 30 fps, 1024x768 px

  &frame 0
    &constants 'FSCommand:', ':On', '_name', 'Clicked', '', '_fadeoutDisabled', '_fadeout1', 'gotoAndPlay', 'onEnterFrame', '_out', 'Frame', 'Resume', 'MaybeFadeButton', 'Options', 'saveEnabled', 'Save', 'loadEnabled', 'Load', 'restartEnabled', 'Restart', 'ExitMission', 'StartFade', 'stopDown', 'pendingClose', 'closing', 'dialogStage', 'OnButtonExecute', 'OnButtonRelease', 'Close', 'GetDialogStage', 'DisableSave', 'DisableLoad', 'DisableRestart', 'onUnload', 'initialized', 'this', '_parent', 'OnContentLoaded', ':OnInitialized'  
    &function2 OnButtonExecute (r:2='buttonClip') (r:1='this')
      &pushsdb 0							//'FSCommand:'
      &push r:1      
      &toString
      &pushsdb 1							//':On'
      &add
      &push r:2      
      &pushsdbgm 2							//'_name'
      &add
      &pushsdb 3							//'Clicked'
      &add
      &concat
      &pushsdb 4							//''
      &getURL2
    &end // of function OnButtonExecute

    &function2 MaybeFadeButton (r:1='buttonClipToFade', r:3='excludedButtonClip', r:2='isEnabled') ()
      &push r:1      
      &push r:3      
      &equals
      &not
      &not
      &jnz label3      
      &push r:2      
      &jnz label1      
      &pushsdb 5							//'_fadeoutDisabled'
      &jmp label2      
     label1:
      &pushsdb 6							//'_fadeout1'
     label2:
      &pushone
      &push r:1      
      &dcallmp 7							// gotoAndPlay()
     label3:
    &end // of function MaybeFadeButton

    &function2 StartFade (r:1='excludedButtonClip') ()
      &pushsdb 8							//'onEnterFrame'
      &delete2
      &pop
      &pushsdb 9							//'_out'
      &pushone
      &pushsdbgv 10							//'Frame'
      &dcallmp 7							// gotoAndPlay()
      &pushtrue
      &push r:1      
      &pushsdbgv 11							//'Resume'
      &pushbyte 3
      &dcallfp 12							// MaybeFadeButton()
      &pushtrue
      &push r:1      
      &pushsdbgv 13							//'Options'
      &pushbyte 3
      &dcallfp 12							// MaybeFadeButton()
      &pushsdbgv 14							//'saveEnabled'
      &push r:1      
      &pushsdbgv 15							//'Save'
      &pushbyte 3
      &dcallfp 12							// MaybeFadeButton()
      &pushsdbgv 16							//'loadEnabled'
      &push r:1      
      &pushsdbgv 17							//'Load'
      &pushbyte 3
      &dcallfp 12							// MaybeFadeButton()
      &pushsdbgv 18							//'restartEnabled'
      &push r:1      
      &pushsdbgv 19							//'Restart'
      &pushbyte 3
      &dcallfp 12							// MaybeFadeButton()
      &pushtrue
      &push r:1      
      &pushsdbgv 20							//'ExitMission'
      &pushbyte 3
      &dcallfp 12							// MaybeFadeButton()
    &end // of function StartFade

    &function2 OnButtonRelease (r:2='buttonClip') (r:1='this')
      &push r:2      
      &pushsdbgv 13							//'Options'
      &equals
      &dup
      &jnz label4      
      &pop
      &push r:2      
      &pushsdbgv 15							//'Save'
      &equals
     label4:
      &dup
      &jnz label5      
      &pop
      &push r:2      
      &pushsdbgv 17							//'Load'
      &equals
     label5:
      &dup
      &jnz label6      
      &pop
      &push r:2      
      &pushsdbgv 11							//'Resume'
      &equals
     label6:
      &not
      &jnz label7      
      &push r:2      
      &pushone
      &dcallfp 21							// StartFade()
      &pushundef
      &return
     label7:
      &push r:2      
      &pushsdb 22							//'stopDown'
      &pushtrue
      &setMember
      &pushsdb 0							//'FSCommand:'
      &push r:1      
      &toString
      &pushsdb 1							//':On'
      &add
      &push r:2      
      &pushsdbgm 2							//'_name'
      &add
      &pushsdb 3							//'Clicked'
      &add
      &concat
      &pushsdb 4							//''
      &getURL2
    &end // of function OnButtonRelease

    &function Close (    )    
      &pushsdbgv 23							//'pendingClose'
      &not
      &dup
      &not
      &jnz label8      
      &pop
      &pushsdbgv 24							//'closing'
      &not
     label8:
      &not
      &jnz label9      
      &pushsdb 23							//'pendingClose'
      &pushtrue
      &setVariable
     label9:
    &end // of function Close

    &function GetDialogStage (    )    
      &pushsdbgv 25							//'dialogStage'
      &toString
      &return
    &end // of function GetDialogStage

    &function DisableSave (    )    
      &pushsdb 14							//'saveEnabled'
      &pushfalse
      &setVariable
    &end // of function DisableSave

    &function DisableLoad (    )    
      &pushsdb 16							//'loadEnabled'
      &pushfalse
      &setVariable
    &end // of function DisableLoad

    &function DisableRestart (    )    
      &pushsdb 18							//'restartEnabled'
      &pushfalse
      &setVariable
    &end // of function DisableRestart

    &function onUnload (    )    
      &pushsdb 26							//'OnButtonExecute'
      &delete2
      &pop
      &pushsdb 27							//'OnButtonRelease'
      &delete2
      &pop
      &pushsdb 12							//'MaybeFadeButton'
      &delete2
      &pop
      &pushsdb 21							//'StartFade'
      &delete2
      &pop
      &pushsdb 28							//'Close'
      &delete2
      &pop
      &pushsdb 29							//'GetDialogStage'
      &delete2
      &pop
      &pushsdb 30							//'DisableSave'
      &delete2
      &pop
      &pushsdb 31							//'DisableLoad'
      &delete2
      &pop
      &pushsdb 32							//'DisableRestart'
      &delete2
      &pop
      &pushsdb 8							//'onEnterFrame'
      &delete2
      &pop
      &pushsdb 33							//'onUnload'
      &delete2
      &pop
    &end // of function onUnload

    &pushsdbgv 34							//'initialized'
    &not
    &not
    &jnz label10    
    &pushthisgv
    &pushone
    &pushsdbgv 36							//'_parent'
    &dcallmp 37							// OnContentLoaded()
    &pushsdb 23							//'pendingClose'
    &pushfalse
    &setVariable
    &pushsdb 24							//'closing'
    &pushfalse
    &setVariable
    &pushsdb 14							//'saveEnabled'
    &pushtrue
    &setVariable
    &pushsdb 16							//'loadEnabled'
    &pushtrue
    &setVariable
    &pushsdb 18							//'restartEnabled'
    &pushtrue
    &setVariable
    &pushsdb 34							//'initialized'
    &pushtrue
    &setVariable
    &pushsdb 0							//'FSCommand:'
    &pushthisgv
    &toString
    &pushsdb 38							//':OnInitialized'
    &add
    &concat
    &pushsdb 4							//''
    &getURL2
   label10:
  &end // of frame 0
  
  &importAssets &from 'libHUD.swf'
    'LoadMovieStage' &as 1
  &end // of importAssets

  &defineMovieClip 4 // total frames: 1
  &end // of defineMovieClip 4

  &defineMovieClip 7 // total frames: 1
  &end // of defineMovieClip 7

  &defineMovieClip 8 // total frames: 1

    &frame 0
    &end // of frame 0

    &placeMovieClip 7 
    
      &onClipEvent &load
        &constants 'text', '$', '_parent', ':Title'  
        &pushsdb 0							//'text'
        &pushsdb 1							//'$'
        &pushsdbgv 2							//'_parent'
        &pushsdbgm 2							//'_parent'
        &pushsdbgm 2							//'_parent'
        &toString
        &add
        &pushsdb 3							//':Title'
        &add
        &setVariable
      &end
    &end // of placeMovieClip 7
  &end // of defineMovieClip 8

  &defineMovieClip 9 // total frames: 39

    &frame 26
      &stop
    &end // of frame 26

    &frame 27
      &pushs '_close'
      &pushone
      &pushsgv 'titleGraphic'
      &pushs 'gotoAndPlay'
      &callmp
    &end // of frame 27

    &frame 38
      &pushs 'FSCommand:'
      &pushsgv '_parent'
      &toString
      &pushs ':OnClosed'
      &add
      &concat
      &pushs ''
      &getURL2
      &stop
    &end // of frame 38
  &end // of defineMovieClip 9

  &defineMovieClip 12 // total frames: 1
  &end // of defineMovieClip 12

  &defineMovieClip 14 // total frames: 1

    &frame 0
    &end // of frame 0
  &end // of defineMovieClip 14

  &defineMovieClip 15 // total frames: 1
  &end // of defineMovieClip 15

  &defineButton 17
  
    &on     &idleToOverUp
      &gotoLabel '_over'
      &play
      &pushs 'FSCommand:'
      &pushsgv '_parent'
      &toString
      &pushs ':OnButtonRollOver'
      &add
      &concat
      &pushs ''
      &getURL2
    &end
  
    &on     &overDownToOverUp
      &constants 'FSCommand:', '_parent', ':OnButtonClicked', '', 'this', 'OnButtonRelease'  
      &gotoLabel '_down'
      &play
      &pushsdb 0							//'FSCommand:'
      &pushsdbgv 1							//'_parent'
      &toString
      &pushsdb 2							//':OnButtonClicked'
      &add
      &concat
      &pushsdb 3							//''
      &getURL2
      &pushthisgv
      &pushone
      &pushsdbgv 1							//'_parent'
      &dcallmp 5							// OnButtonRelease()
    &end
  
    &on     &overUpToIdle    ,&overDownToOutDown    ,&overDownToIdle
      &pushs 'FSCommand:'
      &pushsgv '_parent'
      &toString
      &pushs ':OnButtonRollOut'
      &add
      &concat
      &pushs ''
      &getURL2
      &gotoLabel '_out'
      &play
    &end
  
    &on     &outDownToIdle
      &gotoLabel '_up'
    &end
  &end // of defineButton 17

  &defineMovieClip 20 // total frames: 1
  &end // of defineMovieClip 20

  &defineMovieClip 24 // total frames: 1
  &end // of defineMovieClip 24

  &defineMovieClip 27 // total frames: 1
  &end // of defineMovieClip 27

  &defineMovieClip 28 // total frames: 40
  &end // of defineMovieClip 28

  &defineMovieClip 30 // total frames: 1

    &frame 0
    &end // of frame 0
  &end // of defineMovieClip 30

  &defineMovieClip 31 // total frames: 1
  &end // of defineMovieClip 31

  &defineMovieClip 34 // total frames: 1
  &end // of defineMovieClip 34

  &defineMovieClip 36 // total frames: 1

    &frame 0
    &end // of frame 0
  &end // of defineMovieClip 36

  &defineMovieClip 37 // total frames: 1
  &end // of defineMovieClip 37

  &defineMovieClip 38 // total frames: 107

    &frame 24
      &stop
    &end // of frame 24

    &frame 25
      &pushbyte 20
      &pushone
      &pushsgv 'overClip'
      &pushsgm 'overClipBar'
      &pushs 'gotoAndPlay'
      &callmp
    &end // of frame 25

    &frame 48
      &stop
    &end // of frame 48

    &frame 53
      &pushsgv 'stopDown'
      &not
      &jnz label1      
      &gotoLabel '_up'
     label1:
    &end // of frame 53

    &frame 58
      &pushthisgv
      &pushone
      &pushsgv '_parent'
      &pushs 'OnButtonExecute'
      &callmp
      &stop
    &end // of frame 58

    &frame 68
      &gotoLabel '_up'
      &play
    &end // of frame 68

    &frame 69
      &pushs 'FADEOUT'
      &trace
    &end // of frame 69

    &frame 76
      &stop
    &end // of frame 76

    &frame 77
      &pushs 'FADEOUT1'
      &trace
    &end // of frame 77

    &frame 85
      &stop
    &end // of frame 85

    &frame 99
      &stop
    &end // of frame 99

    &frame 106
      &stop
    &end // of frame 106
  &end // of defineMovieClip 38

  &placeMovieClip 38 &as 'Options'
  
    &onClipEvent &load
      &pushthisgv
      &pushs 'ButtonName'
      &pushs '$'
      &pushsgv '_parent'
      &toString
      &add
      &pushs ':Settings'
      &add
      &setMember
    &end
  &end // of placeMovieClip 38

  &placeMovieClip 38 &as 'Save'
  
    &onClipEvent &load
      &constants 'this', 'ButtonName', '$', '_parent', ':SaveGame', 'saveEnabled'  
      &pushthisgv
      &pushsdb 1							//'ButtonName'
      &pushsdb 2							//'$'
      &pushsdbgv 3							//'_parent'
      &toString
      &add
      &pushsdb 4							//':SaveGame'
      &add
      &setMember
      &pushsdbgv 3							//'_parent'
      &pushsdbgm 5							//'saveEnabled'
      &not
      &not
      &jnz label1      
      &gotoLabel '_fadeinDisabled'
      &play
     label1:
    &end
  &end // of placeMovieClip 38

  &placeMovieClip 38 &as 'Load'
  
    &onClipEvent &load
      &constants 'this', 'ButtonName', '$', '_parent', ':LoadGame', 'loadEnabled'  
      &pushthisgv
      &pushsdb 1							//'ButtonName'
      &pushsdb 2							//'$'
      &pushsdbgv 3							//'_parent'
      &toString
      &add
      &pushsdb 4							//':LoadGame'
      &add
      &setMember
      &pushsdbgv 3							//'_parent'
      &pushsdbgm 5							//'loadEnabled'
      &not
      &not
      &jnz label1      
      &gotoLabel '_fadeinDisabled'
      &play
     label1:
    &end
  &end // of placeMovieClip 38

  &placeMovieClip 38 &as 'Restart'
  
    &onClipEvent &load
      &constants 'this', 'ButtonName', '$', '_parent', ':Restart', 'restartEnabled'  
      &pushthisgv
      &pushsdb 1							//'ButtonName'
      &pushsdb 2							//'$'
      &pushsdbgv 3							//'_parent'
      &toString
      &add
      &pushsdb 4							//':Restart'
      &add
      &setMember
      &pushsdbgv 3							//'_parent'
      &pushsdbgm 5							//'restartEnabled'
      &not
      &not
      &jnz label1      
      &gotoLabel '_fadeinDisabled'
      &play
     label1:
    &end
  &end // of placeMovieClip 38

  &placeMovieClip 38 &as 'ExitMission'
  
    &onClipEvent &load
      &pushthisgv
      &pushs 'ButtonName'
      &pushs '$'
      &pushsgv '_parent'
      &toString
      &add
      &pushs ':ExitMission'
      &add
      &setMember
    &end
  &end // of placeMovieClip 38

  &placeMovieClip 38 &as 'Resume'
  
    &onClipEvent &load
      &pushthisgv
      &pushs 'ButtonName'
      &pushs '$'
      &pushsgv '_parent'
      &toString
      &add
      &pushs ':ResumeGame'
      &add
      &setMember
    &end
  &end // of placeMovieClip 38

  &defineMovieClip 40 // total frames: 1
  &end // of defineMovieClip 40

  &defineMovieClip 41 // total frames: 20

    &frame 0
      &stop
    &end // of frame 0

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19
  &end // of defineMovieClip 41

  &frame 45
    &constants 'pendingClose', 'closing', 'StartFade'  
    &function onEnterFrame (    )    
      &pushsdbgv 0							//'pendingClose'
      &dup
      &not
      &jnz label1      
      &pop
      &pushsdbgv 1							//'closing'
      &not
     label1:
      &not
      &jnz label2      
      &pushsdb 1							//'closing'
      &pushtrue
      &setVariable
      &pushzero
      &dcallfp 2							// StartFade()
     label2:
    &end // of function onEnterFrame

  &end // of frame 45

  &frame 45
    &stop
  &end // of frame 45

  &frame 58
    &pushs 'FSCommand:'
    &pushthisgv
    &toString
    &pushs ':OnClosed'
    &add
    &concat
    &pushs ''
    &getURL2
    &stop
  &end // of frame 58
&end
