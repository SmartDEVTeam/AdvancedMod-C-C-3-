movie 'E:\Projects\CNC3\Data\APTBUI~1\034A3~1.0-D\pc\Output\TA2ABD~1\\TACTIC~1.eaf' &compressed // flash 7, total frames: 10, frame rate: 30 fps, 1024x768 px

  &frame 0
    &constants '_up', 'bttn', 'gotoAndPlay', 'isMouseOver', '_hide', 'RollOver', 'RollOverTop', '_disabled', 'isEnabled', '_visible', 'timerVisible', 'timerOverlay0', 'timerOverlay1', 'Math', 'round', 'gotoAndStop', 'imageTint', 'image', 'colorizer', 'setRGB', 'quantityText', 'SetEnabled', 'SetVisibility', 'SetTimerVisibility', 'SetTimerValue', 'SetImageTint', 'SetQuantityVisibility', 'onUnload', 'extern', 'InGame', '_root', 'GetCurrentFaction', 'Alien', 'initialized', 'this', '_parent', 'OnContentLoaded', 'FSCommand:', ':OnInitialized', ''  
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
      &pushsdb 0							//'_up'
      &pushone
      &pushsdbgv 1							//'bttn'
      &dcallmp 2							// gotoAndPlay()
      &jmp label3      
     label1:
      &pushsdbgv 3							//'isMouseOver'
      &not
      &jnz label2      
      &pushsdb 4							//'_hide'
      &pushone
      &pushsdbgv 1							//'bttn'
      &pushsdbgm 5							//'RollOver'
      &dcallmp 2							// gotoAndPlay()
      &pushsdb 4							//'_hide'
      &pushone
      &pushsdbgv 1							//'bttn'
      &pushsdbgm 6							//'RollOverTop'
      &dcallmp 2							// gotoAndPlay()
     label2:
      &pushsdb 7							//'_disabled'
      &pushone
      &pushsdbgv 1							//'bttn'
      &dcallmp 2							// gotoAndPlay()
     label3:
      &pushsdb 8							//'isEnabled'
      &push r:1      
      &setVariable
    &end // of function SetEnabled

    &function2 SetVisibility (r:1='visArg') ()
      &pushsdbgv 1							//'bttn'
      &pushsdb 9							//'_visible'
      &push r:1      
      &toNumber
      &pushzero
      &equals
      &not
      &setMember
    &end // of function SetVisibility

    &function2 SetTimerVisibility (r:1='vis') ()
      &pushsdb 10							//'timerVisible'
      &push r:1      
      &toNumber
      &pushzero
      &equals
      &not
      &setVariable
      &pushsdbgv 1							//'bttn'
      &pushsdbgm 11							//'timerOverlay0'
      &pushsdb 9							//'_visible'
      &pushsdbgv 10							//'timerVisible'
      &setMember
      &pushsdbgv 1							//'bttn'
      &pushsdbgm 12							//'timerOverlay1'
      &pushsdb 9							//'_visible'
      &pushsdbgv 10							//'timerVisible'
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
      &pushsdbgv 13							//'Math'
      &pushsdb 14							//'round'
      &callMethod
      &pushone
      &add
      &setRegister r:1
      &pop
      &push r:1      
      &pushone
      &pushsdbgv 1							//'bttn'
      &pushsdbgm 11							//'timerOverlay0'
      &dcallmp 15							// gotoAndStop()
      &push r:1      
      &pushone
      &pushsdbgv 1							//'bttn'
      &pushsdbgm 12							//'timerOverlay1'
      &dcallmp 15							// gotoAndStop()
    &end // of function SetTimerValue

    &function2 SetImageTint (r:2='tintColorArg') ()
      &push r:2      
      &toNumber
      &setRegister r:1
      &pop
      &pushsdb 16							//'imageTint'
      &push r:1      
      &setVariable
      &pushsdbgv 1							//'bttn'
      &pushsdbgm 17							//'image'
      &pushsdbgm 18							//'colorizer'
      &pushundef
      &equals
      &not
      &not
      &jnz label4      
      &pushsdbgv 16							//'imageTint'
      &pushone
      &pushsdbgv 1							//'bttn'
      &pushsdbgm 17							//'image'
      &pushsdbgm 18							//'colorizer'
      &dcallmp 19							// setRGB()
     label4:
    &end // of function SetImageTint

    &function2 SetQuantityVisibility (r:2='visArg') ()
      &push r:2      
      &toNumber
      &pushzero
      &equals
      &not
      &setRegister r:1
      &pop
      &pushsdbgv 1							//'bttn'
      &pushsdbgm 20							//'quantityText'
      &pushsdb 9							//'_visible'
      &push r:1      
      &setMember
    &end // of function SetQuantityVisibility

    &function onUnload (    )    
      &pushsdb 21							//'SetEnabled'
      &delete2
      &pop
      &pushsdb 22							//'SetVisibility'
      &delete2
      &pop
      &pushsdb 23							//'SetTimerVisibility'
      &delete2
      &pop
      &pushsdb 24							//'SetTimerValue'
      &delete2
      &pop
      &pushsdb 25							//'SetImageTint'
      &delete2
      &pop
      &pushsdb 26							//'SetQuantityVisibility'
      &delete2
      &pop
      &pushsdb 27							//'onUnload'
      &delete2
      &pop
    &end // of function onUnload

    &pushsdbgv 28							//'extern'
    &pushsdbgm 29							//'InGame'
    &not
    &not
    &jnz label5    
    &pushsdbgv 30							//'_root'
    &pushsdb 31							//'GetCurrentFaction'
    &function  (    )    
      &pushsdb 32							//'Alien'
      &return
    &end // of function 

    &setMember
   label5:
    &pushsdbgv 33							//'initialized'
    &not
    &not
    &jnz label6    
    &pushthisgv
    &pushone
    &pushsdbgv 35							//'_parent'
    &dcallmp 36							// OnContentLoaded()
    &pushsdb 8							//'isEnabled'
    &pushfalse
    &setVariable
    &pushsdb 3							//'isMouseOver'
    &pushfalse
    &setVariable
    &pushsdb 10							//'timerVisible'
    &pushfalse
    &setVariable
    &pushsdb 16							//'imageTint'
    &pushlong 16777215
    &setVariable
    &pushsdb 33							//'initialized'
    &pushtrue
    &setVariable
    &pushsdb 37							//'FSCommand:'
    &pushthisgv
    &toString
    &pushsdb 38							//':OnInitialized'
    &add
    &concat
    &pushsdb 39							//''
    &getURL2
    &pushsdbgv 28							//'extern'
    &pushsdbgm 29							//'InGame'
    &not
    &not
    &jnz label6    
    &pushsdb 8							//'isEnabled'
    &pushtrue
    &setVariable
   label6:
  &end // of frame 0

  &defineButton 2
  
    &on     &overUpToOverDown
      &pushsgv '_parent'
      &pushsgm 'isEnabled'
      &not
      &jnz label1      
      &gotoLabel '_down'
      &play
     label1:
    &end
  
    &on     &overDownToOverUp
      &constants '_parent', 'isEnabled', 'FSCommand:', ':OnClicked', ''  
      &pushsdbgv 0							//'_parent'
      &pushsdbgm 1							//'isEnabled'
      &not
      &jnz label1      
      &gotoLabel '_release'
      &play
     label1:
      &pushsdb 2							//'FSCommand:'
      &pushsdbgv 0							//'_parent'
      &toString
      &pushsdb 3							//':OnClicked'
      &add
      &concat
      &pushsdb 4							//''
      &getURL2
    &end
  
    &on     &idleToOverUp
      &constants '_parent', 'isEnabled', '_show', 'RollOver', 'gotoAndPlay', 'RollOverTop', 'isMouseOver', 'FSCommand:', ':OnRollOver', ''  
      &pushsdbgv 0							//'_parent'
      &pushsdbgm 1							//'isEnabled'
      &not
      &jnz label1      
      &gotoLabel '_over'
      &play
      &pushsdb 2							//'_show'
      &pushone
      &pushsdbgv 3							//'RollOver'
      &dcallmp 4							// gotoAndPlay()
      &pushsdb 2							//'_show'
      &pushone
      &pushsdbgv 5							//'RollOverTop'
      &dcallmp 4							// gotoAndPlay()
     label1:
      &pushsdbgv 0							//'_parent'
      &pushsdb 6							//'isMouseOver'
      &pushtrue
      &setMember
      &pushsdb 7							//'FSCommand:'
      &pushsdbgv 0							//'_parent'
      &toString
      &pushsdb 8							//':OnRollOver'
      &add
      &concat
      &pushsdb 9							//''
      &getURL2
    &end
  
    &on     &overUpToIdle
      &constants '_parent', 'isEnabled', '_hide', 'RollOver', 'gotoAndPlay', 'RollOverTop', 'isMouseOver', 'FSCommand:', ':OnRollOut', ''  
      &pushsdbgv 0							//'_parent'
      &pushsdbgm 1							//'isEnabled'
      &not
      &jnz label1      
      &gotoLabel '_up'
      &play
      &pushsdb 2							//'_hide'
      &pushone
      &pushsdbgv 3							//'RollOver'
      &dcallmp 4							// gotoAndPlay()
      &pushsdb 2							//'_hide'
      &pushone
      &pushsdbgv 5							//'RollOverTop'
      &dcallmp 4							// gotoAndPlay()
     label1:
      &pushsdbgv 0							//'_parent'
      &pushsdb 6							//'isMouseOver'
      &pushfalse
      &setMember
      &pushsdb 7							//'FSCommand:'
      &pushsdbgv 0							//'_parent'
      &toString
      &pushsdb 8							//':OnRollOut'
      &add
      &concat
      &pushsdb 9							//''
      &getURL2
    &end
  &end // of defineButton 2

  &defineMovieClip 10 // total frames: 30

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
  &end // of defineMovieClip 10

  &defineMovieClip 99 // total frames: 101

    &frame 0
      &constants '', '_parent', 'timerVisible'  
      &pushsdb 0							//''
      &pushbyte 7
      &pushsdbgv 1							//'_parent'
      &pushsdbgm 1							//'_parent'
      &pushsdbgm 2							//'timerVisible'
      &setProperty
      &stop
    &end // of frame 0
  &end // of defineMovieClip 99

  &defineMovieClip 106 // total frames: 30

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
  &end // of defineMovieClip 106

  &defineMovieClip 113 // total frames: 30

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
  &end // of defineMovieClip 113

  &defineMovieClip 116 // total frames: 1
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

  &defineMovieClip 129 // total frames: 30

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
  &end // of defineMovieClip 129

  &defineMovieClip 131 // total frames: 1

    &frame 0
      &pushs ''
      &pushbyte 7
      &pushfalse
      &setProperty
    &end // of frame 0
  &end // of defineMovieClip 131

  &defineMovieClip 132 // total frames: 44

    &frame 0
      &stop
    &end // of frame 0

    &frame 13
      &stop
    &end // of frame 13

    &frame 43
      &stop
    &end // of frame 43
  &end // of defineMovieClip 132

  &defineMovieClip 135 // total frames: 1
  &end // of defineMovieClip 135
  
  &importAssets &from 'libHUD.swf'
    'RenderImage' &as 136
  &end // of importAssets

  &defineMovieClip 143 // total frames: 30

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
  &end // of defineMovieClip 143

  &defineMovieClip 146 // total frames: 1
  &end // of defineMovieClip 146

  &defineMovieClip 147 // total frames: 2
  &end // of defineMovieClip 147

  &defineMovieClip 148 // total frames: 50

    &placeMovieClip 122 &as 'disabledImage'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'RenderImageDisabled'
        &pushs '_imageMap'
        &pushssv ''
      &end
    
      &onClipEvent &load
        &constants '_imageMap', '_parent', ':Image'  
        &pushsdb 0							//'_imageMap'
        &pushsdbgv 1							//'_parent'
        &pushsdbgm 1							//'_parent'
        &toString
        &pushsdb 2							//':Image'
        &add
        &setVariable
      &end
    &end // of placeMovieClip 122

    &placeMovieClip 135 &as 'quantityText'
    
      &onClipEvent &load
        &constants 'text', '$', '_parent', ':QuantityText&dropshadow'  
        &pushsdb 0							//'text'
        &pushsdb 1							//'$'
        &pushsdbgv 2							//'_parent'
        &pushsdbgm 2							//'_parent'
        &toString
        &add
        &pushsdb 3							//':QuantityText&dropshadow'
        &add
        &setVariable
      &end
    &end // of placeMovieClip 135

    &frame 8
      &stop
    &end // of frame 8

    &placeMovieClip 136 &as 'image'
    
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
        &pushsdbgm 1							//'_parent'
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
        &pushsdbgm 1							//'_parent'
        &pushsdbgm 6							//'imageTint'
        &pushundef
        &equals
        &not
        &not
        &jnz label1        
        &pushsdbgv 1							//'_parent'
        &pushsdbgm 1							//'_parent'
        &pushsdbgm 6							//'imageTint'
        &pushone
        &pushsdbgv 3							//'colorizer'
        &dcallmp 7							// setRGB()
       label1:
      &end
    &end // of placeMovieClip 136

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
      &gotoLabel '_over'
      &play
    &end // of frame 49
  &end // of defineMovieClip 148

  &placeMovieClip 148 &as 'bttn'
  
    &onClipEvent &load
      &pushs ''
      &pushbyte 7
      &pushfalse
      &setProperty
    &end
  &end // of placeMovieClip 148

  &defineMovieClip 151 // total frames: 1
  &end // of defineMovieClip 151

  &defineMovieClip 152 // total frames: 16

    &frame 15
      &stop
    &end // of frame 15
  &end // of defineMovieClip 152

  &frame 9
    &pushsgv 'bttn'
    &pushs '_visible'
    &pushtrue
    &setMember
  &end // of frame 9
&end
