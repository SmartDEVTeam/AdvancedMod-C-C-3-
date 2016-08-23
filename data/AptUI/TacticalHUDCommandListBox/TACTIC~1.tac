movie 'E:\Projects\CNC3\Data\APTBUI~1\034A3~1.0-D\pc\Output\TACTIC~3\\TACTIC~1.eaf' &compressed // flash 7, total frames: 1, frame rate: 30 fps, 1024x768 px
  
  &importAssets &from 'libHUD.swf'
    'WhiteRectangle' &as 1
  &end // of importAssets

  &defineMovieClip 2 // total frames: 1

    &placeMovieClip 1 
    
      &onClipEvent &load
        &pushs ''
        &pushbyte 7
        &pushfalse
        &setProperty
      &end
    &end // of placeMovieClip 1
  &end // of defineMovieClip 2
  
  &exportAssets
    2 &as 'CommandListButtonStage'
  &end // of exportAssets

  &frame 0
    &constants 'buttonMask', '_y', 'buttonStage', '_height', 'buttonSlots', 'length', 'stage', 'buttonSlotHeight', '_visible', 'nextButtonSlotId', 'LoadMovieStage', 'attachMovie', '_x', 'ShouldButtonSlotBeVisible', 'helpSite', 'HelpBoxSite', 'vertAlignment', 'top', 'horzAlignment', 'right', 'splice', 'FSCommand:', ':OnButtonSlotStageCreated', 'index=', '&name=', 'numColumns', 'Math', 'floor', 'buttonSlotWidth', 'CreateNewButtonSlot', 'MoveButtonSlot', 'scrollBar', 'UpdateScrollBarState', 'removeMovieClip', 'pop', 'onEnterFrame', 'GetCurPos', 'ceil', 'round', 'UpdateButtonSlotVisibility', 'SetLineSize', 'numVisibleRows', 'SetPageSize', 'SetEnabled', 'SetVisible', 'scrollBarParam', 'scrollBarPlaceholder', 'SetHeight', '_xscale', '_yscale', 'OnPosChanged', 'OnScrollBarPosChanged', 'InsertButtonSlot', 'EraseButtonSlot', 'SetButtonSlotCount', 'GetScrollBarParam', 'OnScrollBarLoaded', 'onUnload', 'upButtonParam', 'Object', 'disabledImage', 'VSliderUpButtonDisabledDynFac', 'upImage', 'VSliderUpButtonEnabledDynFac', 'overImage', 'VSliderUpButtonOverDynFac', 'downImage', 'VSliderUpButtonPressDynFac', 'downButtonParam', 'VSliderDownButtonDisabledDynFac', 'VSliderDownButtonEnabledDynFac', 'VSliderDownButtonOverDynFac', 'VSliderDownButtonPressDynFac', 'thumbTop', 'VSliderThumbDisabledTopDynFac', 'VSliderThumbEnabledTopDynFac', 'VSliderThumbOverTopDynFac', 'VSliderThumbPressTopDynFac', 'thumbMiddle', 'VSliderThumbDisabledMiddleDynFac', 'VSliderThumbEnabledMiddleDynFac', 'VSliderThumbOverMiddleDynFac', 'VSliderThumbPressMiddleDynFac', 'thumbBottom', 'VSliderThumbDisabledBottomDynFac', 'VSliderThumbEnabledBottomDynFac', 'VSliderThumbOverBottomDynFac', 'VSliderThumbPressBottomDynFac', 'thumbParam', 'topPiece', 'middlePiece', 'bottomPiece', 'barParam', 'VSliderBarDisabledDynFac', 'VSliderBarUpOverDynFac', 'upButton', 'downButton', 'thumb', 'bar', 'initialized', 'buttonStageWidth', 'buttonStageHeight', 'Array', 'VerticalScrollBar.swf', 'loadMovie', 'this', ':OnInitialized', ''  
    &function2 UpdateButtonSlotVisibility () ()
      &pushsdbgv 0							//'buttonMask'
      &pushsdbgm 1							//'_y'
      &pushsdbgv 2							//'buttonStage'
      &pushsdbgm 1							//'_y'
      &subtract
      &setRegister r:4
      &pop
      &push r:4      
      &pushsdbgv 0							//'buttonMask'
      &pushsdbgm 3							//'_height'
      &add
      &setRegister r:5
      &pop
      &pushzero
      &setRegister r:1
      &pop
     label1:
      &push r:1      
      &pushsdbgv 4							//'buttonSlots'
      &pushsdbgm 5							//'length'
      &lessThan
      &not
      &jnz label3      
      &pushsdbgv 4							//'buttonSlots'
      &push r:1      
      &getMember
      &pushsdbgm 6							//'stage'
      &setRegister r:2
      &pop
      &push r:2      
      &pushsdbgm 1							//'_y'
      &push r:5      
      &lessThan
      &dup
      &not
      &jnz label2      
      &pop
      &push r:2      
      &pushsdbgm 1							//'_y'
      &pushsdbgv 7							//'buttonSlotHeight'
      &add
      &push r:4      
      &greaterThan
     label2:
      &setRegister r:3
      &pop
      &push r:2      
      &pushsdb 8							//'_visible'
      &push r:3      
      &setMember
      &push r:1      
      &increment
      &setRegister r:1
      &pop
      &jmp label1      
     label3:
    &end // of function UpdateButtonSlotVisibility

    &function2 ShouldButtonSlotBeVisible (r:3='slotStage') ()
      &pushzero
      &pushsdbgv 2							//'buttonStage'
      &pushsdbgm 1							//'_y'
      &subtract
      &setRegister r:1
      &pop
      &push r:1      
      &pushsdbgv 0							//'buttonMask'
      &pushsdbgm 3							//'_height'
      &add
      &setRegister r:2
      &pop
      &push r:3      
      &pushsdbgm 1							//'_y'
      &push r:2      
      &lessThan
      &dup
      &not
      &jnz label4      
      &pop
      &push r:3      
      &pushsdbgm 1							//'_y'
      &pushsdbgv 7							//'buttonSlotHeight'
      &add
      &push r:1      
      &greaterThan
     label4:
      &return
    &end // of function ShouldButtonSlotBeVisible

    &function2 CreateNewButtonSlot (r:6='slotIndex', r:10='slotX', r:9='slotY') (r:1='this')
      &pushsdbgv 9							//'nextButtonSlotId'
      &pushsdb 9							//'nextButtonSlotId'
      &pushsdbgv 9							//'nextButtonSlotId'
      &increment
      &setVariable
      &setRegister r:4
      &pop
      &push r:4      
      &push r:4      
      &toString
      &pushsdb 10							//'LoadMovieStage'
      &pushbyte 3
      &pushsdbgv 2							//'buttonStage'
      &pushsdb 11							//'attachMovie'
      &callMethod
      &setRegister r:2
      &pop
      &push r:2      
      &pushsdb 12							//'_x'
      &push r:10      
      &setMember
      &push r:2      
      &pushsdb 1							//'_y'
      &push r:9      
      &setMember
      &push r:2      
      &pushsdb 8							//'_visible'
      &push r:2      
      &pushone
      &pushsdb 13							//'ShouldButtonSlotBeVisible'
      &callFunction
      &setMember
      &push r:4      
      &pushlong 65536
      &add
      &pushsdb 14							//'helpSite'
      &push r:4      
      &toString
      &add
      &pushsdb 15							//'HelpBoxSite'
      &pushbyte 3
      &pushsdbgv 2							//'buttonStage'
      &pushsdb 11							//'attachMovie'
      &callMethod
      &setRegister r:3
      &pop
      &push r:3      
      &pushsdb 12							//'_x'
      &pushzero
      &setMember
      &push r:3      
      &pushsdb 1							//'_y'
      &push r:9      
      &setMember
      &push r:3      
      &pushsdb 16							//'vertAlignment'
      &pushsdb 17							//'top'
      &setMember
      &push r:3      
      &pushsdb 18							//'horzAlignment'
      &pushsdb 19							//'right'
      &setMember
      &push r:2      
      &pushsdb 14							//'helpSite'
      &push r:3      
      &setMember
      &pushsdb 6							//'stage'
      &push r:2      
      &pushsdb 14							//'helpSite'
      &push r:3      
      &pushbyte 2
      &initObject
      &setRegister r:5
      &pop
      &push r:5      
      &pushzero
      &push r:6      
      &pushbyte 3
      &pushsdbgv 4							//'buttonSlots'
      &dcallmp 20							// splice()
      &pushsdb 21							//'FSCommand:'
      &push r:1      
      &toString
      &pushsdb 22							//':OnButtonSlotStageCreated'
      &add
      &concat
      &pushsdb 23							//'index='
      &push r:6      
      &add
      &pushsdb 24							//'&name='
      &add
      &push r:2      
      &toString
      &add
      &getURL2
      &push r:5      
      &return
    &end // of function CreateNewButtonSlot

    &function2 MoveButtonSlot (r:5='slotIndex', r:6='slotX', r:4='slotY') ()
      &pushsdbgv 4							//'buttonSlots'
      &push r:5      
      &getMember
      &setRegister r:2
      &pop
      &push r:2      
      &pushsdbgm 6							//'stage'
      &setRegister r:1
      &pop
      &push r:1      
      &pushsdb 12							//'_x'
      &push r:6      
      &setMember
      &push r:1      
      &pushsdb 1							//'_y'
      &push r:4      
      &setMember
      &push r:1      
      &pushsdb 8							//'_visible'
      &push r:1      
      &pushone
      &pushsdb 13							//'ShouldButtonSlotBeVisible'
      &callFunction
      &setMember
      &push r:2      
      &pushsdbgm 14							//'helpSite'
      &setRegister r:3
      &pop
      &push r:3      
      &pushsdb 1							//'_y'
      &push r:4      
      &setMember
    &end // of function MoveButtonSlot

    &function2 InsertButtonSlot (r:1='index') ()
      &push r:1      
      &pushsdbgv 25							//'numColumns'
      &divide
      &pushone
      &pushsdbgv 26							//'Math'
      &pushsdb 27							//'floor'
      &callMethod
      &setRegister r:5
      &pop
      &push r:1      
      &pushsdbgv 25							//'numColumns'
      &modulo
      &setRegister r:3
      &pop
      &push r:5      
      &pushsdbgv 7							//'buttonSlotHeight'
      &multiply
      &setRegister r:4
      &pop
      &push r:3      
      &pushsdbgv 28							//'buttonSlotWidth'
      &multiply
      &setRegister r:2
      &pop
      &push r:4      
      &push r:2      
      &push r:1      
      &pushbyte 3
      &dcallfp 29							// CreateNewButtonSlot()
      &push r:1      
      &increment
      &setRegister r:1
      &pop
     label5:
      &push r:1      
      &pushsdbgv 4							//'buttonSlots'
      &pushsdbgm 5							//'length'
      &lessThan
      &not
      &jnz label8      
      &push r:3      
      &increment
      &setRegister r:3
      &pop
      &push r:3      
      &pushsdbgv 25							//'numColumns'
      &lessThan
      &not
      &jnz label6      
      &push r:2      
      &pushsdbgv 28							//'buttonSlotWidth'
      &add
      &setRegister r:2
      &pop
      &jmp label7      
     label6:
      &pushzero
      &setRegister r:3
      &pop
      &pushzero
      &setRegister r:2
      &pop
      &push r:4      
      &pushsdbgv 7							//'buttonSlotHeight'
      &add
      &setRegister r:4
      &pop
     label7:
      &push r:4      
      &push r:2      
      &push r:1      
      &pushbyte 3
      &dcallfp 30							// MoveButtonSlot()
      &push r:1      
      &increment
      &setRegister r:1
      &pop
      &jmp label5      
     label8:
      &pushsdbgv 31							//'scrollBar'
      &pushone
      &dcallfp 32							// UpdateScrollBarState()
    &end // of function InsertButtonSlot

    &function2 EraseButtonSlot (r:1='index') ()
      &pushsdbgv 4							//'buttonSlots'
      &push r:1      
      &getMember
      &pushsdbgm 6							//'stage'
      &pushsdbgm 12							//'_x'
      &setRegister r:2
      &pop
      &pushsdbgv 4							//'buttonSlots'
      &push r:1      
      &getMember
      &pushsdbgm 6							//'stage'
      &pushsdbgm 1							//'_y'
      &setRegister r:4
      &pop
      &pushzero
      &pushsdbgv 4							//'buttonSlots'
      &push r:1      
      &getMember
      &pushsdbgm 6							//'stage'
      &dcallmp 33							// removeMovieClip()
      &pushzero
      &pushsdbgv 4							//'buttonSlots'
      &push r:1      
      &getMember
      &pushsdbgm 14							//'helpSite'
      &dcallmp 33							// removeMovieClip()
      &pushone
      &push r:1      
      &pushbyte 2
      &pushsdbgv 4							//'buttonSlots'
      &dcallmp 20							// splice()
      &push r:1      
      &pushsdbgv 25							//'numColumns'
      &modulo
      &setRegister r:3
      &pop
      &pushsdbgv 4							//'buttonSlots'
      &pushsdbgm 5							//'length'
      &pushzero
      &greaterThan
      &not
      &jnz label14      
      &push r:1      
      &pushsdbgv 4							//'buttonSlots'
      &pushsdbgm 5							//'length'
      &lessThan
      &not
      &jnz label13      
     label9:
      &pushfalse
      &jnz label13      
      &push r:4      
      &push r:2      
      &push r:1      
      &pushbyte 3
      &dcallfp 30							// MoveButtonSlot()
      &push r:1      
      &increment
      &setRegister r:1
      &pop
      &push r:1      
      &pushsdbgv 4							//'buttonSlots'
      &pushsdbgm 5							//'length'
      &lessThan
      &not
      &not
      &jnz label10      
      &jmp label13      
     label10:
      &push r:3      
      &increment
      &setRegister r:3
      &pop
      &push r:3      
      &pushsdbgv 25							//'numColumns'
      &lessThan
      &not
      &jnz label11      
      &push r:2      
      &pushsdbgv 28							//'buttonSlotWidth'
      &add
      &setRegister r:2
      &pop
      &jmp label12      
     label11:
      &pushzero
      &setRegister r:3
      &pop
      &pushzero
      &setRegister r:2
      &pop
      &push r:4      
      &pushsdbgv 7							//'buttonSlotHeight'
      &add
      &setRegister r:4
      &pop
     label12:
      &jmp label9      
     label13:
      &jmp label15      
     label14:
      &pushsdb 9							//'nextButtonSlotId'
      &pushzerosv
     label15:
      &pushsdbgv 31							//'scrollBar'
      &pushone
      &dcallfp 32							// UpdateScrollBarState()
    &end // of function EraseButtonSlot

    &function2 SetButtonSlotCount (r:5='newCount') ()
      &push r:5      
      &pushsdbgv 4							//'buttonSlots'
      &pushsdbgm 5							//'length'
      &lessThan
      &not
      &jnz label18      
     label16:
      &pushzero
      &pushsdbgv 4							//'buttonSlots'
      &pushsdb 34							//'pop'
      &callMethod
      &setRegister r:1
      &pop
      &pushzero
      &push r:1      
      &pushsdbgm 6							//'stage'
      &dcallmp 33							// removeMovieClip()
      &pushzero
      &push r:1      
      &pushsdbgm 14							//'helpSite'
      &dcallmp 33							// removeMovieClip()
      &pushsdbgv 4							//'buttonSlots'
      &pushsdbgm 5							//'length'
      &push r:5      
      &greaterThan
      &jnz label16      
      &pushsdbgv 4							//'buttonSlots'
      &pushsdbgm 5							//'length'
      &pushzero
      &equals
      &not
      &jnz label17      
      &pushsdb 9							//'nextButtonSlotId'
      &pushzerosv
     label17:
      &jmp label23      
     label18:
      &push r:5      
      &pushsdbgv 4							//'buttonSlots'
      &pushsdbgm 5							//'length'
      &greaterThan
      &not
      &jnz label23      
      &pushsdbgv 4							//'buttonSlots'
      &pushsdbgm 5							//'length'
      &pushsdbgv 25							//'numColumns'
      &divide
      &pushone
      &pushsdbgv 26							//'Math'
      &pushsdb 27							//'floor'
      &callMethod
      &setRegister r:6
      &pop
      &pushsdbgv 4							//'buttonSlots'
      &pushsdbgm 5							//'length'
      &pushsdbgv 25							//'numColumns'
      &modulo
      &setRegister r:2
      &pop
      &push r:6      
      &pushsdbgv 7							//'buttonSlotHeight'
      &multiply
      &setRegister r:4
      &pop
      &push r:2      
      &pushsdbgv 28							//'buttonSlotWidth'
      &multiply
      &setRegister r:3
      &pop
     label19:
      &pushfalse
      &jnz label23      
      &push r:4      
      &push r:3      
      &pushsdbgv 4							//'buttonSlots'
      &pushsdbgm 5							//'length'
      &pushbyte 3
      &dcallfp 29							// CreateNewButtonSlot()
      &pushsdbgv 4							//'buttonSlots'
      &pushsdbgm 5							//'length'
      &push r:5      
      &lessThan
      &not
      &not
      &jnz label20      
      &jmp label23      
     label20:
      &push r:2      
      &increment
      &setRegister r:2
      &pop
      &push r:2      
      &pushsdbgv 25							//'numColumns'
      &lessThan
      &not
      &jnz label21      
      &push r:3      
      &pushsdbgv 28							//'buttonSlotWidth'
      &add
      &setRegister r:3
      &pop
      &jmp label22      
     label21:
      &pushzero
      &setRegister r:2
      &pop
      &pushzero
      &setRegister r:3
      &pop
      &push r:4      
      &pushsdbgv 7							//'buttonSlotHeight'
      &add
      &setRegister r:4
      &pop
     label22:
      &jmp label19      
     label23:
      &pushsdbgv 31							//'scrollBar'
      &pushone
      &dcallfp 32							// UpdateScrollBarState()
    &end // of function SetButtonSlotCount

    &function2 OnScrollBarPosChanged ('pos') ()
      &pushsdb 35							//'onEnterFrame'
      &function2  () ()
        &pushzero
        &pushsdbgv 31							//'scrollBar'
        &pushsdb 36							//'GetCurPos'
        &callMethod
        &setRegister r:6
        &pop
        &pushsdbgv 4							//'buttonSlots'
        &pushsdbgm 5							//'length'
        &pushsdbgv 25							//'numColumns'
        &divide
        &pushone
        &pushsdbgv 26							//'Math'
        &pushsdb 37							//'ceil'
        &callMethod
        &setRegister r:3
        &pop
        &push r:3        
        &push r:6        
        &multiply
        &pushone
        &pushsdbgv 26							//'Math'
        &pushsdb 38							//'round'
        &callMethod
        &setRegister r:4
        &pop
        &pushzero
        &push r:4        
        &pushsdbgv 7							//'buttonSlotHeight'
        &multiply
        &subtract
        &setRegister r:1
        &pop
        &push r:1        
        &pushsdbgv 2							//'buttonStage'
        &pushsdbgm 1							//'_y'
        &subtract
        &setRegister r:5
        &pop
        &pushsdbgv 2							//'buttonStage'
        &pushsdb 1							//'_y'
        &pushsdbgv 2							//'buttonStage'
        &pushsdbgm 1							//'_y'
        &push r:5        
        &pushbyte 2
        &divide
        &add
        &setMember
        &push r:1        
        &pushsdbgv 2							//'buttonStage'
        &pushsdbgm 1							//'_y'
        &lessThan
        &not
        &jnz label26        
        &pushsdbgv 2							//'buttonStage'
        &pushsdbgm 1							//'_y'
        &pushsdbgv 7							//'buttonSlotHeight'
        &pushbyte 4
        &divide
        &subtract
        &setRegister r:2
        &pop
        &push r:1        
        &push r:2        
        &lessThan
        &not
        &jnz label24        
        &pushsdbgv 2							//'buttonStage'
        &pushsdb 1							//'_y'
        &push r:2        
        &setMember
        &jmp label25        
       label24:
        &pushsdbgv 2							//'buttonStage'
        &pushsdb 1							//'_y'
        &push r:1        
        &setMember
        &pushsdb 35							//'onEnterFrame'
        &delete2
        &pop
       label25:
        &jmp label28        
       label26:
        &pushsdbgv 2							//'buttonStage'
        &pushsdbgm 1							//'_y'
        &pushsdbgv 7							//'buttonSlotHeight'
        &pushbyte 4
        &divide
        &add
        &setRegister r:2
        &pop
        &push r:1        
        &push r:2        
        &greaterThan
        &not
        &jnz label27        
        &pushsdbgv 2							//'buttonStage'
        &pushsdb 1							//'_y'
        &push r:2        
        &setMember
        &jmp label28        
       label27:
        &pushsdbgv 2							//'buttonStage'
        &pushsdb 1							//'_y'
        &push r:1        
        &setMember
        &pushsdb 35							//'onEnterFrame'
        &delete2
        &pop
       label28:
        &pushzero
        &dcallfp 39							// UpdateButtonSlotVisibility()
      &end // of function 

      &setVariable
    &end // of function OnScrollBarPosChanged

    &function2 UpdateScrollBarState (r:2='clip') ()
      &pushsdbgv 4							//'buttonSlots'
      &pushsdbgm 5							//'length'
      &pushsdbgv 25							//'numColumns'
      &divide
      &pushone
      &pushsdbgv 26							//'Math'
      &pushsdb 37							//'ceil'
      &callMethod
      &setRegister r:1
      &pop
      &push r:1      
      &pushone
      &lessThan
      &not
      &jnz label29      
      &pushone
      &setRegister r:1
      &pop
     label29:
      &pushone
      &push r:1      
      &divide
      &pushone
      &push r:2      
      &dcallmp 40							// SetLineSize()
      &push r:1      
      &pushsdbgv 41							//'numVisibleRows'
      &greaterThan
      &not
      &not
      &jnz label30      
      &pushone
      &pushone
      &push r:2      
      &dcallmp 42							// SetPageSize()
      &pushfalse
      &pushone
      &push r:2      
      &dcallmp 43							// SetEnabled()
      &pushfalse
      &pushone
      &push r:2      
      &dcallmp 44							// SetVisible()
      &jmp label31      
     label30:
      &pushsdbgv 41							//'numVisibleRows'
      &push r:1      
      &divide
      &pushone
      &push r:2      
      &dcallmp 42							// SetPageSize()
      &pushtrue
      &pushone
      &push r:2      
      &dcallmp 43							// SetEnabled()
      &pushtrue
      &pushone
      &push r:2      
      &dcallmp 44							// SetVisible()
     label31:
    &end // of function UpdateScrollBarState

    &function GetScrollBarParam ('clip'    )    
      &pushsdbgv 45							//'scrollBarParam'
      &return
    &end // of function GetScrollBarParam

    &function2 OnScrollBarLoaded (r:1='clip') ()
      &pushtrue
      &pushone
      &push r:1      
      &dcallmp 43							// SetEnabled()
      &pushsdbgv 46							//'scrollBarPlaceholder'
      &pushsdbgm 3							//'_height'
      &pushone
      &push r:1      
      &dcallmp 47							// SetHeight()
      &push r:1      
      &pushsdb 48							//'_xscale'
      &pushbyte 100
      &setMember
      &push r:1      
      &pushsdb 49							//'_yscale'
      &pushbyte 100
      &setMember
      &push r:1      
      &pushone
      &dcallfp 32							// UpdateScrollBarState()
      &push r:1      
      &pushsdb 50							//'OnPosChanged'
      &function2  (r:1='pos') ()
        &push r:1        
        &pushone
        &dcallfp 51							// OnScrollBarPosChanged()
      &end // of function 

      &setMember
    &end // of function OnScrollBarLoaded

    &function onUnload (    )    
      &pushsdb 39							//'UpdateButtonSlotVisibility'
      &delete2
      &pop
      &pushsdb 13							//'ShouldButtonSlotBeVisible'
      &delete2
      &pop
      &pushsdb 29							//'CreateNewButtonSlot'
      &delete2
      &pop
      &pushsdb 30							//'MoveButtonSlot'
      &delete2
      &pop
      &pushsdb 52							//'InsertButtonSlot'
      &delete2
      &pop
      &pushsdb 53							//'EraseButtonSlot'
      &delete2
      &pop
      &pushsdb 54							//'SetButtonSlotCount'
      &delete2
      &pop
      &pushsdb 51							//'OnScrollBarPosChanged'
      &delete2
      &pop
      &pushsdb 32							//'UpdateScrollBarState'
      &delete2
      &pop
      &pushsdb 55							//'GetScrollBarParam'
      &delete2
      &pop
      &pushsdb 56							//'OnScrollBarLoaded'
      &delete2
      &pop
      &pushsdb 57							//'onUnload'
      &delete2
      &pop
    &end // of function onUnload

    &pushsdb 58							//'upButtonParam'
    &pushzero
    &pushsdb 59							//'Object'
    &new
    &varEquals
    &pushsdbgv 58							//'upButtonParam'
    &pushsdb 60							//'disabledImage'
    &pushsdb 61							//'VSliderUpButtonDisabledDynFac'
    &setMember
    &pushsdbgv 58							//'upButtonParam'
    &pushsdb 62							//'upImage'
    &pushsdb 63							//'VSliderUpButtonEnabledDynFac'
    &setMember
    &pushsdbgv 58							//'upButtonParam'
    &pushsdb 64							//'overImage'
    &pushsdb 65							//'VSliderUpButtonOverDynFac'
    &setMember
    &pushsdbgv 58							//'upButtonParam'
    &pushsdb 66							//'downImage'
    &pushsdb 67							//'VSliderUpButtonPressDynFac'
    &setMember
    &pushsdb 68							//'downButtonParam'
    &pushzero
    &pushsdb 59							//'Object'
    &new
    &varEquals
    &pushsdbgv 68							//'downButtonParam'
    &pushsdb 60							//'disabledImage'
    &pushsdb 69							//'VSliderDownButtonDisabledDynFac'
    &setMember
    &pushsdbgv 68							//'downButtonParam'
    &pushsdb 62							//'upImage'
    &pushsdb 70							//'VSliderDownButtonEnabledDynFac'
    &setMember
    &pushsdbgv 68							//'downButtonParam'
    &pushsdb 64							//'overImage'
    &pushsdb 71							//'VSliderDownButtonOverDynFac'
    &setMember
    &pushsdbgv 68							//'downButtonParam'
    &pushsdb 66							//'downImage'
    &pushsdb 72							//'VSliderDownButtonPressDynFac'
    &setMember
    &pushsdb 73							//'thumbTop'
    &pushzero
    &pushsdb 59							//'Object'
    &new
    &varEquals
    &pushsdbgv 73							//'thumbTop'
    &pushsdb 60							//'disabledImage'
    &pushsdb 74							//'VSliderThumbDisabledTopDynFac'
    &setMember
    &pushsdbgv 73							//'thumbTop'
    &pushsdb 62							//'upImage'
    &pushsdb 75							//'VSliderThumbEnabledTopDynFac'
    &setMember
    &pushsdbgv 73							//'thumbTop'
    &pushsdb 64							//'overImage'
    &pushsdb 76							//'VSliderThumbOverTopDynFac'
    &setMember
    &pushsdbgv 73							//'thumbTop'
    &pushsdb 66							//'downImage'
    &pushsdb 77							//'VSliderThumbPressTopDynFac'
    &setMember
    &pushsdb 78							//'thumbMiddle'
    &pushzero
    &pushsdb 59							//'Object'
    &new
    &varEquals
    &pushsdbgv 78							//'thumbMiddle'
    &pushsdb 60							//'disabledImage'
    &pushsdb 79							//'VSliderThumbDisabledMiddleDynFac'
    &setMember
    &pushsdbgv 78							//'thumbMiddle'
    &pushsdb 62							//'upImage'
    &pushsdb 80							//'VSliderThumbEnabledMiddleDynFac'
    &setMember
    &pushsdbgv 78							//'thumbMiddle'
    &pushsdb 64							//'overImage'
    &pushsdb 81							//'VSliderThumbOverMiddleDynFac'
    &setMember
    &pushsdbgv 78							//'thumbMiddle'
    &pushsdb 66							//'downImage'
    &pushsdb 82							//'VSliderThumbPressMiddleDynFac'
    &setMember
    &pushsdb 83							//'thumbBottom'
    &pushzero
    &pushsdb 59							//'Object'
    &new
    &varEquals
    &pushsdbgv 83							//'thumbBottom'
    &pushsdb 60							//'disabledImage'
    &pushsdb 84							//'VSliderThumbDisabledBottomDynFac'
    &setMember
    &pushsdbgv 83							//'thumbBottom'
    &pushsdb 62							//'upImage'
    &pushsdb 85							//'VSliderThumbEnabledBottomDynFac'
    &setMember
    &pushsdbgv 83							//'thumbBottom'
    &pushsdb 64							//'overImage'
    &pushsdb 86							//'VSliderThumbOverBottomDynFac'
    &setMember
    &pushsdbgv 83							//'thumbBottom'
    &pushsdb 66							//'downImage'
    &pushsdb 87							//'VSliderThumbPressBottomDynFac'
    &setMember
    &pushsdb 88							//'thumbParam'
    &pushzero
    &pushsdb 59							//'Object'
    &new
    &varEquals
    &pushsdbgv 88							//'thumbParam'
    &pushsdb 89							//'topPiece'
    &pushsdbgv 73							//'thumbTop'
    &setMember
    &pushsdbgv 88							//'thumbParam'
    &pushsdb 90							//'middlePiece'
    &pushsdbgv 78							//'thumbMiddle'
    &setMember
    &pushsdbgv 88							//'thumbParam'
    &pushsdb 91							//'bottomPiece'
    &pushsdbgv 83							//'thumbBottom'
    &setMember
    &pushsdb 92							//'barParam'
    &pushzero
    &pushsdb 59							//'Object'
    &new
    &varEquals
    &pushsdbgv 92							//'barParam'
    &pushsdb 60							//'disabledImage'
    &pushsdb 93							//'VSliderBarDisabledDynFac'
    &setMember
    &pushsdbgv 92							//'barParam'
    &pushsdb 62							//'upImage'
    &pushsdb 94							//'VSliderBarUpOverDynFac'
    &setMember
    &pushsdbgv 92							//'barParam'
    &pushsdb 64							//'overImage'
    &pushsdb 94							//'VSliderBarUpOverDynFac'
    &setMember
    &pushsdb 45							//'scrollBarParam'
    &pushzero
    &pushsdb 59							//'Object'
    &new
    &setVariable
    &pushsdbgv 45							//'scrollBarParam'
    &pushsdb 95							//'upButton'
    &pushsdbgv 58							//'upButtonParam'
    &setMember
    &pushsdbgv 45							//'scrollBarParam'
    &pushsdb 96							//'downButton'
    &pushsdbgv 68							//'downButtonParam'
    &setMember
    &pushsdbgv 45							//'scrollBarParam'
    &pushsdb 97							//'thumb'
    &pushsdbgv 88							//'thumbParam'
    &setMember
    &pushsdbgv 45							//'scrollBarParam'
    &pushsdb 98							//'bar'
    &pushsdbgv 92							//'barParam'
    &setMember
    &pushsdbgv 99							//'initialized'
    &not
    &not
    &jnz label32    
    &pushsdb 100							//'buttonStageWidth'
    &pushbyte 64
    &setVariable
    &pushsdb 101							//'buttonStageHeight'
    &pushbyte 64
    &setVariable
    &pushsdb 28							//'buttonSlotWidth'
    &pushsdbgv 100							//'buttonStageWidth'
    &setVariable
    &pushsdb 7							//'buttonSlotHeight'
    &pushsdbgv 101							//'buttonStageHeight'
    &setVariable
    &pushsdb 25							//'numColumns'
    &pushbyte 3
    &setVariable
    &pushsdb 41							//'numVisibleRows'
    &pushbyte 4
    &setVariable
    &pushsdbgv 0							//'buttonMask'
    &pushsdb 3							//'_height'
    &pushsdbgv 41							//'numVisibleRows'
    &pushsdbgv 7							//'buttonSlotHeight'
    &multiply
    &setMember
    &pushsdb 4							//'buttonSlots'
    &pushzero
    &pushsdb 102							//'Array'
    &new
    &setVariable
    &pushsdb 9							//'nextButtonSlotId'
    &pushzerosv
    &pushsdb 103							//'VerticalScrollBar.swf'
    &pushone
    &pushsdbgv 31							//'scrollBar'
    &dcallmp 104							// loadMovie()
    &pushsdb 21							//'FSCommand:'
    &pushthisgv
    &toString
    &pushsdb 106							//':OnInitialized'
    &add
    &concat
    &pushsdb 107							//''
    &getURL2
    &pushsdb 99							//'initialized'
    &pushtrue
    &setVariable
   label32:
    &stop
  &end // of frame 0
  
  &importAssets &from 'libHUD.swf'
    'LoadMovieStage' &as 3
  &end // of importAssets
  
  &importAssets &from 'HelpBox.swf'
    'HelpBoxSite' &as 4
  &end // of importAssets

  &defineMovieClip 5 // total frames: 2

    &frame 0
      &stop
    &end // of frame 0

    &placeMovieClip 4 
    
      &onClipEvent &construct
        &constants 'vertAlignment', 'center', 'horzAlignment'  
        &pushsdb 0							//'vertAlignment'
        &pushsdb 1							//'center'
        &setVariable
        &pushsdb 2							//'horzAlignment'
        &pushsdb 1							//'center'
        &setVariable
      &end
    &end // of placeMovieClip 4
  &end // of defineMovieClip 5

  &defineMovieClip 6 // total frames: 1

    &placeMovieClip 1 
    
      &onClipEvent &load
        &pushs ''
        &pushbyte 7
        &pushfalse
        &setProperty
      &end
    &end // of placeMovieClip 1
  &end // of defineMovieClip 6

  &defineMovieClip 7 // total frames: 1
  &end // of defineMovieClip 7
  
  &exportAssets
    2 &as 'CommandListButtonStage'
  &end // of exportAssets
&end
