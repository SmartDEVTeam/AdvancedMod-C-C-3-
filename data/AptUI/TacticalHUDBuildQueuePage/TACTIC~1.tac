movie 'E:\Projects\CNC3\Data\APTBUI~1\034A3~1.0-D\pc\Output\TACTIC~2\\TACTIC~1.eaf' &compressed // flash 7, total frames: 1, frame rate: 30 fps, 1024x768 px

  &defineButton 2
  
    &on     &overUpToOverDown
      &constants 'client', 'selectedTabButton', 'this', 'OnPressed'  
      &pushsdbgv 0							//'client'
      &pushsdbgm 1							//'selectedTabButton'
      &pushthisgv
      &equals
      &not
      &not
      &jnz label1      
      &gotoLabel '_down'
      &play
     label1:
      &pushthisgv
      &pushone
      &pushsdbgv 0							//'client'
      &dcallmp 3							// OnPressed()
    &end
  
    &on     &overDownToOverUp
      &constants 'client', 'selectedTabButton', 'this', 'OnClicked'  
      &pushsdbgv 0							//'client'
      &pushsdbgm 1							//'selectedTabButton'
      &pushthisgv
      &equals
      &not
      &not
      &jnz label1      
      &gotoLabel '_over'
      &play
      &pushthisgv
      &pushone
      &pushsdbgv 0							//'client'
      &dcallmp 3							// OnClicked()
     label1:
    &end
  
    &on     &idleToOverUp    ,&outDownToOverDown    ,&idleToOverDown
      &constants 'client', 'selectedTabButton', 'this', 'OnRollOver'  
      &pushsdbgv 0							//'client'
      &pushsdbgm 1							//'selectedTabButton'
      &pushthisgv
      &equals
      &not
      &not
      &jnz label1      
      &gotoLabel '_over'
      &play
     label1:
      &pushthisgv
      &pushone
      &pushsdbgv 0							//'client'
      &dcallmp 3							// OnRollOver()
    &end
  
    &on     &overUpToIdle    ,&overDownToOutDown    ,&overDownToIdle
      &constants 'client', 'selectedTabButton', 'this', 'OnRollOut'  
      &pushsdbgv 0							//'client'
      &pushsdbgm 1							//'selectedTabButton'
      &pushthisgv
      &equals
      &not
      &not
      &jnz label1      
      &gotoLabel '_up'
      &play
     label1:
      &pushthisgv
      &pushone
      &pushsdbgv 0							//'client'
      &dcallmp 3							// OnRollOut()
    &end
  &end // of defineButton 2

  &defineMovieClip 9 // total frames: 30

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
  &end // of defineMovieClip 9

  &defineMovieClip 16 // total frames: 30

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
  &end // of defineMovieClip 16

  &defineMovieClip 17 // total frames: 50

    &frame 0
      &stop
    &end // of frame 0

    &frame 9
      &play
    &end // of frame 9

    &frame 49
      &gotoLabel '_on'
      &play
    &end // of frame 49
  &end // of defineMovieClip 17

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

  &defineMovieClip 29 // total frames: 30

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
  &end // of defineMovieClip 29

  &defineMovieClip 36 // total frames: 30

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
  &end // of defineMovieClip 36

  &defineMovieClip 43 // total frames: 30

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
  &end // of defineMovieClip 43

  &defineMovieClip 50 // total frames: 30

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
  &end // of defineMovieClip 50

  &defineMovieClip 57 // total frames: 30

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
  &end // of defineMovieClip 57

  &defineMovieClip 58 // total frames: 30

    &frame 0
      &pushs '_'
      &pushsgv '_parent'
      &pushsgm 'iconLabel'
      &add
      &gotoAndStop    &end // of frame 0
  &end // of defineMovieClip 58

  &defineMovieClip 63 // total frames: 30

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
  &end // of defineMovieClip 63

  &defineMovieClip 67 // total frames: 30

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
  &end // of defineMovieClip 67

  &defineMovieClip 74 // total frames: 30

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
  &end // of defineMovieClip 74

  &defineMovieClip 81 // total frames: 30

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
  &end // of defineMovieClip 81

  &defineMovieClip 88 // total frames: 30

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
  &end // of defineMovieClip 88

  &defineMovieClip 95 // total frames: 30

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

  &defineMovieClip 103 // total frames: 30

    &frame 0
      &pushs '_'
      &pushsgv '_parent'
      &pushsgm 'iconLabel'
      &add
      &gotoAndStop    &end // of frame 0
  &end // of defineMovieClip 103

  &defineMovieClip 104 // total frames: 40

    &frame 0
      &constants 'client', '_parent'  
      &pushsdbgv 0							//'client'
      &pushundef
      &equals
      &not
      &jnz label1      
      &pushsdb 0							//'client'
      &pushsdbgv 1							//'_parent'
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

    &frame 39
      &stop
    &end // of frame 39
  &end // of defineMovieClip 104
  
  &exportAssets
    104 &as 'TabButton'
  &end // of exportAssets

  &defineMovieClip 105 // total frames: 1
  &end // of defineMovieClip 105

  &defineMovieClip 106 // total frames: 1

    &frame 0
      &constants 'commandList', 'tabHelpSite', 'FSCommand:', ':OnTabPressed', '', ':OnTabRollOver', ':OnTabRollOut', 'GetCommandList', 'GetTabHelpSite', 'OnTabPressed', 'OnTabRollOver', 'OnTabRollOut', 'onUnload', 'initialized', 'disableCommandButtonLoadAnim', 'TacticalHUDCommandListBox.swf', 'loadMovie', 'this', ':OnInitialized'  
      &function GetCommandList (      )      
        &pushsdbgv 0							//'commandList'
        &toString
        &return
      &end // of function GetCommandList

      &function GetTabHelpSite (      )      
        &pushsdbgv 1							//'tabHelpSite'
        &toString
        &return
      &end // of function GetTabHelpSite

      &function2 OnTabPressed () (r:1='this')
        &pushsdb 2							//'FSCommand:'
        &push r:1        
        &toString
        &pushsdb 3							//':OnTabPressed'
        &add
        &concat
        &pushsdb 4							//''
        &getURL2
      &end // of function OnTabPressed

      &function2 OnTabRollOver () (r:1='this')
        &pushsdb 2							//'FSCommand:'
        &push r:1        
        &toString
        &pushsdb 5							//':OnTabRollOver'
        &add
        &concat
        &pushsdb 4							//''
        &getURL2
      &end // of function OnTabRollOver

      &function2 OnTabRollOut () (r:1='this')
        &pushsdb 2							//'FSCommand:'
        &push r:1        
        &toString
        &pushsdb 6							//':OnTabRollOut'
        &add
        &concat
        &pushsdb 4							//''
        &getURL2
      &end // of function OnTabRollOut

      &function onUnload (      )      
        &pushsdb 7							//'GetCommandList'
        &delete2
        &pop
        &pushsdb 8							//'GetTabHelpSite'
        &delete2
        &pop
        &pushsdb 9							//'OnTabPressed'
        &delete2
        &pop
        &pushsdb 10							//'OnTabRollOver'
        &delete2
        &pop
        &pushsdb 11							//'OnTabRollOut'
        &delete2
        &pop
        &pushsdb 12							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 13							//'initialized'
      &not
      &not
      &jnz label1      
      &pushsdb 14							//'disableCommandButtonLoadAnim'
      &pushtrue
      &setVariable
      &pushsdb 15							//'TacticalHUDCommandListBox.swf'
      &pushone
      &pushsdbgv 0							//'commandList'
      &dcallmp 16							// loadMovie()
      &pushsdb 13							//'initialized'
      &pushtrue
      &setVariable
      &pushsdb 2							//'FSCommand:'
      &pushthisgv
      &toString
      &pushsdb 18							//':OnInitialized'
      &add
      &concat
      &pushsdb 4							//''
      &getURL2
     label1:
      &stop
    &end // of frame 0
  &end // of defineMovieClip 106
  
  &exportAssets
    106 &as 'BuildQueuePage'
  &end // of exportAssets

  &frame 0
    &constants 'subTabsInitialized', 'initialized', 'FSCommand:', ':OnInitialized', '', 'pages', 'selectedPage', '_visible', ':OnPageSelected', 'OnTabPressed', 'OnTabRollOver', 'OnTabRollOut', 'subTabs', 'SelectTab', 'MakeTabVisible', 'SetTabFlashing', 'length', '_up', 'tabButton', 'gotoAndPlay', 'nextPageId', 'BuildQueuePage', 'attachMovie', '_x', 'pagePos', '_y', 'tabHelpSite', 'subTabHelpSite', '$', ':Text', 'tabIcon', 'InsertTab', 'splice', 'EraseTab', 'SelectPage', 'removeMovieClip', '_disabled', 'mouseOverTab', ':OnTabRollOver', ':OnTabRollOut', ':OnTabClicked', 'OnSubTabsInitialized', 'OnSubTabSelected', 'OnSubTabPressed', 'OnSubTabRollOver', 'OnSubTabRollOut', 'SetPageHighlighted', 'InsertPage', 'ErasePage', 'OnSubTabClicked', 'TabHelpSite', 'onUnload', 'this', '_parent', 'OnChildLoaded', 'Array'  
    &function2 OnSubTabsInitialized () (r:1='this')
      &pushsdb 0							//'subTabsInitialized'
      &pushtrue
      &setVariable
      &pushsdbgv 1							//'initialized'
      &not
      &jnz label1      
      &pushsdb 2							//'FSCommand:'
      &push r:1      
      &toString
      &pushsdb 3							//':OnInitialized'
      &add
      &concat
      &pushsdb 4							//''
      &getURL2
     label1:
    &end // of function OnSubTabsInitialized

    &function2 OnSubTabSelected (r:3='index') (r:1='this')
      &push r:3      
      &pushzero
      &lessThan
      &not
      &jnz label2      
      &pushundef
      &jmp label3      
     label2:
      &pushsdbgv 5							//'pages'
      &push r:3      
      &getMember
     label3:
      &setRegister r:2
      &pop
      &push r:2      
      &pushsdbgv 6							//'selectedPage'
      &equals
      &not
      &not
      &jnz label6      
      &pushsdbgv 6							//'selectedPage'
      &pushundef
      &equals
      &not
      &not
      &jnz label4      
      &pushsdbgv 6							//'selectedPage'
      &pushsdb 7							//'_visible'
      &pushfalse
      &setMember
     label4:
      &push r:2      
      &pushundef
      &equals
      &not
      &not
      &jnz label5      
      &push r:2      
      &pushsdb 7							//'_visible'
      &pushtrue
      &setMember
     label5:
      &pushsdb 6							//'selectedPage'
      &push r:2      
      &setVariable
      &pushsdb 2							//'FSCommand:'
      &push r:1      
      &toString
      &pushsdb 8							//':OnPageSelected'
      &add
      &concat
      &push r:3      
      &getURL2
     label6:
    &end // of function OnSubTabSelected

    &function2 OnSubTabPressed (r:1='index') ()
      &pushzero
      &pushsdbgv 5							//'pages'
      &push r:1      
      &getMember
      &dcallmp 9							// OnTabPressed()
    &end // of function OnSubTabPressed

    &function2 OnSubTabRollOver (r:1='index') ()
      &pushzero
      &pushsdbgv 5							//'pages'
      &push r:1      
      &getMember
      &dcallmp 10							// OnTabRollOver()
    &end // of function OnSubTabRollOver

    &function2 OnSubTabRollOut (r:1='index') ()
      &pushzero
      &pushsdbgv 5							//'pages'
      &push r:1      
      &getMember
      &dcallmp 11							// OnTabRollOut()
    &end // of function OnSubTabRollOut

    &function2 SelectPage (r:2='indexArg') ()
      &push r:2      
      &toNumber
      &setRegister r:1
      &pop
      &push r:1      
      &pushone
      &pushsdbgv 12							//'subTabs'
      &dcallmp 13							// SelectTab()
      &push r:1      
      &pushone
      &pushsdbgv 12							//'subTabs'
      &dcallmp 14							// MakeTabVisible()
    &end // of function SelectPage

    &function2 SetPageHighlighted (r:4='indexArg', r:3='highlightedArg') ()
      &push r:4      
      &toNumber
      &setRegister r:1
      &pop
      &push r:3      
      &toNumber
      &pushzero
      &equals
      &not
      &setRegister r:2
      &pop
      &push r:2      
      &push r:1      
      &pushbyte 2
      &pushsdbgv 12							//'subTabs'
      &dcallmp 15							// SetTabFlashing()
    &end // of function SetPageHighlighted

    &function2 InsertPage (r:3='index') ()
      &pushsdbgv 5							//'pages'
      &pushsdbgm 16							//'length'
      &pushzero
      &equals
      &not
      &jnz label7      
      &pushsdb 17							//'_up'
      &pushone
      &pushsdbgv 18							//'tabButton'
      &dcallmp 19							// gotoAndPlay()
     label7:
      &pushsdbgv 20							//'nextPageId'
      &pushsdb 20							//'nextPageId'
      &pushsdbgv 20							//'nextPageId'
      &increment
      &setVariable
      &setRegister r:2
      &pop
      &push r:2      
      &push r:2      
      &toString
      &pushsdb 21							//'BuildQueuePage'
      &pushbyte 3
      &pushsdb 22							//'attachMovie'
      &callFunction
      &setRegister r:1
      &pop
      &push r:1      
      &pushsdb 23							//'_x'
      &pushsdbgv 24							//'pagePos'
      &pushsdbgm 23							//'_x'
      &setMember
      &push r:1      
      &pushsdb 25							//'_y'
      &pushsdbgv 24							//'pagePos'
      &pushsdbgm 25							//'_y'
      &setMember
      &push r:1      
      &pushsdb 7							//'_visible'
      &pushfalse
      &setMember
      &push r:1      
      &pushsdb 26							//'tabHelpSite'
      &pushsdbgv 27							//'subTabHelpSite'
      &setMember
      &pushsdb 28							//'$'
      &push r:1      
      &toString
      &add
      &pushsdb 29							//':Text'
      &add
      &pushsdbgv 30							//'tabIcon'
      &push r:3      
      &pushbyte 3
      &pushsdbgv 12							//'subTabs'
      &dcallmp 31							// InsertTab()
      &push r:1      
      &pushzero
      &push r:3      
      &pushbyte 3
      &pushsdbgv 5							//'pages'
      &dcallmp 32							// splice()
      &push r:1      
      &toString
      &return
    &end // of function InsertPage

    &function2 ErasePage (r:3='index') (r:1='_parent')
      &push r:3      
      &pushone
      &pushsdbgv 12							//'subTabs'
      &dcallmp 33							// EraseTab()
      &pushsdbgv 5							//'pages'
      &push r:3      
      &getMember
      &setRegister r:2
      &pop
      &push r:2      
      &pushsdbgv 6							//'selectedPage'
      &equals
      &not
      &jnz label8      
      &pushundef
      &pushone
      &dcallfp 34							// SelectPage()
     label8:
      &pushzero
      &push r:2      
      &dcallmp 35							// removeMovieClip()
      &pushone
      &push r:3      
      &pushbyte 2
      &pushsdbgv 5							//'pages'
      &dcallmp 32							// splice()
      &pushsdbgv 5							//'pages'
      &pushsdbgm 16							//'length'
      &pushzero
      &equals
      &not
      &jnz label10      
      &pushsdb 20							//'nextPageId'
      &pushzerosv
      &pushsdb 4							//''
      &pushbyte 7
      &getProperty
      &not
      &jnz label9      
      &pushzero
      &pushone
      &push r:1      
      &dcallmp 13							// SelectTab()
     label9:
      &pushsdb 36							//'_disabled'
      &pushone
      &pushsdbgv 18							//'tabButton'
      &dcallmp 19							// gotoAndPlay()
      &pushzero
      &dcallfp 11							// OnTabRollOut()
     label10:
    &end // of function ErasePage

    &function2 OnTabRollOver () (r:1='this')
      &pushsdbgv 37							//'mouseOverTab'
      &not
      &not
      &jnz label11      
      &pushsdb 37							//'mouseOverTab'
      &pushtrue
      &setVariable
      &pushsdb 2							//'FSCommand:'
      &push r:1      
      &toString
      &pushsdb 38							//':OnTabRollOver'
      &add
      &concat
      &pushsdb 4							//''
      &getURL2
     label11:
    &end // of function OnTabRollOver

    &function2 OnTabRollOut () (r:1='this')
      &pushsdbgv 37							//'mouseOverTab'
      &not
      &jnz label12      
      &pushsdb 37							//'mouseOverTab'
      &pushfalse
      &setVariable
      &pushsdb 2							//'FSCommand:'
      &push r:1      
      &toString
      &pushsdb 39							//':OnTabRollOut'
      &add
      &concat
      &pushsdb 4							//''
      &getURL2
     label12:
    &end // of function OnTabRollOut

    &function2 OnSubTabClicked (r:2='index') (r:1='this')
      &pushsdb 2							//'FSCommand:'
      &push r:1      
      &toString
      &pushsdb 40							//':OnTabClicked'
      &add
      &concat
      &push r:2      
      &toString
      &getURL2
    &end // of function OnSubTabClicked

    &function GetTabHelpSite (    )    
      &pushsdbgv 26							//'tabHelpSite'
      &toString
      &return
    &end // of function GetTabHelpSite

    &function onUnload (    )    
      &pushsdb 41							//'OnSubTabsInitialized'
      &delete2
      &pop
      &pushsdb 42							//'OnSubTabSelected'
      &delete2
      &pop
      &pushsdb 43							//'OnSubTabPressed'
      &delete2
      &pop
      &pushsdb 44							//'OnSubTabRollOver'
      &delete2
      &pop
      &pushsdb 45							//'OnSubTabRollOut'
      &delete2
      &pop
      &pushsdb 34							//'SelectPage'
      &delete2
      &pop
      &pushsdb 46							//'SetPageHighlighted'
      &delete2
      &pop
      &pushsdb 47							//'InsertPage'
      &delete2
      &pop
      &pushsdb 48							//'ErasePage'
      &delete2
      &pop
      &pushsdb 10							//'OnTabRollOver'
      &delete2
      &pop
      &pushsdb 11							//'OnTabRollOut'
      &delete2
      &pop
      &pushsdb 49							//'OnSubTabClicked'
      &delete2
      &pop
      &pushsdb 50							//'TabHelpSite'
      &delete2
      &pop
      &pushsdb 51							//'onUnload'
      &delete2
      &pop
    &end // of function onUnload

    &pushsdbgv 1							//'initialized'
    &not
    &not
    &jnz label13    
    &pushthisgv
    &pushone
    &pushsdbgv 53							//'_parent'
    &dcallmp 54							// OnChildLoaded()
    &pushsdb 5							//'pages'
    &pushzero
    &pushsdb 55							//'Array'
    &new
    &setVariable
    &pushsdb 20							//'nextPageId'
    &pushzerosv
    &pushsdb 37							//'mouseOverTab'
    &pushfalse
    &setVariable
    &pushsdb 1							//'initialized'
    &pushtrue
    &setVariable
    &pushsdbgv 0							//'subTabsInitialized'
    &not
    &jnz label13    
    &pushsdb 2							//'FSCommand:'
    &pushthisgv
    &toString
    &pushsdb 3							//':OnInitialized'
    &add
    &concat
    &pushsdb 4							//''
    &getURL2
   label13:
    &stop
  &end // of frame 0
  
  &importAssets &from 'HelpBox.swf'
    'HelpBoxSite' &as 107
  &end // of importAssets

  &placeMovieClip 107 &as 'subTabHelpSite'
  
    &onClipEvent &construct
      &pushs 'vertAlignment'
      &pushssv 'top'
      &pushs 'horzAlignment'
      &pushssv 'right'
    &end
  &end // of placeMovieClip 107

  &defineMovieClip 115 // total frames: 30

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
  &end // of defineMovieClip 115

  &defineButton 116
  
    &on     &overUpToOverDown
      &gotoLabel '_down'
      &play
    &end
  
    &on     &overDownToOverUp
      &gotoLabel '_release'
      &play
      &pushthisgv
      &pushone
      &pushsgv '_parent'
      &pushs 'OnSpinnerButtonClicked'
      &callmp
    &end
  
    &on     &idleToOverUp    ,&outDownToOverDown    ,&idleToOverDown
      &gotoLabel '_over'
      &play
    &end
  
    &on     &overUpToIdle    ,&overDownToOutDown    ,&overDownToIdle
      &gotoLabel '_up'
      &play
    &end
  &end // of defineButton 116

  &defineMovieClip 123 // total frames: 30

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
  &end // of defineMovieClip 123

  &defineMovieClip 130 // total frames: 30

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
  &end // of defineMovieClip 130

  &defineMovieClip 131 // total frames: 50

    &frame 0
      &constants 'isEnabled', 'SetEnabled', 'onUnload', 'initialized'  
      &function2 SetEnabled (r:1='enable') ()
        &push r:1        
        &pushsdbgv 0							//'isEnabled'
        &equals
        &not
        &not
        &jnz label3        
        &push r:1        
        &not
        &jnz label1        
        &gotoLabel '_up'
        &play
        &jmp label2        
       label1:
        &gotoLabel '_disabled'
        &play
       label2:
        &pushsdb 0							//'isEnabled'
        &push r:1        
        &setVariable
       label3:
      &end // of function SetEnabled

      &function onUnload (      )      
        &pushsdb 1							//'SetEnabled'
        &delete2
        &pop
        &pushsdb 2							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 3							//'initialized'
      &not
      &not
      &jnz label5      
      &pushsdbgv 0							//'isEnabled'
      &not
      &not
      &jnz label4      
      &gotoLabel '_disabled'
      &play
     label4:
      &pushsdb 3							//'initialized'
      &pushtrue
      &setVariable
     label5:
    &end // of frame 0

    &frame 8
      &stop
    &end // of frame 8

    &frame 18
      &stop
    &end // of frame 18

    &frame 28
      &stop
    &end // of frame 28

    &frame 38
      &gotoLabel '_up'
      &play
    &end // of frame 38

    &frame 49
      &stop
    &end // of frame 49
  &end // of defineMovieClip 131

  &defineMovieClip 132 // total frames: 1

    &frame 0
      &constants 'tabButtons', 'length', 'selectedTabButton', '_up', 'gotoAndPlay', '_selected', 'GetTabButtonIndex', 'client', 'OnSubTabSelected', 'SelectTabButton', '_off', '_on', 'flashClip', 'OnSubTabPressed', 'OnSubTabClicked', 'OnSubTabRollOver', 'OnSubTabRollOut', 'tabSlotWidth', 'buttons', '_x', 'buttonStageLeft', 'numVisibleTabs', '_visible', 'ShouldTabButtonBeVisible', 'tabScrollPos', 'UpdateTabButtonVisibility', 'CanScrollLeft', 'spinLeftButton', 'SetSpinnerButtonEnabled', 'CanScrollRight', 'spinRightButton', 'nextTabButtonId', 'TabButton', 'attachMovie', 'iconLabel', 'text', 'splice', 'removeMovieClip', 'ScrollTo', 'initialized', 'SetEnabled', 'isEnabled', 'SelectTab', 'SetTabFlashing', 'GetSelectedTabNum', 'OnPressed', 'OnClicked', 'OnRollOver', 'OnRollOut', 'InsertTab', 'EraseTab', 'OnSpinnerButtonClicked', 'MakeTabVisible', 'onUnload', 'extern', 'InGame', '_root', 'GetCurrentFaction', 'Alien', '_parent', 'Array', 'this', 'OnSubTabsInitialized'  
      &function2 GetTabButtonIndex (r:2='tabButton') ()
        &push r:2        
        &pushundef
        &equals
        &not
        &jnz label1        
        &pushbyte -1
        &return
       label1:
        &pushzero
        &setRegister r:1
        &pop
       label2:
        &push r:1        
        &pushsdbgv 0							//'tabButtons'
        &pushsdbgm 1							//'length'
        &lessThan
        &not
        &jnz label4        
        &push r:2        
        &pushsdbgv 0							//'tabButtons'
        &push r:1        
        &getMember
        &equals
        &not
        &jnz label3        
        &push r:1        
        &return
       label3:
        &push r:1        
        &increment
        &setRegister r:1
        &pop
        &jmp label2        
       label4:
        &pushbyte -1
        &return
      &end // of function GetTabButtonIndex

      &function2 SelectTabButton (r:1='tabButton') ()
        &push r:1        
        &pushsdbgv 2							//'selectedTabButton'
        &equals
        &not
        &not
        &jnz label7        
        &pushsdbgv 2							//'selectedTabButton'
        &pushundef
        &equals
        &not
        &not
        &jnz label5        
        &pushsdb 3							//'_up'
        &pushone
        &pushsdbgv 2							//'selectedTabButton'
        &dcallmp 4							// gotoAndPlay()
       label5:
        &push r:1        
        &pushundef
        &equals
        &not
        &not
        &jnz label6        
        &pushsdb 5							//'_selected'
        &pushone
        &push r:1        
        &dcallmp 4							// gotoAndPlay()
       label6:
        &pushsdb 2							//'selectedTabButton'
        &push r:1        
        &setVariable
        &push r:1        
        &pushone
        &pushsdb 6							//'GetTabButtonIndex'
        &callFunction
        &pushone
        &pushsdbgv 7							//'client'
        &dcallmp 8							// OnSubTabSelected()
       label7:
      &end // of function SelectTabButton

      &function2 SelectTab (r:1='index') ()
        &pushsdbgv 0							//'tabButtons'
        &push r:1        
        &getMember
        &pushone
        &dcallfp 9							// SelectTabButton()
      &end // of function SelectTab

      &function2 SetTabFlashing (r:1='index', r:2='flashing') ()
        &push r:2        
        &jnz label8        
        &pushsdb 10							//'_off'
        &jmp label9        
       label8:
        &pushsdb 11							//'_on'
       label9:
        &pushone
        &pushsdbgv 0							//'tabButtons'
        &push r:1        
        &getMember
        &pushsdbgm 12							//'flashClip'
        &dcallmp 4							// gotoAndPlay()
      &end // of function SetTabFlashing

      &function GetSelectedTabNum (      )      
        &pushsdbgv 2							//'selectedTabButton'
        &pushone
        &pushsdb 6							//'GetTabButtonIndex'
        &callFunction
        &return
      &end // of function GetSelectedTabNum

      &function2 OnPressed (r:1='buttonClip') ()
        &push r:1        
        &pushone
        &pushsdb 6							//'GetTabButtonIndex'
        &callFunction
        &pushone
        &pushsdbgv 7							//'client'
        &dcallmp 13							// OnSubTabPressed()
      &end // of function OnPressed

      &function2 OnClicked (r:1='buttonClip') ()
        &push r:1        
        &pushone
        &pushsdb 6							//'GetTabButtonIndex'
        &callFunction
        &pushone
        &pushsdbgv 7							//'client'
        &dcallmp 14							// OnSubTabClicked()
        &push r:1        
        &pushone
        &dcallfp 9							// SelectTabButton()
      &end // of function OnClicked

      &function2 OnRollOver (r:1='buttonClip') ()
        &push r:1        
        &pushone
        &pushsdb 6							//'GetTabButtonIndex'
        &callFunction
        &pushone
        &pushsdbgv 7							//'client'
        &dcallmp 15							// OnSubTabRollOver()
      &end // of function OnRollOver

      &function2 OnRollOut (r:1='buttonClip') ()
        &push r:1        
        &pushone
        &pushsdb 6							//'GetTabButtonIndex'
        &callFunction
        &pushone
        &pushsdbgv 7							//'client'
        &dcallmp 16							// OnSubTabRollOut()
      &end // of function OnRollOut

      &function2 ShouldTabButtonBeVisible (r:3='tabButton') ()
        &pushzero
        &pushsdbgv 17							//'tabSlotWidth'
        &subtract
        &pushsdbgv 18							//'buttons'
        &pushsdbgm 19							//'_x'
        &pushsdbgv 20							//'buttonStageLeft'
        &subtract
        &subtract
        &setRegister r:2
        &pop
        &pushsdbgv 17							//'tabSlotWidth'
        &pushsdbgv 21							//'numVisibleTabs'
        &multiply
        &pushsdbgv 18							//'buttons'
        &pushsdbgm 19							//'_x'
        &pushsdbgv 20							//'buttonStageLeft'
        &subtract
        &subtract
        &setRegister r:1
        &pop
        &push r:3        
        &pushsdbgm 19							//'_x'
        &push r:2        
        &greaterThan
        &dup
        &not
        &jnz label10        
        &pop
        &push r:3        
        &pushsdbgm 19							//'_x'
        &push r:1        
        &lessThan
       label10:
        &return
      &end // of function ShouldTabButtonBeVisible

      &function2 UpdateTabButtonVisibility () ()
        &pushzero
        &setRegister r:1
        &pop
       label11:
        &push r:1        
        &pushsdbgv 0							//'tabButtons'
        &pushsdbgm 1							//'length'
        &lessThan
        &not
        &jnz label12        
        &pushsdbgv 0							//'tabButtons'
        &push r:1        
        &getMember
        &pushsdb 22							//'_visible'
        &pushsdbgv 0							//'tabButtons'
        &push r:1        
        &getMember
        &pushone
        &pushsdb 23							//'ShouldTabButtonBeVisible'
        &callFunction
        &setMember
        &push r:1        
        &increment
        &setRegister r:1
        &pop
        &jmp label11        
       label12:
      &end // of function UpdateTabButtonVisibility

      &function2 ScrollTo (r:1='index') ()
        &pushsdbgv 18							//'buttons'
        &pushsdb 19							//'_x'
        &pushsdbgv 20							//'buttonStageLeft'
        &push r:1        
        &pushsdbgv 17							//'tabSlotWidth'
        &multiply
        &subtract
        &setMember
        &pushsdb 24							//'tabScrollPos'
        &push r:1        
        &setVariable
        &pushzero
        &dcallfp 25							// UpdateTabButtonVisibility()
        &pushzero
        &pushsdb 26							//'CanScrollLeft'
        &callFunction
        &pushsdbgv 27							//'spinLeftButton'
        &pushbyte 2
        &dcallfp 28							// SetSpinnerButtonEnabled()
        &pushzero
        &pushsdb 29							//'CanScrollRight'
        &callFunction
        &pushsdbgv 30							//'spinRightButton'
        &pushbyte 2
        &dcallfp 28							// SetSpinnerButtonEnabled()
      &end // of function ScrollTo

      &function2 InsertTab (r:3='index', r:7='iconLabel', r:8='tabText') (r:1='this')
        &push r:3        
        &pushsdbgv 17							//'tabSlotWidth'
        &multiply
        &setRegister r:4
        &pop
        &pushsdbgv 31							//'nextTabButtonId'
        &pushsdb 31							//'nextTabButtonId'
        &pushsdbgv 31							//'nextTabButtonId'
        &increment
        &setVariable
        &setRegister r:6
        &pop
        &push r:6        
        &push r:6        
        &toString
        &pushsdb 32							//'TabButton'
        &pushbyte 3
        &pushsdbgv 18							//'buttons'
        &pushsdb 33							//'attachMovie'
        &callMethod
        &setRegister r:5
        &pop
        &push r:5        
        &pushsdb 19							//'_x'
        &push r:4        
        &setMember
        &push r:5        
        &pushsdb 22							//'_visible'
        &push r:5        
        &pushone
        &pushsdb 23							//'ShouldTabButtonBeVisible'
        &callFunction
        &setMember
        &push r:5        
        &pushsdb 34							//'iconLabel'
        &push r:7        
        &setMember
        &push r:5        
        &pushsdb 35							//'text'
        &push r:8        
        &setMember
        &push r:5        
        &pushsdb 7							//'client'
        &push r:1        
        &setMember
        &push r:5        
        &pushzero
        &push r:3        
        &pushbyte 3
        &pushsdbgv 0							//'tabButtons'
        &dcallmp 36							// splice()
       label13:
        &pushfalse
        &jnz label15        
        &push r:3        
        &increment
        &setRegister r:3
        &pop
        &push r:3        
        &pushsdbgv 0							//'tabButtons'
        &pushsdbgm 1							//'length'
        &lessThan
        &not
        &not
        &jnz label14        
        &jmp label15        
       label14:
        &push r:4        
        &pushsdbgv 17							//'tabSlotWidth'
        &add
        &setRegister r:4
        &pop
        &pushsdbgv 0							//'tabButtons'
        &push r:3        
        &getMember
        &setRegister r:2
        &pop
        &push r:2        
        &pushsdb 19							//'_x'
        &push r:4        
        &setMember
        &push r:2        
        &pushsdb 22							//'_visible'
        &push r:2        
        &pushone
        &pushsdb 23							//'ShouldTabButtonBeVisible'
        &callFunction
        &setMember
        &jmp label13        
       label15:
        &pushzero
        &pushsdb 29							//'CanScrollRight'
        &callFunction
        &pushsdbgv 30							//'spinRightButton'
        &pushbyte 2
        &dcallfp 28							// SetSpinnerButtonEnabled()
      &end // of function InsertTab

      &function2 EraseTab (r:2='index') ()
        &pushsdbgv 0							//'tabButtons'
        &push r:2        
        &getMember
        &setRegister r:5
        &pop
        &push r:5        
        &pushsdbgm 19							//'_x'
        &setRegister r:3
        &pop
        &pushsdbgv 2							//'selectedTabButton'
        &push r:5        
        &equals
        &not
        &jnz label16        
        &pushundef
        &pushone
        &dcallfp 9							// SelectTabButton()
       label16:
        &pushzero
        &push r:5        
        &dcallmp 37							// removeMovieClip()
        &pushone
        &push r:2        
        &pushbyte 2
        &pushsdbgv 0							//'tabButtons'
        &dcallmp 36							// splice()
        &push r:2        
        &pushsdbgv 0							//'tabButtons'
        &pushsdbgm 1							//'length'
        &lessThan
        &not
        &jnz label19        
       label17:
        &pushfalse
        &jnz label19        
        &pushsdbgv 0							//'tabButtons'
        &push r:2        
        &getMember
        &setRegister r:1
        &pop
        &push r:1        
        &pushsdb 19							//'_x'
        &push r:3        
        &setMember
        &push r:1        
        &pushsdb 22							//'_visible'
        &push r:1        
        &pushone
        &pushsdb 23							//'ShouldTabButtonBeVisible'
        &callFunction
        &setMember
        &push r:2        
        &increment
        &setRegister r:2
        &pop
        &push r:2        
        &pushsdbgv 0							//'tabButtons'
        &pushsdbgm 1							//'length'
        &lessThan
        &not
        &not
        &jnz label18        
        &jmp label19        
       label18:
        &push r:3        
        &pushsdbgv 17							//'tabSlotWidth'
        &add
        &setRegister r:3
        &pop
        &jmp label17        
       label19:
        &pushsdbgv 0							//'tabButtons'
        &pushsdbgm 1							//'length'
        &pushzero
        &equals
        &not
        &jnz label20        
        &pushsdb 31							//'nextTabButtonId'
        &pushzerosv
       label20:
        &pushsdbgv 24							//'tabScrollPos'
        &setRegister r:4
        &pop
        &push r:4        
        &pushsdbgv 0							//'tabButtons'
        &pushsdbgm 1							//'length'
        &pushsdbgv 21							//'numVisibleTabs'
        &subtract
        &greaterThan
        &not
        &jnz label21        
        &pushsdbgv 0							//'tabButtons'
        &pushsdbgm 1							//'length'
        &pushsdbgv 21							//'numVisibleTabs'
        &subtract
        &setRegister r:4
        &pop
       label21:
        &push r:4        
        &pushzero
        &lessThan
        &not
        &jnz label22        
        &pushzero
        &setRegister r:4
        &pop
       label22:
        &push r:4        
        &pushsdbgv 24							//'tabScrollPos'
        &equals
        &not
        &not
        &jnz label23        
        &push r:4        
        &pushone
        &dcallfp 38							// ScrollTo()
       label23:
      &end // of function EraseTab

      &function CanScrollLeft (      )      
        &pushsdbgv 24							//'tabScrollPos'
        &pushzero
        &greaterThan
        &return
      &end // of function CanScrollLeft

      &function CanScrollRight (      )      
        &pushsdbgv 24							//'tabScrollPos'
        &pushsdbgv 0							//'tabButtons'
        &pushsdbgm 1							//'length'
        &pushsdbgv 21							//'numVisibleTabs'
        &subtract
        &lessThan
        &return
      &end // of function CanScrollRight

      &function2 SetSpinnerButtonEnabled (r:1='buttonClip', r:2='enable') ()
        &push r:1        
        &pushsdbgm 39							//'initialized'
        &not
        &jnz label24        
        &push r:2        
        &pushone
        &push r:1        
        &dcallmp 40							// SetEnabled()
        &jmp label25        
       label24:
        &push r:1        
        &pushsdb 41							//'isEnabled'
        &push r:2        
        &setMember
       label25:
      &end // of function SetSpinnerButtonEnabled

      &function2 OnSpinnerButtonClicked (r:1='buttonClip') ()
        &push r:1        
        &pushsdbgv 27							//'spinLeftButton'
        &equals
        &not
        &jnz label27        
        &pushzero
        &pushsdb 26							//'CanScrollLeft'
        &callFunction
        &not
        &jnz label26        
        &pushsdbgv 24							//'tabScrollPos'
        &pushone
        &subtract
        &pushone
        &dcallfp 38							// ScrollTo()
       label26:
        &jmp label28        
       label27:
        &pushzero
        &pushsdb 29							//'CanScrollRight'
        &callFunction
        &not
        &jnz label28        
        &pushsdbgv 24							//'tabScrollPos'
        &pushone
        &add
        &pushone
        &dcallfp 38							// ScrollTo()
       label28:
      &end // of function OnSpinnerButtonClicked

      &function2 MakeTabVisible (r:1='index') ()
        &push r:1        
        &pushsdbgv 24							//'tabScrollPos'
        &lessThan
        &not
        &jnz label29        
        &push r:1        
        &pushone
        &dcallfp 38							// ScrollTo()
        &jmp label30        
       label29:
        &push r:1        
        &pushsdbgv 24							//'tabScrollPos'
        &pushsdbgv 21							//'numVisibleTabs'
        &add
        &lessThan
        &not
        &not
        &jnz label30        
        &push r:1        
        &pushsdbgv 21							//'numVisibleTabs'
        &subtract
        &pushone
        &add
        &pushone
        &dcallfp 38							// ScrollTo()
       label30:
      &end // of function MakeTabVisible

      &function onUnload (      )      
        &pushsdb 6							//'GetTabButtonIndex'
        &delete2
        &pop
        &pushsdb 9							//'SelectTabButton'
        &delete2
        &pop
        &pushsdb 42							//'SelectTab'
        &delete2
        &pop
        &pushsdb 43							//'SetTabFlashing'
        &delete2
        &pop
        &pushsdb 44							//'GetSelectedTabNum'
        &delete2
        &pop
        &pushsdb 45							//'OnPressed'
        &delete2
        &pop
        &pushsdb 46							//'OnClicked'
        &delete2
        &pop
        &pushsdb 47							//'OnRollOver'
        &delete2
        &pop
        &pushsdb 48							//'OnRollOut'
        &delete2
        &pop
        &pushsdb 23							//'ShouldTabButtonBeVisible'
        &delete2
        &pop
        &pushsdb 25							//'UpdateTabButtonVisibility'
        &delete2
        &pop
        &pushsdb 38							//'ScrollTo'
        &delete2
        &pop
        &pushsdb 49							//'InsertTab'
        &delete2
        &pop
        &pushsdb 50							//'EraseTab'
        &delete2
        &pop
        &pushsdb 26							//'CanScrollLeft'
        &delete2
        &pop
        &pushsdb 29							//'CanScrollRight'
        &delete2
        &pop
        &pushsdb 28							//'SetSpinnerButtonEnabled'
        &delete2
        &pop
        &pushsdb 51							//'OnSpinnerButtonClicked'
        &delete2
        &pop
        &pushsdb 52							//'MakeTabVisible'
        &delete2
        &pop
        &pushsdb 53							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 39							//'initialized'
      &not
      &not
      &jnz label33      
      &pushsdbgv 54							//'extern'
      &pushsdbgm 55							//'InGame'
      &not
      &not
      &jnz label31      
      &pushsdbgv 56							//'_root'
      &pushsdb 57							//'GetCurrentFaction'
      &function  (      )      
        &pushsdb 58							//'Alien'
        &return
      &end // of function 

      &setMember
     label31:
      &pushsdb 17							//'tabSlotWidth'
      &pushbyte 31
      &setVariable
      &pushsdb 21							//'numVisibleTabs'
      &pushbyte 5
      &setVariable
      &pushsdb 20							//'buttonStageLeft'
      &pushsdbgv 18							//'buttons'
      &pushsdbgm 19							//'_x'
      &setVariable
      &pushsdb 24							//'tabScrollPos'
      &pushzerosv
      &pushsdbgv 7							//'client'
      &pushundef
      &equals
      &not
      &jnz label32      
      &pushsdb 7							//'client'
      &pushsdbgv 59							//'_parent'
      &setVariable
     label32:
      &pushsdb 0							//'tabButtons'
      &pushzero
      &pushsdb 60							//'Array'
      &new
      &setVariable
      &pushsdb 31							//'nextTabButtonId'
      &pushzerosv
      &pushfalse
      &pushsdbgv 27							//'spinLeftButton'
      &pushbyte 2
      &dcallfp 28							// SetSpinnerButtonEnabled()
      &pushfalse
      &pushsdbgv 30							//'spinRightButton'
      &pushbyte 2
      &dcallfp 28							// SetSpinnerButtonEnabled()
      &pushsdb 39							//'initialized'
      &pushtrue
      &setVariable
      &pushthisgv
      &pushone
      &pushsdbgv 7							//'client'
      &dcallmp 62							// OnSubTabsInitialized()
     label33:
    &end // of frame 0
  &end // of defineMovieClip 132
&end
