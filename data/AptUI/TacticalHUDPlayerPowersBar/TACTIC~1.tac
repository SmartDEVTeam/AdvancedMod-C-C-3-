movie 'E:\Projects\CNC3\Data\APTBUI~1\034A3~1.0-D\pc\Output\TADDB0~1\\TACTIC~1.eaf' &compressed // flash 7, total frames: 1, frame rate: 30 fps, 1024x768 px

  &frame 0
    &constants 'numRowsInFirstColumn', 'Math', 'max', 'buttonSlotHeight', 'GetNumRowsInColumn', 'row', 'col', 'nextButtonSlotId', 'LoadMovieStage', 'attachMovie', '_x', '_y', 'helpSite', 'HelpBoxSite', 'buttonStageWidth', 'vertAlignment', 'top', 'horzAlignment', 'left', 'stage', 'buttonSlots', 'splice', 'FSCommand:', ':OnButtonSlotStageCreated', 'index=', '&name=', 'ComputeSlotPositionFromIndex', 'GetColumnVerticalOffset', 'columnHorizontalOffset', 'CreateNewButtonSlot', 'length', 'MoveButtonSlot', 'removeMovieClip', 'pop', 'InsertButtonSlot', 'EraseButtonSlot', 'SetButtonSlotCount', 'onUnload', 'initialized', 'buttonStageHeight', 'buttonSlotWidth', 'Array', 'this', ':OnInitialized', '', 'extern', 'InGame'  
    &function2 GetNumRowsInColumn (r:1='col') ()
      &pushone
      &pushsdbgv 0							//'numRowsInFirstColumn'
      &push r:1      
      &subtract
      &pushbyte 2
      &pushsdbgv 1							//'Math'
      &pushsdb 2							//'max'
      &callMethod
      &return
    &end // of function GetNumRowsInColumn

    &function2 GetColumnVerticalOffset (r:1='col') ()
      &pushsdbgv 3							//'buttonSlotHeight'
      &pushsdbgv 0							//'numRowsInFirstColumn'
      &push r:1      
      &pushone
      &pushsdb 4							//'GetNumRowsInColumn'
      &callFunction
      &subtract
      &multiply
      &pushfloat 0.500000000000000
      &multiply
      &return
    &end // of function GetColumnVerticalOffset

    &function2 ComputeSlotPositionFromIndex (r:4='index') ()
      &pushsdbgv 0							//'numRowsInFirstColumn'
      &setRegister r:1
      &pop
      &pushzero
      &setRegister r:3
      &pop
      &push r:4      
      &setRegister r:2
      &pop
     label1:
      &push r:2      
      &push r:1      
      &lessThan
      &not
      &not
      &jnz label3      
      &push r:3      
      &increment
      &setRegister r:3
      &pop
      &push r:2      
      &push r:1      
      &subtract
      &setRegister r:2
      &pop
      &push r:1      
      &pushone
      &greaterThan
      &not
      &jnz label2      
      &push r:1      
      &decrement
      &setRegister r:1
      &pop
     label2:
      &jmp label1      
     label3:
      &pushsdb 5							//'row'
      &push r:2      
      &pushsdb 6							//'col'
      &push r:3      
      &pushbyte 2
      &initObject
      &return
    &end // of function ComputeSlotPositionFromIndex

    &function2 CreateNewButtonSlot (r:7='slotIndex', r:11='slotX', r:10='slotY') (r:1='this')
      &pushsdbgv 7							//'nextButtonSlotId'
      &pushsdb 7							//'nextButtonSlotId'
      &pushsdbgv 7							//'nextButtonSlotId'
      &increment
      &setVariable
      &setRegister r:2
      &pop
      &push r:2      
      &toString
      &setRegister r:5
      &pop
      &pushshort 2048
      &push r:2      
      &subtract
      &push r:2      
      &toString
      &pushsdb 8							//'LoadMovieStage'
      &pushbyte 3
      &dcallfp 9							// attachMovie()
      &push r:1      
      &push r:5      
      &getMember
      &setRegister r:4
      &pop
      &push r:4      
      &pushsdb 10							//'_x'
      &push r:11      
      &setMember
      &push r:4      
      &pushsdb 11							//'_y'
      &push r:10      
      &setMember
      &pushsdb 12							//'helpSite'
      &push r:2      
      &toString
      &add
      &setRegister r:5
      &pop
      &push r:2      
      &pushlong 65536
      &add
      &pushsdb 12							//'helpSite'
      &push r:2      
      &toString
      &add
      &pushsdb 13							//'HelpBoxSite'
      &pushbyte 3
      &dcallfp 9							// attachMovie()
      &push r:1      
      &push r:5      
      &getMember
      &setRegister r:3
      &pop
      &push r:3      
      &pushsdb 10							//'_x'
      &push r:11      
      &pushsdbgv 14							//'buttonStageWidth'
      &add
      &setMember
      &push r:3      
      &pushsdb 11							//'_y'
      &push r:10      
      &setMember
      &push r:3      
      &pushsdb 15							//'vertAlignment'
      &pushsdb 16							//'top'
      &setMember
      &push r:3      
      &pushsdb 17							//'horzAlignment'
      &pushsdb 18							//'left'
      &setMember
      &push r:4      
      &pushsdb 12							//'helpSite'
      &push r:3      
      &setMember
      &pushsdb 19							//'stage'
      &push r:4      
      &pushsdb 12							//'helpSite'
      &push r:3      
      &pushbyte 2
      &initObject
      &setRegister r:6
      &pop
      &push r:6      
      &pushzero
      &push r:7      
      &pushbyte 3
      &pushsdbgv 20							//'buttonSlots'
      &dcallmp 21							// splice()
      &pushsdb 22							//'FSCommand:'
      &push r:1      
      &toString
      &pushsdb 23							//':OnButtonSlotStageCreated'
      &add
      &concat
      &pushsdb 24							//'index='
      &push r:7      
      &add
      &pushsdb 25							//'&name='
      &add
      &push r:4      
      &toString
      &add
      &getURL2
      &push r:6      
      &return
    &end // of function CreateNewButtonSlot

    &function2 MoveButtonSlot (r:6='slotIndex', r:5='slotX', r:4='slotY') ()
      &pushsdbgv 20							//'buttonSlots'
      &push r:6      
      &getMember
      &setRegister r:1
      &pop
      &push r:1      
      &pushsdbgm 19							//'stage'
      &setRegister r:3
      &pop
      &push r:3      
      &pushsdb 10							//'_x'
      &push r:5      
      &setMember
      &push r:3      
      &pushsdb 11							//'_y'
      &push r:4      
      &setMember
      &push r:1      
      &pushsdbgm 12							//'helpSite'
      &setRegister r:2
      &pop
      &push r:2      
      &pushsdb 10							//'_x'
      &push r:5      
      &pushsdbgv 14							//'buttonStageWidth'
      &add
      &setMember
      &push r:2      
      &pushsdb 11							//'_y'
      &push r:4      
      &setMember
    &end // of function MoveButtonSlot

    &function2 InsertButtonSlot (r:3='index') ()
      &push r:3      
      &pushone
      &pushsdb 26							//'ComputeSlotPositionFromIndex'
      &callFunction
      &setRegister r:7
      &pop
      &push r:7      
      &pushsdbgm 6							//'col'
      &setRegister r:1
      &pop
      &push r:7      
      &pushsdbgm 5							//'row'
      &setRegister r:2
      &pop
      &push r:1      
      &pushone
      &pushsdb 27							//'GetColumnVerticalOffset'
      &callFunction
      &push r:2      
      &pushsdbgv 3							//'buttonSlotHeight'
      &multiply
      &add
      &setRegister r:4
      &pop
      &push r:1      
      &pushsdbgv 28							//'columnHorizontalOffset'
      &multiply
      &setRegister r:5
      &pop
      &push r:4      
      &push r:5      
      &push r:3      
      &pushbyte 3
      &dcallfp 29							// CreateNewButtonSlot()
      &push r:1      
      &pushone
      &pushsdb 4							//'GetNumRowsInColumn'
      &callFunction
      &setRegister r:6
      &pop
      &push r:3      
      &increment
      &setRegister r:3
      &pop
     label4:
      &push r:3      
      &pushsdbgv 20							//'buttonSlots'
      &pushsdbgm 30							//'length'
      &lessThan
      &not
      &jnz label7      
      &push r:2      
      &increment
      &setRegister r:2
      &pop
      &push r:2      
      &push r:6      
      &lessThan
      &not
      &jnz label5      
      &push r:4      
      &pushsdbgv 3							//'buttonSlotHeight'
      &add
      &setRegister r:4
      &pop
      &jmp label6      
     label5:
      &push r:1      
      &increment
      &setRegister r:1
      &pop
      &pushzero
      &setRegister r:2
      &pop
      &push r:1      
      &pushone
      &pushsdb 27							//'GetColumnVerticalOffset'
      &callFunction
      &setRegister r:4
      &pop
      &push r:5      
      &pushsdbgv 28							//'columnHorizontalOffset'
      &add
      &setRegister r:5
      &pop
      &push r:1      
      &pushone
      &pushsdb 4							//'GetNumRowsInColumn'
      &callFunction
      &setRegister r:6
      &pop
     label6:
      &push r:4      
      &push r:5      
      &push r:3      
      &pushbyte 3
      &dcallfp 31							// MoveButtonSlot()
      &push r:3      
      &increment
      &setRegister r:3
      &pop
      &jmp label4      
     label7:
    &end // of function InsertButtonSlot

    &function2 EraseButtonSlot (r:1='index') ()
      &pushsdbgv 20							//'buttonSlots'
      &push r:1      
      &getMember
      &setRegister r:9
      &pop
      &push r:9      
      &pushsdbgm 19							//'stage'
      &setRegister r:7
      &pop
      &push r:1      
      &pushone
      &pushsdb 26							//'ComputeSlotPositionFromIndex'
      &callFunction
      &setRegister r:8
      &pop
      &push r:8      
      &pushsdbgm 6							//'col'
      &setRegister r:2
      &pop
      &push r:8      
      &pushsdbgm 5							//'row'
      &setRegister r:3
      &pop
      &push r:7      
      &pushsdbgm 10							//'_x'
      &setRegister r:5
      &pop
      &push r:7      
      &pushsdbgm 11							//'_y'
      &setRegister r:4
      &pop
      &pushone
      &push r:1      
      &pushbyte 2
      &pushsdbgv 20							//'buttonSlots'
      &dcallmp 21							// splice()
      &pushzero
      &push r:7      
      &dcallmp 32							// removeMovieClip()
      &pushzero
      &push r:9      
      &pushsdbgm 12							//'helpSite'
      &dcallmp 32							// removeMovieClip()
      &pushsdbgv 20							//'buttonSlots'
      &pushsdbgm 30							//'length'
      &pushzero
      &greaterThan
      &not
      &jnz label13      
      &push r:1      
      &pushsdbgv 20							//'buttonSlots'
      &pushsdbgm 30							//'length'
      &lessThan
      &not
      &jnz label12      
      &push r:2      
      &pushone
      &pushsdb 4							//'GetNumRowsInColumn'
      &callFunction
      &setRegister r:6
      &pop
     label8:
      &pushfalse
      &jnz label12      
      &push r:4      
      &push r:5      
      &push r:1      
      &pushbyte 3
      &dcallfp 31							// MoveButtonSlot()
      &push r:1      
      &increment
      &setRegister r:1
      &pop
      &push r:1      
      &pushsdbgv 20							//'buttonSlots'
      &pushsdbgm 30							//'length'
      &lessThan
      &not
      &not
      &jnz label9      
      &jmp label12      
     label9:
      &push r:3      
      &increment
      &setRegister r:3
      &pop
      &push r:3      
      &push r:6      
      &lessThan
      &not
      &jnz label10      
      &push r:4      
      &pushsdbgv 3							//'buttonSlotHeight'
      &add
      &setRegister r:4
      &pop
      &jmp label11      
     label10:
      &push r:2      
      &increment
      &setRegister r:2
      &pop
      &pushzero
      &setRegister r:3
      &pop
      &push r:2      
      &pushone
      &pushsdb 27							//'GetColumnVerticalOffset'
      &callFunction
      &setRegister r:4
      &pop
      &push r:5      
      &pushsdbgv 28							//'columnHorizontalOffset'
      &add
      &setRegister r:5
      &pop
      &push r:2      
      &pushone
      &pushsdb 4							//'GetNumRowsInColumn'
      &callFunction
      &setRegister r:6
      &pop
     label11:
      &jmp label8      
     label12:
      &jmp label14      
     label13:
      &pushsdb 7							//'nextButtonSlotId'
      &pushzerosv
     label14:
    &end // of function EraseButtonSlot

    &function2 SetButtonSlotCount (r:6='newCount') ()
      &push r:6      
      &pushsdbgv 20							//'buttonSlots'
      &pushsdbgm 30							//'length'
      &lessThan
      &not
      &jnz label17      
     label15:
      &pushzero
      &pushsdbgv 20							//'buttonSlots'
      &pushsdb 33							//'pop'
      &callMethod
      &setRegister r:1
      &pop
      &pushzero
      &push r:1      
      &pushsdbgm 19							//'stage'
      &dcallmp 32							// removeMovieClip()
      &pushzero
      &push r:1      
      &pushsdbgm 12							//'helpSite'
      &dcallmp 32							// removeMovieClip()
      &pushsdbgv 20							//'buttonSlots'
      &pushsdbgm 30							//'length'
      &push r:6      
      &greaterThan
      &jnz label15      
      &pushsdbgv 20							//'buttonSlots'
      &pushsdbgm 30							//'length'
      &pushzero
      &equals
      &not
      &jnz label16      
      &pushsdb 7							//'nextButtonSlotId'
      &pushzerosv
     label16:
      &jmp label22      
     label17:
      &push r:6      
      &pushsdbgv 20							//'buttonSlots'
      &pushsdbgm 30							//'length'
      &greaterThan
      &not
      &jnz label22      
      &pushsdbgv 20							//'buttonSlots'
      &pushsdbgm 30							//'length'
      &pushone
      &pushsdb 26							//'ComputeSlotPositionFromIndex'
      &callFunction
      &setRegister r:8
      &pop
      &push r:8      
      &pushsdbgm 6							//'col'
      &setRegister r:2
      &pop
      &push r:8      
      &pushsdbgm 5							//'row'
      &setRegister r:3
      &pop
      &push r:2      
      &pushone
      &pushsdb 27							//'GetColumnVerticalOffset'
      &callFunction
      &push r:3      
      &pushsdbgv 3							//'buttonSlotHeight'
      &multiply
      &add
      &setRegister r:4
      &pop
      &push r:2      
      &pushsdbgv 28							//'columnHorizontalOffset'
      &multiply
      &setRegister r:5
      &pop
      &push r:2      
      &pushone
      &pushsdb 4							//'GetNumRowsInColumn'
      &callFunction
      &setRegister r:7
      &pop
     label18:
      &pushfalse
      &jnz label22      
      &push r:4      
      &push r:5      
      &pushsdbgv 20							//'buttonSlots'
      &pushsdbgm 30							//'length'
      &pushbyte 3
      &dcallfp 29							// CreateNewButtonSlot()
      &pushsdbgv 20							//'buttonSlots'
      &pushsdbgm 30							//'length'
      &push r:6      
      &lessThan
      &not
      &not
      &jnz label19      
      &jmp label22      
     label19:
      &push r:3      
      &increment
      &setRegister r:3
      &pop
      &push r:3      
      &push r:7      
      &lessThan
      &not
      &jnz label20      
      &push r:4      
      &pushsdbgv 3							//'buttonSlotHeight'
      &add
      &setRegister r:4
      &pop
      &jmp label21      
     label20:
      &push r:2      
      &increment
      &setRegister r:2
      &pop
      &pushzero
      &setRegister r:3
      &pop
      &push r:2      
      &pushone
      &pushsdb 27							//'GetColumnVerticalOffset'
      &callFunction
      &setRegister r:4
      &pop
      &push r:5      
      &pushsdbgv 28							//'columnHorizontalOffset'
      &add
      &setRegister r:5
      &pop
      &push r:2      
      &pushone
      &pushsdb 4							//'GetNumRowsInColumn'
      &callFunction
      &setRegister r:7
      &pop
     label21:
      &jmp label18      
     label22:
    &end // of function SetButtonSlotCount

    &function onUnload (    )    
      &pushsdb 4							//'GetNumRowsInColumn'
      &delete2
      &pop
      &pushsdb 27							//'GetColumnVerticalOffset'
      &delete2
      &pop
      &pushsdb 26							//'ComputeSlotPositionFromIndex'
      &delete2
      &pop
      &pushsdb 29							//'CreateNewButtonSlot'
      &delete2
      &pop
      &pushsdb 31							//'MoveButtonSlot'
      &delete2
      &pop
      &pushsdb 34							//'InsertButtonSlot'
      &delete2
      &pop
      &pushsdb 35							//'EraseButtonSlot'
      &delete2
      &pop
      &pushsdb 36							//'SetButtonSlotCount'
      &delete2
      &pop
      &pushsdb 37							//'onUnload'
      &delete2
      &pop
    &end // of function onUnload

    &pushsdbgv 38							//'initialized'
    &not
    &not
    &jnz label23    
    &pushsdb 14							//'buttonStageWidth'
    &pushbyte 58
    &setVariable
    &pushsdb 39							//'buttonStageHeight'
    &pushbyte 58
    &setVariable
    &pushsdb 40							//'buttonSlotWidth'
    &pushsdbgv 14							//'buttonStageWidth'
    &setVariable
    &pushsdb 3							//'buttonSlotHeight'
    &pushsdbgv 39							//'buttonStageHeight'
    &setVariable
    &pushsdb 28							//'columnHorizontalOffset'
    &pushsdbgv 40							//'buttonSlotWidth'
    &pushfloat 0.750000000000000
    &multiply
    &setVariable
    &pushsdb 0							//'numRowsInFirstColumn'
    &pushbyte 8
    &setVariable
    &pushsdb 20							//'buttonSlots'
    &pushzero
    &pushsdb 41							//'Array'
    &new
    &setVariable
    &pushsdb 7							//'nextButtonSlotId'
    &pushzerosv
    &pushsdb 38							//'initialized'
    &pushtrue
    &setVariable
    &pushsdb 22							//'FSCommand:'
    &pushthisgv
    &toString
    &pushsdb 43							//':OnInitialized'
    &add
    &concat
    &pushsdb 44							//''
    &getURL2
    &pushsdbgv 45							//'extern'
    &pushsdbgm 46							//'InGame'
    &not
    &not
    &jnz label23    
    &pushbyte 3
    &pushone
    &dcallfp 36							// SetButtonSlotCount()
   label23:
    &stop
  &end // of frame 0
  
  &importAssets &from 'libHUD.swf'
    'LoadMovieStage' &as 1
  &end // of importAssets
  
  &importAssets &from 'HelpBox.swf'
    'HelpBoxSite' &as 2
  &end // of importAssets

  &defineMovieClip 3 // total frames: 2

    &frame 0
      &stop
    &end // of frame 0

    &placeMovieClip 2 
    
      &onClipEvent &construct
        &constants 'vertAlignment', 'center', 'horzAlignment'  
        &pushsdb 0							//'vertAlignment'
        &pushsdb 1							//'center'
        &setVariable
        &pushsdb 2							//'horzAlignment'
        &pushsdb 1							//'center'
        &setVariable
      &end
    &end // of placeMovieClip 2
  &end // of defineMovieClip 3
&end
