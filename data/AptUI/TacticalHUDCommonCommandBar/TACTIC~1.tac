movie 'E:\Projects\CNC3\Data\APTBUI~1\034A3~1.0-D\pc\Output\TA1EC5~1\\TACTIC~1.eaf' &compressed // flash 7, total frames: 1, frame rate: 30 fps, 1024x768 px

  &defineMovieClip 3 // total frames: 1
  &end // of defineMovieClip 3

  &defineMovieClip 4 // total frames: 40

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29

    &frame 39
      &stop
    &end // of frame 39
  &end // of defineMovieClip 4
  
  &exportAssets
    4 &as 'ReverseMoveHighlighted'
  &end // of exportAssets

  &defineMovieClip 7 // total frames: 1
  &end // of defineMovieClip 7

  &defineMovieClip 8 // total frames: 40

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29

    &frame 39
      &stop
    &end // of frame 39
  &end // of defineMovieClip 8
  
  &exportAssets
    8 &as 'PlanningModeHighlighted'
  &end // of exportAssets

  &defineMovieClip 11 // total frames: 1
  &end // of defineMovieClip 11

  &defineMovieClip 12 // total frames: 40

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29

    &frame 39
      &stop
    &end // of frame 39
  &end // of defineMovieClip 12
  
  &exportAssets
    12 &as 'WaypointModeHighlighted'
  &end // of exportAssets

  &defineMovieClip 13 // total frames: 40

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29

    &frame 39
      &stop
    &end // of frame 39
  &end // of defineMovieClip 13
  
  &exportAssets
    13 &as 'ReverseMoveNormal'
  &end // of exportAssets

  &defineMovieClip 14 // total frames: 40

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29

    &frame 39
      &stop
    &end // of frame 39
  &end // of defineMovieClip 14
  
  &exportAssets
    14 &as 'PlanningModeNormal'
  &end // of exportAssets

  &defineMovieClip 15 // total frames: 40

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29

    &frame 39
      &stop
    &end // of frame 39
  &end // of defineMovieClip 15
  
  &exportAssets
    15 &as 'WaypointModeNormal'
  &end // of exportAssets

  &defineMovieClip 22 // total frames: 30

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
  &end // of defineMovieClip 22

  &defineMovieClip 23 // total frames: 40

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29

    &frame 39
      &stop
    &end // of frame 39
  &end // of defineMovieClip 23
  
  &exportAssets
    23 &as 'HoldFireStanceHighlighted'
  &end // of exportAssets

  &defineMovieClip 26 // total frames: 1
  &end // of defineMovieClip 26

  &defineMovieClip 27 // total frames: 40

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29

    &frame 39
      &stop
    &end // of frame 39
  &end // of defineMovieClip 27
  
  &exportAssets
    27 &as 'HoldFireStanceNormal'
  &end // of exportAssets

  &defineMovieClip 34 // total frames: 30

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
  &end // of defineMovieClip 34

  &defineMovieClip 35 // total frames: 40

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29

    &frame 39
      &stop
    &end // of frame 39
  &end // of defineMovieClip 35
  
  &exportAssets
    35 &as 'HoldGroundStanceHighlighted'
  &end // of exportAssets

  &defineMovieClip 38 // total frames: 1
  &end // of defineMovieClip 38

  &defineMovieClip 39 // total frames: 40

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29

    &frame 39
      &stop
    &end // of frame 39
  &end // of defineMovieClip 39
  
  &exportAssets
    39 &as 'HoldGroundStanceNormal'
  &end // of exportAssets

  &defineMovieClip 46 // total frames: 30

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
  &end // of defineMovieClip 46

  &defineMovieClip 47 // total frames: 40

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29

    &frame 39
      &stop
    &end // of frame 39
  &end // of defineMovieClip 47
  
  &exportAssets
    47 &as 'GuardStanceHighlighted'
  &end // of exportAssets

  &defineMovieClip 50 // total frames: 1
  &end // of defineMovieClip 50

  &defineMovieClip 51 // total frames: 40

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29

    &frame 39
      &stop
    &end // of frame 39
  &end // of defineMovieClip 51
  
  &exportAssets
    51 &as 'GuardStanceNormal'
  &end // of exportAssets

  &defineMovieClip 58 // total frames: 30

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
  &end // of defineMovieClip 58

  &defineMovieClip 59 // total frames: 40

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29

    &frame 39
      &stop
    &end // of frame 39
  &end // of defineMovieClip 59
  
  &exportAssets
    59 &as 'AggressiveStanceHighlighted'
  &end // of exportAssets

  &defineMovieClip 62 // total frames: 1
  &end // of defineMovieClip 62

  &defineMovieClip 63 // total frames: 40

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29

    &frame 39
      &stop
    &end // of frame 39
  &end // of defineMovieClip 63
  
  &exportAssets
    63 &as 'AggressiveStanceNormal'
  &end // of exportAssets

  &defineMovieClip 66 // total frames: 1
  &end // of defineMovieClip 66

  &defineMovieClip 67 // total frames: 40

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29

    &frame 39
      &stop
    &end // of frame 39
  &end // of defineMovieClip 67
  
  &exportAssets
    67 &as 'ForceFireHighlighted'
  &end // of exportAssets

  &defineMovieClip 68 // total frames: 40

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29

    &frame 39
      &stop
    &end // of frame 39
  &end // of defineMovieClip 68
  
  &exportAssets
    68 &as 'ForceFireNormal'
  &end // of exportAssets

  &defineMovieClip 71 // total frames: 1
  &end // of defineMovieClip 71

  &defineMovieClip 72 // total frames: 40

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29

    &frame 39
      &stop
    &end // of frame 39
  &end // of defineMovieClip 72
  
  &exportAssets
    72 &as 'StopHighlighted'
  &end // of exportAssets

  &defineMovieClip 73 // total frames: 40

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29

    &frame 39
      &stop
    &end // of frame 39
  &end // of defineMovieClip 73
  
  &exportAssets
    73 &as 'StopNormal'
  &end // of exportAssets

  &defineMovieClip 76 // total frames: 1
  &end // of defineMovieClip 76

  &defineMovieClip 77 // total frames: 40

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29

    &frame 39
      &stop
    &end // of frame 39
  &end // of defineMovieClip 77
  
  &exportAssets
    77 &as 'ForceMoveHighlighted'
  &end // of exportAssets

  &defineMovieClip 80 // total frames: 1
  &end // of defineMovieClip 80

  &defineMovieClip 81 // total frames: 40

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29

    &frame 39
      &stop
    &end // of frame 39
  &end // of defineMovieClip 81
  
  &exportAssets
    81 &as 'AttackMoveHighlighted'
  &end // of exportAssets

  &defineMovieClip 82 // total frames: 40

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29

    &frame 39
      &stop
    &end // of frame 39
  &end // of defineMovieClip 82
  
  &exportAssets
    82 &as 'ForceMoveNormal'
  &end // of exportAssets

  &defineMovieClip 83 // total frames: 40

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29

    &frame 39
      &stop
    &end // of frame 39
  &end // of defineMovieClip 83
  
  &exportAssets
    83 &as 'AttackMoveNormal'
  &end // of exportAssets

  &defineMovieClip 90 // total frames: 30

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
  &end // of defineMovieClip 90

  &defineMovieClip 91 // total frames: 40

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29

    &frame 39
      &stop
    &end // of frame 39
  &end // of defineMovieClip 91
  
  &exportAssets
    91 &as 'CommandButtonBackgroundNormal'
  &end // of exportAssets

  &defineMovieClip 92 // total frames: 40

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29

    &frame 39
      &stop
    &end // of frame 39
  &end // of defineMovieClip 92
  
  &exportAssets
    92 &as 'StanceButtonBackgroundNormal'
  &end // of exportAssets

  &defineMovieClip 99 // total frames: 30

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
  &end // of defineMovieClip 99

  &defineMovieClip 100 // total frames: 40

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29

    &frame 39
      &stop
    &end // of frame 39
  &end // of defineMovieClip 100
  
  &exportAssets
    100 &as 'StanceButtonBackgroundHighlighted'
  &end // of exportAssets

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

  &defineMovieClip 108 // total frames: 40

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29

    &frame 39
      &stop
    &end // of frame 39
  &end // of defineMovieClip 108
  
  &exportAssets
    108 &as 'CommandButtonBackgroundHighlighted'
  &end // of exportAssets

  &frame 0
    &constants 'inGame', 'FSCommand:', ':OnClicked', '', 'isEnabled', 'isSelected', '1', '0', 'SetSelected', 'OnCommandButtonClicked', 'GetButton', 'onUnload', 'initialized', 'extern', 'InGame', 'buttonNames', 'holdFireStance', 'holdGroundStance', 'guardStance', 'aggressiveStance', 'planningMode', 'waypointMode', 'reverseMove', 'forceMove', 'attackMove', 'forceAttack', 'i', 'length', 'buttonName', 'buttonClip', 'this', 'Button', 'helpSiteClip', 'HelpSite', 'm_glowIdx', 'helpSite', ':OnInitialized'  
    &function2 OnCommandButtonClicked (r:1='buttonClip') ()
      &pushsdbgv 0							//'inGame'
      &not
      &jnz label1      
      &pushsdb 1							//'FSCommand:'
      &push r:1      
      &toString
      &pushsdb 2							//':OnClicked'
      &add
      &concat
      &pushsdb 3							//''
      &getURL2
      &jmp label4      
     label1:
      &push r:1      
      &pushsdbgm 4							//'isEnabled'
      &not
      &jnz label4      
      &push r:1      
      &pushsdbgm 5							//'isSelected'
      &jnz label2      
      &pushsdb 6							//'1'
      &jmp label3      
     label2:
      &pushsdb 7							//'0'
     label3:
      &pushone
      &push r:1      
      &dcallmp 8							// SetSelected()
     label4:
    &end // of function OnCommandButtonClicked

    &function2 GetButton (r:2='buttonNameArg') (r:1='this')
      &push r:1      
      &push r:2      
      &toString
      &getMember
      &toString
      &return
    &end // of function GetButton

    &function onUnload (    )    
      &pushsdb 9							//'OnCommandButtonClicked'
      &delete2
      &pop
      &pushsdb 10							//'GetButton'
      &delete2
      &pop
      &pushsdb 11							//'onUnload'
      &delete2
      &pop
    &end // of function onUnload

    &pushsdbgv 12							//'initialized'
    &not
    &not
    &jnz label7    
    &pushsdb 0							//'inGame'
    &pushsdbgv 13							//'extern'
    &pushsdbgm 14							//'InGame'
    &setVariable
    &pushsdb 15							//'buttonNames'
    &pushsdb 16							//'holdFireStance'
    &pushsdb 17							//'holdGroundStance'
    &pushsdb 18							//'guardStance'
    &pushsdb 19							//'aggressiveStance'
    &pushsdb 20							//'planningMode'
    &pushsdb 21							//'waypointMode'
    &pushsdb 22							//'reverseMove'
    &pushsdb 23							//'forceMove'
    &pushsdb 24							//'attackMove'
    &pushsdb 25							//'forceAttack'
    &pushbyte 10
    &initArray
    &varEquals
    &pushsdb 26							//'i'
    &pushzero
    &varEquals
   label5:
    &pushsdbgv 26							//'i'
    &pushsdbgv 15							//'buttonNames'
    &pushsdbgm 27							//'length'
    &lessThan
    &not
    &jnz label6    
    &pushsdb 28							//'buttonName'
    &pushsdbgv 15							//'buttonNames'
    &pushsdbgv 26							//'i'
    &getMember
    &varEquals
    &pushsdb 29							//'buttonClip'
    &pushthisgv
    &pushsdbgv 28							//'buttonName'
    &pushsdb 31							//'Button'
    &add
    &getMember
    &varEquals
    &pushsdb 32							//'helpSiteClip'
    &pushthisgv
    &pushsdbgv 28							//'buttonName'
    &pushsdb 33							//'HelpSite'
    &add
    &getMember
    &varEquals
    &pushsdbgv 29							//'buttonClip'
    &pushsdb 34							//'m_glowIdx'
    &pushsdbgv 26							//'i'
    &setMember
    &pushsdbgv 29							//'buttonClip'
    &pushsdb 35							//'helpSite'
    &pushsdbgv 32							//'helpSiteClip'
    &setMember
    &pushsdb 26							//'i'
    &pushsdbgv 26							//'i'
    &increment
    &setVariable
    &jmp label5    
   label6:
    &pushsdb 12							//'initialized'
    &pushtrue
    &setVariable
    &pushsdb 1							//'FSCommand:'
    &pushthisgv
    &toString
    &pushsdb 36							//':OnInitialized'
    &add
    &concat
    &pushsdb 3							//''
    &getURL2
   label7:
  &end // of frame 0

  &defineMovieClip 115 // total frames: 30

    &frame 1
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
    &end // of frame 1

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 115

  &defineMovieClip 118 // total frames: 1
  &end // of defineMovieClip 118

  &defineMovieClip 123 // total frames: 30

    &placeMovieClip 118 
    
      &onClipEvent &load
        &pushs ''
        &pushbyte 7
        &pushfalse
        &setProperty
      &end
    &end // of placeMovieClip 118

    &frame 1
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
    &end // of frame 1

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 123

  &defineButton 125
  
    &on     &overUpToOverDown
      &pushsgv 'isEnabled'
      &not
      &jnz label1      
      &pushs '_down'
      &pushone
      &pushs 'SetState'
      &callfp
     label1:
    &end
  
    &on     &overDownToOverUp
      &pushsgv 'isEnabled'
      &not
      &jnz label1      
      &pushs '_over'
      &pushone
      &pushs 'SetState'
      &callfp
      &pushzero
      &pushs 'TriggerGlow'
      &callfp
     label1:
      &pushthisgv
      &pushone
      &pushsgv 'client'
      &pushs 'OnCommandButtonClicked'
      &callmp
    &end
  
    &on     &idleToOverUp
      &pushsgv 'isEnabled'
      &not
      &jnz label1      
      &pushs '_over'
      &pushone
      &pushs 'SetState'
      &callfp
     label1:
      &pushs 'FSCommand:'
      &pushthisgv
      &toString
      &pushs ':OnRollOver'
      &add
      &concat
      &pushs ''
      &getURL2
    &end
  
    &on     &overUpToIdle
      &pushsgv 'isEnabled'
      &not
      &jnz label1      
      &pushs '_up'
      &pushone
      &pushs 'SetState'
      &callfp
     label1:
      &pushs 'FSCommand:'
      &pushthisgv
      &toString
      &pushs ':OnRollOut'
      &add
      &concat
      &pushs ''
      &getURL2
    &end
  &end // of defineButton 125

  &defineMovieClip 127 // total frames: 1
  &end // of defineMovieClip 127

  &defineMovieClip 128 // total frames: 1
  &end // of defineMovieClip 128

  &defineMovieClip 129 // total frames: 1

    &frame 0
      &constants 'imageStage', 'clip', 'gotoAndPlay', 'backgroundStage', 'currentStateLabel', 'isEnabled', '_disabled', '_up', 'SetState', 'stageClip >> ', ' : prefix >> ', 'removeMovieClip', 'isSelected', 'Normal', 'Highlighted', 'attachMovie', 'imageClip', 'ReattachContent', 'backgroundClip', '', 'helpSite', 'SetEnabled', 'SetSelected', 'SetVisibility', 'GetHelpSite', 'TriggerGlow', 'onUnload', 'm_glowIdx', 'GlowEffect', 'PlayEffect', 'initialized', 'client', '_parent', '1', 'FSCommand:', 'this', ':OnInitialized', 'extern', 'InGame'  
      &function2 SetState (r:1='stateLabel') ()
        &push r:1        
        &pushone
        &pushsdbgv 0							//'imageStage'
        &pushsdbgm 1							//'clip'
        &dcallmp 2							// gotoAndPlay()
        &push r:1        
        &pushone
        &pushsdbgv 3							//'backgroundStage'
        &pushsdbgm 1							//'clip'
        &dcallmp 2							// gotoAndPlay()
        &pushsdb 4							//'currentStateLabel'
        &push r:1        
        &setVariable
      &end // of function SetState

      &function2 SetEnabled (r:2='enableArg') ()
        &push r:2        
        &toNumber
        &pushzero
        &equals
        &not
        &setRegister r:1
        &pop
        &push r:1        
        &pushsdbgv 5							//'isEnabled'
        &equals
        &not
        &not
        &jnz label3        
        &pushsdb 5							//'isEnabled'
        &push r:1        
        &setVariable
        &push r:1        
        &jnz label1        
        &pushsdb 6							//'_disabled'
        &jmp label2        
       label1:
        &pushsdb 7							//'_up'
       label2:
        &pushone
        &dcallfp 8							// SetState()
       label3:
      &end // of function SetEnabled

      &function2 ReattachContent (r:3='stageClip', r:4='prefix') ()
        &pushsdb 9							//'stageClip >> '
        &push r:3        
        &add
        &pushsdb 10							//' : prefix >> '
        &add
        &push r:4        
        &add
        &trace
        &push r:3        
        &pushsdbgm 1							//'clip'
        &setRegister r:1
        &pop
        &push r:1        
        &pushundef
        &equals
        &not
        &not
        &jnz label4        
        &pushzero
        &push r:1        
        &dcallmp 11							// removeMovieClip()
       label4:
        &push r:4        
        &pushsdbgv 12							//'isSelected'
        &jnz label5        
        &pushsdb 13							//'Normal'
        &jmp label6        
       label5:
        &pushsdb 14							//'Highlighted'
       label6:
        &add
        &setRegister r:2
        &pop
        &pushzero
        &pushsdb 1							//'clip'
        &push r:2        
        &pushbyte 3
        &push r:3        
        &pushsdb 15							//'attachMovie'
        &callMethod
        &setRegister r:1
        &pop
        &pushsdbgv 4							//'currentStateLabel'
        &pushone
        &push r:1        
        &dcallmp 2							// gotoAndPlay()
      &end // of function ReattachContent

      &function2 SetSelected (r:2='selectedArg') ()
        &push r:2        
        &toNumber
        &pushzero
        &equals
        &not
        &setRegister r:1
        &pop
        &push r:1        
        &pushsdbgv 12							//'isSelected'
        &equals
        &not
        &not
        &jnz label7        
        &pushsdb 12							//'isSelected'
        &push r:1        
        &setVariable
        &pushsdbgv 16							//'imageClip'
        &pushsdbgv 0							//'imageStage'
        &pushbyte 2
        &dcallfp 17							// ReattachContent()
        &pushsdbgv 18							//'backgroundClip'
        &pushsdbgv 3							//'backgroundStage'
        &pushbyte 2
        &dcallfp 17							// ReattachContent()
       label7:
      &end // of function SetSelected

      &function2 SetVisibility (r:2='visArg') ()
        &push r:2        
        &toNumber
        &pushzero
        &equals
        &not
        &setRegister r:1
        &pop
        &pushsdb 19							//''
        &pushbyte 7
        &push r:1        
        &setProperty
      &end // of function SetVisibility

      &function GetHelpSite (      )      
        &pushsdbgv 20							//'helpSite'
        &toString
        &return
      &end // of function GetHelpSite

      &function onUnload (      )      
        &pushsdb 8							//'SetState'
        &delete2
        &pop
        &pushsdb 21							//'SetEnabled'
        &delete2
        &pop
        &pushsdb 17							//'ReattachContent'
        &delete2
        &pop
        &pushsdb 22							//'SetSelected'
        &delete2
        &pop
        &pushsdb 23							//'SetVisibility'
        &delete2
        &pop
        &pushsdb 24							//'GetHelpSite'
        &delete2
        &pop
        &pushsdb 25							//'TriggerGlow'
        &delete2
        &pop
        &pushsdb 26							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &function2 TriggerGlow () (r:1='_parent')
        &pushsdbgv 27							//'m_glowIdx'
        &pushone
        &push r:1        
        &pushsdbgm 28							//'GlowEffect'
        &dcallmp 29							// PlayEffect()
      &end // of function TriggerGlow

      &pushsdbgv 30							//'initialized'
      &not
      &not
      &jnz label9      
      &pushsdbgv 31							//'client'
      &pushundef
      &equals
      &not
      &jnz label8      
      &pushsdb 31							//'client'
      &pushsdbgv 32							//'_parent'
      &setVariable
     label8:
      &pushsdb 4							//'currentStateLabel'
      &pushsdb 6							//'_disabled'
      &setVariable
      &pushsdb 5							//'isEnabled'
      &pushfalse
      &setVariable
      &pushsdb 12							//'isSelected'
      &pushfalse
      &setVariable
      &pushsdb 33							//'1'
      &pushone
      &dcallfp 21							// SetEnabled()
      &pushsdb 30							//'initialized'
      &pushtrue
      &setVariable
      &pushsdb 34							//'FSCommand:'
      &pushthisgv
      &toString
      &pushsdb 36							//':OnInitialized'
      &add
      &concat
      &pushsdb 19							//''
      &getURL2
      &pushsdbgv 37							//'extern'
      &pushsdbgm 38							//'InGame'
      &not
      &not
      &jnz label9      
      &pushsdb 33							//'1'
      &pushone
      &dcallfp 21							// SetEnabled()
     label9:
    &end // of frame 0

    &placeMovieClip 127 
    
      &onClipEvent &load
        &pushs ''
        &pushbyte 7
        &pushfalse
        &setProperty
      &end
    &end // of placeMovieClip 127

    &placeMovieClip 128 &as 'backgroundStage'
    
      &onClipEvent &load
        &constants '_parent', 'imageClip', 'clip', 'backgroundClip', 'isSelected', 'Normal', 'Highlighted', 'this', 'attachMovie', 'currentStateLabel', 'gotoAndPlay'  
        &pushsdbgv 0							//'_parent'
        &pushsdbgm 1							//'imageClip'
        &pushundef
        &equals
        &not
        &not
        &jnz label3        
        &pushsdb 2							//'clip'
        &pushzero
        &pushsdb 2							//'clip'
        &pushsdbgv 0							//'_parent'
        &pushsdbgm 3							//'backgroundClip'
        &pushsdbgv 0							//'_parent'
        &pushsdbgm 4							//'isSelected'
        &jnz label1        
        &pushsdb 5							//'Normal'
        &jmp label2        
       label1:
        &pushsdb 6							//'Highlighted'
       label2:
        &add
        &pushbyte 3
        &pushthisgv
        &pushsdb 8							//'attachMovie'
        &callMethod
        &varEquals
        &pushsdbgv 0							//'_parent'
        &pushsdbgm 9							//'currentStateLabel'
        &pushone
        &pushsdbgv 2							//'clip'
        &dcallmp 10							// gotoAndPlay()
       label3:
      &end
    &end // of placeMovieClip 128

    &placeMovieClip 128 &as 'imageStage'
    
      &onClipEvent &load
        &constants '_parent', 'imageClip', 'clip', 'isSelected', 'Normal', 'Highlighted', 'this', 'attachMovie', 'currentStateLabel', 'gotoAndPlay'  
        &pushsdbgv 0							//'_parent'
        &pushsdbgm 1							//'imageClip'
        &pushundef
        &equals
        &not
        &not
        &jnz label3        
        &pushsdb 2							//'clip'
        &pushzero
        &pushsdb 2							//'clip'
        &pushsdbgv 0							//'_parent'
        &pushsdbgm 1							//'imageClip'
        &pushsdbgv 0							//'_parent'
        &pushsdbgm 3							//'isSelected'
        &jnz label1        
        &pushsdb 4							//'Normal'
        &jmp label2        
       label1:
        &pushsdb 5							//'Highlighted'
       label2:
        &add
        &pushbyte 3
        &pushthisgv
        &pushsdb 7							//'attachMovie'
        &callMethod
        &varEquals
        &pushsdbgv 0							//'_parent'
        &pushsdbgm 8							//'currentStateLabel'
        &pushone
        &pushsdbgv 2							//'clip'
        &dcallmp 9							// gotoAndPlay()
       label3:
      &end
    &end // of placeMovieClip 128
  &end // of defineMovieClip 129

  &placeMovieClip 129 &as 'holdFireStanceButton'
  
    &onClipEvent &construct
      &pushs 'imageClip'
      &pushssv 'HoldFireStance'
      &pushs 'backgroundClip'
      &pushssv 'StanceButtonBackground'
    &end
  &end // of placeMovieClip 129
  
  &importAssets &from 'HelpBox.swf'
    'HelpBoxSite' &as 130
  &end // of importAssets

  &placeMovieClip 130 &as 'holdFireStanceHelpSite'
  
    &onClipEvent &construct
      &pushs 'vertAlignment'
      &pushssv 'bottom'
      &pushs 'horzAlignment'
      &pushssv 'left'
    &end
  &end // of placeMovieClip 130

  &placeMovieClip 129 &as 'holdGroundStanceButton'
  
    &onClipEvent &construct
      &pushs 'imageClip'
      &pushssv 'HoldGroundStance'
      &pushs 'backgroundClip'
      &pushssv 'StanceButtonBackground'
    &end
  &end // of placeMovieClip 129

  &placeMovieClip 130 &as 'holdGroundStanceHelpSite'
  
    &onClipEvent &construct
      &pushs 'vertAlignment'
      &pushssv 'bottom'
      &pushs 'horzAlignment'
      &pushssv 'left'
    &end
  &end // of placeMovieClip 130

  &placeMovieClip 129 &as 'guardStanceButton'
  
    &onClipEvent &construct
      &pushs 'imageClip'
      &pushssv 'GuardStance'
      &pushs 'backgroundClip'
      &pushssv 'StanceButtonBackground'
    &end
  &end // of placeMovieClip 129

  &placeMovieClip 130 &as 'guardStanceHelpSite'
  
    &onClipEvent &construct
      &pushs 'vertAlignment'
      &pushssv 'bottom'
      &pushs 'horzAlignment'
      &pushssv 'left'
    &end
  &end // of placeMovieClip 130

  &placeMovieClip 129 &as 'aggressiveStanceButton'
  
    &onClipEvent &construct
      &pushs 'imageClip'
      &pushssv 'AggressiveStance'
      &pushs 'backgroundClip'
      &pushssv 'StanceButtonBackground'
    &end
  &end // of placeMovieClip 129

  &placeMovieClip 130 &as 'aggressiveStanceHelpSite'
  
    &onClipEvent &construct
      &pushs 'vertAlignment'
      &pushssv 'bottom'
      &pushs 'horzAlignment'
      &pushssv 'left'
    &end
  &end // of placeMovieClip 130

  &placeMovieClip 129 &as 'planningModeButton'
  
    &onClipEvent &construct
      &pushs 'imageClip'
      &pushssv 'PlanningMode'
      &pushs 'backgroundClip'
      &pushssv 'CommandButtonBackground'
    &end
  &end // of placeMovieClip 129

  &placeMovieClip 130 &as 'planningModeHelpSite'
  
    &onClipEvent &construct
      &pushs 'vertAlignment'
      &pushssv 'bottom'
      &pushs 'horzAlignment'
      &pushssv 'left'
    &end
  &end // of placeMovieClip 130

  &placeMovieClip 129 &as 'waypointModeButton'
  
    &onClipEvent &construct
      &pushs 'imageClip'
      &pushssv 'WaypointMode'
      &pushs 'backgroundClip'
      &pushssv 'CommandButtonBackground'
    &end
  &end // of placeMovieClip 129

  &placeMovieClip 130 &as 'waypointModeHelpSite'
  
    &onClipEvent &construct
      &pushs 'vertAlignment'
      &pushssv 'bottom'
      &pushs 'horzAlignment'
      &pushssv 'left'
    &end
  &end // of placeMovieClip 130

  &placeMovieClip 129 &as 'reverseMoveButton'
  
    &onClipEvent &construct
      &pushs 'imageClip'
      &pushssv 'ReverseMove'
      &pushs 'backgroundClip'
      &pushssv 'CommandButtonBackground'
    &end
  &end // of placeMovieClip 129

  &placeMovieClip 130 &as 'reverseMoveHelpSite'
  
    &onClipEvent &construct
      &pushs 'vertAlignment'
      &pushssv 'bottom'
      &pushs 'horzAlignment'
      &pushssv 'left'
    &end
  &end // of placeMovieClip 130

  &placeMovieClip 129 &as 'forceMoveButton'
  
    &onClipEvent &construct
      &pushs 'imageClip'
      &pushssv 'ForceMove'
      &pushs 'backgroundClip'
      &pushssv 'CommandButtonBackground'
    &end
  &end // of placeMovieClip 129

  &placeMovieClip 130 &as 'forceMoveHelpSite'
  
    &onClipEvent &construct
      &pushs 'vertAlignment'
      &pushssv 'bottom'
      &pushs 'horzAlignment'
      &pushssv 'left'
    &end
  &end // of placeMovieClip 130

  &placeMovieClip 129 &as 'attackMoveButton'
  
    &onClipEvent &construct
      &pushs 'imageClip'
      &pushssv 'AttackMove'
      &pushs 'backgroundClip'
      &pushssv 'CommandButtonBackground'
    &end
  &end // of placeMovieClip 129

  &placeMovieClip 130 &as 'attackMoveHelpSite'
  
    &onClipEvent &construct
      &pushs 'vertAlignment'
      &pushssv 'bottom'
      &pushs 'horzAlignment'
      &pushssv 'left'
    &end
  &end // of placeMovieClip 130

  &placeMovieClip 129 &as 'forceAttackButton'
  
    &onClipEvent &construct
      &pushs 'imageClip'
      &pushssv 'ForceFire'
      &pushs 'backgroundClip'
      &pushssv 'CommandButtonBackground'
    &end
  &end // of placeMovieClip 129

  &placeMovieClip 130 &as 'forceAttackHelpSite'
  
    &onClipEvent &construct
      &pushs 'vertAlignment'
      &pushssv 'bottom'
      &pushs 'horzAlignment'
      &pushssv 'left'
    &end
  &end // of placeMovieClip 130

  &defineMovieClip 133 // total frames: 1
  &end // of defineMovieClip 133

  &defineMovieClip 136 // total frames: 30

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

    &placeMovieClip 133 
    
      &onClipEvent &load
        &pushs ''
        &pushbyte 7
        &pushfalse
        &setProperty
      &end
    &end // of placeMovieClip 133

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 136

  &defineMovieClip 139 // total frames: 1
  &end // of defineMovieClip 139

  &defineMovieClip 140 // total frames: 15

    &frame 0
      &stop
    &end // of frame 0

    &placeMovieClip 139 
    
      &onClipEvent &load
        &pushs ''
        &pushbyte 7
        &pushfalse
        &setProperty
      &end
    &end // of placeMovieClip 139

    &frame 14
      &gotoFrame 0
    &end // of frame 14
  &end // of defineMovieClip 140

  &defineMovieClip 141 // total frames: 1

    &frame 0
      &function2 PlayEffect (r:2='GlowNumber') (r:1='this')
        &pushs '_show'
        &pushone
        &push r:1        
        &push r:2        
        &getMember
        &pushs 'gotoAndPlay'
        &callmp
      &end // of function PlayEffect

      &function onUnload (      )      
        &pushs 'PlayEffect'
        &delete2
        &pop
        &pushs 'onUnload'
        &delete2
        &pop
      &end // of function onUnload

    &end // of frame 0
  &end // of defineMovieClip 141
&end
