movie 'E:\Projects\CNC3\Data\APTBUI~1\034A3~1.0-D\pc\Output\TABDD2~1\\TACTIC~1.eaf' &compressed // flash 7, total frames: 21, frame rate: 30 fps, 1024x768 px

  &defineMovieClip 11 // total frames: 30

    &frame 0
      &pushs '_'
      &pushsgv 'imageLabel'
      &add
      &gotoAndPlay    &end // of frame 0

    &frame 4
      &stop
    &end // of frame 4

    &frame 9
      &stop
    &end // of frame 9

    &frame 14
      &stop
    &end // of frame 14

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 11
  
  &exportAssets
    11 &as 'BuildQueueIndicator'
  &end // of exportAssets

  &defineMovieClip 14 // total frames: 1
  &end // of defineMovieClip 14

  &defineMovieClip 15 // total frames: 22

    &frame 10
      &constants 'onEnterFrame', 'done'  
      &stop
      &pushsdb 0							//'onEnterFrame'
      &function2  () (r:1='this')
        &push r:1        
        &pushsdbgm 1							//'done'
        &not
        &jnz label1        
        &pushsdb 0							//'onEnterFrame'
        &delete2
        &pop
        &gotoLabel '_fadeOut'
        &play
       label1:
      &end // of function 

      &setVariable
    &end // of frame 10

    &frame 21
      &constants '_parent', 'initialized', 'this', 'DestroyPing', 'removeMovieClip'  
      &pushsdbgv 0							//'_parent'
      &pushsdbgm 1							//'initialized'
      &not
      &jnz label1      
      &pushthisgv
      &pushone
      &pushsdbgv 0							//'_parent'
      &dcallmp 3							// DestroyPing()
      &jmp label2      
     label1:
      &pushzero
      &pushthisgv
      &dcallmp 4							// removeMovieClip()
     label2:
    &end // of frame 21
  &end // of defineMovieClip 15
  
  &exportAssets
    15 &as 'PingOneRing'
  &end // of exportAssets

  &defineMovieClip 18 // total frames: 1
  &end // of defineMovieClip 18

  &defineMovieClip 22 // total frames: 1
  &end // of defineMovieClip 22

  &defineMovieClip 25 // total frames: 1
  &end // of defineMovieClip 25

  &defineMovieClip 26 // total frames: 85

    &frame 0
      &pushglobalgv
      &pushsgm 'MinLOD'
      &not
      &jnz label1      
      &pushsgv 'effect1'
      &pushs '_visible'
      &pushzero
      &setMember
     label1:
    &end // of frame 0

    &frame 15
      &pushglobalgv
      &pushsgm 'MinLOD'
      &not
      &jnz label1      
      &pushsgv 'effect2'
      &pushs '_visible'
      &pushzero
      &setMember
     label1:
    &end // of frame 15

    &frame 69
      &constants 'this', 'done', '_loop', 'gotoAndPlay'  
      &pushthisgv
      &pushsdbgm 1							//'done'
      &pushundef
      &equals
      &dup
      &jnz label1      
      &pop
      &pushthisgv
      &pushsdbgm 1							//'done'
      &not
     label1:
      &not
      &jnz label2      
      &pushsdb 2							//'_loop'
      &pushone
      &pushthisgv
      &dcallmp 3							// gotoAndPlay()
     label2:
    &end // of frame 69

    &frame 84
      &constants '_parent', 'initialized', 'this', 'DestroyPing', 'removeMovieClip'  
      &pushsdbgv 0							//'_parent'
      &pushsdbgm 1							//'initialized'
      &not
      &jnz label1      
      &pushthisgv
      &pushone
      &pushsdbgv 0							//'_parent'
      &dcallmp 3							// DestroyPing()
      &jmp label2      
     label1:
      &pushzero
      &pushthisgv
      &dcallmp 4							// removeMovieClip()
     label2:
    &end // of frame 84
  &end // of defineMovieClip 26
  
  &exportAssets
    26 &as 'PingGeneric'
  &end // of exportAssets

  &defineMovieClip 29 // total frames: 1
  &end // of defineMovieClip 29

  &defineMovieClip 32 // total frames: 1
  &end // of defineMovieClip 32

  &defineMovieClip 33 // total frames: 20

    &frame 0
      &pushsgv 'isBonus'
      &not
      &jnz label1      
      &gotoLabel '_bonus'
      &play
     label1:
    &end // of frame 0

    &placeMovieClip 32 
    
      &onClipEvent &load
        &constants 'text', '$', '_parent', ':Ordinal', '_name'  
        &pushsdb 0							//'text'
        &pushsdb 1							//'$'
        &pushsdbgv 2							//'_parent'
        &pushsdbgm 2							//'_parent'
        &toString
        &add
        &pushsdb 3							//':Ordinal'
        &add
        &pushsdbgv 2							//'_parent'
        &pushsdbgm 4							//'_name'
        &add
        &setVariable
      &end
    &end // of placeMovieClip 32

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19
  &end // of defineMovieClip 33
  
  &exportAssets
    33 &as 'ObjectiveIndicator'
  &end // of exportAssets

  &defineMovieClip 36 // total frames: 1
  &end // of defineMovieClip 36

  &defineMovieClip 39 // total frames: 1
  &end // of defineMovieClip 39

  &defineMovieClip 40 // total frames: 20
  &end // of defineMovieClip 40

  &defineMovieClip 43 // total frames: 1
  &end // of defineMovieClip 43

  &defineMovieClip 46 // total frames: 1
  &end // of defineMovieClip 46

  &defineMovieClip 49 // total frames: 1
  &end // of defineMovieClip 49

  &defineMovieClip 50 // total frames: 30
  &end // of defineMovieClip 50

  &defineMovieClip 51 // total frames: 1
  &end // of defineMovieClip 51

  &defineMovieClip 53 // total frames: 1
  &end // of defineMovieClip 53

  &defineMovieClip 54 // total frames: 72

    &frame 56
      &constants '_parent', 'done', '_loop', 'this', 'gotoAndPlay'  
      &pushsdbgv 0							//'_parent'
      &pushsdbgm 1							//'done'
      &pushundef
      &equals
      &dup
      &jnz label1      
      &pop
      &pushsdbgv 0							//'_parent'
      &pushsdbgm 1							//'done'
      &not
     label1:
      &not
      &jnz label2      
      &pushsdb 2							//'_loop'
      &pushone
      &pushthisgv
      &dcallmp 4							// gotoAndPlay()
     label2:
    &end // of frame 56

    &frame 71
      &constants '_parent', 'initialized', 'this', 'DestroyPing', 'removeMovieClip'  
      &pushsdbgv 0							//'_parent'
      &pushsdbgm 1							//'initialized'
      &not
      &jnz label1      
      &pushthisgv
      &pushone
      &pushsdbgv 0							//'_parent'
      &dcallmp 3							// DestroyPing()
      &jmp label2      
     label1:
      &pushzero
      &pushthisgv
      &dcallmp 4							// removeMovieClip()
     label2:
    &end // of frame 71
  &end // of defineMovieClip 54

  &defineMovieClip 55 // total frames: 1
  &end // of defineMovieClip 55
  
  &exportAssets
    55 &as 'PingAttack'
  &end // of exportAssets

  &defineMovieClip 58 // total frames: 1
  &end // of defineMovieClip 58

  &defineMovieClip 60 // total frames: 1
  &end // of defineMovieClip 60

  &defineMovieClip 63 // total frames: 1
  &end // of defineMovieClip 63

  &defineMovieClip 64 // total frames: 20
  &end // of defineMovieClip 64

  &defineMovieClip 65 // total frames: 55

    &frame 54
      &constants 'this', 'done', 'gotoAndPlay', '_parent', 'initialized', 'DestroyPing', 'removeMovieClip'  
      &pushthisgv
      &pushsdbgm 1							//'done'
      &pushundef
      &equals
      &dup
      &jnz label1      
      &pop
      &pushthisgv
      &pushsdbgm 1							//'done'
      &not
     label1:
      &not
      &jnz label2      
      &pushone
      &pushone
      &pushthisgv
      &dcallmp 2							// gotoAndPlay()
      &jmp label4      
     label2:
      &pushsdbgv 3							//'_parent'
      &pushsdbgm 4							//'initialized'
      &not
      &jnz label3      
      &pushthisgv
      &pushone
      &pushsdbgv 3							//'_parent'
      &dcallmp 5							// DestroyPing()
      &jmp label4      
     label3:
      &pushzero
      &pushthisgv
      &dcallmp 6							// removeMovieClip()
     label4:
    &end // of frame 54
  &end // of defineMovieClip 65

  &defineMovieClip 66 // total frames: 1
  &end // of defineMovieClip 66
  
  &exportAssets
    66 &as 'PingBeacon'
  &end // of exportAssets

  &defineMovieClip 69 // total frames: 1
  &end // of defineMovieClip 69

  &defineMovieClip 71 // total frames: 1
  &end // of defineMovieClip 71

  &defineMovieClip 74 // total frames: 1
  &end // of defineMovieClip 74

  &defineMovieClip 75 // total frames: 20
  &end // of defineMovieClip 75

  &defineMovieClip 76 // total frames: 53

    &frame 39
      &constants '_parent', 'done', '_loop', 'this', 'gotoAndPlay'  
      &pushsdbgv 0							//'_parent'
      &pushsdbgm 1							//'done'
      &pushundef
      &equals
      &dup
      &jnz label1      
      &pop
      &pushsdbgv 0							//'_parent'
      &pushsdbgm 1							//'done'
      &not
     label1:
      &not
      &jnz label2      
      &pushsdb 2							//'_loop'
      &pushone
      &pushthisgv
      &dcallmp 4							// gotoAndPlay()
     label2:
    &end // of frame 39

    &frame 52
      &constants '_parent', 'initialized', 'this', 'DestroyPing', 'removeMovieClip'  
      &pushsdbgv 0							//'_parent'
      &pushsdbgm 1							//'initialized'
      &not
      &jnz label1      
      &pushthisgv
      &pushone
      &pushsdbgv 0							//'_parent'
      &dcallmp 3							// DestroyPing()
      &jmp label2      
     label1:
      &pushzero
      &pushthisgv
      &dcallmp 4							// removeMovieClip()
     label2:
    &end // of frame 52
  &end // of defineMovieClip 76

  &defineMovieClip 77 // total frames: 1
  &end // of defineMovieClip 77
  
  &exportAssets
    77 &as 'PingInformation'
  &end // of exportAssets

  &defineMovieClip 80 // total frames: 1
  &end // of defineMovieClip 80

  &defineMovieClip 83 // total frames: 1
  &end // of defineMovieClip 83

  &defineMovieClip 84 // total frames: 30
  &end // of defineMovieClip 84

  &defineMovieClip 85 // total frames: 1
  &end // of defineMovieClip 85

  &defineMovieClip 86 // total frames: 59

    &frame 45
      &constants '_parent', 'done', '_loop', 'this', 'gotoAndPlay'  
      &pushsdbgv 0							//'_parent'
      &pushsdbgm 1							//'done'
      &pushundef
      &equals
      &dup
      &jnz label1      
      &pop
      &pushsdbgv 0							//'_parent'
      &pushsdbgm 1							//'done'
      &not
     label1:
      &not
      &jnz label2      
      &pushsdb 2							//'_loop'
      &pushone
      &pushthisgv
      &dcallmp 4							// gotoAndPlay()
     label2:
    &end // of frame 45

    &frame 58
      &constants '_parent', 'initialized', 'this', 'DestroyPing', 'removeMovieClip'  
      &pushsdbgv 0							//'_parent'
      &pushsdbgm 1							//'initialized'
      &not
      &jnz label1      
      &pushthisgv
      &pushone
      &pushsdbgv 0							//'_parent'
      &dcallmp 3							// DestroyPing()
      &jmp label2      
     label1:
      &pushzero
      &pushthisgv
      &dcallmp 4							// removeMovieClip()
     label2:
    &end // of frame 58
  &end // of defineMovieClip 86

  &defineMovieClip 87 // total frames: 1
  &end // of defineMovieClip 87
  
  &exportAssets
    87 &as 'PingUpgrade'
  &end // of exportAssets

  &frame 0
    &constants 'panel', 'viewBoxSurface', 'staticSurface', 'pingSurface', 'objectiveStage', 'movieSurface', 'buildQueueStage', 'mapWidth', 'mapHeight', '_x', 'mapX', '_y', 'mapY', '_width', '_height', 'mapAspectRatio', 'backAspectRatio', 'backWidth', 'backX', 'backY', 'backHeight', 'MoveToMapArea', 'shroudSurface', 'objectsSurface', 'taintSurface', 'terrainSurface', 'inputCatcher', 'initialized', 'Resize', 'sizer', 'jammedMessage', '_visible', 'Open', 'Close', 'GetViewBoxSurface', 'GetStaticSurface', 'GetPingStage', 'GetObjectiveStage', 'GetMovieSurface', 'GetBuildQueueStage', 'GetMapWidth', 'GetMapHeight', 'SetMapAspectRatio', 'SetJammedMessageVisibility', 'onUnload', 'back', 'FSCommand:', 'this', ':OnInitialized', '', 'extern', 'InGame'  
    &function Open (    )    
      &gotoLabel '_open'
      &play
    &end // of function Open

    &function Close (    )    
      &gotoLabel '_close'
      &play
    &end // of function Close

    &function GetViewBoxSurface (    )    
      &pushsdbgv 0							//'panel'
      &pushsdbgm 1							//'viewBoxSurface'
      &toString
      &return
    &end // of function GetViewBoxSurface

    &function GetStaticSurface (    )    
      &pushsdbgv 0							//'panel'
      &pushsdbgm 2							//'staticSurface'
      &toString
      &return
    &end // of function GetStaticSurface

    &function GetPingStage (    )    
      &pushsdbgv 0							//'panel'
      &pushsdbgm 3							//'pingSurface'
      &toString
      &return
    &end // of function GetPingStage

    &function GetObjectiveStage (    )    
      &pushsdbgv 0							//'panel'
      &pushsdbgm 4							//'objectiveStage'
      &toString
      &return
    &end // of function GetObjectiveStage

    &function GetMovieSurface (    )    
      &pushsdbgv 5							//'movieSurface'
      &toString
      &return
    &end // of function GetMovieSurface

    &function GetBuildQueueStage (    )    
      &pushsdbgv 0							//'panel'
      &pushsdbgm 6							//'buildQueueStage'
      &toString
      &return
    &end // of function GetBuildQueueStage

    &function GetMapWidth (    )    
      &pushsdbgv 7							//'mapWidth'
      &toString
      &return
    &end // of function GetMapWidth

    &function GetMapHeight (    )    
      &pushsdbgv 8							//'mapHeight'
      &toString
      &return
    &end // of function GetMapHeight

    &function2 MoveToMapArea (r:1='clip') ()
      &push r:1      
      &pushsdb 9							//'_x'
      &pushsdbgv 10							//'mapX'
      &setMember
      &push r:1      
      &pushsdb 11							//'_y'
      &pushsdbgv 12							//'mapY'
      &setMember
      &push r:1      
      &pushsdb 13							//'_width'
      &pushsdbgv 7							//'mapWidth'
      &setMember
      &push r:1      
      &pushsdb 14							//'_height'
      &pushsdbgv 8							//'mapHeight'
      &setMember
    &end // of function MoveToMapArea

    &function2 SetMapAspectRatio (r:5='newRatioArg') ()
      &push r:5      
      &toNumber
      &setRegister r:4
      &pop
      &push r:4      
      &pushsdbgv 15							//'mapAspectRatio'
      &equals
      &not
      &jnz label1      
      &pushundef
      &return
     label1:
      &push r:4      
      &pushsdbgv 16							//'backAspectRatio'
      &greaterThan
      &not
      &jnz label2      
      &pushsdb 7							//'mapWidth'
      &pushsdbgv 17							//'backWidth'
      &setVariable
      &pushsdb 8							//'mapHeight'
      &pushsdbgv 7							//'mapWidth'
      &push r:4      
      &divide
      &setVariable
      &pushsdb 10							//'mapX'
      &pushsdbgv 18							//'backX'
      &setVariable
      &pushsdb 12							//'mapY'
      &pushsdbgv 19							//'backY'
      &pushsdbgv 20							//'backHeight'
      &pushsdbgv 8							//'mapHeight'
      &subtract
      &pushbyte 2
      &divide
      &add
      &setVariable
      &jmp label3      
     label2:
      &pushsdb 8							//'mapHeight'
      &pushsdbgv 20							//'backHeight'
      &setVariable
      &pushsdb 7							//'mapWidth'
      &pushsdbgv 8							//'mapHeight'
      &push r:4      
      &multiply
      &setVariable
      &pushsdb 12							//'mapY'
      &pushsdbgv 19							//'backY'
      &setVariable
      &pushsdb 10							//'mapX'
      &pushsdbgv 18							//'backX'
      &pushsdbgv 17							//'backWidth'
      &pushsdbgv 7							//'mapWidth'
      &subtract
      &pushbyte 2
      &divide
      &add
      &setVariable
     label3:
      &pushsdb 15							//'mapAspectRatio'
      &push r:4      
      &setVariable
      &pushsdbgv 0							//'panel'
      &pushsdbgm 1							//'viewBoxSurface'
      &pushone
      &dcallfp 21							// MoveToMapArea()
      &pushsdbgv 0							//'panel'
      &pushsdbgm 22							//'shroudSurface'
      &pushone
      &dcallfp 21							// MoveToMapArea()
      &pushsdbgv 0							//'panel'
      &pushsdbgm 23							//'objectsSurface'
      &pushone
      &dcallfp 21							// MoveToMapArea()
      &pushsdbgv 0							//'panel'
      &pushsdbgm 24							//'taintSurface'
      &pushone
      &dcallfp 21							// MoveToMapArea()
      &pushsdbgv 0							//'panel'
      &pushsdbgm 25							//'terrainSurface'
      &pushone
      &dcallfp 21							// MoveToMapArea()
      &pushsdbgv 0							//'panel'
      &pushsdbgm 26							//'inputCatcher'
      &pushone
      &dcallfp 21							// MoveToMapArea()
      &pushsdbgv 0							//'panel'
      &pushsdbgm 3							//'pingSurface'
      &setRegister r:2
      &pop
      &push r:2      
      &pushsdb 9							//'_x'
      &pushsdbgv 10							//'mapX'
      &setMember
      &push r:2      
      &pushsdb 11							//'_y'
      &pushsdbgv 12							//'mapY'
      &setMember
      &push r:2      
      &pushsdbgm 27							//'initialized'
      &not
      &jnz label4      
      &pushsdbgv 8							//'mapHeight'
      &pushsdbgv 7							//'mapWidth'
      &pushbyte 2
      &push r:2      
      &dcallmp 28							// Resize()
      &jmp label5      
     label4:
      &push r:2      
      &pushsdbgm 29							//'sizer'
      &pushsdb 13							//'_width'
      &pushsdbgv 7							//'mapWidth'
      &setMember
      &push r:2      
      &pushsdbgm 29							//'sizer'
      &pushsdb 14							//'_height'
      &pushsdbgv 8							//'mapHeight'
      &setMember
     label5:
      &pushsdbgv 0							//'panel'
      &pushsdbgm 4							//'objectiveStage'
      &setRegister r:1
      &pop
      &push r:1      
      &pushsdb 9							//'_x'
      &pushsdbgv 10							//'mapX'
      &setMember
      &push r:1      
      &pushsdb 11							//'_y'
      &pushsdbgv 12							//'mapY'
      &setMember
      &push r:1      
      &pushsdbgm 27							//'initialized'
      &not
      &jnz label6      
      &pushsdbgv 8							//'mapHeight'
      &pushsdbgv 7							//'mapWidth'
      &pushbyte 2
      &push r:1      
      &dcallmp 28							// Resize()
      &jmp label7      
     label6:
      &push r:1      
      &pushsdbgm 29							//'sizer'
      &pushsdb 13							//'_width'
      &pushsdbgv 7							//'mapWidth'
      &setMember
      &push r:1      
      &pushsdbgm 29							//'sizer'
      &pushsdb 14							//'_height'
      &pushsdbgv 8							//'mapHeight'
      &setMember
     label7:
      &pushsdbgv 0							//'panel'
      &pushsdbgm 6							//'buildQueueStage'
      &setRegister r:3
      &pop
      &push r:3      
      &pushsdb 9							//'_x'
      &pushsdbgv 10							//'mapX'
      &setMember
      &push r:3      
      &pushsdb 11							//'_y'
      &pushsdbgv 12							//'mapY'
      &setMember
      &push r:3      
      &pushsdbgm 27							//'initialized'
      &not
      &jnz label8      
      &pushsdbgv 8							//'mapHeight'
      &pushsdbgv 7							//'mapWidth'
      &pushbyte 2
      &push r:3      
      &dcallmp 28							// Resize()
      &jmp label9      
     label8:
      &push r:3      
      &pushsdbgm 29							//'sizer'
      &pushsdb 13							//'_width'
      &pushsdbgv 7							//'mapWidth'
      &setMember
      &push r:3      
      &pushsdbgm 29							//'sizer'
      &pushsdb 14							//'_height'
      &pushsdbgv 8							//'mapHeight'
      &setMember
     label9:
    &end // of function SetMapAspectRatio

    &function2 SetJammedMessageVisibility (r:1='visArg') ()
      &pushsdbgv 30							//'jammedMessage'
      &pushsdb 31							//'_visible'
      &push r:1      
      &toNumber
      &pushzero
      &equals
      &not
      &setMember
    &end // of function SetJammedMessageVisibility

    &function onUnload (    )    
      &pushsdb 32							//'Open'
      &delete2
      &pop
      &pushsdb 33							//'Close'
      &delete2
      &pop
      &pushsdb 34							//'GetViewBoxSurface'
      &delete2
      &pop
      &pushsdb 35							//'GetStaticSurface'
      &delete2
      &pop
      &pushsdb 36							//'GetPingStage'
      &delete2
      &pop
      &pushsdb 37							//'GetObjectiveStage'
      &delete2
      &pop
      &pushsdb 38							//'GetMovieSurface'
      &delete2
      &pop
      &pushsdb 39							//'GetBuildQueueStage'
      &delete2
      &pop
      &pushsdb 40							//'GetMapWidth'
      &delete2
      &pop
      &pushsdb 41							//'GetMapHeight'
      &delete2
      &pop
      &pushsdb 21							//'MoveToMapArea'
      &delete2
      &pop
      &pushsdb 42							//'SetMapAspectRatio'
      &delete2
      &pop
      &pushsdb 43							//'SetJammedMessageVisibility'
      &delete2
      &pop
      &pushsdb 44							//'onUnload'
      &delete2
      &pop
    &end // of function onUnload

    &pushsdbgv 27							//'initialized'
    &not
    &not
    &jnz label10    
    &pushsdb 18							//'backX'
    &pushsdbgv 0							//'panel'
    &pushsdbgm 45							//'back'
    &pushsdbgm 9							//'_x'
    &setVariable
    &pushsdb 19							//'backY'
    &pushsdbgv 0							//'panel'
    &pushsdbgm 45							//'back'
    &pushsdbgm 11							//'_y'
    &setVariable
    &pushsdb 17							//'backWidth'
    &pushsdbgv 0							//'panel'
    &pushsdbgm 45							//'back'
    &pushsdbgm 13							//'_width'
    &setVariable
    &pushsdb 20							//'backHeight'
    &pushsdbgv 0							//'panel'
    &pushsdbgm 45							//'back'
    &pushsdbgm 14							//'_height'
    &setVariable
    &pushsdb 16							//'backAspectRatio'
    &pushsdbgv 17							//'backWidth'
    &pushsdbgv 20							//'backHeight'
    &divide
    &setVariable
    &pushsdb 10							//'mapX'
    &pushsdbgv 18							//'backX'
    &setVariable
    &pushsdb 12							//'mapY'
    &pushsdbgv 19							//'backY'
    &setVariable
    &pushsdb 7							//'mapWidth'
    &pushsdbgv 17							//'backWidth'
    &setVariable
    &pushsdb 8							//'mapHeight'
    &pushsdbgv 20							//'backHeight'
    &setVariable
    &pushsdb 15							//'mapAspectRatio'
    &pushsdbgv 16							//'backAspectRatio'
    &setVariable
    &pushsdbgv 30							//'jammedMessage'
    &pushsdb 31							//'_visible'
    &pushfalse
    &setMember
    &pushsdb 27							//'initialized'
    &pushtrue
    &setVariable
    &pushsdb 46							//'FSCommand:'
    &pushthisgv
    &toString
    &pushsdb 48							//':OnInitialized'
    &add
    &concat
    &pushsdb 49							//''
    &getURL2
    &pushsdbgv 50							//'extern'
    &pushsdbgm 51							//'InGame'
    &not
    &not
    &jnz label10    
    &pushbyte 2
    &pushone
    &dcallfp 42							// SetMapAspectRatio()
    &pushzero
    &dcallfp 32							// Open()
   label10:
  &end // of frame 0

  &frame 0
    &pushsgv 'panel'
    &pushs '_visible'
    &pushfalse
    &setMember
    &stop
  &end // of frame 0
  
  &importAssets &from 'libHUD.swf'
    'WhiteRectangle' &as 88
  &end // of importAssets

  &defineButton 90
  
    &on     &idleToOverUp    ,&outDownToOverDown    ,&idleToOverDown
      &constants 'FSCommand:', '_parent', ':OnEnter', 'GetMousePosString', 'isMouseOver'  
      &pushsdb 0							//'FSCommand:'
      &pushsdbgv 1							//'_parent'
      &pushsdbgm 1							//'_parent'
      &toString
      &pushsdb 2							//':OnEnter'
      &add
      &concat
      &pushzero
      &pushsdb 3							//'GetMousePosString'
      &callFunction
      &getURL2
      &pushsdb 4							//'isMouseOver'
      &pushtrue
      &setVariable
    &end
  
    &on     &overUpToIdle    ,&overDownToOutDown    ,&overDownToIdle
      &constants 'isMouseOver', 'FSCommand:', '_parent', ':OnLeave', ''  
      &pushsdb 0							//'isMouseOver'
      &pushfalse
      &setVariable
      &pushsdb 1							//'FSCommand:'
      &pushsdbgv 2							//'_parent'
      &pushsdbgm 2							//'_parent'
      &toString
      &pushsdb 3							//':OnLeave'
      &add
      &concat
      &pushsdb 4							//''
      &getURL2
    &end
  &end // of defineButton 90
  
  &importAssets &from 'libHUD.swf'
    'BlackRectangle' &as 91
  &end // of importAssets

  &defineMovieClip 92 // total frames: 1

    &frame 0
      &constants '_parent', '_xmouse', 'mapX', 'mapWidth', '_ymouse', 'mapY', 'mapHeight', 'x=', '&y=', 'isMouseOver', 'isDragging', 'lastXMouse', 'lastYMouse', 'FSCommand:', ':OnMove', 'GetMousePosString', ':OnPress', ':OnRelease', 'onMouseMove', 'onMouseDown', 'onMouseUp', 'onUnload'  
      &function2 GetMousePosString () (r:1='_parent')
        &push r:1        
        &pushsdbgm 0							//'_parent'
        &pushsdbgm 1							//'_xmouse'
        &push r:1        
        &pushsdbgm 0							//'_parent'
        &pushsdbgm 2							//'mapX'
        &subtract
        &push r:1        
        &pushsdbgm 0							//'_parent'
        &pushsdbgm 3							//'mapWidth'
        &divide
        &setRegister r:3
        &pop
        &push r:1        
        &pushsdbgm 0							//'_parent'
        &pushsdbgm 4							//'_ymouse'
        &push r:1        
        &pushsdbgm 0							//'_parent'
        &pushsdbgm 5							//'mapY'
        &subtract
        &push r:1        
        &pushsdbgm 0							//'_parent'
        &pushsdbgm 6							//'mapHeight'
        &divide
        &setRegister r:2
        &pop
        &pushsdb 7							//'x='
        &push r:3        
        &add
        &pushsdb 8							//'&y='
        &add
        &push r:2        
        &add
        &return
      &end // of function GetMousePosString

      &function2 onMouseMove () (r:1='_parent')
        &pushsdbgv 9							//'isMouseOver'
        &dup
        &jnz label1        
        &pop
        &pushsdbgv 10							//'isDragging'
       label1:
        &not
        &jnz label3        
        &push r:1        
        &pushsdbgm 0							//'_parent'
        &pushsdbgm 1							//'_xmouse'
        &setRegister r:3
        &pop
        &push r:1        
        &pushsdbgm 0							//'_parent'
        &pushsdbgm 4							//'_ymouse'
        &setRegister r:2
        &pop
        &push r:3        
        &pushsdbgv 11							//'lastXMouse'
        &equals
        &not
        &dup
        &jnz label2        
        &pop
        &push r:2        
        &pushsdbgv 12							//'lastYMouse'
        &equals
        &not
       label2:
        &not
        &jnz label3        
        &pushsdb 11							//'lastXMouse'
        &push r:3        
        &setVariable
        &pushsdb 12							//'lastYMouse'
        &push r:2        
        &setVariable
        &pushsdb 13							//'FSCommand:'
        &push r:1        
        &pushsdbgm 0							//'_parent'
        &toString
        &pushsdb 14							//':OnMove'
        &add
        &concat
        &pushzero
        &pushsdb 15							//'GetMousePosString'
        &callFunction
        &getURL2
       label3:
      &end // of function onMouseMove

      &function2 onMouseDown () (r:1='_parent')
        &pushsdbgv 9							//'isMouseOver'
        &not
        &jnz label4        
        &pushsdb 13							//'FSCommand:'
        &push r:1        
        &pushsdbgm 0							//'_parent'
        &toString
        &pushsdb 16							//':OnPress'
        &add
        &concat
        &pushzero
        &pushsdb 15							//'GetMousePosString'
        &callFunction
        &getURL2
        &pushsdb 10							//'isDragging'
        &pushtrue
        &setVariable
       label4:
      &end // of function onMouseDown

      &function2 onMouseUp () (r:1='_parent')
        &pushsdbgv 10							//'isDragging'
        &not
        &jnz label5        
        &pushsdb 13							//'FSCommand:'
        &push r:1        
        &pushsdbgm 0							//'_parent'
        &toString
        &pushsdb 17							//':OnRelease'
        &add
        &concat
        &pushzero
        &pushsdb 15							//'GetMousePosString'
        &callFunction
        &getURL2
        &pushsdb 10							//'isDragging'
        &pushfalse
        &setVariable
       label5:
      &end // of function onMouseUp

      &function onUnload (      )      
        &pushsdb 15							//'GetMousePosString'
        &delete2
        &pop
        &pushsdb 18							//'onMouseMove'
        &delete2
        &pop
        &pushsdb 19							//'onMouseDown'
        &delete2
        &pop
        &pushsdb 20							//'onMouseUp'
        &delete2
        &pop
        &pushsdb 21							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

    &end // of frame 0

    &placeMovieClip 91 
    
      &onClipEvent &load
        &pushs ''
        &pushbyte 7
        &pushfalse
        &setProperty
      &end
    &end // of placeMovieClip 91
  &end // of defineMovieClip 92
  
  &importAssets &from 'libHUD.swf'
    'RenderImage' &as 93
  &end // of importAssets

  &defineMovieClip 94 // total frames: 1

    &frame 0
      &constants 'sizer', '_width', '_height', 'indicators', 'length', 'relX', 'relY', '_x', '_y', 'DestroyIndicator', 'BuildQueueIndicator', 'attachMovie', 'imageLabel', 'push', 'splice', 'removeMovieClip', 'Resize', 'AddIndicator', 'RemoveIndicator', 'MoveIndicator', 'onUnload', 'initialized', 'Array', 'FSCommand:', 'this', ':OnInitialized', '', 'extern', 'InGame', 'Def', 'Air'  
      &function2 Resize (r:4='newWidth', r:3='newHeight') ()
        &pushsdbgv 0							//'sizer'
        &pushsdb 1							//'_width'
        &push r:4        
        &setMember
        &pushsdbgv 0							//'sizer'
        &pushsdb 2							//'_height'
        &push r:3        
        &setMember
        &pushzero
        &setRegister r:2
        &pop
       label1:
        &push r:2        
        &pushsdbgv 3							//'indicators'
        &pushsdbgm 4							//'length'
        &lessThan
        &not
        &jnz label5        
        &pushsdbgv 3							//'indicators'
        &push r:2        
        &getMember
        &setRegister r:1
        &pop
        &push r:1        
        &pushundef
        &equals
        &not
        &dup
        &not
        &jnz label2        
        &pop
        &push r:1        
        &pushsdbgm 5							//'relX'
        &pushundef
        &equals
        &not
       label2:
        &dup
        &not
        &jnz label3        
        &pop
        &push r:1        
        &pushsdbgm 6							//'relY'
        &pushundef
        &equals
        &not
       label3:
        &not
        &jnz label4        
        &push r:1        
        &pushsdb 7							//'_x'
        &push r:1        
        &pushsdbgm 5							//'relX'
        &push r:4        
        &multiply
        &setMember
        &push r:1        
        &pushsdb 8							//'_y'
        &push r:1        
        &pushsdbgm 6							//'relY'
        &push r:3        
        &multiply
        &setMember
       label4:
        &push r:2        
        &increment
        &setRegister r:2
        &pop
        &jmp label1        
       label5:
      &end // of function Resize

      &function2 AddIndicator (r:6='idArg', r:5='imageLabelArg') (r:1='this')
        &push r:6        
        &toNumber
        &setRegister r:3
        &pop
        &push r:5        
        &toString
        &setRegister r:4
        &pop
        &push r:1        
        &push r:3        
        &toString
        &getMember
        &setRegister r:2
        &pop
        &push r:2        
        &pushundef
        &equals
        &not
        &not
        &jnz label6        
        &push r:2        
        &pushone
        &dcallfp 9							// DestroyIndicator()
       label6:
        &push r:3        
        &push r:3        
        &toString
        &pushsdb 10							//'BuildQueueIndicator'
        &pushbyte 3
        &pushsdb 11							//'attachMovie'
        &callFunction
        &setRegister r:2
        &pop
        &push r:2        
        &pushsdb 12							//'imageLabel'
        &push r:4        
        &setMember
        &push r:2        
        &pushsdb 5							//'relX'
        &pushzero
        &setMember
        &push r:2        
        &pushsdb 6							//'relY'
        &pushzero
        &setMember
        &push r:2        
        &pushone
        &pushsdbgv 3							//'indicators'
        &dcallmp 13							// push()
      &end // of function AddIndicator

      &function2 RemoveIndicator (r:4='idArg') (r:1='this')
        &push r:4        
        &toNumber
        &setRegister r:3
        &pop
        &push r:1        
        &push r:3        
        &toString
        &getMember
        &setRegister r:2
        &pop
        &push r:2        
        &pushone
        &dcallfp 9							// DestroyIndicator()
      &end // of function RemoveIndicator

      &function2 MoveIndicator (r:7='idArg', r:8='relXArg', r:6='relYArg') (r:1='this')
        &push r:7        
        &toNumber
        &setRegister r:5
        &pop
        &push r:8        
        &toNumber
        &setRegister r:4
        &pop
        &push r:6        
        &toNumber
        &setRegister r:3
        &pop
        &push r:1        
        &push r:5        
        &toString
        &getMember
        &setRegister r:2
        &pop
        &push r:2        
        &pushsdb 5							//'relX'
        &push r:4        
        &setMember
        &push r:2        
        &pushsdb 6							//'relY'
        &push r:3        
        &setMember
        &push r:2        
        &pushsdb 7							//'_x'
        &push r:4        
        &pushsdbgv 0							//'sizer'
        &pushsdbgm 1							//'_width'
        &multiply
        &setMember
        &push r:2        
        &pushsdb 8							//'_y'
        &push r:3        
        &pushsdbgv 0							//'sizer'
        &pushsdbgm 2							//'_height'
        &multiply
        &setMember
      &end // of function MoveIndicator

      &function2 DestroyIndicator (r:2='indicator') ()
        &pushzero
        &setRegister r:1
        &pop
       label7:
        &push r:1        
        &pushsdbgv 3							//'indicators'
        &pushsdbgm 4							//'length'
        &lessThan
        &not
        &jnz label9        
        &pushsdbgv 3							//'indicators'
        &push r:1        
        &getMember
        &push r:2        
        &equals
        &not
        &jnz label8        
        &pushone
        &push r:1        
        &pushbyte 2
        &pushsdbgv 3							//'indicators'
        &dcallmp 14							// splice()
        &jmp label9        
       label8:
        &push r:1        
        &increment
        &setRegister r:1
        &pop
        &jmp label7        
       label9:
        &pushzero
        &push r:2        
        &dcallmp 15							// removeMovieClip()
      &end // of function DestroyIndicator

      &function onUnload (      )      
        &pushsdb 16							//'Resize'
        &delete2
        &pop
        &pushsdb 17							//'AddIndicator'
        &delete2
        &pop
        &pushsdb 18							//'RemoveIndicator'
        &delete2
        &pop
        &pushsdb 19							//'MoveIndicator'
        &delete2
        &pop
        &pushsdb 9							//'DestroyIndicator'
        &delete2
        &pop
        &pushsdb 20							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 21							//'initialized'
      &not
      &not
      &jnz label10      
      &pushsdb 3							//'indicators'
      &pushzero
      &pushsdb 22							//'Array'
      &new
      &setVariable
      &pushsdb 21							//'initialized'
      &pushtrue
      &setVariable
      &pushsdb 23							//'FSCommand:'
      &pushthisgv
      &toString
      &pushsdb 25							//':OnInitialized'
      &add
      &concat
      &pushsdb 26							//''
      &getURL2
      &pushsdbgv 27							//'extern'
      &pushsdbgm 28							//'InGame'
      &not
      &not
      &jnz label10      
      &pushsdb 29							//'Def'
      &pushzero
      &pushbyte 2
      &dcallfp 17							// AddIndicator()
      &pushfloat 0.500000000000000
      &pushfloat 0.250000000000000
      &pushzero
      &pushbyte 3
      &dcallfp 19							// MoveIndicator()
      &pushsdb 30							//'Air'
      &pushone
      &pushbyte 2
      &dcallfp 17							// AddIndicator()
      &pushfloat 0.500000000000000
      &pushfloat 0.750000000000000
      &pushone
      &pushbyte 3
      &dcallfp 19							// MoveIndicator()
     label10:
      &stop
    &end // of frame 0

    &placeMovieClip 88 &as 'sizer'
    
      &onClipEvent &load
        &pushs ''
        &pushbyte 7
        &pushfalse
        &setProperty
      &end
    &end // of placeMovieClip 88
  &end // of defineMovieClip 94

  &defineMovieClip 95 // total frames: 1

    &frame 0
      &constants 'sizer', '_width', '_height', 'indicators', 'length', 'relX', 'relY', '_x', '_y', 'DestroyIndicator', 'ObjectiveIndicator', 'attachMovie', 'isBonus', 'push', 'splice', 'removeMovieClip', 'Resize', 'AddIndicator', 'RemoveIndicator', 'MoveIndicator', 'onUnload', 'initialized', 'Array', 'FSCommand:', 'this', ':OnInitialized', '', 'extern', 'InGame'  
      &function2 Resize (r:4='newWidth', r:3='newHeight') ()
        &pushsdbgv 0							//'sizer'
        &pushsdb 1							//'_width'
        &push r:4        
        &setMember
        &pushsdbgv 0							//'sizer'
        &pushsdb 2							//'_height'
        &push r:3        
        &setMember
        &pushzero
        &setRegister r:2
        &pop
       label1:
        &push r:2        
        &pushsdbgv 3							//'indicators'
        &pushsdbgm 4							//'length'
        &lessThan
        &not
        &jnz label5        
        &pushsdbgv 3							//'indicators'
        &push r:2        
        &getMember
        &setRegister r:1
        &pop
        &push r:1        
        &pushundef
        &equals
        &not
        &dup
        &not
        &jnz label2        
        &pop
        &push r:1        
        &pushsdbgm 5							//'relX'
        &pushundef
        &equals
        &not
       label2:
        &dup
        &not
        &jnz label3        
        &pop
        &push r:1        
        &pushsdbgm 6							//'relY'
        &pushundef
        &equals
        &not
       label3:
        &not
        &jnz label4        
        &push r:1        
        &pushsdb 7							//'_x'
        &push r:1        
        &pushsdbgm 5							//'relX'
        &push r:4        
        &multiply
        &setMember
        &push r:1        
        &pushsdb 8							//'_y'
        &push r:1        
        &pushsdbgm 6							//'relY'
        &push r:3        
        &multiply
        &setMember
       label4:
        &push r:2        
        &increment
        &setRegister r:2
        &pop
        &jmp label1        
       label5:
      &end // of function Resize

      &function2 AddIndicator (r:6='idArg', r:5='bonusArg') (r:1='this')
        &push r:6        
        &toNumber
        &setRegister r:3
        &pop
        &push r:5        
        &toNumber
        &pushzero
        &equals
        &not
        &setRegister r:4
        &pop
        &push r:1        
        &push r:3        
        &toString
        &getMember
        &setRegister r:2
        &pop
        &push r:2        
        &pushundef
        &equals
        &not
        &not
        &jnz label6        
        &push r:2        
        &pushone
        &dcallfp 9							// DestroyIndicator()
       label6:
        &push r:3        
        &push r:3        
        &toString
        &pushsdb 10							//'ObjectiveIndicator'
        &pushbyte 3
        &pushsdb 11							//'attachMovie'
        &callFunction
        &setRegister r:2
        &pop
        &push r:2        
        &pushsdb 12							//'isBonus'
        &push r:4        
        &setMember
        &push r:2        
        &pushsdb 5							//'relX'
        &pushzero
        &setMember
        &push r:2        
        &pushsdb 6							//'relY'
        &pushzero
        &setMember
        &push r:2        
        &pushone
        &pushsdbgv 3							//'indicators'
        &dcallmp 13							// push()
      &end // of function AddIndicator

      &function2 RemoveIndicator (r:4='idArg') (r:1='this')
        &push r:4        
        &toNumber
        &setRegister r:3
        &pop
        &push r:1        
        &push r:3        
        &toString
        &getMember
        &setRegister r:2
        &pop
        &push r:2        
        &pushone
        &dcallfp 9							// DestroyIndicator()
      &end // of function RemoveIndicator

      &function2 MoveIndicator (r:7='idArg', r:8='relXArg', r:6='relYArg') (r:1='this')
        &push r:7        
        &toNumber
        &setRegister r:5
        &pop
        &push r:8        
        &toNumber
        &setRegister r:4
        &pop
        &push r:6        
        &toNumber
        &setRegister r:3
        &pop
        &push r:1        
        &push r:5        
        &toString
        &getMember
        &setRegister r:2
        &pop
        &push r:2        
        &pushsdb 5							//'relX'
        &push r:4        
        &setMember
        &push r:2        
        &pushsdb 6							//'relY'
        &push r:3        
        &setMember
        &push r:2        
        &pushsdb 7							//'_x'
        &push r:4        
        &pushsdbgv 0							//'sizer'
        &pushsdbgm 1							//'_width'
        &multiply
        &setMember
        &push r:2        
        &pushsdb 8							//'_y'
        &push r:3        
        &pushsdbgv 0							//'sizer'
        &pushsdbgm 2							//'_height'
        &multiply
        &setMember
      &end // of function MoveIndicator

      &function2 DestroyIndicator (r:2='indicator') ()
        &pushzero
        &setRegister r:1
        &pop
       label7:
        &push r:1        
        &pushsdbgv 3							//'indicators'
        &pushsdbgm 4							//'length'
        &lessThan
        &not
        &jnz label9        
        &pushsdbgv 3							//'indicators'
        &push r:1        
        &getMember
        &push r:2        
        &equals
        &not
        &jnz label8        
        &pushone
        &push r:1        
        &pushbyte 2
        &pushsdbgv 3							//'indicators'
        &dcallmp 14							// splice()
        &jmp label9        
       label8:
        &push r:1        
        &increment
        &setRegister r:1
        &pop
        &jmp label7        
       label9:
        &pushzero
        &push r:2        
        &dcallmp 15							// removeMovieClip()
      &end // of function DestroyIndicator

      &function onUnload (      )      
        &pushsdb 16							//'Resize'
        &delete2
        &pop
        &pushsdb 17							//'AddIndicator'
        &delete2
        &pop
        &pushsdb 18							//'RemoveIndicator'
        &delete2
        &pop
        &pushsdb 19							//'MoveIndicator'
        &delete2
        &pop
        &pushsdb 9							//'DestroyIndicator'
        &delete2
        &pop
        &pushsdb 20							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 21							//'initialized'
      &not
      &not
      &jnz label10      
      &pushsdb 3							//'indicators'
      &pushzero
      &pushsdb 22							//'Array'
      &new
      &setVariable
      &pushsdb 21							//'initialized'
      &pushtrue
      &setVariable
      &pushsdb 23							//'FSCommand:'
      &pushthisgv
      &toString
      &pushsdb 25							//':OnInitialized'
      &add
      &concat
      &pushsdb 26							//''
      &getURL2
      &pushsdbgv 27							//'extern'
      &pushsdbgm 28							//'InGame'
      &not
      &not
      &jnz label10      
      &pushzero
      &pushzero
      &pushbyte 2
      &dcallfp 17							// AddIndicator()
      &pushfloat 0.750000000000000
      &pushfloat 0.250000000000000
      &pushzero
      &pushbyte 3
      &dcallfp 19							// MoveIndicator()
      &pushone
      &pushone
      &pushbyte 2
      &dcallfp 17							// AddIndicator()
      &pushfloat 0.750000000000000
      &pushfloat 0.750000000000000
      &pushone
      &pushbyte 3
      &dcallfp 19							// MoveIndicator()
     label10:
      &stop
    &end // of frame 0

    &placeMovieClip 88 &as 'sizer'
    
      &onClipEvent &load
        &pushs ''
        &pushbyte 7
        &pushfalse
        &setProperty
      &end
    &end // of placeMovieClip 88
  &end // of defineMovieClip 95

  &defineMovieClip 96 // total frames: 1

    &frame 0
      &constants 'DestroyPing', 'attachMovie', 'relX', 'relY', 'pings', 'push', 'done', '_x', 'sizer', '_width', '_y', '_height', 'length', 'splice', 'removeMovieClip', 'Resize', 'CreatePing', 'DetachPing', 'MovePing', 'onUnload', 'newHeight', 'newWidth', 'i', 'ping', 'initialized', 'Array', 'FSCommand:', 'this', ':OnInitialized', '', 'extern', 'InGame', 'PingAttack', 'PingBeacon', 'PingUpgrade'  
      &function2 CreatePing (r:4='type', r:3='id') (r:1='this')
        &push r:1        
        &push r:3        
        &toString
        &getMember
        &setRegister r:2
        &pop
        &push r:2        
        &pushundef
        &equals
        &not
        &not
        &jnz label1        
        &push r:2        
        &pushone
        &dcallfp 0							// DestroyPing()
       label1:
        &push r:3        
        &toNumber
        &push r:3        
        &toString
        &push r:4        
        &pushbyte 3
        &pushsdb 1							//'attachMovie'
        &callFunction
        &setRegister r:2
        &pop
        &push r:2        
        &pushundef
        &equals
        &not
        &not
        &jnz label2        
        &push r:2        
        &pushsdb 2							//'relX'
        &pushzero
        &setMember
        &push r:2        
        &pushsdb 3							//'relY'
        &pushzero
        &setMember
        &push r:2        
        &pushone
        &pushsdbgv 4							//'pings'
        &dcallmp 5							// push()
       label2:
      &end // of function CreatePing

      &function2 DetachPing (r:3='id') (r:1='this')
        &push r:1        
        &push r:3        
        &toString
        &getMember
        &setRegister r:2
        &pop
        &push r:2        
        &pushundef
        &equals
        &not
        &not
        &jnz label3        
        &push r:2        
        &pushsdb 6							//'done'
        &pushtrue
        &setMember
       label3:
      &end // of function DetachPing

      &function2 MovePing (r:3='id', r:5='relX', r:4='relY') (r:1='this')
        &push r:1        
        &push r:3        
        &toString
        &getMember
        &setRegister r:2
        &pop
        &push r:2        
        &pushundef
        &equals
        &not
        &not
        &jnz label4        
        &push r:2        
        &pushsdb 2							//'relX'
        &push r:5        
        &toNumber
        &setMember
        &push r:2        
        &pushsdb 3							//'relY'
        &push r:4        
        &toNumber
        &setMember
        &push r:2        
        &pushsdb 7							//'_x'
        &push r:2        
        &pushsdbgm 2							//'relX'
        &pushsdbgv 8							//'sizer'
        &pushsdbgm 9							//'_width'
        &multiply
        &setMember
        &push r:2        
        &pushsdb 10							//'_y'
        &push r:2        
        &pushsdbgm 3							//'relY'
        &pushsdbgv 8							//'sizer'
        &pushsdbgm 11							//'_height'
        &multiply
        &setMember
       label4:
      &end // of function MovePing

      &function2 DestroyPing (r:2='ping') ()
        &pushzero
        &setRegister r:1
        &pop
       label5:
        &push r:1        
        &pushsdbgv 4							//'pings'
        &pushsdbgm 12							//'length'
        &lessThan
        &not
        &jnz label7        
        &pushsdbgv 4							//'pings'
        &push r:1        
        &getMember
        &push r:2        
        &equals
        &not
        &jnz label6        
        &pushone
        &push r:1        
        &pushbyte 2
        &pushsdbgv 4							//'pings'
        &dcallmp 13							// splice()
        &jmp label7        
       label6:
        &push r:1        
        &increment
        &setRegister r:1
        &pop
        &jmp label5        
       label7:
        &pushzero
        &push r:2        
        &dcallmp 14							// removeMovieClip()
      &end // of function DestroyPing

      &function onUnload (      )      
        &pushsdb 15							//'Resize'
        &delete2
        &pop
        &pushsdb 16							//'CreatePing'
        &delete2
        &pop
        &pushsdb 17							//'DetachPing'
        &delete2
        &pop
        &pushsdb 18							//'MovePing'
        &delete2
        &pop
        &pushsdb 0							//'DestroyPing'
        &delete2
        &pop
        &pushsdb 19							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 20							//'newHeight'
      &pushsdbgv 21							//'newWidth'
      &pushbyte 2
      &dcallfp 15							// Resize()
      &pushundef
      &pop
      &pushsdbgv 8							//'sizer'
      &pushsdb 9							//'_width'
      &pushsdbgv 21							//'newWidth'
      &setMember
      &pushsdbgv 8							//'sizer'
      &pushsdb 11							//'_height'
      &pushsdbgv 20							//'newHeight'
      &setMember
      &pushsdb 22							//'i'
      &var
      &pushsdb 22							//'i'
      &pushzerosv
     label8:
      &pushsdbgv 22							//'i'
      &pushsdbgv 4							//'pings'
      &pushsdbgm 12							//'length'
      &lessThan
      &not
      &jnz label12      
      &pushsdb 23							//'ping'
      &pushsdbgv 4							//'pings'
      &pushsdbgv 22							//'i'
      &getMember
      &varEquals
      &pushsdbgv 23							//'ping'
      &pushundef
      &equals
      &not
      &dup
      &not
      &jnz label9      
      &pop
      &pushsdbgv 23							//'ping'
      &pushsdbgm 2							//'relX'
      &pushundef
      &equals
      &not
     label9:
      &dup
      &not
      &jnz label10      
      &pop
      &pushsdbgv 23							//'ping'
      &pushsdbgm 3							//'relY'
      &pushundef
      &equals
      &not
     label10:
      &not
      &jnz label11      
      &pushsdbgv 23							//'ping'
      &pushsdb 7							//'_x'
      &pushsdbgv 23							//'ping'
      &pushsdbgm 2							//'relX'
      &pushsdbgv 21							//'newWidth'
      &multiply
      &setMember
      &pushsdbgv 23							//'ping'
      &pushsdb 10							//'_y'
      &pushsdbgv 23							//'ping'
      &pushsdbgm 3							//'relY'
      &pushsdbgv 20							//'newHeight'
      &multiply
      &setMember
     label11:
      &pushsdb 22							//'i'
      &pushsdbgv 22							//'i'
      &increment
      &setVariable
      &jmp label8      
     label12:
      &pushsdbgv 24							//'initialized'
      &not
      &not
      &jnz label13      
      &pushsdb 4							//'pings'
      &pushzero
      &pushsdb 25							//'Array'
      &new
      &setVariable
      &pushsdb 24							//'initialized'
      &pushtrue
      &setVariable
      &pushsdb 26							//'FSCommand:'
      &pushthisgv
      &toString
      &pushsdb 28							//':OnInitialized'
      &add
      &concat
      &pushsdb 29							//''
      &getURL2
      &pushsdbgv 30							//'extern'
      &pushsdbgm 31							//'InGame'
      &not
      &not
      &jnz label13      
      &pushzero
      &pushsdb 32							//'PingAttack'
      &pushbyte 2
      &dcallfp 16							// CreatePing()
      &pushfloat 0.500000000000000
      &pushfloat 0.500000000000000
      &pushzero
      &pushbyte 3
      &dcallfp 18							// MovePing()
      &pushone
      &pushsdb 33							//'PingBeacon'
      &pushbyte 2
      &dcallfp 16							// CreatePing()
      &pushfloat 0.250000000000000
      &pushfloat 0.250000000000000
      &pushone
      &pushbyte 3
      &dcallfp 18							// MovePing()
      &pushbyte 2
      &pushsdb 34							//'PingUpgrade'
      &pushbyte 2
      &dcallfp 16							// CreatePing()
      &pushfloat 0.250000000000000
      &pushfloat 0.750000000000000
      &pushbyte 2
      &pushbyte 3
      &dcallfp 18							// MovePing()
     label13:
      &stop
    &end // of frame 0

    &placeMovieClip 88 &as 'sizer'
    
      &onClipEvent &load
        &pushs ''
        &pushbyte 7
        &pushfalse
        &setProperty
      &end
    &end // of placeMovieClip 88
  &end // of defineMovieClip 96
  
  &importAssets &from 'libHUD.swf'
    'SimpleRenderingSurface' &as 97
  &end // of importAssets

  &defineMovieClip 98 // total frames: 1

    &placeMovieClip 93 &as 'terrainSurface'
    
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
        &constants '_imageMap', '_parent', ':Terrain'  
        &pushsdb 0							//'_imageMap'
        &pushsdbgv 1							//'_parent'
        &pushsdbgm 1							//'_parent'
        &toString
        &pushsdb 2							//':Terrain'
        &add
        &setVariable
      &end
    &end // of placeMovieClip 93

    &placeMovieClip 93 &as 'taintSurface'
    
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
        &constants '_imageMap', '_parent', ':Taint'  
        &pushsdb 0							//'_imageMap'
        &pushsdbgv 1							//'_parent'
        &pushsdbgm 1							//'_parent'
        &toString
        &pushsdb 2							//':Taint'
        &add
        &setVariable
      &end
    &end // of placeMovieClip 93

    &placeMovieClip 93 &as 'objectsSurface'
    
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
        &constants '_imageMap', '_parent', ':Objects'  
        &pushsdb 0							//'_imageMap'
        &pushsdbgv 1							//'_parent'
        &pushsdbgm 1							//'_parent'
        &toString
        &pushsdb 2							//':Objects'
        &add
        &setVariable
      &end
    &end // of placeMovieClip 93

    &placeMovieClip 93 &as 'shroudSurface'
    
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
        &constants '_imageMap', '_parent', ':Shroud'  
        &pushsdb 0							//'_imageMap'
        &pushsdbgv 1							//'_parent'
        &pushsdbgm 1							//'_parent'
        &toString
        &pushsdb 2							//':Shroud'
        &add
        &setVariable
      &end
    &end // of placeMovieClip 93
  &end // of defineMovieClip 98

  &defineMovieClip 100 // total frames: 1

    &placeMovieClip 88 
    
      &onClipEvent &load
        &pushs ''
        &pushbyte 7
        &pushfalse
        &setProperty
      &end
    &end // of placeMovieClip 88
  &end // of defineMovieClip 100

  &defineMovieClip 107 // total frames: 30

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
  &end // of defineMovieClip 107

  &defineMovieClip 110 // total frames: 1
  &end // of defineMovieClip 110

  &defineMovieClip 111 // total frames: 4
  &end // of defineMovieClip 111

  &defineMovieClip 114 // total frames: 1
  &end // of defineMovieClip 114

  &placeMovieClip 114 &as 'jammedMessage'
  
    &onClipEvent &load
      &pushs 'text'
      &pushs '$'
      &pushsgv '_parent'
      &toString
      &add
      &pushs ':JammedMessage&dropshadow'
      &add
      &setVariable
    &end
  &end // of placeMovieClip 114

  &frame 1
    &pushsgv 'panel'
    &pushs '_visible'
    &pushtrue
    &setMember
    &play
  &end // of frame 1

  &defineMovieClip 115 // total frames: 16

    &frame 15
      &stop
    &end // of frame 15
  &end // of defineMovieClip 115

  &defineMovieClip 116 // total frames: 16

    &frame 15
      &stop
    &end // of frame 15
  &end // of defineMovieClip 116

  &defineMovieClip 117 // total frames: 1
  &end // of defineMovieClip 117

  &defineMovieClip 120 // total frames: 1
  &end // of defineMovieClip 120

  &defineMovieClip 123 // total frames: 1
  &end // of defineMovieClip 123

  &defineMovieClip 124 // total frames: 32

    &frame 17
      &stop
    &end // of frame 17
  &end // of defineMovieClip 124

  &frame 10
    &pushsgv 'inputShield'
    &pushs '_visible'
    &pushfalse
    &setMember
    &pushs 'FSCommand:'
    &pushthisgv
    &toString
    &pushs ':OnOpened'
    &add
    &concat
    &pushs ''
    &getURL2
    &stop
  &end // of frame 10

  &frame 11
    &pushsgv 'inputShield'
    &pushs '_visible'
    &pushtrue
    &setMember
    &play
  &end // of frame 11

  &defineMovieClip 125 // total frames: 16

    &frame 15
      &stop
    &end // of frame 15
  &end // of defineMovieClip 125

  &defineMovieClip 126 // total frames: 16

    &frame 15
      &stop
    &end // of frame 15
  &end // of defineMovieClip 126

  &defineMovieClip 127 // total frames: 1
  &end // of defineMovieClip 127

  &defineMovieClip 128 // total frames: 26

    &frame 21
      &stop
    &end // of frame 21
  &end // of defineMovieClip 128

  &frame 20
    &pushs 'FSCommand:'
    &pushthisgv
    &toString
    &pushs ':OnClosed'
    &add
    &concat
    &pushs ''
    &getURL2
    &gotoLabel '_closed'
    &play
  &end // of frame 20
&end
