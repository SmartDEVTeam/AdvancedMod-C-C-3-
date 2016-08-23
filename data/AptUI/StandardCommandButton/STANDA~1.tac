movie 'E:\Projects\CNC3\Data\APTBUI~1\034A3~1.0-D\pc\Output\STANDA~1\\STANDA~1.eaf' &compressed // flash 7, total frames: 50, frame rate: 30 fps, 1024x768 px

  &frame 0
    &constants 'isMouseOver', '_hide', 'RollOver', 'gotoAndPlay', 'RollOverTop', 'isEnabled', '', 'numberText', '_visible', 'isSelected', 'IS_SELECTED:  ', 'selectedOverlay', 'Show', 'Hide', 'timerVisible', 'timerOverlay0', 'timerOverlay1', 'Math', 'round', 'gotoAndStop', 'imageTint', 'image', 'colorizer', 'setRGB', 'healthBar', 'useAlternateColor', '_normal', '_alternate', 'bg', 'frame', 'SetEnabled', 'SetVisibility', 'SetNumberVisibility', 'SetSelected', 'SetTimerVisibility', 'SetTimerValue', 'SetImageTint', 'SetHealthBarVisibility', 'SetHealthBarValue', 'UseAlternateColors', 'onUnload', 'extern', 'InGame', '_root', 'GetCurrentFaction', 'Gdi', 'initialized', 'this', '_parent', 'OnContentLoaded', 'FSCommand:', ':OnInitialized'  
    &function2 SetEnabled (r:2='enableArg') ()
      &push r:2      
      &toNumber
      &pushzero
      &equals
      &not
      &setRegister r:1
      &pop
      &push r:1      
      &not
      &jnz label1      
      &gotoLabel '_up'
      &play
      &jmp label3      
     label1:
      &pushsdbgv 0							//'isMouseOver'
      &not
      &jnz label2      
      &pushsdb 1							//'_hide'
      &pushone
      &pushsdbgv 2							//'RollOver'
      &dcallmp 3							// gotoAndPlay()
      &pushsdb 1							//'_hide'
      &pushone
      &pushsdbgv 4							//'RollOverTop'
      &dcallmp 3							// gotoAndPlay()
     label2:
      &gotoLabel '_disabled'
      &play
     label3:
      &pushsdb 5							//'isEnabled'
      &push r:1      
      &setVariable
    &end // of function SetEnabled

    &function2 SetVisibility (r:1='visArg') ()
      &pushsdb 6							//''
      &pushbyte 7
      &push r:1      
      &toNumber
      &pushzero
      &equals
      &not
      &setProperty
    &end // of function SetVisibility

    &function2 SetNumberVisibility (r:1='visArg') ()
      &pushsdbgv 7							//'numberText'
      &pushsdb 8							//'_visible'
      &push r:1      
      &toNumber
      &pushzero
      &equals
      &not
      &setMember
    &end // of function SetNumberVisibility

    &function2 SetSelected (r:2='selectArg') ()
      &push r:2      
      &toNumber
      &pushzero
      &equals
      &not
      &setRegister r:1
      &pop
      &pushsdb 9							//'isSelected'
      &push r:1      
      &setVariable
      &pushsdb 10							//'IS_SELECTED:  '
      &pushsdbgv 9							//'isSelected'
      &add
      &trace
      &pushsdbgv 9							//'isSelected'
      &not
      &jnz label4      
      &pushzero
      &pushsdbgv 11							//'selectedOverlay'
      &dcallmp 12							// Show()
      &jmp label5      
     label4:
      &pushzero
      &pushsdbgv 11							//'selectedOverlay'
      &dcallmp 13							// Hide()
     label5:
    &end // of function SetSelected

    &function2 SetTimerVisibility (r:1='visArg') ()
      &pushsdb 14							//'timerVisible'
      &push r:1      
      &toNumber
      &pushzero
      &equals
      &not
      &setVariable
      &pushsdbgv 15							//'timerOverlay0'
      &pushsdb 8							//'_visible'
      &pushsdbgv 14							//'timerVisible'
      &setMember
      &pushsdbgv 16							//'timerOverlay1'
      &pushsdb 8							//'_visible'
      &pushsdbgv 14							//'timerVisible'
      &setMember
    &end // of function SetTimerVisibility

    &function2 SetTimerValue (r:3='valArg') ()
      &push r:3      
      &toNumber
      &setRegister r:2
      &pop
      &push r:2      
      &pushbyte 100
      &multiply
      &pushone
      &pushsdbgv 17							//'Math'
      &pushsdb 18							//'round'
      &callMethod
      &pushone
      &add
      &setRegister r:1
      &pop
      &push r:1      
      &pushone
      &pushsdbgv 15							//'timerOverlay0'
      &dcallmp 19							// gotoAndStop()
      &push r:1      
      &pushone
      &pushsdbgv 16							//'timerOverlay1'
      &dcallmp 19							// gotoAndStop()
    &end // of function SetTimerValue

    &function2 SetImageTint (r:2='tintColorArg') ()
      &push r:2      
      &toNumber
      &setRegister r:1
      &pop
      &pushsdb 20							//'imageTint'
      &push r:1      
      &setVariable
      &pushsdbgv 21							//'image'
      &pushsdbgm 22							//'colorizer'
      &pushundef
      &equals
      &not
      &not
      &jnz label6      
      &pushsdbgv 20							//'imageTint'
      &pushone
      &pushsdbgv 21							//'image'
      &pushsdbgm 22							//'colorizer'
      &dcallmp 23							// setRGB()
     label6:
    &end // of function SetImageTint

    &function2 SetHealthBarVisibility (r:2='visArg') ()
      &push r:2      
      &toNumber
      &pushzero
      &equals
      &not
      &setRegister r:1
      &pop
      &pushsdbgv 24							//'healthBar'
      &pushsdb 8							//'_visible'
      &push r:1      
      &setMember
    &end // of function SetHealthBarVisibility

    &function2 SetHealthBarValue (r:2='valueArg') ()
      &push r:2      
      &toNumber
      &setRegister r:1
      &pop
      &push r:1      
      &pushbyte 100
      &multiply
      &pushone
      &add
      &pushone
      &pushsdbgv 24							//'healthBar'
      &dcallmp 19							// gotoAndStop()
    &end // of function SetHealthBarValue

    &function2 UseAlternateColors (r:2='arg') ()
      &pushsdb 25							//'useAlternateColor'
      &push r:2      
      &toNumber
      &pushzero
      &equals
      &not
      &setVariable
      &pushsdbgv 25							//'useAlternateColor'
      &jnz label7      
      &pushsdb 26							//'_normal'
      &jmp label8      
     label7:
      &pushsdb 27							//'_alternate'
     label8:
      &setRegister r:1
      &pop
      &push r:1      
      &pushone
      &pushsdbgv 28							//'bg'
      &pushsdbgm 21							//'image'
      &dcallmp 3							// gotoAndPlay()
      &push r:1      
      &pushone
      &pushsdbgv 29							//'frame'
      &pushsdbgm 21							//'image'
      &dcallmp 3							// gotoAndPlay()
    &end // of function UseAlternateColors

    &function onUnload (    )    
      &pushsdb 30							//'SetEnabled'
      &delete2
      &pop
      &pushsdb 31							//'SetVisibility'
      &delete2
      &pop
      &pushsdb 32							//'SetNumberVisibility'
      &delete2
      &pop
      &pushsdb 33							//'SetSelected'
      &delete2
      &pop
      &pushsdb 34							//'SetTimerVisibility'
      &delete2
      &pop
      &pushsdb 35							//'SetTimerValue'
      &delete2
      &pop
      &pushsdb 36							//'SetImageTint'
      &delete2
      &pop
      &pushsdb 37							//'SetHealthBarVisibility'
      &delete2
      &pop
      &pushsdb 38							//'SetHealthBarValue'
      &delete2
      &pop
      &pushsdb 39							//'UseAlternateColors'
      &delete2
      &pop
      &pushsdb 40							//'onUnload'
      &delete2
      &pop
    &end // of function onUnload

    &pushsdbgv 41							//'extern'
    &pushsdbgm 42							//'InGame'
    &not
    &not
    &jnz label9    
    &pushsdbgv 43							//'_root'
    &pushsdb 44							//'GetCurrentFaction'
    &function  (    )    
      &pushsdb 45							//'Gdi'
      &return
    &end // of function 

    &setMember
    &gotoLabel '_up'
    &play
   label9:
    &pushsdbgv 46							//'initialized'
    &not
    &not
    &jnz label10    
    &pushthisgv
    &pushone
    &pushsdbgv 48							//'_parent'
    &dcallmp 49							// OnContentLoaded()
    &pushsdbgv 24							//'healthBar'
    &pushsdb 8							//'_visible'
    &pushfalse
    &setMember
    &pushsdb 25							//'useAlternateColor'
    &pushfalse
    &setVariable
    &pushsdb 5							//'isEnabled'
    &pushfalse
    &setVariable
    &pushsdb 9							//'isSelected'
    &pushfalse
    &setVariable
    &pushsdb 0							//'isMouseOver'
    &pushfalse
    &setVariable
    &pushsdb 14							//'timerVisible'
    &pushfalse
    &setVariable
    &pushsdbgv 7							//'numberText'
    &pushsdb 8							//'_visible'
    &pushfalse
    &setMember
    &pushsdb 20							//'imageTint'
    &pushlong 16777215
    &setVariable
    &pushbyte 101
    &pushone
    &pushsdbgv 24							//'healthBar'
    &dcallmp 19							// gotoAndStop()
    &pushsdb 46							//'initialized'
    &pushtrue
    &setVariable
    &pushsdb 50							//'FSCommand:'
    &pushthisgv
    &toString
    &pushsdb 51							//':OnInitialized'
    &add
    &concat
    &pushsdb 6							//''
    &getURL2
    &pushsdbgv 41							//'extern'
    &pushsdbgm 42							//'InGame'
    &not
    &not
    &jnz label10    
    &pushsdb 5							//'isEnabled'
    &pushtrue
    &setVariable
    &pushone
    &pushone
    &dcallfp 37							// SetHealthBarVisibility()
    &pushbyte 100
    &random
    &pushbyte 100
    &divide
    &pushone
    &dcallfp 38							// SetHealthBarValue()
   label10:
  &end // of frame 0

  &defineButton 2
  
    &on     &overUpToOverDown
      &pushsgv 'isEnabled'
      &not
      &jnz label1      
      &gotoLabel '_down'
      &play
     label1:
    &end
  
    &on     &overDownToOverUp
      &pushsgv 'isEnabled'
      &not
      &jnz label1      
      &gotoLabel '_release'
      &play
     label1:
      &pushs 'FSCommand:'
      &pushthisgv
      &toString
      &pushs ':OnClicked'
      &add
      &concat
      &pushs ''
      &getURL2
    &end
  
    &on     &idleToOverUp
      &constants 'isEnabled', '_show', 'RollOver', 'gotoAndPlay', 'RollOverTop', 'isMouseOver', 'FSCommand:', 'this', ':OnRollOver', ''  
      &pushsdbgv 0							//'isEnabled'
      &not
      &jnz label1      
      &gotoLabel '_over'
      &play
      &pushsdb 1							//'_show'
      &pushone
      &pushsdbgv 2							//'RollOver'
      &dcallmp 3							// gotoAndPlay()
      &pushsdb 1							//'_show'
      &pushone
      &pushsdbgv 4							//'RollOverTop'
      &dcallmp 3							// gotoAndPlay()
     label1:
      &pushsdb 5							//'isMouseOver'
      &pushtrue
      &setVariable
      &pushsdb 6							//'FSCommand:'
      &pushthisgv
      &toString
      &pushsdb 8							//':OnRollOver'
      &add
      &concat
      &pushsdb 9							//''
      &getURL2
    &end
  
    &on     &overUpToIdle    ,&overDownToOutDown    ,&overDownToIdle
      &constants 'isEnabled', '_hide', 'RollOver', 'gotoAndPlay', 'RollOverTop', 'isMouseOver', 'FSCommand:', 'this', ':OnRollOut', ''  
      &pushsdbgv 0							//'isEnabled'
      &not
      &jnz label1      
      &gotoLabel '_up'
      &play
      &pushsdb 1							//'_hide'
      &pushone
      &pushsdbgv 2							//'RollOver'
      &dcallmp 3							// gotoAndPlay()
      &pushsdb 1							//'_hide'
      &pushone
      &pushsdbgv 4							//'RollOverTop'
      &dcallmp 3							// gotoAndPlay()
     label1:
      &pushsdb 5							//'isMouseOver'
      &pushfalse
      &setVariable
      &pushsdb 6							//'FSCommand:'
      &pushthisgv
      &toString
      &pushsdb 8							//':OnRollOut'
      &add
      &concat
      &pushsdb 9							//''
      &getURL2
    &end
  &end // of defineButton 2

  &defineMovieClip 5 // total frames: 1
  &end // of defineMovieClip 5

  &defineMovieClip 6 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'initialized', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &push r:1        
        &gotoAndPlay      &end // of function OnCurrentFactionChanged

      &function2 onUnload () (r:1='this', r:2='_root')
        &push r:1        
        &pushone
        &push r:2        
        &dcallmp 0							// DetachFactionObserver()
        &pushsdb 1							//'OnCurrentFactionChanged'
        &delete2
        &pop
        &pushsdb 2							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 3							//'initialized'
      &not
      &not
      &jnz label1      
      &pushzero
      &pushsdbgv 4							//'_root'
      &pushsdb 5							//'GetCurrentFaction'
      &callMethod
      &gotoAndPlay      &pushthisgv
      &pushone
      &pushsdbgv 4							//'_root'
      &dcallmp 7							// AttachFactionObserver()
      &pushsdb 3							//'initialized'
      &pushtrue
      &setVariable
     label1:
    &end // of frame 0

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 6

  &defineMovieClip 95 // total frames: 101

    &frame 0
      &pushs ''
      &pushbyte 7
      &pushsgv '_parent'
      &pushsgm 'timerVisible'
      &setProperty
      &stop
    &end // of frame 0
  &end // of defineMovieClip 95

  &defineMovieClip 102 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'initialized', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &push r:1        
        &gotoAndPlay      &end // of function OnCurrentFactionChanged

      &function2 onUnload () (r:1='this', r:2='_root')
        &push r:1        
        &pushone
        &push r:2        
        &dcallmp 0							// DetachFactionObserver()
        &pushsdb 1							//'OnCurrentFactionChanged'
        &delete2
        &pop
        &pushsdb 2							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 3							//'initialized'
      &not
      &not
      &jnz label1      
      &pushzero
      &pushsdbgv 4							//'_root'
      &pushsdb 5							//'GetCurrentFaction'
      &callMethod
      &gotoAndPlay      &pushthisgv
      &pushone
      &pushsdbgv 4							//'_root'
      &dcallmp 7							// AttachFactionObserver()
      &pushsdb 3							//'initialized'
      &pushtrue
      &setVariable
     label1:
    &end // of frame 0

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 102

  &defineMovieClip 109 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'initialized', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &push r:1        
        &gotoAndPlay      &end // of function OnCurrentFactionChanged

      &function2 onUnload () (r:1='this', r:2='_root')
        &push r:1        
        &pushone
        &push r:2        
        &dcallmp 0							// DetachFactionObserver()
        &pushsdb 1							//'OnCurrentFactionChanged'
        &delete2
        &pop
        &pushsdb 2							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 3							//'initialized'
      &not
      &not
      &jnz label1      
      &pushzero
      &pushsdbgv 4							//'_root'
      &pushsdb 5							//'GetCurrentFaction'
      &callMethod
      &gotoAndPlay      &pushthisgv
      &pushone
      &pushsdbgv 4							//'_root'
      &dcallmp 7							// AttachFactionObserver()
      &pushsdb 3							//'initialized'
      &pushtrue
      &setVariable
     label1:
    &end // of frame 0

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 109

  &defineMovieClip 116 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'initialized', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &push r:1        
        &gotoAndPlay      &end // of function OnCurrentFactionChanged

      &function2 onUnload () (r:1='this', r:2='_root')
        &push r:1        
        &pushone
        &push r:2        
        &dcallmp 0							// DetachFactionObserver()
        &pushsdb 1							//'OnCurrentFactionChanged'
        &delete2
        &pop
        &pushsdb 2							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 3							//'initialized'
      &not
      &not
      &jnz label1      
      &pushzero
      &pushsdbgv 4							//'_root'
      &pushsdb 5							//'GetCurrentFaction'
      &callMethod
      &gotoAndPlay      &pushthisgv
      &pushone
      &pushsdbgv 4							//'_root'
      &dcallmp 7							// AttachFactionObserver()
      &pushsdb 3							//'initialized'
      &pushtrue
      &setVariable
     label1:
    &end // of frame 0

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 116

  &defineMovieClip 119 // total frames: 1
  &end // of defineMovieClip 119

  &defineMovieClip 120 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'initialized', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &push r:1        
        &gotoAndPlay      &end // of function OnCurrentFactionChanged

      &function2 onUnload () (r:1='this', r:2='_root')
        &push r:1        
        &pushone
        &push r:2        
        &dcallmp 0							// DetachFactionObserver()
        &pushsdb 1							//'OnCurrentFactionChanged'
        &delete2
        &pop
        &pushsdb 2							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 3							//'initialized'
      &not
      &not
      &jnz label1      
      &pushzero
      &pushsdbgv 4							//'_root'
      &pushsdb 5							//'GetCurrentFaction'
      &callMethod
      &gotoAndPlay      &pushthisgv
      &pushone
      &pushsdbgv 4							//'_root'
      &dcallmp 7							// AttachFactionObserver()
      &pushsdb 3							//'initialized'
      &pushtrue
      &setVariable
     label1:
    &end // of frame 0

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 120

  &defineMovieClip 121 // total frames: 44

    &frame 0
      &stop
    &end // of frame 0

    &placeMovieClip 116 
    
      &onClipEvent &load
        &pushs ''
        &pushbyte 7
        &pushfalse
        &setProperty
      &end
    &end // of placeMovieClip 116

    &frame 13
      &stop
    &end // of frame 13

    &frame 43
      &stop
    &end // of frame 43
  &end // of defineMovieClip 121
  
  &importAssets &from 'libHUD.swf'
    'RenderImageDisabled' &as 122
  &end // of importAssets

  &placeMovieClip 122 &as 'disabledImage'
  
    &onClipEvent &construct
      &pushs '_type'
      &pushssv 'RenderImageDisabled'
      &pushs '_imageMap'
      &pushssv ''
    &end
  
    &onClipEvent &load
      &pushs '_imageMap'
      &pushsgv '_parent'
      &toString
      &pushs ':Image'
      &add
      &setVariable
    &end
  &end // of placeMovieClip 122

  &defineMovieClip 125 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'initialized', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &push r:1        
        &gotoAndPlay      &end // of function OnCurrentFactionChanged

      &function2 onUnload () (r:1='this', r:2='_root')
        &push r:1        
        &pushone
        &push r:2        
        &dcallmp 0							// DetachFactionObserver()
        &pushsdb 1							//'OnCurrentFactionChanged'
        &delete2
        &pop
        &pushsdb 2							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 3							//'initialized'
      &not
      &not
      &jnz label1      
      &pushzero
      &pushsdbgv 4							//'_root'
      &pushsdb 5							//'GetCurrentFaction'
      &callMethod
      &gotoAndPlay      &pushthisgv
      &pushone
      &pushsdbgv 4							//'_root'
      &dcallmp 7							// AttachFactionObserver()
      &pushsdb 3							//'initialized'
      &pushtrue
      &setVariable
     label1:
    &end // of frame 0

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 125

  &defineMovieClip 126 // total frames: 44

    &frame 0
      &stop
    &end // of frame 0

    &frame 13
      &stop
    &end // of frame 13

    &frame 43
      &stop
    &end // of frame 43
  &end // of defineMovieClip 126

  &defineMovieClip 133 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'initialized', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &push r:1        
        &gotoAndPlay      &end // of function OnCurrentFactionChanged

      &function2 onUnload () (r:1='this', r:2='_root')
        &push r:1        
        &pushone
        &push r:2        
        &dcallmp 0							// DetachFactionObserver()
        &pushsdb 1							//'OnCurrentFactionChanged'
        &delete2
        &pop
        &pushsdb 2							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 3							//'initialized'
      &not
      &not
      &jnz label1      
      &pushzero
      &pushsdbgv 4							//'_root'
      &pushsdb 5							//'GetCurrentFaction'
      &callMethod
      &gotoAndPlay      &pushthisgv
      &pushone
      &pushsdbgv 4							//'_root'
      &dcallmp 7							// AttachFactionObserver()
      &pushsdb 3							//'initialized'
      &pushtrue
      &setVariable
     label1:
    &end // of frame 0

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 133

  &defineMovieClip 140 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'initialized', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &push r:1        
        &gotoAndPlay      &end // of function OnCurrentFactionChanged

      &function2 onUnload () (r:1='this', r:2='_root')
        &push r:1        
        &pushone
        &push r:2        
        &dcallmp 0							// DetachFactionObserver()
        &pushsdb 1							//'OnCurrentFactionChanged'
        &delete2
        &pop
        &pushsdb 2							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 3							//'initialized'
      &not
      &not
      &jnz label1      
      &pushzero
      &pushsdbgv 4							//'_root'
      &pushsdb 5							//'GetCurrentFaction'
      &callMethod
      &gotoAndPlay      &pushthisgv
      &pushone
      &pushsdbgv 4							//'_root'
      &dcallmp 7							// AttachFactionObserver()
      &pushsdb 3							//'initialized'
      &pushtrue
      &setVariable
     label1:
    &end // of frame 0

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 140

  &defineMovieClip 147 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'initialized', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &push r:1        
        &gotoAndPlay      &end // of function OnCurrentFactionChanged

      &function2 onUnload () (r:1='this', r:2='_root')
        &push r:1        
        &pushone
        &push r:2        
        &dcallmp 0							// DetachFactionObserver()
        &pushsdb 1							//'OnCurrentFactionChanged'
        &delete2
        &pop
        &pushsdb 2							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 3							//'initialized'
      &not
      &not
      &jnz label1      
      &pushzero
      &pushsdbgv 4							//'_root'
      &pushsdb 5							//'GetCurrentFaction'
      &callMethod
      &gotoAndPlay      &pushthisgv
      &pushone
      &pushsdbgv 4							//'_root'
      &dcallmp 7							// AttachFactionObserver()
      &pushsdb 3							//'initialized'
      &pushtrue
      &setVariable
     label1:
    &end // of frame 0

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 147

  &defineMovieClip 185 // total frames: 41

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'initialized', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &push r:1        
        &gotoAndPlay      &end // of function OnCurrentFactionChanged

      &function2 onUnload () (r:1='this', r:2='_root')
        &push r:1        
        &pushone
        &push r:2        
        &dcallmp 0							// DetachFactionObserver()
        &pushsdb 1							//'OnCurrentFactionChanged'
        &delete2
        &pop
        &pushsdb 2							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 3							//'initialized'
      &not
      &not
      &jnz label1      
      &pushzero
      &pushsdbgv 4							//'_root'
      &pushsdb 5							//'GetCurrentFaction'
      &callMethod
      &gotoAndPlay      &pushthisgv
      &pushone
      &pushsdbgv 4							//'_root'
      &dcallmp 7							// AttachFactionObserver()
      &pushsdb 3							//'initialized'
      &pushtrue
      &setVariable
     label1:
    &end // of frame 0

    &frame 11
      &stop
    &end // of frame 11

    &frame 25
      &stop
    &end // of frame 25

    &frame 40
      &stop
    &end // of frame 40
  &end // of defineMovieClip 185

  &defineMovieClip 186 // total frames: 75

    &frame 13
      &stop
    &end // of frame 13

    &frame 28
      &stop
    &end // of frame 28

    &frame 43
      &stop
    &end // of frame 43

    &frame 58
      &stop
    &end // of frame 58

    &frame 74
      &stop
    &end // of frame 74
  &end // of defineMovieClip 186

  &defineMovieClip 193 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'initialized', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &push r:1        
        &gotoAndPlay      &end // of function OnCurrentFactionChanged

      &function2 onUnload () (r:1='this', r:2='_root')
        &push r:1        
        &pushone
        &push r:2        
        &dcallmp 0							// DetachFactionObserver()
        &pushsdb 1							//'OnCurrentFactionChanged'
        &delete2
        &pop
        &pushsdb 2							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 3							//'initialized'
      &not
      &not
      &jnz label1      
      &pushzero
      &pushsdbgv 4							//'_root'
      &pushsdb 5							//'GetCurrentFaction'
      &callMethod
      &gotoAndPlay      &pushthisgv
      &pushone
      &pushsdbgv 4							//'_root'
      &dcallmp 7							// AttachFactionObserver()
      &pushsdb 3							//'initialized'
      &pushtrue
      &setVariable
     label1:
    &end // of frame 0

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 193

  &defineMovieClip 194 // total frames: 2
  &end // of defineMovieClip 194

  &defineMovieClip 195 // total frames: 32

    &frame 0
      &constants 'onUnload', 'Show', 'Hide', '_parent', 'isSelected'  
      &function Show (      )      
        &gotoLabel '_show'
        &play
      &end // of function Show

      &function Hide (      )      
        &gotoLabel '_hide'
        &play
      &end // of function Hide

      &pushsdb 0							//'onUnload'
      &function  (      )      
        &pushsdb 1							//'Show'
        &delete2
        &pop
        &pushsdb 2							//'Hide'
        &delete2
        &pop
        &pushsdb 0							//'onUnload'
        &delete2
        &pop
      &end // of function 

      &setVariable
      &pushsdbgv 3							//'_parent'
      &pushsdbgm 4							//'isSelected'
      &not
      &jnz label1      
      &gotoLabel '_show'
      &play
      &jmp label2      
     label1:
      &stop
     label2:
    &end // of frame 0

    &placeMovieClip 116 
    
      &onClipEvent &load
        &pushs ''
        &pushbyte 7
        &pushfalse
        &setProperty
      &end
    &end // of placeMovieClip 116

    &frame 8
      &stop
    &end // of frame 8

    &frame 9
      &pushs '_snow'
      &pushbyte 5
      &random
      &add
      &pushone
      &pushsgv 'Snow'
      &pushs 'gotoAndPlay'
      &callmp
    &end // of frame 9

    &frame 20
      &stop
    &end // of frame 20

    &frame 31
      &gotoLabel '_hidden'
      &play
    &end // of frame 31
  &end // of defineMovieClip 195

  &defineMovieClip 199 // total frames: 1
  &end // of defineMovieClip 199

  &defineMovieClip 202 // total frames: 101

    &frame 0
      &stop
    &end // of frame 0

    &placeMovieClip 199 
    
      &onClipEvent &load
        &pushs ''
        &pushbyte 7
        &pushfalse
        &setProperty
      &end
    &end // of placeMovieClip 199
  &end // of defineMovieClip 202

  &defineMovieClip 207 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'initialized', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &push r:1        
        &gotoAndPlay      &end // of function OnCurrentFactionChanged

      &function2 onUnload () (r:1='this', r:2='_root')
        &push r:1        
        &pushone
        &push r:2        
        &dcallmp 0							// DetachFactionObserver()
        &pushsdb 1							//'OnCurrentFactionChanged'
        &delete2
        &pop
        &pushsdb 2							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 3							//'initialized'
      &not
      &not
      &jnz label1      
      &pushzero
      &pushsdbgv 4							//'_root'
      &pushsdb 5							//'GetCurrentFaction'
      &callMethod
      &gotoAndPlay      &pushthisgv
      &pushone
      &pushsdbgv 4							//'_root'
      &dcallmp 7							// AttachFactionObserver()
      &pushsdb 3							//'initialized'
      &pushtrue
      &setVariable
     label1:
    &end // of frame 0

    &frame 8
      &stop
    &end // of frame 8

    &frame 18
      &stop
    &end // of frame 18

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 207

  &defineMovieClip 210 // total frames: 1
  &end // of defineMovieClip 210

  &placeMovieClip 210 &as 'numberText'
  
    &onClipEvent &load
      &pushs 'text'
      &pushs '$'
      &pushsgv '_parent'
      &toString
      &add
      &pushs ':Number&dropshadow'
      &add
      &setVariable
    &end
  &end // of placeMovieClip 210

  &defineMovieClip 212 // total frames: 1
  &end // of defineMovieClip 212

  &defineMovieClip 213 // total frames: 24

    &frame 0
      &constants 'ancestor', '_parent', 'disableCommandButtonLoadAnim'  
      &pushsdb 0							//'ancestor'
      &pushsdbgv 1							//'_parent'
      &pushsdbgm 1							//'_parent'
      &varEquals
     label1:
      &pushsdbgv 0							//'ancestor'
      &pushundef
      &equals
      &not
      &not
      &jnz label3      
      &pushsdbgv 0							//'ancestor'
      &pushsdbgm 2							//'disableCommandButtonLoadAnim'
      &not
      &jnz label2      
      &gotoLabel '_off'
      &play
      &jmp label3      
     label2:
      &pushsdb 0							//'ancestor'
      &pushsdbgv 0							//'ancestor'
      &pushsdbgm 1							//'_parent'
      &setVariable
      &jmp label1      
     label3:
    &end // of frame 0

    &frame 20
      &stop
    &end // of frame 20
  &end // of defineMovieClip 213

  &frame 9
    &stop
  &end // of frame 9

  &defineMovieClip 218 // total frames: 20

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19
  &end // of defineMovieClip 218

  &defineMovieClip 223 // total frames: 20

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19
  &end // of defineMovieClip 223

  &defineMovieClip 228 // total frames: 20

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19
  &end // of defineMovieClip 228

  &defineMovieClip 229 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'initialized', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &push r:1        
        &gotoAndPlay      &end // of function OnCurrentFactionChanged

      &function2 onUnload () (r:1='this', r:2='_root')
        &push r:1        
        &pushone
        &push r:2        
        &dcallmp 0							// DetachFactionObserver()
        &pushsdb 1							//'OnCurrentFactionChanged'
        &delete2
        &pop
        &pushsdb 2							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 3							//'initialized'
      &not
      &not
      &jnz label1      
      &pushzero
      &pushsdbgv 4							//'_root'
      &pushsdb 5							//'GetCurrentFaction'
      &callMethod
      &gotoAndPlay      &pushthisgv
      &pushone
      &pushsdbgv 4							//'_root'
      &dcallmp 7							// AttachFactionObserver()
      &pushsdb 3							//'initialized'
      &pushtrue
      &setVariable
     label1:
    &end // of frame 0

    &placeMovieClip 218 &as 'image'
    
      &onClipEvent &load
        &constants '_parent', 'useAlternateColor'  
        &pushsdbgv 0							//'_parent'
        &pushsdbgm 0							//'_parent'
        &pushsdbgm 1							//'useAlternateColor'
        &not
        &jnz label1        
        &gotoLabel '_alternate'
        &play
       label1:
      &end
    &end // of placeMovieClip 218

    &frame 9
      &stop
    &end // of frame 9

    &placeMovieClip 223 &as 'image'
    
      &onClipEvent &load
        &constants '_parent', 'useAlternateColor'  
        &pushsdbgv 0							//'_parent'
        &pushsdbgm 0							//'_parent'
        &pushsdbgm 1							//'useAlternateColor'
        &not
        &jnz label1        
        &gotoLabel '_alternate'
        &play
       label1:
      &end
    &end // of placeMovieClip 223

    &frame 19
      &stop
    &end // of frame 19

    &placeMovieClip 228 &as 'image'
    
      &onClipEvent &load
        &constants '_parent', 'useAlternateColor'  
        &pushsdbgv 0							//'_parent'
        &pushsdbgm 0							//'_parent'
        &pushsdbgm 1							//'useAlternateColor'
        &not
        &jnz label1        
        &gotoLabel '_alternate'
        &play
       label1:
      &end
    &end // of placeMovieClip 228

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 229
  
  &importAssets &from 'libHUD.swf'
    'RenderImage' &as 230
  &end // of importAssets

  &placeMovieClip 230 &as 'image'
  
    &onClipEvent &construct
      &constants '_type', 'RenderImage', '_imageMap', '', '_mode'  
      &pushsdb 0							//'_type'
      &pushsdb 1							//'RenderImage'
      &setVariable
      &pushsdb 2							//'_imageMap'
      &pushsdb 3							//''
      &setVariable
      &pushsdb 4							//'_mode'
      &pushsdb 3							//''
      &setVariable
    &end
  
    &onClipEvent &load
      &constants '_imageMap', '_parent', ':Image', 'colorizer', 'this', 'Color', 'imageTint', 'setRGB'  
      &pushsdb 0							//'_imageMap'
      &pushsdbgv 1							//'_parent'
      &toString
      &pushsdb 2							//':Image'
      &add
      &setVariable
      &pushsdb 3							//'colorizer'
      &pushthisgv
      &pushone
      &pushsdb 5							//'Color'
      &new
      &setVariable
      &pushsdbgv 1							//'_parent'
      &pushsdbgm 6							//'imageTint'
      &pushundef
      &equals
      &not
      &not
      &jnz label1      
      &pushsdbgv 1							//'_parent'
      &pushsdbgm 6							//'imageTint'
      &pushone
      &pushsdbgv 3							//'colorizer'
      &dcallmp 7							// setRGB()
     label1:
    &end
  &end // of placeMovieClip 230

  &defineMovieClip 235 // total frames: 20

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19
  &end // of defineMovieClip 235

  &defineMovieClip 240 // total frames: 20

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19
  &end // of defineMovieClip 240

  &defineMovieClip 245 // total frames: 20

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19
  &end // of defineMovieClip 245

  &defineMovieClip 246 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'initialized', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &push r:1        
        &gotoAndPlay      &end // of function OnCurrentFactionChanged

      &function2 onUnload () (r:1='this', r:2='_root')
        &push r:1        
        &pushone
        &push r:2        
        &dcallmp 0							// DetachFactionObserver()
        &pushsdb 1							//'OnCurrentFactionChanged'
        &delete2
        &pop
        &pushsdb 2							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 3							//'initialized'
      &not
      &not
      &jnz label1      
      &pushzero
      &pushsdbgv 4							//'_root'
      &pushsdb 5							//'GetCurrentFaction'
      &callMethod
      &gotoAndPlay      &pushthisgv
      &pushone
      &pushsdbgv 4							//'_root'
      &dcallmp 7							// AttachFactionObserver()
      &pushsdb 3							//'initialized'
      &pushtrue
      &setVariable
     label1:
    &end // of frame 0

    &placeMovieClip 235 &as 'image'
    
      &onClipEvent &load
        &constants '_parent', 'useAlternateColor'  
        &pushsdbgv 0							//'_parent'
        &pushsdbgm 0							//'_parent'
        &pushsdbgm 1							//'useAlternateColor'
        &not
        &jnz label1        
        &gotoLabel '_alternate'
        &play
       label1:
      &end
    &end // of placeMovieClip 235

    &frame 9
      &stop
    &end // of frame 9

    &placeMovieClip 240 &as 'image'
    
      &onClipEvent &load
        &constants '_parent', 'useAlternateColor'  
        &pushsdbgv 0							//'_parent'
        &pushsdbgm 0							//'_parent'
        &pushsdbgm 1							//'useAlternateColor'
        &not
        &jnz label1        
        &gotoLabel '_alternate'
        &play
       label1:
      &end
    &end // of placeMovieClip 240

    &frame 19
      &stop
    &end // of frame 19

    &placeMovieClip 245 &as 'image'
    
      &onClipEvent &load
        &constants '_parent', 'useAlternateColor'  
        &pushsdbgv 0							//'_parent'
        &pushsdbgm 0							//'_parent'
        &pushsdbgm 1							//'useAlternateColor'
        &not
        &jnz label1        
        &gotoLabel '_alternate'
        &play
       label1:
      &end
    &end // of placeMovieClip 245

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 246

  &frame 19
    &stop
  &end // of frame 19

  &frame 28
    &stop
  &end // of frame 28

  &frame 29
    &pushs 'inDownState'
    &pushtrue
    &setVariable
  &end // of frame 29

  &defineMovieClip 249 // total frames: 1
  &end // of defineMovieClip 249

  &frame 38
    &stop
  &end // of frame 38

  &frame 39
    &pushsgv 'extern'
    &pushsgm 'InGame'
    &not
    &not
    &jnz label1    
    &pushzero
    &pushsgv 'selectedOverlay'
    &pushs 'Show'
    &callmp
   label1:
  &end // of frame 39

  &frame 49
    &gotoLabel '_over'
    &play
  &end // of frame 49
&end
