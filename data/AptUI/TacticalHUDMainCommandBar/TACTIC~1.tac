movie 'E:\Projects\CNC3\Data\APTBUI~1\034A3~1.0-D\pc\Output\TA143F~1\\TACTIC~1.eaf' &compressed // flash 7, total frames: 1, frame rate: 30 fps, 1024x768 px

  &frame 0
    &constants 'sel', 'pages', 'length', 'clip', '_name', 'tabs', 'SelectPage', 'SetPageHighlighted', 'visiblePageNum', '_visible', 'FSCommand:', ':OnSelectionRefinementPageSelected', '', ':OnBuildQueueTypePageSelected', ':OnSelectionRefinementTabClicked', ':OnBuildQueueTypeTabClicked', 'OnTabRollOver', 'OnTabRollOut', 'tabsInitialized', 'SelectTab', 'selectedTabNum', 'tabFlashing', 'SetTabFlashing', 'GetSelectedTabNum', 'tabButton', 'tabIcon', 'tabHelpSite', 'GetSelectionRefinementPage', 'GetBuildQueueTypePage', 'GetBuildQueueTypeTab', 'SelectSelectionRefinementPage', 'SelectBuildQueueTypePage', 'SetBuildQueueTypePageHighlighted', 'OnTabSelected', 'OnTabsInitialized', 'OnChildLoaded', 'onUnload', 'initialized', 'aircraft', 'Air', 'vehicles', 'Veh', 'infantry', 'Inf', 'otherStructure', 'Def', 'mainStructure', 'Str', 'Con', 'TacticalHUDSelectionRefinementPage.swf', 'loadMovie', 'TacticalHUDBuildQueuePage.swf', 'this', ':OnInitialized'  
    &function GetSelectionRefinementPage (    )    
      &pushsdbgv 0							//'sel'
      &toString
      &return
    &end // of function GetSelectionRefinementPage

    &function2 GetBuildQueueTypePage (r:2='pageName') (r:1='this')
      &push r:1      
      &push r:2      
      &getMember
      &toString
      &return
    &end // of function GetBuildQueueTypePage

    &function2 GetBuildQueueTypeTab (r:3='pageNameArg') ()
      &push r:3      
      &toString
      &setRegister r:2
      &pop
      &pushzero
      &setRegister r:1
      &pop
     label1:
      &push r:1      
      &pushsdbgv 1							//'pages'
      &pushsdbgm 2							//'length'
      &lessThan
      &not
      &jnz label3      
      &pushsdbgv 1							//'pages'
      &push r:1      
      &getMember
      &pushsdbgm 3							//'clip'
      &pushsdbgm 4							//'_name'
      &push r:2      
      &equals
      &not
      &jnz label2      
      &pushsdbgv 5							//'tabs'
      &push r:1      
      &toString
      &getMember
      &toString
      &return
     label2:
      &push r:1      
      &increment
      &setRegister r:1
      &pop
      &jmp label1      
     label3:
      &pushundef
      &return
    &end // of function GetBuildQueueTypeTab

    &function SelectSelectionRefinementPage (    )    
      &pushsdbgv 0							//'sel'
      &pushone
      &dcallfp 6							// SelectPage()
    &end // of function SelectSelectionRefinementPage

    &function2 SelectBuildQueueTypePage (r:2='pageName') (r:1='this')
      &push r:1      
      &push r:2      
      &getMember
      &pushone
      &dcallfp 6							// SelectPage()
    &end // of function SelectBuildQueueTypePage

    &function2 SetBuildQueueTypePageHighlighted (r:3='pageNameArg', r:2='highlightedArg') (r:1='this')
      &push r:2      
      &toNumber
      &pushzero
      &equals
      &not
      &push r:1      
      &push r:3      
      &toString
      &getMember
      &pushbyte 2
      &dcallfp 7							// SetPageHighlighted()
    &end // of function SetBuildQueueTypePageHighlighted

    &function2 OnTabSelected (r:3='tabNum') (r:1='this')
      &push r:3      
      &pushsdbgv 8							//'visiblePageNum'
      &equals
      &not
      &not
      &jnz label5      
      &pushsdbgv 1							//'pages'
      &pushsdbgv 8							//'visiblePageNum'
      &getMember
      &pushsdbgm 3							//'clip'
      &pushsdb 9							//'_visible'
      &pushfalse
      &setMember
      &pushsdbgv 1							//'pages'
      &push r:3      
      &getMember
      &pushsdbgm 3							//'clip'
      &setRegister r:2
      &pop
      &push r:2      
      &pushsdb 9							//'_visible'
      &pushtrue
      &setMember
      &pushsdb 8							//'visiblePageNum'
      &push r:3      
      &setVariable
      &push r:2      
      &pushsdbgv 0							//'sel'
      &equals
      &not
      &jnz label4      
      &pushsdb 10							//'FSCommand:'
      &push r:1      
      &toString
      &pushsdb 11							//':OnSelectionRefinementPageSelected'
      &add
      &concat
      &pushsdb 12							//''
      &getURL2
      &jmp label5      
     label4:
      &pushsdb 10							//'FSCommand:'
      &push r:1      
      &toString
      &pushsdb 13							//':OnBuildQueueTypePageSelected'
      &add
      &concat
      &push r:2      
      &pushsdbgm 4							//'_name'
      &getURL2
     label5:
    &end // of function OnTabSelected

    &function2 OnSelectedTabClicked (r:3='tabNum') (r:1='this')
      &pushsdbgv 1							//'pages'
      &push r:3      
      &getMember
      &pushsdbgm 3							//'clip'
      &setRegister r:2
      &pop
      &push r:2      
      &pushsdbgv 0							//'sel'
      &equals
      &not
      &jnz label6      
      &pushsdb 10							//'FSCommand:'
      &push r:1      
      &toString
      &pushsdb 14							//':OnSelectionRefinementTabClicked'
      &add
      &concat
      &pushsdb 12							//''
      &getURL2
      &jmp label7      
     label6:
      &pushsdb 10							//'FSCommand:'
      &push r:1      
      &toString
      &pushsdb 15							//':OnBuildQueueTypeTabClicked'
      &add
      &concat
      &push r:2      
      &pushsdbgm 4							//'_name'
      &getURL2
     label7:
    &end // of function OnSelectedTabClicked

    &function2 OnTabRollOver (r:1='tabNum') ()
      &pushzero
      &pushsdbgv 1							//'pages'
      &push r:1      
      &getMember
      &pushsdbgm 3							//'clip'
      &dcallmp 16							// OnTabRollOver()
    &end // of function OnTabRollOver

    &function2 OnTabRollOut (r:1='tabNum') ()
      &pushzero
      &pushsdbgv 1							//'pages'
      &push r:1      
      &getMember
      &pushsdbgm 3							//'clip'
      &dcallmp 17							// OnTabRollOut()
    &end // of function OnTabRollOut

    &function2 SelectTab (r:1='tabNum') ()
      &pushsdbgv 18							//'tabsInitialized'
      &not
      &jnz label8      
      &push r:1      
      &pushone
      &pushsdbgv 5							//'tabs'
      &dcallmp 19							// SelectTab()
      &jmp label9      
     label8:
      &pushsdb 20							//'selectedTabNum'
      &push r:1      
      &setVariable
     label9:
    &end // of function SelectTab

    &function2 SelectPage (r:2='pageClip') ()
      &pushzero
      &setRegister r:1
      &pop
     label10:
      &push r:1      
      &pushsdbgv 1							//'pages'
      &pushsdbgm 2							//'length'
      &lessThan
      &not
      &jnz label12      
      &pushsdbgv 1							//'pages'
      &push r:1      
      &getMember
      &pushsdbgm 3							//'clip'
      &push r:2      
      &equals
      &not
      &jnz label11      
      &push r:1      
      &pushone
      &dcallfp 19							// SelectTab()
      &jmp label12      
     label11:
      &push r:1      
      &increment
      &setRegister r:1
      &pop
      &jmp label10      
     label12:
    &end // of function SelectPage

    &function2 SetPageHighlighted (r:3='pageClip', r:2='highlighted') ()
      &pushzero
      &setRegister r:1
      &pop
     label13:
      &push r:1      
      &pushsdbgv 1							//'pages'
      &pushsdbgm 2							//'length'
      &lessThan
      &not
      &jnz label16      
      &pushsdbgv 1							//'pages'
      &push r:1      
      &getMember
      &pushsdbgm 3							//'clip'
      &push r:3      
      &equals
      &not
      &jnz label15      
      &pushsdbgv 1							//'pages'
      &push r:1      
      &getMember
      &pushsdb 21							//'tabFlashing'
      &push r:2      
      &setMember
      &pushsdbgv 18							//'tabsInitialized'
      &not
      &jnz label14      
      &push r:2      
      &push r:1      
      &pushbyte 2
      &pushsdbgv 5							//'tabs'
      &dcallmp 22							// SetTabFlashing()
     label14:
      &jmp label16      
     label15:
      &push r:1      
      &increment
      &setRegister r:1
      &pop
      &jmp label13      
     label16:
    &end // of function SetPageHighlighted

    &function2 OnTabsInitialized ('clip') ()
      &pushsdbgv 18							//'tabsInitialized'
      &not
      &not
      &jnz label20      
      &pushsdb 18							//'tabsInitialized'
      &pushtrue
      &setVariable
      &pushsdb 8							//'visiblePageNum'
      &pushzero
      &pushsdbgv 5							//'tabs'
      &pushsdb 23							//'GetSelectedTabNum'
      &callMethod
      &toString
      &setVariable
      &pushsdbgv 1							//'pages'
      &pushsdbgv 8							//'visiblePageNum'
      &getMember
      &pushsdbgm 3							//'clip'
      &pushsdb 9							//'_visible'
      &pushtrue
      &setMember
      &pushsdbgv 20							//'selectedTabNum'
      &pushundef
      &equals
      &not
      &not
      &jnz label17      
      &pushsdbgv 20							//'selectedTabNum'
      &pushone
      &pushsdbgv 5							//'tabs'
      &dcallmp 19							// SelectTab()
      &pushsdb 20							//'selectedTabNum'
      &delete2
      &pop
     label17:
      &pushzero
      &setRegister r:1
      &pop
     label18:
      &push r:1      
      &pushsdbgv 1							//'pages'
      &pushsdbgm 2							//'length'
      &lessThan
      &not
      &jnz label20      
      &pushsdbgv 1							//'pages'
      &push r:1      
      &getMember
      &pushsdbgm 21							//'tabFlashing'
      &not
      &jnz label19      
      &pushtrue
      &push r:1      
      &pushbyte 2
      &pushsdbgv 5							//'tabs'
      &dcallmp 22							// SetTabFlashing()
     label19:
      &push r:1      
      &increment
      &setRegister r:1
      &pop
      &jmp label18      
     label20:
    &end // of function OnTabsInitialized

    &function2 OnChildLoaded (r:2='childClip') ()
      &pushfalse
      &setRegister r:3
      &pop
      &pushsdbgv 8							//'visiblePageNum'
      &pushundef
      &equals
      &not
      &not
      &jnz label21      
      &push r:2      
      &pushsdbgv 1							//'pages'
      &pushsdbgv 8							//'visiblePageNum'
      &getMember
      &pushsdbgm 3							//'clip'
      &equals
      &setRegister r:3
      &pop
     label21:
      &push r:2      
      &pushsdb 9							//'_visible'
      &push r:3      
      &setMember
      &pushzero
      &setRegister r:1
      &pop
     label22:
      &push r:1      
      &pushsdbgv 1							//'pages'
      &pushsdbgm 2							//'length'
      &lessThan
      &not
      &jnz label24      
      &pushsdbgv 1							//'pages'
      &push r:1      
      &getMember
      &pushsdbgm 3							//'clip'
      &push r:2      
      &equals
      &not
      &jnz label23      
      &push r:2      
      &pushsdb 24							//'tabButton'
      &pushsdbgv 5							//'tabs'
      &push r:1      
      &toString
      &getMember
      &setMember
      &push r:2      
      &pushsdb 25							//'tabIcon'
      &pushsdbgv 1							//'pages'
      &push r:1      
      &getMember
      &pushsdbgm 25							//'tabIcon'
      &setMember
      &jmp label24      
     label23:
      &push r:1      
      &increment
      &setRegister r:1
      &pop
      &jmp label22      
     label24:
      &push r:2      
      &pushsdb 26							//'tabHelpSite'
      &pushsdbgv 26							//'tabHelpSite'
      &setMember
    &end // of function OnChildLoaded

    &function onUnload (    )    
      &pushsdb 27							//'GetSelectionRefinementPage'
      &delete2
      &pop
      &pushsdb 28							//'GetBuildQueueTypePage'
      &delete2
      &pop
      &pushsdb 29							//'GetBuildQueueTypeTab'
      &delete2
      &pop
      &pushsdb 30							//'SelectSelectionRefinementPage'
      &delete2
      &pop
      &pushsdb 31							//'SelectBuildQueueTypePage'
      &delete2
      &pop
      &pushsdb 32							//'SetBuildQueueTypePageHighlighted'
      &delete2
      &pop
      &pushsdb 33							//'OnTabSelected'
      &delete2
      &pop
      &pushsdb 16							//'OnTabRollOver'
      &delete2
      &pop
      &pushsdb 17							//'OnTabRollOut'
      &delete2
      &pop
      &pushsdb 19							//'SelectTab'
      &delete2
      &pop
      &pushsdb 6							//'SelectPage'
      &delete2
      &pop
      &pushsdb 7							//'SetPageHighlighted'
      &delete2
      &pop
      &pushsdb 34							//'OnTabsInitialized'
      &delete2
      &pop
      &pushsdb 35							//'OnChildLoaded'
      &delete2
      &pop
      &pushsdb 36							//'onUnload'
      &delete2
      &pop
    &end // of function onUnload

    &pushsdbgv 37							//'initialized'
    &not
    &not
    &jnz label26    
    &pushsdb 1							//'pages'
    &pushsdb 3							//'clip'
    &pushsdbgv 38							//'aircraft'
    &pushsdb 25							//'tabIcon'
    &pushsdb 39							//'Air'
    &pushsdb 21							//'tabFlashing'
    &pushfalse
    &pushbyte 3
    &initObject
    &pushsdb 3							//'clip'
    &pushsdbgv 40							//'vehicles'
    &pushsdb 25							//'tabIcon'
    &pushsdb 41							//'Veh'
    &pushsdb 21							//'tabFlashing'
    &pushfalse
    &pushbyte 3
    &initObject
    &pushsdb 3							//'clip'
    &pushsdbgv 42							//'infantry'
    &pushsdb 25							//'tabIcon'
    &pushsdb 43							//'Inf'
    &pushsdb 21							//'tabFlashing'
    &pushfalse
    &pushbyte 3
    &initObject
    &pushsdb 3							//'clip'
    &pushsdbgv 44							//'otherStructure'
    &pushsdb 25							//'tabIcon'
    &pushsdb 45							//'Def'
    &pushsdb 21							//'tabFlashing'
    &pushfalse
    &pushbyte 3
    &initObject
    &pushsdb 3							//'clip'
    &pushsdbgv 46							//'mainStructure'
    &pushsdb 25							//'tabIcon'
    &pushsdb 47							//'Str'
    &pushsdb 21							//'tabFlashing'
    &pushfalse
    &pushbyte 3
    &initObject
    &pushsdb 3							//'clip'
    &pushsdbgv 0							//'sel'
    &pushsdb 25							//'tabIcon'
    &pushsdb 48							//'Con'
    &pushsdb 21							//'tabFlashing'
    &pushfalse
    &pushbyte 3
    &initObject
    &pushbyte 6
    &initArray
    &setVariable
    &pushsdbgv 18							//'tabsInitialized'
    &not
    &jnz label25    
    &pushsdb 8							//'visiblePageNum'
    &pushzero
    &pushsdbgv 5							//'tabs'
    &pushsdb 23							//'GetSelectedTabNum'
    &callMethod
    &toString
    &setVariable
    &pushsdbgv 1							//'pages'
    &pushsdbgv 8							//'visiblePageNum'
    &getMember
    &pushsdbgm 3							//'clip'
    &pushsdb 9							//'_visible'
    &pushtrue
    &setMember
   label25:
    &pushsdb 49							//'TacticalHUDSelectionRefinementPage.swf'
    &pushone
    &pushsdbgv 0							//'sel'
    &dcallmp 50							// loadMovie()
    &pushsdb 51							//'TacticalHUDBuildQueuePage.swf'
    &pushone
    &pushsdbgv 46							//'mainStructure'
    &dcallmp 50							// loadMovie()
    &pushsdb 51							//'TacticalHUDBuildQueuePage.swf'
    &pushone
    &pushsdbgv 44							//'otherStructure'
    &dcallmp 50							// loadMovie()
    &pushsdb 51							//'TacticalHUDBuildQueuePage.swf'
    &pushone
    &pushsdbgv 42							//'infantry'
    &dcallmp 50							// loadMovie()
    &pushsdb 51							//'TacticalHUDBuildQueuePage.swf'
    &pushone
    &pushsdbgv 40							//'vehicles'
    &dcallmp 50							// loadMovie()
    &pushsdb 51							//'TacticalHUDBuildQueuePage.swf'
    &pushone
    &pushsdbgv 38							//'aircraft'
    &dcallmp 50							// loadMovie()
    &pushsdb 37							//'initialized'
    &pushtrue
    &setVariable
    &pushsdb 10							//'FSCommand:'
    &pushthisgv
    &toString
    &pushsdb 53							//':OnInitialized'
    &add
    &concat
    &pushsdb 12							//''
    &getURL2
   label26:
    &stop
  &end // of frame 0

  &defineMovieClip 1 // total frames: 1
  &end // of defineMovieClip 1

  &placeMovieClip 1 &as 'aircraft'
  
    &onClipEvent &load
      &pushs ''
      &pushbyte 7
      &pushfalse
      &setProperty
    &end
  &end // of placeMovieClip 1

  &placeMovieClip 1 &as 'vehicles'
  
    &onClipEvent &load
      &pushs ''
      &pushbyte 7
      &pushfalse
      &setProperty
    &end
  &end // of placeMovieClip 1

  &placeMovieClip 1 &as 'infantry'
  
    &onClipEvent &load
      &pushs ''
      &pushbyte 7
      &pushfalse
      &setProperty
    &end
  &end // of placeMovieClip 1

  &placeMovieClip 1 &as 'otherStructure'
  
    &onClipEvent &load
      &pushs ''
      &pushbyte 7
      &pushfalse
      &setProperty
    &end
  &end // of placeMovieClip 1

  &placeMovieClip 1 &as 'mainStructure'
  
    &onClipEvent &load
      &pushs ''
      &pushbyte 7
      &pushfalse
      &setProperty
    &end
  &end // of placeMovieClip 1

  &placeMovieClip 1 &as 'sel'
  
    &onClipEvent &load
      &pushs ''
      &pushbyte 7
      &pushfalse
      &setProperty
    &end
  &end // of placeMovieClip 1
  
  &importAssets &from 'HelpBox.swf'
    'HelpBoxSite' &as 4
  &end // of importAssets

  &placeMovieClip 4 &as 'tabHelpSite'
  
    &onClipEvent &construct
      &pushs 'vertAlignment'
      &pushssv 'top'
      &pushs 'horzAlignment'
      &pushssv 'right'
    &end
  &end // of placeMovieClip 4

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

  &defineMovieClip 18 // total frames: 30

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
  &end // of defineMovieClip 18

  &defineMovieClip 25 // total frames: 30

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
  &end // of defineMovieClip 25

  &defineMovieClip 32 // total frames: 30

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
  &end // of defineMovieClip 32

  &defineMovieClip 39 // total frames: 30

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
  &end // of defineMovieClip 39

  &defineMovieClip 46 // total frames: 30

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
  &end // of defineMovieClip 46

  &defineMovieClip 47 // total frames: 30

    &frame 0
      &pushs '_'
      &pushsgv '_parent'
      &pushsgm '_name'
      &add
      &gotoAndStop    &end // of frame 0
  &end // of defineMovieClip 47

  &defineMovieClip 51 // total frames: 1
  &end // of defineMovieClip 51

  &defineMovieClip 54 // total frames: 1
  &end // of defineMovieClip 54

  &defineMovieClip 57 // total frames: 1
  &end // of defineMovieClip 57

  &defineMovieClip 60 // total frames: 1
  &end // of defineMovieClip 60

  &defineMovieClip 61 // total frames: 46

    &frame 0
      &stop
    &end // of frame 0

    &frame 9
      &play
    &end // of frame 9

    &frame 40
      &gotoLabel '_on'
      &play
    &end // of frame 40
  &end // of defineMovieClip 61

  &defineButton 63
  
    &on     &overUpToOverDown
      &constants '_parent', 'selectedTabNum', '_name', '_down', 'gotoAndPlay'  
      &pushsdbgv 0							//'_parent'
      &pushsdbgm 0							//'_parent'
      &pushsdbgm 1							//'selectedTabNum'
      &pushsdbgv 0							//'_parent'
      &pushsdbgm 2							//'_name'
      &toNumber
      &equals
      &not
      &not
      &jnz label1      
      &pushsdb 3							//'_down'
      &pushone
      &pushsdbgv 0							//'_parent'
      &dcallmp 4							// gotoAndPlay()
     label1:
    &end
  
    &on     &overDownToOverUp
      &constants '_parent', 'selectedTabNum', '_name', '_over', 'gotoAndPlay', 'client', 'OnClicked'  
      &pushsdbgv 0							//'_parent'
      &pushsdbgm 0							//'_parent'
      &pushsdbgm 1							//'selectedTabNum'
      &pushsdbgv 0							//'_parent'
      &pushsdbgm 2							//'_name'
      &toNumber
      &equals
      &not
      &not
      &jnz label1      
      &pushsdb 3							//'_over'
      &pushone
      &pushsdbgv 0							//'_parent'
      &dcallmp 4							// gotoAndPlay()
     label1:
      &pushsdbgv 0							//'_parent'
      &pushone
      &pushsdbgv 0							//'_parent'
      &pushsdbgm 5							//'client'
      &dcallmp 6							// OnClicked()
    &end
  
    &on     &idleToOverUp    ,&outDownToOverDown    ,&idleToOverDown
      &constants '_parent', 'selectedTabNum', '_name', '_over', 'gotoAndPlay', 'client', 'OnRollOver'  
      &pushsdbgv 0							//'_parent'
      &pushsdbgm 0							//'_parent'
      &pushsdbgm 1							//'selectedTabNum'
      &pushsdbgv 0							//'_parent'
      &pushsdbgm 2							//'_name'
      &toNumber
      &equals
      &not
      &not
      &jnz label1      
      &pushsdb 3							//'_over'
      &pushone
      &pushsdbgv 0							//'_parent'
      &dcallmp 4							// gotoAndPlay()
     label1:
      &pushsdbgv 0							//'_parent'
      &pushone
      &pushsdbgv 0							//'_parent'
      &pushsdbgm 5							//'client'
      &dcallmp 6							// OnRollOver()
    &end
  
    &on     &overUpToIdle    ,&overDownToOutDown    ,&overDownToIdle
      &constants '_parent', 'selectedTabNum', '_name', '_up', 'gotoAndPlay', 'client', 'OnRollOut'  
      &pushsdbgv 0							//'_parent'
      &pushsdbgm 0							//'_parent'
      &pushsdbgm 1							//'selectedTabNum'
      &pushsdbgv 0							//'_parent'
      &pushsdbgm 2							//'_name'
      &toNumber
      &equals
      &not
      &not
      &jnz label1      
      &pushsdb 3							//'_up'
      &pushone
      &pushsdbgv 0							//'_parent'
      &dcallmp 4							// gotoAndPlay()
     label1:
      &pushsdbgv 0							//'_parent'
      &pushone
      &pushsdbgv 0							//'_parent'
      &pushsdbgm 5							//'client'
      &dcallmp 6							// OnRollOut()
    &end
  &end // of defineButton 63

  &defineMovieClip 65 // total frames: 1
  &end // of defineMovieClip 65

  &defineMovieClip 72 // total frames: 30

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
  &end // of defineMovieClip 72

  &defineMovieClip 79 // total frames: 30

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
  &end // of defineMovieClip 79

  &defineMovieClip 86 // total frames: 30

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
  &end // of defineMovieClip 86

  &defineMovieClip 93 // total frames: 30

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
  &end // of defineMovieClip 93

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

  &defineMovieClip 107 // total frames: 30

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
  &end // of defineMovieClip 107

  &defineMovieClip 108 // total frames: 30

    &frame 0
      &pushs '_'
      &pushsgv '_parent'
      &pushsgm 'iconLabel'
      &add
      &gotoAndStop    &end // of frame 0
  &end // of defineMovieClip 108

  &defineMovieClip 115 // total frames: 30

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
  &end // of defineMovieClip 115

  &defineMovieClip 122 // total frames: 30

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
  &end // of defineMovieClip 122

  &defineMovieClip 123 // total frames: 30

    &frame 0
      &pushs '_'
      &pushsgv '_parent'
      &pushsgm '_name'
      &add
      &gotoAndStop    &end // of frame 0
  &end // of defineMovieClip 123

  &defineMovieClip 130 // total frames: 30

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
  &end // of defineMovieClip 130

  &defineMovieClip 137 // total frames: 30

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
  &end // of defineMovieClip 137

  &defineMovieClip 144 // total frames: 30

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
  &end // of defineMovieClip 144

  &defineMovieClip 151 // total frames: 30

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
  &end // of defineMovieClip 151

  &defineMovieClip 158 // total frames: 30

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
  &end // of defineMovieClip 158

  &defineMovieClip 165 // total frames: 30

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
  &end // of defineMovieClip 165

  &defineMovieClip 166 // total frames: 30

    &frame 0
      &pushs '_'
      &pushsgv '_parent'
      &pushsgm 'iconLabel'
      &add
      &gotoAndStop    &end // of frame 0
  &end // of defineMovieClip 166

  &defineMovieClip 167 // total frames: 50

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

    &placeMovieClip 65 &as 'ButtonContact'
    
      &onClipEvent &load
        &pushsgv '_parent'
        &pushsgm '_name'
        &pushs '0'
        &equals
        &not
        &jnz label1        
        &pushs ''
        &pushbyte 8
        &pushbyte 34
        &setProperty
       label1:
      &end
    &end // of placeMovieClip 65

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29

    &frame 39
      &stop
    &end // of frame 39

    &frame 49
      &stop
    &end // of frame 49
  &end // of defineMovieClip 167

  &defineMovieClip 170 // total frames: 1
  &end // of defineMovieClip 170

  &defineMovieClip 171 // total frames: 20

    &frame 19
      &stop
    &end // of frame 19
  &end // of defineMovieClip 171

  &defineMovieClip 172 // total frames: 60

    &frame 0
      &stop
    &end // of frame 0
  &end // of defineMovieClip 172

  &defineMovieClip 173 // total frames: 1

    &frame 0
      &constants 'selectedTabNum', '_up', 'gotoAndPlay', '_selected', 'client', 'OnTabSelected', '_name', 'SelectTab', '_', 'TabButtonGlow', 'gotoAndStop', 'OnSelectedTabClicked', 'OnTabRollOver', 'OnTabRollOut', '_off', '_on', 'flashClip', 'GetSelectedTabNum', 'OnClicked', 'OnRollOver', 'OnRollOut', 'SetTabFlashing', 'onUnload', 'initialized', 'i', '_parent', 'pages', 'length', 'this', 'iconLabel', 'tabIcon', '0', 'OnTabsInitialized'  
      &function2 SelectTab (r:2='tabNum') (r:1='this')
        &push r:2        
        &pushsdbgv 0							//'selectedTabNum'
        &equals
        &not
        &not
        &jnz label1        
        &pushsdb 1							//'_up'
        &pushone
        &push r:1        
        &pushsdbgv 0							//'selectedTabNum'
        &toString
        &getMember
        &dcallmp 2							// gotoAndPlay()
        &pushsdb 3							//'_selected'
        &pushone
        &push r:1        
        &push r:2        
        &toString
        &getMember
        &dcallmp 2							// gotoAndPlay()
        &pushsdb 0							//'selectedTabNum'
        &push r:2        
        &setVariable
        &pushsdbgv 0							//'selectedTabNum'
        &pushone
        &pushsdbgv 4							//'client'
        &dcallmp 5							// OnTabSelected()
       label1:
      &end // of function SelectTab

      &function GetSelectedTabNum (      )      
        &pushsdbgv 0							//'selectedTabNum'
        &return
      &end // of function GetSelectedTabNum

      &function2 OnClicked (r:2='buttonClip') ()
        &push r:2        
        &pushsdbgm 6							//'_name'
        &toNumber
        &setRegister r:1
        &pop
        &push r:1        
        &pushsdbgv 0							//'selectedTabNum'
        &equals
        &not
        &not
        &jnz label2        
        &push r:1        
        &pushone
        &dcallfp 7							// SelectTab()
        &pushsdb 8							//'_'
        &push r:2        
        &pushsdbgm 6							//'_name'
        &add
        &pushone
        &pushsdbgv 9							//'TabButtonGlow'
        &dcallmp 10							// gotoAndStop()
        &jmp label3        
       label2:
        &push r:1        
        &pushone
        &pushsdbgv 4							//'client'
        &dcallmp 11							// OnSelectedTabClicked()
       label3:
      &end // of function OnClicked

      &function2 OnRollOver (r:1='buttonClip') ()
        &push r:1        
        &pushsdbgm 6							//'_name'
        &toNumber
        &pushone
        &pushsdbgv 4							//'client'
        &dcallmp 12							// OnTabRollOver()
      &end // of function OnRollOver

      &function2 OnRollOut (r:1='buttonClip') ()
        &push r:1        
        &pushsdbgm 6							//'_name'
        &toNumber
        &pushone
        &pushsdbgv 4							//'client'
        &dcallmp 13							// OnTabRollOut()
      &end // of function OnRollOut

      &function2 SetTabFlashing (r:3='tabNum', r:4='flashing') (r:1='this')
        &push r:1        
        &push r:3        
        &toString
        &getMember
        &setRegister r:2
        &pop
        &push r:4        
        &jnz label4        
        &pushsdb 14							//'_off'
        &jmp label5        
       label4:
        &pushsdb 15							//'_on'
       label5:
        &pushone
        &push r:2        
        &pushsdbgm 16							//'flashClip'
        &dcallmp 2							// gotoAndPlay()
      &end // of function SetTabFlashing

      &function onUnload (      )      
        &pushsdb 7							//'SelectTab'
        &delete2
        &pop
        &pushsdb 17							//'GetSelectedTabNum'
        &delete2
        &pop
        &pushsdb 18							//'OnClicked'
        &delete2
        &pop
        &pushsdb 19							//'OnRollOver'
        &delete2
        &pop
        &pushsdb 20							//'OnRollOut'
        &delete2
        &pop
        &pushsdb 21							//'SetTabFlashing'
        &delete2
        &pop
        &pushsdb 22							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 23							//'initialized'
      &not
      &not
      &jnz label9      
      &pushsdb 24							//'i'
      &pushzero
      &varEquals
     label6:
      &pushsdbgv 24							//'i'
      &pushsdbgv 25							//'_parent'
      &pushsdbgm 26							//'pages'
      &pushsdbgm 27							//'length'
      &lessThan
      &not
      &jnz label7      
      &pushthisgv
      &pushsdbgv 24							//'i'
      &toString
      &getMember
      &pushsdb 29							//'iconLabel'
      &pushsdbgv 25							//'_parent'
      &pushsdbgm 26							//'pages'
      &pushsdbgv 24							//'i'
      &getMember
      &pushsdbgm 30							//'tabIcon'
      &setMember
      &pushsdb 24							//'i'
      &pushsdbgv 24							//'i'
      &increment
      &setVariable
      &jmp label6      
     label7:
      &pushsdbgv 4							//'client'
      &pushundef
      &equals
      &not
      &jnz label8      
      &pushsdb 4							//'client'
      &pushsdbgv 25							//'_parent'
      &setVariable
     label8:
      &pushsdb 0							//'selectedTabNum'
      &pushzerosv
      &pushsdb 3							//'_selected'
      &pushone
      &pushthisgv
      &pushsdbgm 31							//'0'
      &dcallmp 2							// gotoAndPlay()
      &pushsdb 23							//'initialized'
      &pushtrue
      &setVariable
      &pushthisgv
      &pushone
      &pushsdbgv 4							//'client'
      &dcallmp 32							// OnTabsInitialized()
     label9:
    &end // of frame 0
  &end // of defineMovieClip 173
&end
