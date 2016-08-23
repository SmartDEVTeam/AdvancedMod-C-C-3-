movie 'E:\Projects\CNC3\Data\APTBUI~1\034A3~1.0-D\pc\Output\TACTIC~4\\TACTIC~1.eaf' &compressed // flash 7, total frames: 1, frame rate: 30 fps, 1024x768 px

  &defineButton 2
  
    &on     &overUpToOverDown
      &pushzero
      &pushsgv 'client'
      &pushs 'OnPress'
      &callmp
    &end
  
    &on     &overDownToOverUp
      &pushzero
      &pushsgv 'client'
      &pushs 'OnRelease'
      &callmp
    &end
  
    &on     &idleToOverUp    ,&outDownToOverDown    ,&idleToOverDown
      &pushzero
      &pushsgv 'client'
      &pushs 'OnRollOver'
      &callmp
    &end
  
    &on     &overUpToIdle    ,&overDownToOutDown    ,&overDownToIdle
      &pushzero
      &pushsgv 'client'
      &pushs 'OnRollOut'
      &callmp
    &end
  &end // of defineButton 2

  &defineMovieClip 3 // total frames: 40

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
  &end // of defineMovieClip 3
  
  &exportAssets
    3 &as 'ObjectivesButtonButton'
  &end // of exportAssets

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
    4 &as 'CommandModeButtonButton'
  &end // of exportAssets

  &defineMovieClip 11 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'initialized', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &push r:1        
        &trace
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
  &end // of defineMovieClip 11

  &defineMovieClip 20 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'initialized', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &push r:1        
        &trace
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
  &end // of defineMovieClip 20

  &defineMovieClip 21 // total frames: 40

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
  &end // of defineMovieClip 21
  
  &exportAssets
    21 &as 'IDButtonBackgroundHighlited'
  &end // of exportAssets

  &defineMovieClip 28 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'initialized', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &push r:1        
        &trace
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
  &end // of defineMovieClip 28

  &defineMovieClip 32 // total frames: 1
  &end // of defineMovieClip 32

  &defineMovieClip 35 // total frames: 54

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 43
      &gotoLabel '_over'
      &play
    &end // of frame 43

    &frame 53
      &stop
    &end // of frame 53
  &end // of defineMovieClip 35
  
  &exportAssets
    35 &as 'IDButtonBackgroundNormal'
  &end // of exportAssets

  &defineMovieClip 42 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'initialized', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &push r:1        
        &trace
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
  &end // of defineMovieClip 42

  &defineMovieClip 49 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'initialized', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &push r:1        
        &trace
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
  &end // of defineMovieClip 49

  &defineMovieClip 59 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'initialized', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &push r:1        
        &trace
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
  &end // of defineMovieClip 59

  &defineMovieClip 60 // total frames: 54

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 43
      &gotoLabel '_over'
      &play
    &end // of frame 43

    &frame 53
      &stop
    &end // of frame 53
  &end // of defineMovieClip 60
  
  &exportAssets
    60 &as 'ObjectivesButtonBackgroundNormal'
  &end // of exportAssets

  &defineMovieClip 66 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'initialized', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &push r:1        
        &trace
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
    67 &as 'CommandModeButtonBackgroundNormal'
  &end // of exportAssets

  &defineMovieClip 74 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'initialized', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &push r:1        
        &trace
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
  &end // of defineMovieClip 74

  &defineMovieClip 75 // total frames: 40

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
  &end // of defineMovieClip 75
  
  &exportAssets
    75 &as 'CommandModeButtonBackgroundHighlighted'
  &end // of exportAssets

  &defineMovieClip 78 // total frames: 40

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
  &end // of defineMovieClip 78
  
  &exportAssets
    78 &as 'SellButtonImageHighlighted'
  &end // of exportAssets

  &defineMovieClip 85 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'initialized', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &push r:1        
        &trace
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
  &end // of defineMovieClip 85

  &defineMovieClip 86 // total frames: 40

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
  &end // of defineMovieClip 86
  
  &exportAssets
    86 &as 'SellButtonImageNormal'
  &end // of exportAssets

  &defineMovieClip 89 // total frames: 40

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
  &end // of defineMovieClip 89
  
  &exportAssets
    89 &as 'PowerButtonImageHighlighted'
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
    92 &as 'OtherButtonImageHighlighted'
  &end // of exportAssets

  &defineMovieClip 93 // total frames: 40

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
  &end // of defineMovieClip 93
  
  &exportAssets
    93 &as 'RepairButtonImageHighlighted'
  &end // of exportAssets

  &defineMovieClip 100 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'initialized', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &push r:1        
        &trace
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
  &end // of defineMovieClip 100

  &defineMovieClip 101 // total frames: 40

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
  &end // of defineMovieClip 101
  
  &exportAssets
    101 &as 'OtherButtonImageNormal'
  &end // of exportAssets

  &defineMovieClip 102 // total frames: 40

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
  &end // of defineMovieClip 102
  
  &exportAssets
    102 &as 'RepairButtonImageNormal'
  &end // of exportAssets

  &defineMovieClip 109 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'initialized', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &push r:1        
        &trace
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
        &trace
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

  &defineMovieClip 117 // total frames: 40

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
  &end // of defineMovieClip 117
  
  &exportAssets
    117 &as 'PlayerStatusButtonImageNormal'
  &end // of exportAssets

  &defineMovieClip 124 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'initialized', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &push r:1        
        &trace
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
  &end // of defineMovieClip 124

  &defineMovieClip 131 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'initialized', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &push r:1        
        &trace
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
  &end // of defineMovieClip 131

  &defineMovieClip 132 // total frames: 40

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
  &end // of defineMovieClip 132
  
  &exportAssets
    132 &as 'MessengerButtonImageNormal'
  &end // of exportAssets

  &defineMovieClip 139 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'initialized', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &push r:1        
        &trace
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
  &end // of defineMovieClip 139

  &defineMovieClip 146 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'initialized', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &push r:1        
        &trace
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
  &end // of defineMovieClip 146

  &defineMovieClip 147 // total frames: 40

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
  &end // of defineMovieClip 147
  
  &exportAssets
    147 &as 'IDButtonImageNormal'
  &end // of exportAssets

  &defineMovieClip 154 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'initialized', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &push r:1        
        &trace
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
  &end // of defineMovieClip 154

  &defineMovieClip 161 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'initialized', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &push r:1        
        &trace
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
  &end // of defineMovieClip 161

  &defineMovieClip 162 // total frames: 40

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
  &end // of defineMovieClip 162
  
  &exportAssets
    162 &as 'ObjectivesButtonImageNormal'
  &end // of exportAssets

  &defineMovieClip 169 // total frames: 30

    &frame 0
      &constants 'DetachFactionObserver', 'OnCurrentFactionChanged', 'onUnload', 'initialized', '_root', 'GetCurrentFaction', 'this', 'AttachFactionObserver'  
      &function2 OnCurrentFactionChanged (r:1='faction') ()
        &push r:1        
        &trace
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
  &end // of defineMovieClip 169

  &defineMovieClip 170 // total frames: 40

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
  &end // of defineMovieClip 170
  
  &exportAssets
    170 &as 'PowerButtonImageNormal'
  &end // of exportAssets

  &frame 0
    &constants 'sellButton', 'powerButton', 'repairButton', 'objectivesButton', 'playerStatusButton', 'intelDBButton', 'messengerButton', 'GetSellButton', 'GetPowerButton', 'GetRepairButton', 'GetObjectivesButton', 'GetPlayerStatusButton', 'GetIntelDBButton', 'GetMessengerButton', 'onUnload', 'initialized', 'helpSite', 'flashyThingy', 'objectivesButtonFlashyThingy', 'intelDBButtonFlashyThingy', 'FSCommand:', 'this', ':OnInitialized', ''  
    &function GetSellButton (    )    
      &pushsdbgv 0							//'sellButton'
      &toString
      &return
    &end // of function GetSellButton

    &function GetPowerButton (    )    
      &pushsdbgv 1							//'powerButton'
      &toString
      &return
    &end // of function GetPowerButton

    &function GetRepairButton (    )    
      &pushsdbgv 2							//'repairButton'
      &toString
      &return
    &end // of function GetRepairButton

    &function GetObjectivesButton (    )    
      &pushsdbgv 3							//'objectivesButton'
      &toString
      &return
    &end // of function GetObjectivesButton

    &function GetPlayerStatusButton (    )    
      &pushsdbgv 4							//'playerStatusButton'
      &toString
      &return
    &end // of function GetPlayerStatusButton

    &function GetIntelDBButton (    )    
      &pushsdbgv 5							//'intelDBButton'
      &toString
      &return
    &end // of function GetIntelDBButton

    &function GetMessengerButton (    )    
      &pushsdbgv 6							//'messengerButton'
      &toString
      &return
    &end // of function GetMessengerButton

    &function onUnload (    )    
      &pushsdb 7							//'GetSellButton'
      &delete2
      &pop
      &pushsdb 8							//'GetPowerButton'
      &delete2
      &pop
      &pushsdb 9							//'GetRepairButton'
      &delete2
      &pop
      &pushsdb 10							//'GetObjectivesButton'
      &delete2
      &pop
      &pushsdb 11							//'GetPlayerStatusButton'
      &delete2
      &pop
      &pushsdb 12							//'GetIntelDBButton'
      &delete2
      &pop
      &pushsdb 13							//'GetMessengerButton'
      &delete2
      &pop
      &pushsdb 14							//'onUnload'
      &delete2
      &pop
    &end // of function onUnload

    &pushsdbgv 15							//'initialized'
    &not
    &not
    &jnz label1    
    &pushsdbgv 0							//'sellButton'
    &pushsdb 16							//'helpSite'
    &pushsdbgv 16							//'helpSite'
    &setMember
    &pushsdbgv 1							//'powerButton'
    &pushsdb 16							//'helpSite'
    &pushsdbgv 16							//'helpSite'
    &setMember
    &pushsdbgv 2							//'repairButton'
    &pushsdb 16							//'helpSite'
    &pushsdbgv 16							//'helpSite'
    &setMember
    &pushsdbgv 3							//'objectivesButton'
    &pushsdb 16							//'helpSite'
    &pushsdbgv 16							//'helpSite'
    &setMember
    &pushsdbgv 3							//'objectivesButton'
    &pushsdb 17							//'flashyThingy'
    &pushsdbgv 18							//'objectivesButtonFlashyThingy'
    &setMember
    &pushsdbgv 4							//'playerStatusButton'
    &pushsdb 16							//'helpSite'
    &pushsdbgv 16							//'helpSite'
    &setMember
    &pushsdbgv 5							//'intelDBButton'
    &pushsdb 16							//'helpSite'
    &pushsdbgv 16							//'helpSite'
    &setMember
    &pushsdbgv 5							//'intelDBButton'
    &pushsdb 17							//'flashyThingy'
    &pushsdbgv 19							//'intelDBButtonFlashyThingy'
    &setMember
    &pushsdbgv 6							//'messengerButton'
    &pushsdb 16							//'helpSite'
    &pushsdbgv 16							//'helpSite'
    &setMember
    &pushsdb 15							//'initialized'
    &pushtrue
    &setVariable
    &pushsdb 20							//'FSCommand:'
    &pushthisgv
    &toString
    &pushsdb 22							//':OnInitialized'
    &add
    &concat
    &pushsdb 23							//''
    &getURL2
   label1:
    &stop
  &end // of frame 0
  
  &importAssets &from 'HelpBox.swf'
    'HelpBoxSite' &as 171
  &end // of importAssets

  &placeMovieClip 171 &as 'helpSite'
  
    &onClipEvent &construct
      &pushs 'vertAlignment'
      &pushssv 'top'
      &pushs 'horzAlignment'
      &pushssv 'right'
    &end
  &end // of placeMovieClip 171

  &defineMovieClip 172 // total frames: 1
  &end // of defineMovieClip 172

  &defineMovieClip 173 // total frames: 1

    &frame 0
      &constants 'stateLabel', 'imageStage', 'clip', 'gotoAndPlay', 'backgroundStage', 'buttonStage', 'isEnabled', '_down', 'SetState', '_over', 'FSCommand:', ':OnClicked', '', 'isOver', ':OnRollOver', '_up', ':OnRollOut', 'removeMovieClip', 'imageClipName', 'isSelected', 'Normal', 'Highlighted', 'attachMovie', 'backgroundClipName', 'flashyThingy', '_visible', '_disabled', 'AttachContent', 'initialized', 'Start', 'Stop', 'shouldPlay', 'helpSite', 'OnPress', 'OnRelease', 'OnRollOver', 'OnRollOut', 'SetVisibility', 'SetEnabled', 'SetSelected', 'SetFlashing', 'GetHelpSite', 'onUnload', 'buttonClip', 'buttonClipName', 'client', 'this', '1', ':OnInitialized', 'extern', 'InGame'  
      &function2 SetState (r:1='newStateLabel') ()
        &push r:1        
        &pushsdbgv 0							//'stateLabel'
        &equals
        &not
        &not
        &jnz label1        
        &push r:1        
        &pushone
        &pushsdbgv 1							//'imageStage'
        &pushsdbgm 2							//'clip'
        &dcallmp 3							// gotoAndPlay()
        &push r:1        
        &pushone
        &pushsdbgv 4							//'backgroundStage'
        &pushsdbgm 2							//'clip'
        &dcallmp 3							// gotoAndPlay()
        &push r:1        
        &pushone
        &pushsdbgv 5							//'buttonStage'
        &pushsdbgm 2							//'clip'
        &dcallmp 3							// gotoAndPlay()
        &pushsdb 0							//'stateLabel'
        &push r:1        
        &setVariable
       label1:
      &end // of function SetState

      &function OnPress (      )      
        &pushsdbgv 6							//'isEnabled'
        &not
        &jnz label2        
        &pushsdb 7							//'_down'
        &pushone
        &dcallfp 8							// SetState()
       label2:
      &end // of function OnPress

      &function2 OnRelease () (r:1='this')
        &pushsdbgv 6							//'isEnabled'
        &not
        &jnz label3        
        &pushsdb 9							//'_over'
        &pushone
        &dcallfp 8							// SetState()
       label3:
        &pushsdb 10							//'FSCommand:'
        &push r:1        
        &toString
        &pushsdb 11							//':OnClicked'
        &add
        &concat
        &pushsdb 12							//''
        &getURL2
      &end // of function OnRelease

      &function2 OnRollOver () (r:1='this')
        &pushsdbgv 13							//'isOver'
        &not
        &not
        &jnz label5        
        &pushsdbgv 6							//'isEnabled'
        &not
        &jnz label4        
        &pushsdb 9							//'_over'
        &pushone
        &dcallfp 8							// SetState()
       label4:
        &pushsdb 13							//'isOver'
        &pushtrue
        &setVariable
        &pushsdb 10							//'FSCommand:'
        &push r:1        
        &toString
        &pushsdb 14							//':OnRollOver'
        &add
        &concat
        &pushsdb 12							//''
        &getURL2
       label5:
      &end // of function OnRollOver

      &function2 OnRollOut () (r:1='this')
        &pushsdbgv 13							//'isOver'
        &not
        &jnz label7        
        &pushsdbgv 6							//'isEnabled'
        &not
        &jnz label6        
        &pushsdb 15							//'_up'
        &pushone
        &dcallfp 8							// SetState()
       label6:
        &pushsdb 13							//'isOver'
        &pushfalse
        &setVariable
        &pushsdb 10							//'FSCommand:'
        &push r:1        
        &toString
        &pushsdb 16							//':OnRollOut'
        &add
        &concat
        &pushsdb 12							//''
        &getURL2
       label7:
      &end // of function OnRollOut

      &function2 AttachContent () ()
        &pushsdbgv 1							//'imageStage'
        &pushsdbgm 2							//'clip'
        &setRegister r:1
        &pop
        &push r:1        
        &pushundef
        &equals
        &not
        &not
        &jnz label8        
        &pushzero
        &push r:1        
        &dcallmp 17							// removeMovieClip()
       label8:
        &pushzero
        &pushsdb 2							//'clip'
        &pushsdbgv 18							//'imageClipName'
        &pushsdbgv 19							//'isSelected'
        &jnz label9        
        &pushsdb 20							//'Normal'
        &jmp label10        
       label9:
        &pushsdb 21							//'Highlighted'
       label10:
        &add
        &pushbyte 3
        &pushsdbgv 1							//'imageStage'
        &pushsdb 22							//'attachMovie'
        &callMethod
        &setRegister r:1
        &pop
        &pushsdbgv 0							//'stateLabel'
        &pushone
        &push r:1        
        &dcallmp 3							// gotoAndPlay()
        &pushsdbgv 4							//'backgroundStage'
        &pushsdbgm 2							//'clip'
        &setRegister r:1
        &pop
        &push r:1        
        &pushundef
        &equals
        &not
        &not
        &jnz label11        
        &pushzero
        &push r:1        
        &dcallmp 17							// removeMovieClip()
       label11:
        &pushzero
        &pushsdb 2							//'clip'
        &pushsdbgv 23							//'backgroundClipName'
        &pushsdbgv 19							//'isSelected'
        &jnz label12        
        &pushsdb 20							//'Normal'
        &jmp label13        
       label12:
        &pushsdb 21							//'Highlighted'
       label13:
        &add
        &pushbyte 3
        &pushsdbgv 4							//'backgroundStage'
        &pushsdb 22							//'attachMovie'
        &callMethod
        &setRegister r:1
        &pop
        &pushsdbgv 0							//'stateLabel'
        &pushone
        &push r:1        
        &dcallmp 3							// gotoAndPlay()
      &end // of function AttachContent

      &function2 SetVisibility (r:2='visArg') ()
        &push r:2        
        &toNumber
        &pushzero
        &equals
        &not
        &setRegister r:1
        &pop
        &pushsdb 12							//''
        &pushbyte 7
        &push r:1        
        &setProperty
        &pushsdbgv 24							//'flashyThingy'
        &pushsdb 25							//'_visible'
        &push r:1        
        &setMember
      &end // of function SetVisibility

      &function2 SetEnabled (r:2='enableArg') ()
        &push r:2        
        &toNumber
        &pushzero
        &equals
        &not
        &setRegister r:1
        &pop
        &push r:1        
        &pushsdbgv 6							//'isEnabled'
        &equals
        &not
        &not
        &jnz label16        
        &pushsdb 6							//'isEnabled'
        &push r:1        
        &setVariable
        &pushsdbgv 6							//'isEnabled'
        &jnz label14        
        &pushsdb 26							//'_disabled'
        &jmp label15        
       label14:
        &pushsdb 15							//'_up'
       label15:
        &pushone
        &dcallfp 8							// SetState()
       label16:
      &end // of function SetEnabled

      &function2 SetSelected (r:2='selectArg') ()
        &push r:2        
        &toNumber
        &pushzero
        &equals
        &not
        &setRegister r:1
        &pop
        &push r:1        
        &pushsdbgv 19							//'isSelected'
        &equals
        &not
        &not
        &jnz label17        
        &pushsdb 19							//'isSelected'
        &push r:1        
        &setVariable
        &pushzero
        &dcallfp 27							// AttachContent()
       label17:
      &end // of function SetSelected

      &function2 SetFlashing (r:2='flashArg') ()
        &pushsdbgv 24							//'flashyThingy'
        &pushundef
        &equals
        &not
        &jnz label18        
        &pushundef
        &return
       label18:
        &push r:2        
        &toNumber
        &pushzero
        &equals
        &not
        &setRegister r:1
        &pop
        &pushsdbgv 24							//'flashyThingy'
        &pushsdbgm 28							//'initialized'
        &not
        &jnz label21        
        &push r:1        
        &not
        &jnz label19        
        &pushzero
        &pushsdbgv 24							//'flashyThingy'
        &dcallmp 29							// Start()
        &jmp label20        
       label19:
        &pushzero
        &pushsdbgv 24							//'flashyThingy'
        &dcallmp 30							// Stop()
       label20:
        &jmp label22        
       label21:
        &pushsdbgv 24							//'flashyThingy'
        &pushsdb 31							//'shouldPlay'
        &push r:1        
        &setMember
       label22:
      &end // of function SetFlashing

      &function GetHelpSite (      )      
        &pushsdbgv 32							//'helpSite'
        &toString
        &return
      &end // of function GetHelpSite

      &function onUnload (      )      
        &pushsdb 8							//'SetState'
        &delete2
        &pop
        &pushsdb 33							//'OnPress'
        &delete2
        &pop
        &pushsdb 34							//'OnRelease'
        &delete2
        &pop
        &pushsdb 35							//'OnRollOver'
        &delete2
        &pop
        &pushsdb 36							//'OnRollOut'
        &delete2
        &pop
        &pushsdb 27							//'AttachContent'
        &delete2
        &pop
        &pushsdb 37							//'SetVisibility'
        &delete2
        &pop
        &pushsdb 38							//'SetEnabled'
        &delete2
        &pop
        &pushsdb 39							//'SetSelected'
        &delete2
        &pop
        &pushsdb 40							//'SetFlashing'
        &delete2
        &pop
        &pushsdb 41							//'GetHelpSite'
        &delete2
        &pop
        &pushsdb 42							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 28							//'initialized'
      &not
      &not
      &jnz label24      
      &pushsdb 0							//'stateLabel'
      &pushsdb 26							//'_disabled'
      &setVariable
      &pushsdb 6							//'isEnabled'
      &pushfalse
      &setVariable
      &pushsdb 19							//'isSelected'
      &pushfalse
      &setVariable
      &pushsdb 13							//'isOver'
      &pushfalse
      &setVariable
      &pushsdb 43							//'buttonClip'
      &pushzero
      &pushsdb 2							//'clip'
      &pushsdbgv 44							//'buttonClipName'
      &pushbyte 3
      &pushsdbgv 5							//'buttonStage'
      &pushsdb 22							//'attachMovie'
      &callMethod
      &varEquals
      &pushsdbgv 43							//'buttonClip'
      &pushsdb 45							//'client'
      &pushthisgv
      &setMember
      &pushsdb 26							//'_disabled'
      &pushone
      &pushsdbgv 43							//'buttonClip'
      &dcallmp 3							// gotoAndPlay()
      &pushzero
      &dcallfp 27							// AttachContent()
      &pushsdb 47							//'1'
      &pushone
      &dcallfp 38							// SetEnabled()
      &pushsdb 28							//'initialized'
      &pushtrue
      &setVariable
      &pushsdb 10							//'FSCommand:'
      &pushthisgv
      &toString
      &pushsdb 48							//':OnInitialized'
      &add
      &concat
      &pushsdb 12							//''
      &getURL2
      &pushsdbgv 49							//'extern'
      &pushsdbgm 50							//'InGame'
      &not
      &dup
      &not
      &jnz label23      
      &pop
      &pushsdbgv 24							//'flashyThingy'
      &pushundef
      &equals
      &not
     label23:
      &not
      &jnz label24      
      &pushsdb 47							//'1'
      &pushone
      &dcallfp 40							// SetFlashing()
     label24:
      &stop
    &end // of frame 0
  &end // of defineMovieClip 173

  &placeMovieClip 173 &as 'repairButton'
  
    &onClipEvent &construct
      &pushs 'buttonClipName'
      &pushssv 'CommandModeButtonButton'
      &pushs 'imageClipName'
      &pushssv 'RepairButtonImage'
      &pushs 'backgroundClipName'
      &pushssv 'CommandModeButtonBackground'
    &end
  &end // of placeMovieClip 173

  &placeMovieClip 173 &as 'powerButton'
  
    &onClipEvent &construct
      &pushs 'buttonClipName'
      &pushssv 'CommandModeButtonButton'
      &pushs 'imageClipName'
      &pushssv 'PowerButtonImage'
      &pushs 'backgroundClipName'
      &pushssv 'CommandModeButtonBackground'
    &end
  &end // of placeMovieClip 173

  &placeMovieClip 173 &as 'sellButton'
  
    &onClipEvent &construct
      &pushs 'buttonClipName'
      &pushssv 'CommandModeButtonButton'
      &pushs 'imageClipName'
      &pushssv 'SellButtonImage'
      &pushs 'backgroundClipName'
      &pushssv 'CommandModeButtonBackground'
    &end
  &end // of placeMovieClip 173

  &placeMovieClip 173 &as 'playerStatusButton'
  
    &onClipEvent &construct
      &pushs 'buttonClipName'
      &pushssv 'ObjectivesButtonButton'
      &pushs 'imageClipName'
      &pushssv 'PlayerStatusButtonImage'
      &pushs 'backgroundClipName'
      &pushssv 'ObjectivesButtonBackground'
    &end
  &end // of placeMovieClip 173

  &placeMovieClip 173 &as 'messengerButton'
  
    &onClipEvent &construct
      &pushs 'buttonClipName'
      &pushssv 'ObjectivesButtonButton'
      &pushs 'imageClipName'
      &pushssv 'MessengerButtonImage'
      &pushs 'backgroundClipName'
      &pushssv 'IDButtonBackground'
    &end
  &end // of placeMovieClip 173

  &placeMovieClip 173 &as 'objectivesButton'
  
    &onClipEvent &construct
      &pushs 'buttonClipName'
      &pushssv 'ObjectivesButtonButton'
      &pushs 'imageClipName'
      &pushssv 'ObjectivesButtonImage'
      &pushs 'backgroundClipName'
      &pushssv 'ObjectivesButtonBackground'
    &end
  &end // of placeMovieClip 173

  &placeMovieClip 173 &as 'intelDBButton'
  
    &onClipEvent &construct
      &pushs 'buttonClipName'
      &pushssv 'ObjectivesButtonButton'
      &pushs 'imageClipName'
      &pushssv 'IDButtonImage'
      &pushs 'backgroundClipName'
      &pushssv 'IDButtonBackground'
    &end
  &end // of placeMovieClip 173

  &defineMovieClip 176 // total frames: 1
  &end // of defineMovieClip 176

  &defineMovieClip 177 // total frames: 35

    &frame 0
      &constants 'shouldPlay', 'isPlaying', 'Start', 'Stop', 'onUnload', 'initialized'  
      &function Start (      )      
        &pushsdbgv 0							//'shouldPlay'
        &not
        &not
        &jnz label1        
        &pushsdb 0							//'shouldPlay'
        &pushtrue
        &setVariable
        &pushsdbgv 1							//'isPlaying'
        &not
        &not
        &jnz label1        
        &gotoLabel '_play'
        &play
        &pushsdb 1							//'isPlaying'
        &pushtrue
        &setVariable
       label1:
      &end // of function Start

      &function Stop (      )      
        &pushsdb 0							//'shouldPlay'
        &pushfalse
        &setVariable
      &end // of function Stop

      &function onUnload (      )      
        &pushsdb 2							//'Start'
        &delete2
        &pop
        &pushsdb 3							//'Stop'
        &delete2
        &pop
        &pushsdb 4							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 5							//'initialized'
      &not
      &not
      &jnz label3      
      &pushsdb 1							//'isPlaying'
      &pushfalse
      &setVariable
      &pushsdbgv 0							//'shouldPlay'
      &not
      &jnz label2      
      &gotoLabel '_play'
      &play
      &pushsdb 1							//'isPlaying'
      &pushtrue
      &setVariable
     label2:
      &pushsdb 5							//'initialized'
      &pushtrue
      &setVariable
     label3:
    &end // of frame 0

    &frame 4
      &stop
    &end // of frame 4

    &placeMovieClip 176 
    &end // of placeMovieClip 176

    &placeMovieClip 176 
    &end // of placeMovieClip 176

    &frame 34
      &pushsgv 'shouldPlay'
      &not
      &jnz label1      
      &gotoLabel '_play'
      &play
      &jmp label2      
     label1:
      &pushs 'isPlaying'
      &pushfalse
      &setVariable
      &gotoLabel '_stop'
      &play
     label2:
    &end // of frame 34

    &placeMovieClip 176 
    &end // of placeMovieClip 176

    &placeMovieClip 176 
    &end // of placeMovieClip 176
  &end // of defineMovieClip 177

  &defineMovieClip 180 // total frames: 1
  &end // of defineMovieClip 180

  &defineMovieClip 184 // total frames: 1
  &end // of defineMovieClip 184

  &defineMovieClip 186 // total frames: 1
  &end // of defineMovieClip 186

  &defineMovieClip 187 // total frames: 24

    &frame 0
      &constants 'shouldPlay', 'isPlaying', 'Start', 'Stop', 'onUnload', 'initialized'  
      &function Start (      )      
        &pushsdbgv 0							//'shouldPlay'
        &not
        &not
        &jnz label1        
        &pushsdb 0							//'shouldPlay'
        &pushtrue
        &setVariable
        &pushsdbgv 1							//'isPlaying'
        &not
        &not
        &jnz label1        
        &gotoLabel '_play'
        &play
        &pushsdb 1							//'isPlaying'
        &pushtrue
        &setVariable
       label1:
      &end // of function Start

      &function Stop (      )      
        &pushsdb 0							//'shouldPlay'
        &pushfalse
        &setVariable
      &end // of function Stop

      &function onUnload (      )      
        &pushsdb 2							//'Start'
        &delete2
        &pop
        &pushsdb 3							//'Stop'
        &delete2
        &pop
        &pushsdb 4							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 5							//'initialized'
      &not
      &not
      &jnz label3      
      &pushsdb 1							//'isPlaying'
      &pushfalse
      &setVariable
      &pushsdbgv 0							//'shouldPlay'
      &not
      &jnz label2      
      &gotoLabel '_play'
      &play
      &pushsdb 1							//'isPlaying'
      &pushtrue
      &setVariable
     label2:
      &pushsdb 5							//'initialized'
      &pushtrue
      &setVariable
     label3:
    &end // of frame 0

    &frame 3
      &stop
    &end // of frame 3

    &frame 23
      &pushsgv 'shouldPlay'
      &not
      &jnz label1      
      &gotoLabel '_play'
      &play
      &jmp label2      
     label1:
      &pushs 'isPlaying'
      &pushfalse
      &setVariable
      &gotoLabel '_stop'
      &play
     label2:
    &end // of frame 23
  &end // of defineMovieClip 187
&end
