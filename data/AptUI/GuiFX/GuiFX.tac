movie 'E:\Projects\CNC3\Data\APTBUI~1\034A3~1.0-D\pc\Output\GuiFX\\GuiFX.eaf' &compressed // flash 7, total frames: 3, frame rate: 30 fps, 1024x768 px

  &defineMovieClip 2 // total frames: 1
  &end // of defineMovieClip 2

  &defineMovieClip 5 // total frames: 1
  &end // of defineMovieClip 5

  &defineMovieClip 6 // total frames: 1
  &end // of defineMovieClip 6

  &defineMovieClip 8 // total frames: 1
  &end // of defineMovieClip 8

  &defineMovieClip 9 // total frames: 1
  &end // of defineMovieClip 9

  &defineMovieClip 11 // total frames: 1
  &end // of defineMovieClip 11

  &defineMovieClip 12 // total frames: 1
  &end // of defineMovieClip 12

  &defineMovieClip 15 // total frames: 1
  &end // of defineMovieClip 15

  &defineMovieClip 16 // total frames: 1
  &end // of defineMovieClip 16

  &defineMovieClip 19 // total frames: 1
  &end // of defineMovieClip 19

  &defineMovieClip 20 // total frames: 1
  &end // of defineMovieClip 20

  &defineMovieClip 21 // total frames: 4

    &frame 0
      &constants 'easeFactor', 'alphaFactor', 'targetSizeX', '_parent', 'targetSizeY', 'sideXPos', 'side', '_x', 'sideXMover', 'sideSize', '_height', 'sideScaler', 'cornerTop', 'cornerBot', 'cornerYPos', '_y', 'cornerYMover', 'barTop', 'barBot', 'barSize', '_width', 'barScaler', 'bgBox', 'showTraces', 'boxHeight', 'barBot._y * 2'  
      &pushsdb 0							//'easeFactor'
      &pushfloat 2.500000000000000
      &setVariable
      &pushsdb 1							//'alphaFactor'
      &pushbyte 10
      &setVariable
      &pushsdb 2							//'targetSizeX'
      &pushsdbgv 3							//'_parent'
      &pushsdbgm 2							//'targetSizeX'
      &setVariable
      &pushsdb 4							//'targetSizeY'
      &pushsdbgv 3							//'_parent'
      &pushsdbgm 4							//'targetSizeY'
      &pushbyte 2
      &divide
      &setVariable
      &pushsdb 5							//'sideXPos'
      &pushsdbgv 6							//'side'
      &pushsdbgm 7							//'_x'
      &setVariable
      &pushsdb 8							//'sideXMover'
      &pushsdbgv 2							//'targetSizeX'
      &pushsdbgv 5							//'sideXPos'
      &subtract
      &setVariable
      &pushsdbgv 6							//'side'
      &pushsdb 7							//'_x'
      &pushsdbgv 5							//'sideXPos'
      &pushsdbgv 8							//'sideXMover'
      &pushsdbgv 0							//'easeFactor'
      &divide
      &add
      &setMember
      &pushsdb 9							//'sideSize'
      &pushsdbgv 6							//'side'
      &pushsdbgm 10							//'_height'
      &setVariable
      &pushsdb 11							//'sideScaler'
      &pushsdbgv 4							//'targetSizeY'
      &pushbyte 2
      &multiply
      &pushsdbgv 9							//'sideSize'
      &subtract
      &setVariable
      &pushsdbgv 6							//'side'
      &pushsdb 10							//'_height'
      &pushsdbgv 9							//'sideSize'
      &pushsdbgv 11							//'sideScaler'
      &pushsdbgv 0							//'easeFactor'
      &divide
      &add
      &setMember
      &pushsdbgv 12							//'cornerTop'
      &pushsdb 7							//'_x'
      &pushsdbgv 6							//'side'
      &pushsdbgm 7							//'_x'
      &setMember
      &pushsdbgv 13							//'cornerBot'
      &pushsdb 7							//'_x'
      &pushsdbgv 6							//'side'
      &pushsdbgm 7							//'_x'
      &setMember
      &pushsdb 14							//'cornerYPos'
      &pushsdbgv 13							//'cornerBot'
      &pushsdbgm 15							//'_y'
      &setVariable
      &pushsdb 16							//'cornerYMover'
      &pushsdbgv 4							//'targetSizeY'
      &pushsdbgv 14							//'cornerYPos'
      &subtract
      &setVariable
      &pushsdbgv 12							//'cornerTop'
      &pushsdb 15							//'_y'
      &pushsdbgv 14							//'cornerYPos'
      &pushsdbgv 16							//'cornerYMover'
      &pushsdbgv 0							//'easeFactor'
      &divide
      &add
      &pushbyte -1
      &multiply
      &setMember
      &pushsdbgv 13							//'cornerBot'
      &pushsdb 15							//'_y'
      &pushsdbgv 14							//'cornerYPos'
      &pushsdbgv 16							//'cornerYMover'
      &pushsdbgv 0							//'easeFactor'
      &divide
      &add
      &setMember
      &pushsdbgv 17							//'barTop'
      &pushsdb 15							//'_y'
      &pushsdbgv 12							//'cornerTop'
      &pushsdbgm 15							//'_y'
      &setMember
      &pushsdbgv 18							//'barBot'
      &pushsdb 15							//'_y'
      &pushsdbgv 13							//'cornerBot'
      &pushsdbgm 15							//'_y'
      &setMember
      &pushsdb 19							//'barSize'
      &pushsdbgv 17							//'barTop'
      &pushsdbgm 20							//'_width'
      &setVariable
      &pushsdb 21							//'barScaler'
      &pushsdbgv 2							//'targetSizeX'
      &pushsdbgv 19							//'barSize'
      &subtract
      &setVariable
      &pushsdbgv 17							//'barTop'
      &pushsdb 20							//'_width'
      &pushsdbgv 19							//'barSize'
      &pushsdbgv 21							//'barScaler'
      &pushsdbgv 0							//'easeFactor'
      &divide
      &add
      &setMember
      &pushsdbgv 18							//'barBot'
      &pushsdb 20							//'_width'
      &pushsdbgv 17							//'barTop'
      &pushsdbgm 20							//'_width'
      &setMember
      &pushsdbgv 22							//'bgBox'
      &pushsdb 20							//'_width'
      &pushsdbgv 12							//'cornerTop'
      &pushsdbgm 7							//'_x'
      &pushbyte 4
      &add
      &setMember
      &pushsdbgv 22							//'bgBox'
      &pushsdb 10							//'_height'
      &pushsdbgv 18							//'barBot'
      &pushsdbgm 15							//'_y'
      &pushbyte 2
      &multiply
      &pushbyte 4
      &add
      &setMember
      &pushsdb 23							//'showTraces'
      &pushfalse
      &setVariable
      &pushsdbgv 23							//'showTraces'
      &not
      &jnz label1      
      &pushsdb 24							//'boxHeight'
      &pushsdbgv 22							//'bgBox'
      &pushsdbgm 10							//'_height'
      &add
      &trace
      &pushsdb 25							//'barBot._y * 2'
      &pushsdbgv 18							//'barBot'
      &pushsdbgm 15							//'_y'
      &pushbyte 2
      &multiply
      &add
      &trace
     label1:
    &end // of frame 0

    &frame 1
      &constants 'bufferCheckSize', 'barTop', '_width', 'barSize', '_y', 'cornerYPos', 'alphaNum'  
      &pushsdb 0							//'bufferCheckSize'
      &pushfloat 0.200000002980232
      &setVariable
      &pushsdbgv 1							//'barTop'
      &pushsdbgm 2							//'_width'
      &pushsdbgv 3							//'barSize'
      &pushsdbgv 0							//'bufferCheckSize'
      &add
      &greaterThan
      &not
      &dup
      &not
      &jnz label1      
      &pop
      &pushsdbgv 1							//'barTop'
      &pushsdbgm 2							//'_width'
      &pushsdbgv 3							//'barSize'
      &pushsdbgv 0							//'bufferCheckSize'
      &subtract
      &lessThan
      &not
     label1:
      &dup
      &not
      &jnz label2      
      &pop
      &pushsdbgv 1							//'barTop'
      &pushsdbgm 4							//'_y'
      &pushsdbgv 5							//'cornerYPos'
      &pushsdbgv 0							//'bufferCheckSize'
      &add
      &greaterThan
      &not
     label2:
      &not
      &jnz label3      
      &pushsdb 6							//'alphaNum'
      &pushbyte 100
      &setVariable
      &gotoLabel 'loopFade'
      &play
      &jmp label4      
     label3:
      &gotoLabel 'loop'
      &play
     label4:
    &end // of frame 1

    &frame 2
      &constants 'alphaNum', 'alphaFactor', 'barTop', 'glow', '_alpha', 'barBot', 'barUp', 'barDown', 'side', 'cornerTop', 'cornerBot'  
      &pushsdb 0							//'alphaNum'
      &pushsdbgv 0							//'alphaNum'
      &pushsdbgv 1							//'alphaFactor'
      &subtract
      &setVariable
      &pushsdbgv 2							//'barTop'
      &pushsdbgm 3							//'glow'
      &pushsdb 4							//'_alpha'
      &pushsdbgv 0							//'alphaNum'
      &setMember
      &pushsdbgv 5							//'barBot'
      &pushsdbgm 3							//'glow'
      &pushsdb 4							//'_alpha'
      &pushsdbgv 0							//'alphaNum'
      &setMember
      &pushsdbgv 6							//'barUp'
      &pushsdbgm 3							//'glow'
      &pushsdb 4							//'_alpha'
      &pushsdbgv 0							//'alphaNum'
      &setMember
      &pushsdbgv 7							//'barDown'
      &pushsdbgm 3							//'glow'
      &pushsdb 4							//'_alpha'
      &pushsdbgv 0							//'alphaNum'
      &setMember
      &pushsdbgv 8							//'side'
      &pushsdbgm 3							//'glow'
      &pushsdb 4							//'_alpha'
      &pushsdbgv 0							//'alphaNum'
      &setMember
      &pushsdbgv 9							//'cornerTop'
      &pushsdbgm 3							//'glow'
      &pushsdb 4							//'_alpha'
      &pushsdbgv 0							//'alphaNum'
      &setMember
      &pushsdbgv 10							//'cornerBot'
      &pushsdbgm 3							//'glow'
      &pushsdb 4							//'_alpha'
      &pushsdbgv 0							//'alphaNum'
      &setMember
    &end // of frame 2

    &frame 3
      &pushsgv 'alphaNum'
      &pushzero
      &greaterThan
      &not
      &not
      &jnz label1      
      &stop
      &jmp label2      
     label1:
      &gotoLabel 'loopFade'
      &play
     label2:
    &end // of frame 3
  &end // of defineMovieClip 21

  &defineMovieClip 23 // total frames: 1
  &end // of defineMovieClip 23

  &defineMovieClip 24 // total frames: 6

    &frame 0
      &constants 'targetSizeX', 'targetSizeY', ''  
      &function2 Show (r:1='width', r:2='height') ()
        &pushsdb 0							//'targetSizeX'
        &push r:1        
        &toNumber
        &setVariable
        &pushsdb 1							//'targetSizeY'
        &push r:2        
        &toNumber
        &setVariable
        &pushsdbgv 1							//'targetSizeY'
        &pushbyte 18
        &lessThan
        &not
        &jnz label1        
        &pushsdb 1							//'targetSizeY'
        &pushbyte 18
        &setVariable
       label1:
        &gotoFrame 1
        &play
      &end // of function Show

      &function Hide (      )      
        &gotoFrame 0
        &play
      &end // of function Hide

      &function2 Move (r:7='x', r:6='y') ()
        &push r:7        
        &toNumber
        &setRegister r:1
        &pop
        &push r:6        
        &toNumber
        &setRegister r:2
        &pop
        &pushsdbgv 0							//'targetSizeX'
        &pushsdb 2							//''
        &pushbyte 2
        &getProperty
        &multiply
        &pushbyte 100
        &divide
        &pushbyte 27
        &add
        &setRegister r:3
        &pop
        &push r:1        
        &push r:3        
        &add
        &setRegister r:1
        &pop
        &push r:1        
        &pushshort 1024
        &push r:3        
        &subtract
        &greaterThan
        &not
        &jnz label2        
        &push r:1        
        &push r:3        
        &pushbyte 2
        &multiply
        &subtract
        &setRegister r:1
        &pop
        &push r:1        
        &push r:3        
        &lessThan
        &not
        &jnz label2        
        &push r:3        
        &setRegister r:1
        &pop
       label2:
        &pushsdbgv 1							//'targetSizeY'
        &pushsdb 2							//''
        &pushbyte 3
        &getProperty
        &multiply
        &pushbyte 100
        &divide
        &pushbyte 2
        &divide
        &pushbyte 20
        &add
        &setRegister r:4
        &pop
        &push r:2        
        &push r:4        
        &lessThan
        &not
        &jnz label3        
        &push r:4        
        &setRegister r:2
        &pop
        &jmp label4        
       label3:
        &pushshort 768
        &push r:4        
        &subtract
        &setRegister r:5
        &pop
        &push r:2        
        &push r:5        
        &greaterThan
        &not
        &jnz label4        
        &push r:5        
        &setRegister r:2
        &pop
       label4:
        &pushsdb 2							//''
        &pushzero
        &push r:1        
        &setProperty
        &pushsdb 2							//''
        &pushone
        &push r:2        
        &setProperty
      &end // of function Move

    &end // of frame 0

    &frame 0
      &stop
    &end // of frame 0

    &frame 2
      &play
    &end // of frame 2

    &frame 5
      &stop
    &end // of frame 5

    &placeMovieClip 23 
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'ToolTipText'
      &end
    &end // of placeMovieClip 23
  &end // of defineMovieClip 24
  
  &exportAssets
    24 &as 'ToolTip'
  &end // of exportAssets

  &frame 0
    &constants 'Call ', '(', ')', 'FSCommand:', 'Initialized', 'FSCommand:PlaySound', 'EnableComponents:', 'FSCommand:EnableComponents', 'DisableComponents:', 'FSCommand:DisableComponents', 'InGame', 'extern', 'ToolTip', 'Show', 'Hide', 'Move', 'curEndGameMovie', '1', 'Victory', 'Defeat', '_', 'gotoAndPlay', 'PlaySound', 'length', 'View3D', 'DeleteComponent', 'GameCode', '_hide', 'ShowingMessageBox: ', 'MessageBox', 'messageType', '_show', 'isLarge', 'isAtLeastPartiallyVisible', '_change', 'ShowMessageBox', '_instant', '_close', 'StatusBox', '_open', 'fileTransferPopUp', 'ProgressBars', 'SetBarTo', 'colorInnerFrameA', '3399FF', 'colorInnerFrameB', 'colorLine', 'colorGadgetBox', 'colorGadgetGameSpeed', 'colorTextDark', '0x57512B', 'colorTextBright', '0x31210F', 'colorSubTextBright', '0xC2F47D', 'colorSubTextDark', '0x57842B', 'colorTitleA', '0xCDE47E', 'tabTextColorDark', '0x123B15', 'tabTextColorBritght', '0x8ac14d', '0x0F390D', '0xBCD46D', '_root', 'InitialSetup'  
    &function2 GameCode (r:1='func', r:2='params') ()
      &pushsdb 0							//'Call '
      &push r:1      
      &add
      &pushsdb 1							//'('
      &add
      &push r:2      
      &add
      &pushsdb 2							//')'
      &add
      &trace
      &pushsdb 3							//'FSCommand:'
      &push r:1      
      &concat
      &push r:2      
      &getURL2
    &end // of function GameCode

    &function2 PlaySound (r:2='name') (r:1='_root')
      &push r:1      
      &pushsdbgm 4							//'Initialized'
      &not
      &not
      &jnz label1      
      &pushundef
      &return
     label1:
      &pushsdb 5							//'FSCommand:PlaySound'
      &push r:2      
      &getURL2
    &end // of function PlaySound

    &function2 EnableComponents (r:1='path') ()
      &pushsdb 6							//'EnableComponents:'
      &push r:1      
      &add
      &trace
      &pushsdb 7							//'FSCommand:EnableComponents'
      &push r:1      
      &getURL2
    &end // of function EnableComponents

    &function2 DisableComponents (r:1='path') ()
      &pushsdb 8							//'DisableComponents:'
      &push r:1      
      &add
      &trace
      &pushsdb 9							//'FSCommand:DisableComponents'
      &push r:1      
      &getURL2
    &end // of function DisableComponents

    &function2 GetExtern (r:3='ext') (r:1='_root', r:2='_global')
      &push r:2      
      &pushsdbgm 10							//'InGame'
      &not
      &jnz label2      
      &pushsdbgv 11							//'extern'
      &push r:3      
      &getMember
      &return
      &jmp label3      
     label2:
      &push r:1      
      &push r:3      
      &getMember
      &return
     label3:
    &end // of function GetExtern

    &function2 SetExtern (r:4='ext', r:3='to') (r:1='_root', r:2='_global')
      &push r:2      
      &pushsdbgm 10							//'InGame'
      &not
      &jnz label4      
      &pushsdbgv 11							//'extern'
      &push r:4      
      &push r:3      
      &setMember
      &jmp label5      
     label4:
      &push r:1      
      &push r:4      
      &push r:3      
      &setMember
     label5:
    &end // of function SetExtern

    &function2 ToggleExtern (r:3='ext') (r:1='_root', r:2='_global')
      &push r:2      
      &pushsdbgm 10							//'InGame'
      &not
      &jnz label6      
      &pushsdbgv 11							//'extern'
      &push r:3      
      &pushsdbgv 11							//'extern'
      &push r:3      
      &getMember
      &toNumber
      &not
      &setMember
      &jmp label7      
     label6:
      &push r:1      
      &push r:3      
      &push r:1      
      &push r:3      
      &getMember
      &not
      &setMember
     label7:
    &end // of function ToggleExtern

    &function2 InitialSetup () (r:1='_root', r:2='_global')
      &push r:1      
      &pushsdb 4							//'Initialized'
      &pushfalse
      &setMember
      &pushsdbgv 11							//'extern'
      &pushsdbgm 10							//'InGame'
      &not
      &jnz label8      
      &push r:2      
      &pushsdb 10							//'InGame'
      &pushtrue
      &setMember
     label8:
      &push r:1      
      &pushsdb 4							//'Initialized'
      &pushtrue
      &setMember
    &end // of function InitialSetup

    &function2 ShowToolTip (r:2='width', r:3='height') (r:1='_root')
      &push r:3      
      &toNumber
      &push r:2      
      &toNumber
      &pushbyte 2
      &push r:1      
      &pushsdbgm 12							//'ToolTip'
      &dcallmp 13							// Show()
    &end // of function ShowToolTip

    &function2 HideToolTip () (r:1='_root')
      &pushzero
      &push r:1      
      &pushsdbgm 12							//'ToolTip'
      &dcallmp 14							// Hide()
    &end // of function HideToolTip

    &function2 MoveToolTip (r:3='x', r:2='y') (r:1='_root')
      &push r:2      
      &push r:3      
      &pushbyte 2
      &push r:1      
      &pushsdbgm 12							//'ToolTip'
      &dcallmp 15							// Move()
    &end // of function MoveToolTip

    &function2 ShowEndGame (r:5='side', r:4='isDefeat', r:3='sfx1', r:2='sfx2') (r:1='_root')
      &pushsdbgv 16							//'curEndGameMovie'
      &pushundef
      &equals
      &not
      &jnz label13      
      &pushsdb 16							//'curEndGameMovie'
      &push r:4      
      &pushsdb 17							//'1'
      &equals
      &jnz label9      
      &push r:1      
      &pushsdbgm 18							//'Victory'
      &jmp label10      
     label9:
      &push r:1      
      &pushsdbgm 19							//'Defeat'
     label10:
      &setVariable
      &pushsdb 20							//'_'
      &push r:5      
      &add
      &pushone
      &pushsdbgv 16							//'curEndGameMovie'
      &dcallmp 21							// gotoAndPlay()
      &push r:3      
      &pushundef
      &equals
      &not
      &not
      &jnz label11      
      &push r:3      
      &pushone
      &dcallfp 22							// PlaySound()
     label11:
      &push r:2      
      &pushundef
      &equals
      &not
      &dup
      &not
      &jnz label12      
      &pop
      &push r:2      
      &pushsdbgm 23							//'length'
      &pushzero
      &greaterThan
     label12:
      &not
      &jnz label13      
      &push r:2      
      &pushone
      &dcallfp 22							// PlaySound()
     label13:
    &end // of function ShowEndGame

    &function2 HideEndGame () (r:1='_root')
      &pushsdbgv 16							//'curEndGameMovie'
      &pushundef
      &equals
      &not
      &not
      &jnz label14      
      &pushsdbgv 16							//'curEndGameMovie'
      &pushsdbgm 24							//'View3D'
      &pushsdb 25							//'DeleteComponent'
      &pushbyte 2
      &push r:1      
      &dcallmp 26							// GameCode()
      &pushsdb 27							//'_hide'
      &pushone
      &pushsdbgv 16							//'curEndGameMovie'
      &dcallmp 21							// gotoAndPlay()
      &pushsdb 16							//'curEndGameMovie'
      &pushundef
      &setVariable
     label14:
    &end // of function HideEndGame

    &function2 ShowMessageBox (r:1='msgType', r:2='isLarge') ()
      &pushsdb 28							//'ShowingMessageBox: '
      &push r:1      
      &add
      &trace
      &pushsdbgv 29							//'MessageBox'
      &pushsdb 30							//'messageType'
      &push r:1      
      &setMember
      &pushsdb 31							//'_show'
      &pushone
      &pushsdbgv 29							//'MessageBox'
      &dcallmp 21							// gotoAndPlay()
      &pushsdbgv 29							//'MessageBox'
      &pushsdb 32							//'isLarge'
      &push r:2      
      &setMember
    &end // of function ShowMessageBox

    &function2 ChangeMessageBox (r:1='msgType') ()
      &pushsdbgv 29							//'MessageBox'
      &pushsdbgm 33							//'isAtLeastPartiallyVisible'
      &not
      &jnz label15      
      &pushsdbgv 29							//'MessageBox'
      &pushsdb 30							//'messageType'
      &push r:1      
      &setMember
      &pushsdb 34							//'_change'
      &pushone
      &pushsdbgv 29							//'MessageBox'
      &dcallmp 21							// gotoAndPlay()
      &jmp label16      
     label15:
      &pushfalse
      &push r:1      
      &pushbyte 2
      &dcallfp 35							// ShowMessageBox()
     label16:
    &end // of function ChangeMessageBox

    &function2 HideMessageBox (r:1='instant') ()
      &pushsdbgv 29							//'MessageBox'
      &pushsdbgm 33							//'isAtLeastPartiallyVisible'
      &not
      &jnz label19      
      &push r:1      
      &not
      &jnz label17      
      &pushsdb 36							//'_instant'
      &pushone
      &pushsdbgv 29							//'MessageBox'
      &dcallmp 21							// gotoAndPlay()
      &jmp label18      
     label17:
      &pushsdb 37							//'_close'
      &pushone
      &pushsdbgv 29							//'MessageBox'
      &dcallmp 21							// gotoAndPlay()
     label18:
      &jmp label20      
     label19:
      &pushsdb 36							//'_instant'
      &pushone
      &pushsdbgv 29							//'MessageBox'
      &dcallmp 21							// gotoAndPlay()
     label20:
    &end // of function HideMessageBox

    &function ShowStatusBox (    )    
      &pushsdb 31							//'_show'
      &pushone
      &pushsdbgv 38							//'StatusBox'
      &dcallmp 21							// gotoAndPlay()
    &end // of function ShowStatusBox

    &function HideStatusBox (    )    
      &pushsdb 37							//'_close'
      &pushone
      &pushsdbgv 38							//'StatusBox'
      &dcallmp 21							// gotoAndPlay()
    &end // of function HideStatusBox

    &function FileTransferPopUpOpen (    )    
      &pushsdb 39							//'_open'
      &pushone
      &pushsdbgv 40							//'fileTransferPopUp'
      &dcallmp 21							// gotoAndPlay()
    &end // of function FileTransferPopUpOpen

    &function FileTransferPopUpClose (    )    
      &pushsdb 37							//'_close'
      &pushone
      &pushsdbgv 40							//'fileTransferPopUp'
      &dcallmp 21							// gotoAndPlay()
    &end // of function FileTransferPopUpClose

    &function2 SetBarTo (r:2='index', r:1='percent') ()
      &push r:1      
      &push r:2      
      &pushbyte 2
      &pushsdbgv 40							//'fileTransferPopUp'
      &pushsdbgm 41							//'ProgressBars'
      &dcallmp 42							// SetBarTo()
    &end // of function SetBarTo

    &stop
    &pushsdb 43							//'colorInnerFrameA'
    &pushsdb 44							//'3399FF'
    &setVariable
    &pushsdb 45							//'colorInnerFrameB'
    &pushsdb 44							//'3399FF'
    &setVariable
    &pushsdb 46							//'colorLine'
    &pushsdb 44							//'3399FF'
    &setVariable
    &pushsdb 47							//'colorGadgetBox'
    &pushsdb 44							//'3399FF'
    &setVariable
    &pushsdb 48							//'colorGadgetGameSpeed'
    &pushsdb 44							//'3399FF'
    &setVariable
    &pushsdb 49							//'colorTextDark'
    &pushsdb 50							//'0x57512B'
    &setVariable
    &pushsdb 51							//'colorTextBright'
    &pushsdb 52							//'0x31210F'
    &setVariable
    &pushsdb 53							//'colorSubTextBright'
    &pushsdb 54							//'0xC2F47D'
    &setVariable
    &pushsdb 55							//'colorSubTextDark'
    &pushsdb 56							//'0x57842B'
    &setVariable
    &pushsdb 57							//'colorTitleA'
    &pushsdb 58							//'0xCDE47E'
    &setVariable
    &pushsdb 59							//'tabTextColorDark'
    &pushsdb 60							//'0x123B15'
    &setVariable
    &pushsdb 61							//'tabTextColorBritght'
    &pushsdb 62							//'0x8ac14d'
    &setVariable
    &pushsdb 49							//'colorTextDark'
    &pushsdb 63							//'0x0F390D'
    &setVariable
    &pushsdb 51							//'colorTextBright'
    &pushsdb 64							//'0xBCD46D'
    &setVariable
    &pushsdbgv 65							//'_root'
    &pushsdbgm 4							//'Initialized'
    &not
    &not
    &jnz label21    
    &pushzero
    &dcallfp 66							// InitialSetup()
   label21:
    &pushsdb 16							//'curEndGameMovie'
    &pushundef
    &varEquals
  &end // of frame 0
  
  &exportAssets
    24 &as 'ToolTip'
  &end // of exportAssets
  
  &importAssets &from 'ShellContent.swf'
    'ShellContent_View3D' &as 25
  &end // of importAssets

  &defineMovieClip 28 // total frames: 1
  &end // of defineMovieClip 28

  &defineMovieClip 31 // total frames: 1
  &end // of defineMovieClip 31

  &defineMovieClip 32 // total frames: 1
  &end // of defineMovieClip 32

  &defineMovieClip 33 // total frames: 1
  &end // of defineMovieClip 33
  
  &importAssets &from 'Commander.swf'
    'Commander_glowline' &as 34
  &end // of importAssets
  
  &importAssets &from 'Commander.swf'
    'light streak' &as 35
  &end // of importAssets
  
  &importAssets &from 'Commander.swf'
    'light' &as 36
  &end // of importAssets
  
  &importAssets &from 'Commander.swf'
    'mask' &as 37
  &end // of importAssets
  
  &importAssets &from 'Commander.swf'
    'glow' &as 38
  &end // of importAssets

  &defineMovieClip 41 // total frames: 1
  &end // of defineMovieClip 41

  &defineMovieClip 43 // total frames: 1
  &end // of defineMovieClip 43

  &defineMovieClip 44 // total frames: 1
  &end // of defineMovieClip 44

  &defineMovieClip 49 // total frames: 1
  &end // of defineMovieClip 49

  &defineMovieClip 53 // total frames: 1
  &end // of defineMovieClip 53

  &defineMovieClip 54 // total frames: 117
  &end // of defineMovieClip 54

  &defineMovieClip 55 // total frames: 30
  &end // of defineMovieClip 55
  
  &importAssets &from 'Commander.swf'
    'Commander_fastblur' &as 56
  &end // of importAssets

  &defineMovieClip 57 // total frames: 200

    &frame 199
      &stop
    &end // of frame 199
  &end // of defineMovieClip 57

  &defineMovieClip 58 // total frames: 42

    &frame 0
      &stop
    &end // of frame 0

    &frame 9
      &stop
    &end // of frame 9

    &placeMovieClip 25 &as 'View3D'
    
      &onClipEvent &construct
        &pushs '_RenderObj'
        &pushssv 'GDI_LogoD'
        &pushs '_type'
        &pushssv 'View3D'
        &pushs '_KeepAspectRatio'
        &pushtrue
        &setVariable
        &pushs '_AnimMode'
        &pushssv 'LOOP'
        &pushs '_Frame'
        &pushzerosv
      &end
    &end // of placeMovieClip 25

    &frame 17
      &stop
    &end // of frame 17

    &placeMovieClip 25 &as 'View3D'
    
      &onClipEvent &construct
        &pushs '_RenderObj'
        &pushssv 'Nod_LogoD'
        &pushs '_type'
        &pushssv 'View3D'
        &pushs '_KeepAspectRatio'
        &pushtrue
        &setVariable
        &pushs '_AnimMode'
        &pushssv 'LOOP'
        &pushs '_Frame'
        &pushzerosv
      &end
    &end // of placeMovieClip 25

    &frame 27
      &stop
    &end // of frame 27

    &placeMovieClip 25 &as 'View3D'
    
      &onClipEvent &construct
        &pushs '_RenderObj'
        &pushssv 'Alien_LogoD'
        &pushs '_type'
        &pushssv 'View3D'
        &pushs '_KeepAspectRatio'
        &pushtrue
        &setVariable
        &pushs '_AnimMode'
        &pushssv 'LOOP'
        &pushs '_Frame'
        &pushzerosv
      &end
    &end // of placeMovieClip 25

    &frame 41
      &gotoLabel '_hidden'
    &end // of frame 41
  &end // of defineMovieClip 58

  &defineMovieClip 59 // total frames: 42

    &frame 0
      &stop
    &end // of frame 0

    &frame 9
      &stop
    &end // of frame 9

    &placeMovieClip 25 &as 'View3D'
    
      &onClipEvent &construct
        &pushs '_RenderObj'
        &pushssv 'GDI_Logo'
        &pushs '_type'
        &pushssv 'View3D'
        &pushs '_KeepAspectRatio'
        &pushtrue
        &setVariable
        &pushs '_AnimMode'
        &pushssv 'LOOP'
        &pushs '_Frame'
        &pushzerosv
      &end
    &end // of placeMovieClip 25

    &frame 17
      &stop
    &end // of frame 17

    &placeMovieClip 25 &as 'View3D'
    
      &onClipEvent &construct
        &pushs '_RenderObj'
        &pushssv 'NOD_Logo'
        &pushs '_type'
        &pushssv 'View3D'
        &pushs '_KeepAspectRatio'
        &pushtrue
        &setVariable
        &pushs '_AnimMode'
        &pushssv 'LOOP'
        &pushs '_Frame'
        &pushzerosv
      &end
    &end // of placeMovieClip 25

    &frame 27
      &stop
    &end // of frame 27

    &placeMovieClip 25 &as 'View3D'
    
      &onClipEvent &construct
        &pushs '_RenderObj'
        &pushssv 'Alien_Logo'
        &pushs '_type'
        &pushssv 'View3D'
        &pushs '_KeepAspectRatio'
        &pushtrue
        &setVariable
        &pushs '_AnimMode'
        &pushssv 'LOOP'
        &pushs '_Frame'
        &pushzerosv
      &end
    &end // of placeMovieClip 25

    &frame 41
      &gotoLabel '_hidden'
    &end // of frame 41
  &end // of defineMovieClip 59

  &defineMovieClip 62 // total frames: 1
  &end // of defineMovieClip 62

  &defineMovieClip 63 // total frames: 1

    &placeMovieClip 62 &as 'StringInst'
    
      &onClipEvent &load
        &constants 'component', '_parent', 'this', 'stringValue', '$', 'stringName', '_name', 'TheString', '_width', 'stringWidth', 'theColor', 'Color', 'externName', 'FileTransfer:PlayerColor:', 'colorVal', '_root', 'GetExtern', 'setRGB'  
        &pushsdb 0							//'component'
        &pushsdbgv 1							//'_parent'
        &pushsdbgm 1							//'_parent'
        &varEquals
        &pushthisgv
        &pushsdb 3							//'stringValue'
        &pushsdb 4							//'$'
        &pushsdbgv 0							//'component'
        &pushsdbgm 5							//'stringName'
        &add
        &pushsdbgv 1							//'_parent'
        &pushsdbgm 6							//'_name'
        &add
        &setMember
        &pushthisgv
        &pushsdbgm 7							//'TheString'
        &pushsdb 8							//'_width'
        &pushsdbgv 0							//'component'
        &pushsdbgm 9							//'stringWidth'
        &setMember
        &pushsdb 10							//'theColor'
        &pushsdbgv 7							//'TheString'
        &pushone
        &pushsdb 11							//'Color'
        &new
        &varEquals
        &pushsdb 12							//'externName'
        &pushsdb 13							//'FileTransfer:PlayerColor:'
        &pushsdbgv 1							//'_parent'
        &pushsdbgm 6							//'_name'
        &add
        &varEquals
        &pushsdb 14							//'colorVal'
        &pushsdbgv 12							//'externName'
        &pushone
        &pushsdbgv 15							//'_root'
        &pushsdb 16							//'GetExtern'
        &callMethod
        &varEquals
        &pushsdbgv 14							//'colorVal'
        &pushundef
        &equals
        &not
        &jnz label1        
        &pushsdb 14							//'colorVal'
        &pushfloat 4280283648.000000000000000
        &pushsdbgv 1							//'_parent'
        &pushsdbgm 6							//'_name'
        &toNumber
        &pushone
        &add
        &multiply
        &setVariable
       label1:
        &pushsdbgv 14							//'colorVal'
        &toNumber
        &pushone
        &pushsdbgv 10							//'theColor'
        &dcallmp 17							// setRGB()
      &end
    &end // of placeMovieClip 62
  &end // of defineMovieClip 63

  &defineMovieClip 64 // total frames: 1
  &end // of defineMovieClip 64

  &defineMovieClip 67 // total frames: 1
  &end // of defineMovieClip 67

  &defineMovieClip 70 // total frames: 1
  &end // of defineMovieClip 70

  &defineMovieClip 71 // total frames: 1

    &frame 0
      &constants '_x', 'vSpacingX', 'vDepth', '_name', '_', 'duplicateMovieClip', 'vCurPercent:', 'vCurPercent', ' ,', 'vNumSegments', 'Math', 'round', 'ProgressFull', 'AddSegment', 'vIntervalId', 'clearInterval', 'seg', 'ProgressEmpty', 'FrameUpdate', 'setInterval'  
      &function2 AddSegment (r:1='from', r:5='seg') ()
        &push r:1        
        &pushsdbgm 0							//'_x'
        &push r:5        
        &pushsdbgv 1							//'vSpacingX'
        &multiply
        &add
        &setRegister r:2
        &pop
        &pushsdb 0							//'_x'
        &push r:2        
        &pushone
        &initObject
        &pushsdbgv 2							//'vDepth'
        &pushsdb 2							//'vDepth'
        &pushsdbgv 2							//'vDepth'
        &increment
        &setVariable
        &push r:1        
        &pushsdbgm 3							//'_name'
        &pushsdb 4							//'_'
        &add
        &push r:5        
        &add
        &pushbyte 3
        &push r:1        
        &pushsdb 5							//'duplicateMovieClip'
        &callMethod
        &setRegister r:3
        &pop
      &end // of function AddSegment

      &function2 SetPercent (r:4='newPercent') ()
        &pushfalse
        &setRegister r:2
        &pop
       label1:
        &push r:2        
        &not
        &not
        &jnz label6        
        &pushtrue
        &setRegister r:2
        &pop
        &pushsdb 6							//'vCurPercent:'
        &pushsdbgv 7							//'vCurPercent'
        &add
        &pushsdb 8							//' ,'
        &add
        &push r:4        
        &add
        &trace
        &pushsdbgv 7							//'vCurPercent'
        &push r:4        
        &lessThan
        &dup
        &not
        &jnz label2        
        &pop
        &pushsdbgv 7							//'vCurPercent'
        &pushbyte 100
        &lessThan
       label2:
        &not
        &jnz label5        
        &pushsdbgv 9							//'vNumSegments'
        &pushsdbgv 7							//'vCurPercent'
        &multiply
        &pushbyte 100
        &divide
        &pushone
        &pushsdbgv 10							//'Math'
        &pushsdb 11							//'round'
        &callMethod
        &setRegister r:3
        &pop
        &pushsdb 7							//'vCurPercent'
        &pushsdbgv 7							//'vCurPercent'
        &increment
        &setVariable
        &pushsdb 6							//'vCurPercent:'
        &pushsdbgv 7							//'vCurPercent'
        &add
        &trace
        &pushsdbgv 9							//'vNumSegments'
        &pushsdbgv 7							//'vCurPercent'
        &multiply
        &pushbyte 100
        &divide
        &pushone
        &pushsdbgv 10							//'Math'
        &pushsdb 11							//'round'
        &callMethod
        &setRegister r:1
        &pop
        &push r:3        
        &push r:1        
        &equals
        &not
        &not
        &jnz label3        
        &push r:1        
        &pushsdbgv 12							//'ProgressFull'
        &pushbyte 2
        &dcallfp 13							// AddSegment()
       label3:
        &pushsdbgv 7							//'vCurPercent'
        &pushbyte 100
        &equals
        &not
        &jnz label4        
        &pushsdbgv 14							//'vIntervalId'
        &pushone
        &dcallfp 15							// clearInterval()
        &jmp label5        
       label4:
        &pushsdbgv 7							//'vCurPercent'
        &push r:4        
        &lessThan
        &not
        &setRegister r:2
        &pop
       label5:
        &jmp label1        
       label6:
      &end // of function SetPercent

      &pushsdb 7							//'vCurPercent'
      &pushzero
      &varEquals
      &pushsdb 9							//'vNumSegments'
      &pushbyte 25
      &varEquals
      &pushsdb 1							//'vSpacingX'
      &pushbyte 11
      &varEquals
      &pushsdb 2							//'vDepth'
      &pushbyte 100
      &varEquals
      &pushsdb 16							//'seg'
      &pushone
      &varEquals
     label7:
      &pushsdbgv 16							//'seg'
      &pushsdbgv 9							//'vNumSegments'
      &greaterThan
      &not
      &not
      &jnz label8      
      &pushsdbgv 16							//'seg'
      &pushsdbgv 17							//'ProgressEmpty'
      &pushbyte 2
      &dcallfp 13							// AddSegment()
      &pushsdb 16							//'seg'
      &pushsdbgv 16							//'seg'
      &increment
      &setVariable
      &jmp label7      
     label8:
      &pushsdb 14							//'vIntervalId'
      &pushbyte 100
      &pushsdbgv 18							//'FrameUpdate'
      &pushbyte 2
      &pushsdb 19							//'setInterval'
      &callFunction
      &varEquals
    &end // of frame 0
  &end // of defineMovieClip 71

  &defineMovieClip 73 // total frames: 1

    &frame 0
      &constants 'vCurrentPrecent', '', 'Text', 'text', '%', '&dropShadow', 'Bar', 'SetPercent'  
      &function2 SetPercent (r:1='to') ()
        &push r:1        
        &pushsdbgv 0							//'vCurrentPrecent'
        &lessThan
        &not
        &not
        &jnz label3        
        &pushsdb 0							//'vCurrentPrecent'
        &push r:1        
        &setVariable
        &push r:1        
        &pushzero
        &greaterThan
        &not
        &not
        &jnz label1        
        &pushsdb 1							//''
        &pushbyte 7
        &pushfalse
        &setProperty
        &pushsdbgv 2							//'Text'
        &pushsdb 3							//'text'
        &pushsdb 1							//''
        &setMember
        &jmp label2        
       label1:
        &pushsdb 1							//''
        &pushbyte 7
        &pushtrue
        &setProperty
        &pushsdbgv 2							//'Text'
        &pushsdb 3							//'text'
        &pushsdbgv 0							//'vCurrentPrecent'
        &toString
        &pushsdb 4							//'%'
        &add
        &pushsdb 5							//'&dropShadow'
        &add
        &setMember
       label2:
        &push r:1        
        &pushone
        &pushsdbgv 6							//'Bar'
        &dcallmp 7							// SetPercent()
       label3:
      &end // of function SetPercent

      &pushsdb 0							//'vCurrentPrecent'
      &pushbyte -1
      &varEquals
      &pushbyte -1
      &pushone
      &dcallfp 7							// SetPercent()
    &end // of frame 0
  &end // of defineMovieClip 73

  &defineMovieClip 74 // total frames: 1

    &frame 0
      &function2 SetBarTo (r:4='index', r:3='percent') (r:1='this')
        &pushs 'Bar'
        &push r:4        
        &add
        &setRegister r:2
        &pop
        &pushs 'SetBarTo:'
        &push r:2        
        &add
        &pushs '='
        &add
        &push r:1        
        &push r:2        
        &getMember
        &add
        &trace
        &push r:3        
        &pushone
        &push r:1        
        &push r:2        
        &getMember
        &pushs 'SetPercent'
        &callmp
      &end // of function SetBarTo

    &end // of frame 0
  &end // of defineMovieClip 74

  &defineMovieClip 81 // total frames: 1
  &end // of defineMovieClip 81

  &defineMovieClip 82 // total frames: 20

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19
  &end // of defineMovieClip 82

  &defineMovieClip 86 // total frames: 1
  &end // of defineMovieClip 86

  &defineMovieClip 87 // total frames: 1
  &end // of defineMovieClip 87

  &defineMovieClip 88 // total frames: 15

    &placeMovieClip 87 
    
      &onClipEvent &load
        &pushs 'visible'
        &pushfalse
        &setVariable
      &end
    &end // of placeMovieClip 87

    &frame 14
      &stop
    &end // of frame 14
  &end // of defineMovieClip 88

  &defineMovieClip 90 // total frames: 1

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
  &end // of defineMovieClip 90

  &defineMovieClip 92 // total frames: 1

    &frame 0
      &constants 'colorInnerA', 'this', 'Color', '0x', '_root', 'colorInnerFrameA', 'setRGB'  
      &pushsdb 0							//'colorInnerA'
      &pushthisgv
      &pushone
      &pushsdb 2							//'Color'
      &new
      &setVariable
      &pushsdb 3							//'0x'
      &pushsdbgv 4							//'_root'
      &pushsdbgm 5							//'colorInnerFrameA'
      &add
      &pushone
      &pushsdbgv 0							//'colorInnerA'
      &dcallmp 6							// setRGB()
    &end // of frame 0
  &end // of defineMovieClip 92

  &defineMovieClip 93 // total frames: 1
  &end // of defineMovieClip 93

  &defineMovieClip 95 // total frames: 1
  &end // of defineMovieClip 95

  &defineMovieClip 97 // total frames: 1

    &frame 0
      &pushsgv 'Text'
      &pushs 'textColor'
      &pushsgv '_root'
      &pushsgm 'colorTextBright'
      &setMember
    &end // of frame 0
  &end // of defineMovieClip 97

  &defineMovieClip 99 // total frames: 1
  &end // of defineMovieClip 99

  &defineMovieClip 100 // total frames: 1

    &placeMovieClip 99 
    
      &onClipEvent &load
        &pushthisgv
        &pushs 'stringName'
        &pushssm '$FileTransferLoadingPlayerName'
      &end
    &end // of placeMovieClip 99

    &placeMovieClip 99 
    
      &onClipEvent &load
        &pushthisgv
        &pushs 'stringName'
        &pushssm '$FileTransferLoadingProgress'
      &end
    &end // of placeMovieClip 99

    &placeMovieClip 99 
    
      &onClipEvent &load
        &pushthisgv
        &pushs 'stringName'
        &pushssm '$FileTransferLoadingStatus'
      &end
    &end // of placeMovieClip 99
  &end // of defineMovieClip 100

  &defineMovieClip 101 // total frames: 40

    &frame 0
      &pushglobalgv
      &pushsgm 'InGame'
      &not
      &not
      &jnz label1      
      &stop
      &jmp label2      
     label1:
      &stop
     label2:
    &end // of frame 0

    &frame 1
      &play
      &pushzero
      &pushsgv '_root'
      &pushs 'DisableComponents'
      &callmp
    &end // of frame 1

    &placeMovieClip 64 &as 'PlayerName'
    
      &onClipEvent &construct
        &pushs 'stringWidth'
        &pushshort 160
        &setVariable
        &pushs 'stringName'
        &pushssv 'FileTransfer::PlayerName'
      &end
    &end // of placeMovieClip 64

    &placeMovieClip 64 &as 'PlayerName'
    
      &onClipEvent &construct
        &pushs 'stringWidth'
        &pushshort 160
        &setVariable
        &pushs 'stringName'
        &pushssv 'FileTransfer::Status'
      &end
    &end // of placeMovieClip 64

    &placeMovieClip 64 &as 'PlayerName'
    
      &onClipEvent &construct
        &pushs 'stringWidth'
        &pushshort 160
        &setVariable
        &pushs 'stringName'
        &pushssv 'FileTransfer::PlayerName'
      &end
    &end // of placeMovieClip 64

    &placeMovieClip 64 &as 'PlayerName'
    
      &onClipEvent &construct
        &pushs 'stringWidth'
        &pushshort 160
        &setVariable
        &pushs 'stringName'
        &pushssv 'FileTransfer::Status'
      &end
    &end // of placeMovieClip 64

    &frame 28
      &stop
    &end // of frame 28

    &frame 39
      &pushzero
      &pushsgv '_root'
      &pushs 'EnableComponents'
      &callmp
      &gotoFrame 0
    &end // of frame 39
  &end // of defineMovieClip 101

  &defineMovieClip 103 // total frames: 1
  &end // of defineMovieClip 103

  &defineMovieClip 106 // total frames: 1
  &end // of defineMovieClip 106

  &defineMovieClip 107 // total frames: 1
  &end // of defineMovieClip 107

  &defineMovieClip 110 // total frames: 1
  &end // of defineMovieClip 110

  &defineMovieClip 111 // total frames: 63

    &frame 0
      &pushsgv '_parent'
      &pushsgm 'isLarge'
      &not
      &jnz label1      
      &gotoLabel '_large'
      &play
      &jmp label2      
     label1:
      &gotoLabel '_small'
      &play
     label2:
    &end // of frame 0

    &frame 18
      &stop
    &end // of frame 18

    &frame 43
      &stop
    &end // of frame 43
  &end // of defineMovieClip 111

  &defineMovieClip 113 // total frames: 1
  &end // of defineMovieClip 113

  &defineMovieClip 115 // total frames: 1

    &frame 0
      &constants '_parent', 'strategic', 'Title', 'textColor', '0xF1BB01'  
      &pushsdbgv 0							//'_parent'
      &pushsdbgm 0							//'_parent'
      &pushsdbgm 1							//'strategic'
      &not
      &jnz label1      
      &pushsdbgv 2							//'Title'
      &pushsdb 3							//'textColor'
      &pushsdb 4							//'0xF1BB01'
      &setMember
     label1:
    &end // of frame 0
  &end // of defineMovieClip 115

  &defineMovieClip 117 // total frames: 1
  &end // of defineMovieClip 117

  &defineMovieClip 119 // total frames: 1
  &end // of defineMovieClip 119

  &defineMovieClip 120 // total frames: 3

    &frame 0
      &constants '_parent', 'isLarge', 'strategic'  
      &pushsdbgv 0							//'_parent'
      &pushsdbgm 1							//'isLarge'
      &not
      &jnz label1      
      &gotoFrame 1
      &jmp label3      
     label1:
      &pushsdbgv 0							//'_parent'
      &pushsdbgm 2							//'strategic'
      &pushtrue
      &equals
      &not
      &jnz label2      
      &gotoFrame 2
      &jmp label3      
     label2:
      &stop
     label3:
    &end // of frame 0

    &placeMovieClip 113 
    
      &onClipEvent &load
        &constants 'text', '$', '_parent', '_Text'  
        &pushsdb 0							//'text'
        &pushsdb 1							//'$'
        &pushsdbgv 2							//'_parent'
        &pushsdbgm 2							//'_parent'
        &toString
        &add
        &pushsdb 3							//'_Text'
        &add
        &setVariable
      &end
    &end // of placeMovieClip 113

    &placeMovieClip 115 
    
      &onClipEvent &load
        &constants 'text', '$', '_parent', '_Title'  
        &pushsdb 0							//'text'
        &pushsdb 1							//'$'
        &pushsdbgv 2							//'_parent'
        &pushsdbgm 2							//'_parent'
        &toString
        &add
        &pushsdb 3							//'_Title'
        &add
        &setVariable
      &end
    &end // of placeMovieClip 115

    &placeMovieClip 117 
    
      &onClipEvent &load
        &constants 'text', '$', '_parent', '_Text'  
        &pushsdb 0							//'text'
        &pushsdb 1							//'$'
        &pushsdbgv 2							//'_parent'
        &pushsdbgm 2							//'_parent'
        &toString
        &add
        &pushsdb 3							//'_Text'
        &add
        &setVariable
      &end
    &end // of placeMovieClip 117

    &placeMovieClip 119 
    
      &onClipEvent &load
        &constants 'text', '$', '_parent', '_Text'  
        &pushsdb 0							//'text'
        &pushsdb 1							//'$'
        &pushsdbgv 2							//'_parent'
        &pushsdbgm 2							//'_parent'
        &toString
        &add
        &pushsdb 3							//'_Text'
        &add
        &setVariable
      &end
    &end // of placeMovieClip 119
  &end // of defineMovieClip 120
  
  &importAssets &from 'ShellButtons.swf'
    'ShellButtons Small' &as 121
  &end // of importAssets

  &defineMovieClip 122 // total frames: 9

    &placeMovieClip 121 &as 'MessageBoxNo'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv ''
      &end
    
      &onClipEvent &load
        &constants 'this', 'commandName', '_parent', '_OnButtonNo', 'ReleaseCallback', 'GameCode', '_close', 'gotoAndPlay'  
        &pushthisgv
        &pushsdb 1							//'commandName'
        &pushsdbgv 2							//'_parent'
        &pushsdbgm 2							//'_parent'
        &toString
        &pushsdb 3							//'_OnButtonNo'
        &add
        &setMember
        &pushsdb 4							//'ReleaseCallback'
        &function2  () (r:1='this', r:2='_root', r:3='_parent')
          &push r:1          
          &pushsdbgm 1							//'commandName'
          &pushone
          &push r:2          
          &dcallmp 5							// GameCode()
          &pushsdb 6							//'_close'
          &pushone
          &push r:3          
          &pushsdbgm 2							//'_parent'
          &dcallmp 7							// gotoAndPlay()
        &end // of function 

        &setVariable
      &end
    &end // of placeMovieClip 121

    &placeMovieClip 121 &as 'MessageBoxYes'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv ''
      &end
    
      &onClipEvent &load
        &constants 'this', 'commandName', '_parent', '_OnButtonYes', 'ReleaseCallback', 'GameCode', '_close', 'gotoAndPlay'  
        &pushthisgv
        &pushsdb 1							//'commandName'
        &pushsdbgv 2							//'_parent'
        &pushsdbgm 2							//'_parent'
        &toString
        &pushsdb 3							//'_OnButtonYes'
        &add
        &setMember
        &pushsdb 4							//'ReleaseCallback'
        &function2  () (r:1='this', r:2='_root', r:3='_parent')
          &push r:1          
          &pushsdbgm 1							//'commandName'
          &pushone
          &push r:2          
          &dcallmp 5							// GameCode()
          &pushsdb 6							//'_close'
          &pushone
          &push r:3          
          &pushsdbgm 2							//'_parent'
          &dcallmp 7							// gotoAndPlay()
        &end // of function 

        &setVariable
      &end
    &end // of placeMovieClip 121

    &frame 8
      &stop
    &end // of frame 8
  &end // of defineMovieClip 122

  &defineMovieClip 123 // total frames: 9

    &placeMovieClip 121 &as 'MessageBoxCancel'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv ''
      &end
    
      &onClipEvent &load
        &constants 'this', 'commandName', '_parent', '_OnButtonCancel', 'ReleaseCallback', 'GameCode', '_close', 'gotoAndPlay'  
        &pushthisgv
        &pushsdb 1							//'commandName'
        &pushsdbgv 2							//'_parent'
        &pushsdbgm 2							//'_parent'
        &toString
        &pushsdb 3							//'_OnButtonCancel'
        &add
        &setMember
        &pushsdb 4							//'ReleaseCallback'
        &function2  () (r:1='this', r:2='_root', r:3='_parent')
          &push r:1          
          &pushsdbgm 1							//'commandName'
          &pushone
          &push r:2          
          &dcallmp 5							// GameCode()
          &pushsdb 6							//'_close'
          &pushone
          &push r:3          
          &pushsdbgm 2							//'_parent'
          &dcallmp 7							// gotoAndPlay()
        &end // of function 

        &setVariable
      &end
    &end // of placeMovieClip 121

    &placeMovieClip 121 &as 'MessageBoxOk'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv ''
      &end
    
      &onClipEvent &load
        &constants 'this', 'commandName', '_parent', '_OnButtonOk', 'ReleaseCallback', 'GameCode', '_close', 'gotoAndPlay'  
        &pushthisgv
        &pushsdb 1							//'commandName'
        &pushsdbgv 2							//'_parent'
        &pushsdbgm 2							//'_parent'
        &toString
        &pushsdb 3							//'_OnButtonOk'
        &add
        &setMember
        &pushsdb 4							//'ReleaseCallback'
        &function2  () (r:1='this', r:2='_root', r:3='_parent')
          &push r:1          
          &pushsdbgm 1							//'commandName'
          &pushone
          &push r:2          
          &dcallmp 5							// GameCode()
          &pushsdb 6							//'_close'
          &pushone
          &push r:3          
          &pushsdbgm 2							//'_parent'
          &dcallmp 7							// gotoAndPlay()
        &end // of function 

        &setVariable
      &end
    &end // of placeMovieClip 121

    &frame 8
      &stop
    &end // of frame 8
  &end // of defineMovieClip 123

  &defineMovieClip 124 // total frames: 9

    &placeMovieClip 121 &as 'MessageBoxOk'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv ''
      &end
    
      &onClipEvent &load
        &constants 'this', 'commandName', '_parent', '_OnButtonOk', 'ReleaseCallback', 'GameCode', '_close', 'gotoAndPlay'  
        &pushthisgv
        &pushsdb 1							//'commandName'
        &pushsdbgv 2							//'_parent'
        &pushsdbgm 2							//'_parent'
        &toString
        &pushsdb 3							//'_OnButtonOk'
        &add
        &setMember
        &pushsdb 4							//'ReleaseCallback'
        &function2  () (r:1='this', r:2='_root', r:3='_parent')
          &push r:1          
          &pushsdbgm 1							//'commandName'
          &pushone
          &push r:2          
          &dcallmp 5							// GameCode()
          &pushsdb 6							//'_close'
          &pushone
          &push r:3          
          &pushsdbgm 2							//'_parent'
          &dcallmp 7							// gotoAndPlay()
        &end // of function 

        &setVariable
      &end
    &end // of placeMovieClip 121

    &frame 8
      &stop
    &end // of frame 8
  &end // of defineMovieClip 124

  &defineMovieClip 125 // total frames: 9

    &placeMovieClip 121 &as 'MessageBoxCancel'
    
      &onClipEvent &construct
        &pushs 'vStartMode'
        &pushssv ''
      &end
    
      &onClipEvent &load
        &constants 'this', 'commandName', '_parent', '_OnButtonCancel', 'ReleaseCallback', 'GameCode', '_close', 'gotoAndPlay'  
        &pushthisgv
        &pushsdb 1							//'commandName'
        &pushsdbgv 2							//'_parent'
        &pushsdbgm 2							//'_parent'
        &toString
        &pushsdb 3							//'_OnButtonCancel'
        &add
        &setMember
        &pushsdb 4							//'ReleaseCallback'
        &function2  () (r:1='this', r:2='_root', r:3='_parent')
          &push r:1          
          &pushsdbgm 1							//'commandName'
          &pushone
          &push r:2          
          &dcallmp 5							// GameCode()
          &pushsdb 6							//'_close'
          &pushone
          &push r:3          
          &pushsdbgm 2							//'_parent'
          &dcallmp 7							// gotoAndPlay()
        &end // of function 

        &setVariable
      &end
    &end // of placeMovieClip 121

    &frame 8
      &stop
    &end // of frame 8
  &end // of defineMovieClip 125

  &defineMovieClip 126 // total frames: 39

    &frame 0
      &constants 'ShowingMessageBox: ', 'messageType', 'isLarge', 'isAtLeastPartiallyVisible', 'Show', '_global', 'InGame', 'OkCancel'  
      &function2 Show (r:1='msgType', r:2='large') ()
        &pushsdb 0							//'ShowingMessageBox: '
        &push r:1        
        &add
        &trace
        &pushsdb 1							//'messageType'
        &push r:1        
        &setVariable
        &gotoLabel '_show'
        &play
        &pushsdb 2							//'isLarge'
        &push r:2        
        &setVariable
      &end // of function Show

      &function2 Change (r:1='msgType') ()
        &pushsdbgv 3							//'isAtLeastPartiallyVisible'
        &not
        &jnz label1        
        &pushsdb 1							//'messageType'
        &push r:1        
        &setVariable
        &gotoLabel '_change'
        &play
        &jmp label2        
       label1:
        &pushfalse
        &push r:1        
        &pushbyte 2
        &dcallfp 4							// Show()
       label2:
      &end // of function Change

      &function2 Hide (r:1='instant') ()
        &pushsdbgv 3							//'isAtLeastPartiallyVisible'
        &not
        &jnz label5        
        &push r:1        
        &not
        &jnz label3        
        &gotoLabel '_instant'
        &play
        &jmp label4        
       label3:
        &gotoLabel '_close'
        &play
       label4:
        &jmp label6        
       label5:
        &gotoLabel '_instant'
        &play
       label6:
      &end // of function Hide

      &pushglobalgv
      &pushsdbgm 6							//'InGame'
      &not
      &not
      &jnz label7      
      &pushsdb 2							//'isLarge'
      &pushtrue
      &setVariable
      &pushtrue
      &pushsdb 7							//'OkCancel'
      &pushbyte 2
      &dcallfp 4							// Show()
      &jmp label8      
     label7:
      &stop
     label8:
      &pushsdb 3							//'isAtLeastPartiallyVisible'
      &pushfalse
      &setVariable
    &end // of frame 0

    &frame 1
      &constants 'callWhenDone', '', 'isAtLeastPartiallyVisible', '_root', 'DisableComponents', 'ButtonsYesNo', '_visible', 'messageType', 'YesNo', 'ButtonsOk', 'Ok', 'ButtonsCancel', 'Cancel', 'ButtonsOkCancel', 'OkCancel', 'FSCommand:', 'this', '_OnShowing', 'strategic', 'StrategicFrame', 'ShellFrame'  
      &pushsdb 0							//'callWhenDone'
      &pushsdb 1							//''
      &setVariable
      &pushsdb 2							//'isAtLeastPartiallyVisible'
      &pushfalse
      &setVariable
      &pushzero
      &pushsdbgv 3							//'_root'
      &dcallmp 4							// DisableComponents()
      &pushsdbgv 5							//'ButtonsYesNo'
      &pushsdb 6							//'_visible'
      &pushsdbgv 7							//'messageType'
      &pushsdb 8							//'YesNo'
      &equals
      &setMember
      &pushsdbgv 9							//'ButtonsOk'
      &pushsdb 6							//'_visible'
      &pushsdbgv 7							//'messageType'
      &pushsdb 10							//'Ok'
      &equals
      &setMember
      &pushsdbgv 11							//'ButtonsCancel'
      &pushsdb 6							//'_visible'
      &pushsdbgv 7							//'messageType'
      &pushsdb 12							//'Cancel'
      &equals
      &setMember
      &pushsdbgv 13							//'ButtonsOkCancel'
      &pushsdb 6							//'_visible'
      &pushsdbgv 7							//'messageType'
      &pushsdb 14							//'OkCancel'
      &equals
      &setMember
      &play
      &pushsdb 15							//'FSCommand:'
      &pushthisgv
      &toString
      &pushsdb 17							//'_OnShowing'
      &add
      &concat
      &pushsdb 1							//''
      &getURL2
      &pushsdbgv 18							//'strategic'
      &not
      &jnz label1      
      &pushsdbgv 19							//'StrategicFrame'
      &pushsdb 6							//'_visible'
      &pushtrue
      &setMember
      &pushsdbgv 20							//'ShellFrame'
      &pushsdb 6							//'_visible'
      &pushfalse
      &setMember
      &jmp label2      
     label1:
      &pushsdbgv 19							//'StrategicFrame'
      &pushsdb 6							//'_visible'
      &pushfalse
      &setMember
      &pushsdbgv 20							//'ShellFrame'
      &pushsdb 6							//'_visible'
      &pushtrue
      &setMember
     label2:
    &end // of frame 1

    &frame 2
      &pushs 'isAtLeastPartiallyVisible'
      &pushtrue
      &setVariable
    &end // of frame 2

    &frame 12
      &stop
      &pushs 'FSCommand:'
      &pushthisgv
      &toString
      &pushs '_OnShown'
      &add
      &concat
      &pushs ''
      &getURL2
    &end // of frame 12

    &frame 18
      &constants 'ButtonsYesNo', '_visible', 'messageType', 'YesNo', 'ButtonsOk', 'Ok', 'ButtonsOkCancel', 'OkCancel'  
      &pushsdbgv 0							//'ButtonsYesNo'
      &pushsdb 1							//'_visible'
      &pushsdbgv 2							//'messageType'
      &pushsdb 3							//'YesNo'
      &equals
      &setMember
      &pushsdbgv 4							//'ButtonsOk'
      &pushsdb 1							//'_visible'
      &pushsdbgv 2							//'messageType'
      &pushsdb 5							//'Ok'
      &equals
      &setMember
      &pushsdbgv 6							//'ButtonsOkCancel'
      &pushsdb 1							//'_visible'
      &pushsdbgv 2							//'messageType'
      &pushsdb 7							//'OkCancel'
      &equals
      &setMember
      &gotoLabel '_open'
      &play
    &end // of frame 18

    &frame 26
      &constants '_close', 'backdrop', 'gotoAndPlay', 'messageType', 'YesNo', 'messageDown', 'MessageBoxYes', '_exit', 'ButtonsYesNo', 'MessageBoxNo', 'OkCancel', 'MessageBoxOk', 'ButtonsOkCancel', 'MessageBoxCancel', 'isAtLeastPartiallyVisible', 'FSCommand:', 'this', '_OnHiding', ''  
      &pushsdb 0							//'_close'
      &pushone
      &pushsdbgv 1							//'backdrop'
      &dcallmp 2							// gotoAndPlay()
      &pushsdbgv 3							//'messageType'
      &pushsdb 4							//'YesNo'
      &equals
      &not
      &jnz label3      
      &pushsdbgv 5							//'messageDown'
      &pushsdb 6							//'MessageBoxYes'
      &equals
      &not
      &jnz label1      
      &pushsdb 7							//'_exit'
      &pushone
      &pushsdbgv 8							//'ButtonsYesNo'
      &pushsdbgm 9							//'MessageBoxNo'
      &dcallmp 2							// gotoAndPlay()
      &jmp label2      
     label1:
      &pushsdbgv 5							//'messageDown'
      &pushsdb 9							//'MessageBoxNo'
      &equals
      &not
      &jnz label2      
      &pushsdb 7							//'_exit'
      &pushone
      &pushsdbgv 8							//'ButtonsYesNo'
      &pushsdbgm 6							//'MessageBoxYes'
      &dcallmp 2							// gotoAndPlay()
     label2:
      &jmp label5      
     label3:
      &pushsdbgv 3							//'messageType'
      &pushsdb 10							//'OkCancel'
      &equals
      &not
      &jnz label5      
      &pushsdbgv 5							//'messageDown'
      &pushsdb 11							//'MessageBoxOk'
      &equals
      &not
      &jnz label4      
      &pushsdb 7							//'_exit'
      &pushone
      &pushsdbgv 12							//'ButtonsOkCancel'
      &pushsdbgm 13							//'MessageBoxCancel'
      &dcallmp 2							// gotoAndPlay()
      &jmp label5      
     label4:
      &pushsdbgv 5							//'messageDown'
      &pushsdb 13							//'MessageBoxCancel'
      &equals
      &not
      &jnz label5      
      &pushsdb 7							//'_exit'
      &pushone
      &pushsdbgv 12							//'ButtonsOkCancel'
      &pushsdbgm 11							//'MessageBoxOk'
      &dcallmp 2							// gotoAndPlay()
     label5:
      &pushsdb 14							//'isAtLeastPartiallyVisible'
      &pushtrue
      &setVariable
      &pushsdb 15							//'FSCommand:'
      &pushthisgv
      &toString
      &pushsdb 17							//'_OnHiding'
      &add
      &concat
      &pushsdb 18							//''
      &getURL2
    &end // of frame 26

    &frame 33
      &constants '_root', 'EnableComponents', 'isAtLeastPartiallyVisible', 'callWhenDone', 'FSCommand:', '', 'this', '_OnHidden'  
      &pushzero
      &pushsdbgv 0							//'_root'
      &dcallmp 1							// EnableComponents()
      &pushsdb 2							//'isAtLeastPartiallyVisible'
      &pushfalse
      &setVariable
      &pushsdbgv 3							//'callWhenDone'
      &pushundef
      &equals
      &not
      &not
      &jnz label1      
      &pushsdb 4							//'FSCommand:'
      &pushsdbgv 3							//'callWhenDone'
      &concat
      &pushsdb 5							//''
      &getURL2
      &pushsdb 3							//'callWhenDone'
      &pushsdb 5							//''
      &setVariable
     label1:
      &pushsdb 4							//'FSCommand:'
      &pushthisgv
      &toString
      &pushsdb 7							//'_OnHidden'
      &add
      &concat
      &pushsdb 5							//''
      &getURL2
    &end // of frame 33

    &frame 38
      &stop
    &end // of frame 38
  &end // of defineMovieClip 126

  &frame 1
    &stop
  &end // of frame 1

  &frame 2
    &stop
  &end // of frame 2

  &defineMovieClip 129 // total frames: 1
  &end // of defineMovieClip 129

  &defineMovieClip 130 // total frames: 29

    &frame 1
      &play
      &pushs '_open'
      &pushone
      &pushsgv 'backdrop'
      &pushs 'gotoAndPlay'
      &callmp
    &end // of frame 1

    &frame 17
      &stop
    &end // of frame 17

    &frame 18
      &pushs '_close'
      &pushone
      &pushsgv 'backdrop'
      &pushs 'gotoAndPlay'
      &callmp
      &pushs 'StatusBoxHiding'
      &pushone
      &pushsgv '_root'
      &pushs 'GameCode'
      &callmp
    &end // of frame 18

    &frame 28
      &pushzero
      &pushsgv '_root'
      &pushs 'EnableComponents'
      &callmp
      &stop
    &end // of frame 28
  &end // of defineMovieClip 130
&end
