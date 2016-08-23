movie 'E:\Projects\CNC3\Data\APTBUI~1\034A3~1.0-D\pc\Output\YESNOD~1\\YESNOD~1.eaf' &compressed // flash 7, total frames: 1, frame rate: 30 fps, 1024x768 px

  &frame 0
    &constants 'closing', '_close', 'popup', 'gotoAndPlay', 'Close', 'onUnload', 'initialized', 'this', '_parent', 'OnContentLoaded', 'FSCommand:', ':OnInitialized', ''  
    &function Close (    )    
      &pushsdbgv 0							//'closing'
      &not
      &not
      &jnz label1      
      &pushsdb 0							//'closing'
      &pushtrue
      &setVariable
      &pushsdb 1							//'_close'
      &pushone
      &pushsdbgv 2							//'popup'
      &dcallmp 3							// gotoAndPlay()
     label1:
    &end // of function Close

    &function onUnload (    )    
      &pushsdb 4							//'Close'
      &delete2
      &pop
      &pushsdb 5							//'onUnload'
      &delete2
      &pop
    &end // of function onUnload

    &pushsdbgv 6							//'initialized'
    &not
    &not
    &jnz label2    
    &pushthisgv
    &pushone
    &pushsdbgv 8							//'_parent'
    &dcallmp 9							// OnContentLoaded()
    &pushsdb 0							//'closing'
    &pushfalse
    &setVariable
    &pushsdb 6							//'initialized'
    &pushtrue
    &setVariable
    &pushsdb 10							//'FSCommand:'
    &pushthisgv
    &toString
    &pushsdb 11							//':OnInitialized'
    &add
    &concat
    &pushsdb 12							//''
    &getURL2
   label2:
  &end // of frame 0

  &defineMovieClip 4 // total frames: 1
  &end // of defineMovieClip 4

  &defineMovieClip 5 // total frames: 20

    &frame 0
      &stop
    &end // of frame 0

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19
  &end // of defineMovieClip 5

  &placeMovieClip 5 &as 'backdrop'
  
    &onClipEvent &load
      &constants '_root', 'displayLeft', '', 'displayTop', 'displayWidth', 'displayHeight'  
      &pushsdbgv 0							//'_root'
      &pushsdbgm 1							//'displayLeft'
      &pushundef
      &equals
      &not
      &not
      &jnz label1      
      &pushsdb 2							//''
      &pushzero
      &pushsdbgv 0							//'_root'
      &pushsdbgm 1							//'displayLeft'
      &setProperty
      &pushsdb 2							//''
      &pushone
      &pushsdbgv 0							//'_root'
      &pushsdbgm 3							//'displayTop'
      &setProperty
      &pushsdb 2							//''
      &pushbyte 8
      &pushsdbgv 0							//'_root'
      &pushsdbgm 4							//'displayWidth'
      &setProperty
      &pushsdb 2							//''
      &pushbyte 9
      &pushsdbgv 0							//'_root'
      &pushsdbgm 5							//'displayHeight'
      &setProperty
     label1:
    &end
  &end // of placeMovieClip 5

  &defineMovieClip 8 // total frames: 15

    &frame 14
      &stop
    &end // of frame 14
  &end // of defineMovieClip 8

  &defineMovieClip 11 // total frames: 1
  &end // of defineMovieClip 11

  &defineMovieClip 14 // total frames: 1

    &frame 0
    &end // of frame 0
  &end // of defineMovieClip 14

  &defineMovieClip 15 // total frames: 1
  &end // of defineMovieClip 15

  &defineButton 17
  
    &on     &idleToOverUp
      &constants 'FSCommand:', '_parent', ':OnButtonRollOver', ''  
      &gotoLabel '_over'
      &play
      &pushsdb 0							//'FSCommand:'
      &pushsdbgv 1							//'_parent'
      &pushsdbgm 1							//'_parent'
      &pushsdbgm 1							//'_parent'
      &toString
      &pushsdb 2							//':OnButtonRollOver'
      &add
      &concat
      &pushsdb 3							//''
      &getURL2
    &end
  
    &on     &overDownToOverUp
      &constants 'FSCommand:', '_parent', ':OnButtonClicked', '', 'this', 'OnRelease', 'child', '_exit', 'gotoAndPlay'  
      &pushsdb 0							//'FSCommand:'
      &pushsdbgv 1							//'_parent'
      &pushsdbgm 1							//'_parent'
      &pushsdbgm 1							//'_parent'
      &toString
      &pushsdb 2							//':OnButtonClicked'
      &add
      &concat
      &pushsdb 3							//''
      &getURL2
      &pushthisgv
      &pushone
      &pushsdbgv 1							//'_parent'
      &dcallmp 5							// OnRelease()
      &gotoLabel '_down'
      &play
      &pushsdbgv 1							//'_parent'
      &enumerateValue
     label1:
      &setRegister r:0
      &pushnull
      &equals
      &jnz label3      
      &pushsdb 6							//'child'
      &push r:0      
      &setVariable
      &pushsdb 3							//''
      &pushbyte 13
      &getProperty
      &pushsdbgv 6							//'child'
      &equals
      &not
      &not
      &jnz label2      
      &pushsdb 7							//'_exit'
      &pushone
      &pushsdbgv 1							//'_parent'
      &pushsdbgv 6							//'child'
      &getMember
      &dcallmp 8							// gotoAndPlay()
     label2:
      &jmp label1      
     label3:
    &end
  
    &on     &overUpToIdle    ,&overDownToOutDown    ,&overDownToIdle
      &constants 'FSCommand:', '_parent', ':OnButtonRollOut', ''  
      &gotoLabel '_rollout'
      &play
      &pushsdb 0							//'FSCommand:'
      &pushsdbgv 1							//'_parent'
      &pushsdbgm 1							//'_parent'
      &pushsdbgm 1							//'_parent'
      &toString
      &pushsdb 2							//':OnButtonRollOut'
      &add
      &concat
      &pushsdb 3							//''
      &getURL2
    &end
  &end // of defineButton 17

  &defineMovieClip 20 // total frames: 1
  &end // of defineMovieClip 20

  &defineMovieClip 24 // total frames: 1
  &end // of defineMovieClip 24

  &defineMovieClip 28 // total frames: 1

    &frame 0
    &end // of frame 0
  &end // of defineMovieClip 28

  &defineMovieClip 29 // total frames: 51
  &end // of defineMovieClip 29

  &defineMovieClip 33 // total frames: 1

    &frame 0
    &end // of frame 0
  &end // of defineMovieClip 33

  &defineMovieClip 34 // total frames: 1
  &end // of defineMovieClip 34

  &defineMovieClip 35 // total frames: 93

    &frame 16
      &stop
    &end // of frame 16

    &frame 17
      &pushbyte 20
      &pushone
      &pushsgv 'overClip'
      &pushs 'gotoAndPlay'
      &callmp
    &end // of frame 17

    &frame 51
      &stop
    &end // of frame 51

    &frame 63
      &gotoLabel '_up'
      &play
    &end // of frame 63

    &frame 74
      &constants '', '_parent', 'popupAssign'  
      &pushsdb 0							//''
      &pushbyte 13
      &getProperty
      &pushone
      &pushsdbgv 1							//'_parent'
      &pushsdbgm 1							//'_parent'
      &pushsdbgm 1							//'_parent'
      &dcallmp 2							// popupAssign()
      &stop
    &end // of frame 74

    &frame 86
      &stop
    &end // of frame 86

    &frame 92
      &stop
    &end // of frame 92
  &end // of defineMovieClip 35

  &defineMovieClip 36 // total frames: 6

    &frame 0
      &constants 'Yes', 'FSCommand:', '_parent', ':OnYesClicked', '', 'No', ':OnNoClicked', '_close', 'gotoAndPlay', 'OnRelease', 'onUnload'  
      &function2 OnRelease (r:2='buttonClip') (r:1='_parent')
        &push r:2        
        &pushsdbgv 0							//'Yes'
        &equals
        &not
        &jnz label1        
        &pushsdb 1							//'FSCommand:'
        &push r:1        
        &pushsdbgm 2							//'_parent'
        &toString
        &pushsdb 3							//':OnYesClicked'
        &add
        &concat
        &pushsdb 4							//''
        &getURL2
        &jmp label2        
       label1:
        &push r:2        
        &pushsdbgv 5							//'No'
        &equals
        &not
        &jnz label2        
        &pushsdb 1							//'FSCommand:'
        &push r:1        
        &pushsdbgm 2							//'_parent'
        &toString
        &pushsdb 6							//':OnNoClicked'
        &add
        &concat
        &pushsdb 4							//''
        &getURL2
       label2:
        &pushsdb 7							//'_close'
        &pushone
        &push r:1        
        &dcallmp 8							// gotoAndPlay()
      &end // of function OnRelease

      &function onUnload (      )      
        &pushsdb 9							//'OnRelease'
        &delete2
        &pop
        &pushsdb 10							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

    &end // of frame 0

    &placeMovieClip 35 &as 'Yes'
    
      &onClipEvent &load
        &constants 'this', 'buttonName', '$', '_parent', ':YesButtonLabel'  
        &pushthisgv
        &pushsdb 1							//'buttonName'
        &pushsdb 2							//'$'
        &pushsdbgv 3							//'_parent'
        &pushsdbgm 3							//'_parent'
        &pushsdbgm 3							//'_parent'
        &toString
        &add
        &pushsdb 4							//':YesButtonLabel'
        &add
        &setMember
      &end
    &end // of placeMovieClip 35

    &placeMovieClip 35 &as 'No'
    
      &onClipEvent &load
        &constants 'this', 'buttonName', '$', '_parent', ':NoButtonLabel'  
        &pushthisgv
        &pushsdb 1							//'buttonName'
        &pushsdb 2							//'$'
        &pushsdbgv 3							//'_parent'
        &pushsdbgm 3							//'_parent'
        &pushsdbgm 3							//'_parent'
        &toString
        &add
        &pushsdb 4							//':NoButtonLabel'
        &add
        &setMember
      &end
    &end // of placeMovieClip 35

    &frame 5
      &stop
    &end // of frame 5
  &end // of defineMovieClip 36

  &defineMovieClip 39 // total frames: 1
  &end // of defineMovieClip 39

  &defineMovieClip 41 // total frames: 1
  &end // of defineMovieClip 41

  &defineMovieClip 42 // total frames: 40

    &frame 1
      &pushs '_open'
      &pushone
      &pushsgv '_parent'
      &pushsgm 'backdrop'
      &pushs 'gotoAndPlay'
      &callmp
    &end // of frame 1

    &frame 7
      &constants 'txtTitle', 'stringName', '$', '_parent', ':Title', 'txtMessage', ':Prompt'  
      &pushsdbgv 0							//'txtTitle'
      &pushsdb 1							//'stringName'
      &pushsdb 2							//'$'
      &pushsdbgv 3							//'_parent'
      &toString
      &add
      &pushsdb 4							//':Title'
      &add
      &setMember
      &pushsdbgv 5							//'txtMessage'
      &pushsdb 1							//'stringName'
      &pushsdb 2							//'$'
      &pushsdbgv 3							//'_parent'
      &toString
      &add
      &pushsdb 6							//':Prompt'
      &add
      &setMember
    &end // of frame 7

    &frame 27
      &stop
    &end // of frame 27

    &frame 28
      &pushs '_close'
      &pushone
      &pushsgv '_parent'
      &pushsgm 'backdrop'
      &pushs 'gotoAndPlay'
      &callmp
    &end // of frame 28

    &frame 39
      &stop
      &pushs 'FSCommand:'
      &pushsgv '_parent'
      &toString
      &pushs ':OnClosed'
      &add
      &concat
      &pushs ''
      &getURL2
    &end // of frame 39
  &end // of defineMovieClip 42
&end
