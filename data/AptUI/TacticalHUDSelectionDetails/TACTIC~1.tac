movie 'E:\Projects\CNC3\Data\APTBUI~1\034A3~1.0-D\pc\Output\TA4C39~1\\TACTIC~1.eaf' &compressed // flash 7, total frames: 40, frame rate: 30 fps, 1024x768 px

  &defineMovieClip 5 // total frames: 20

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19
  &end // of defineMovieClip 5
  
  &exportAssets
    5 &as 'AmmoPip'
  &end // of exportAssets

  &frame 0
    &constants 'abilities', 'stage', 'unitCategory', 'unitCategoryInd', 'gotoAndPlay', 'weaponCategory', 'weaponCategoryInd', 'rank', 'Math', 'max', 'min', 'rankFactionLabel', 'rankInd', 'factionLabel', '_', 'image', 'healthPct', 'healthBar', 'gotoAndStop', '.upgrades', 'portraitHelpSite', 'ammoCapacity', 'ammoLoad', 'ammoDisplay', 'initialized', 'SetCapacity', 'SetLoad', 'GetAbilityButtonStage', 'SetState', 'SetUnitCategory', 'SetWeaponCategory', 'SetRank', 'SetHealth', 'GetUpgradeIconList', 'GetPortraitHelpSite', 'SetLargeBarVisibility', 'SetAmmo', 'onUnload', '_hide', 'FSCommand:', 'this', ':OnInitialized', '', 'extern', 'InGame', '_infantry', '_gun', 'SetUnitHealth'  
    &function2 GetAbilityButtonStage (r:1='index') ()
      &pushsdbgv 0							//'abilities'
      &push r:1      
      &toString
      &getMember
      &pushsdbgm 1							//'stage'
      &toString
      &return
    &end // of function GetAbilityButtonStage

    &function2 SetState (r:1='state') ()
      &push r:1      
      &gotoAndPlay    &end // of function SetState

    &function2 SetUnitCategory (r:1='arg') ()
      &pushsdb 2							//'unitCategory'
      &push r:1      
      &setVariable
      &pushsdbgv 2							//'unitCategory'
      &pushone
      &pushsdbgv 3							//'unitCategoryInd'
      &dcallmp 4							// gotoAndPlay()
    &end // of function SetUnitCategory

    &function2 SetWeaponCategory (r:1='arg') ()
      &pushsdb 5							//'weaponCategory'
      &push r:1      
      &setVariable
      &pushsdbgv 5							//'weaponCategory'
      &pushone
      &pushsdbgv 6							//'weaponCategoryInd'
      &dcallmp 4							// gotoAndPlay()
    &end // of function SetWeaponCategory

    &function2 SetRank (r:2='rankArg', r:1='factionArg') ()
      &pushsdb 7							//'rank'
      &pushbyte 4
      &pushone
      &push r:2      
      &toNumber
      &pushbyte 2
      &pushsdbgv 8							//'Math'
      &pushsdb 9							//'max'
      &callMethod
      &pushbyte 2
      &pushsdbgv 8							//'Math'
      &dcallmsv 10							// min()
      &pushsdb 11							//'rankFactionLabel'
      &push r:1      
      &toString
      &setVariable
      &pushsdbgv 12							//'rankInd'
      &pushsdb 13							//'factionLabel'
      &push r:1      
      &toString
      &setMember
      &pushsdb 14							//'_'
      &pushsdbgv 7							//'rank'
      &toString
      &add
      &pushone
      &pushsdbgv 12							//'rankInd'
      &dcallmp 4							// gotoAndPlay()
      &pushsdbgv 12							//'rankInd'
      &pushsdbgm 13							//'factionLabel'
      &pushone
      &pushsdbgv 12							//'rankInd'
      &pushsdbgm 15							//'image'
      &dcallmp 4							// gotoAndPlay()
    &end // of function SetRank

    &function2 SetHealth (r:4='curHealthArg', r:3='maxHealthArg') ()
      &push r:3      
      &toNumber
      &setRegister r:1
      &pop
      &push r:1      
      &pushzero
      &equals
      &not
      &not
      &jnz label1      
      &pushsdb 16							//'healthPct'
      &push r:4      
      &toNumber
      &push r:3      
      &toNumber
      &divide
      &pushbyte 100
      &multiply
      &setVariable
      &jmp label2      
     label1:
      &pushsdb 16							//'healthPct'
      &pushzerosv
     label2:
      &pushsdbgv 16							//'healthPct'
      &pushone
      &add
      &setRegister r:2
      &pop
      &push r:2      
      &pushone
      &pushsdbgv 17							//'healthBar'
      &dcallmp 18							// gotoAndStop()
    &end // of function SetHealth

    &function2 GetUpgradeIconList () (r:1='this')
      &push r:1      
      &toString
      &pushsdb 19							//'.upgrades'
      &add
      &return
    &end // of function GetUpgradeIconList

    &function GetPortraitHelpSite (    )    
      &pushsdbgv 20							//'portraitHelpSite'
      &toString
      &return
    &end // of function GetPortraitHelpSite

    &function2 SetAmmo (r:4='newAmmoCapacityArg', r:3='newAmmoLoadArg') ()
      &push r:4      
      &toNumber
      &setRegister r:1
      &pop
      &push r:3      
      &toNumber
      &setRegister r:2
      &pop
      &push r:1      
      &pushsdbgv 21							//'ammoCapacity'
      &equals
      &not
      &dup
      &jnz label3      
      &pop
      &push r:2      
      &pushsdbgv 22							//'ammoLoad'
      &equals
      &not
     label3:
      &not
      &jnz label5      
      &pushsdb 21							//'ammoCapacity'
      &push r:1      
      &setVariable
      &pushsdb 22							//'ammoLoad'
      &push r:2      
      &setVariable
      &pushsdbgv 23							//'ammoDisplay'
      &pushundef
      &equals
      &not
      &dup
      &not
      &jnz label4      
      &pop
      &pushsdbgv 23							//'ammoDisplay'
      &pushsdbgm 24							//'initialized'
     label4:
      &not
      &jnz label5      
      &push r:1      
      &pushone
      &pushsdbgv 23							//'ammoDisplay'
      &dcallmp 25							// SetCapacity()
      &push r:2      
      &pushone
      &pushsdbgv 23							//'ammoDisplay'
      &dcallmp 26							// SetLoad()
     label5:
    &end // of function SetAmmo

    &function onUnload (    )    
      &pushsdb 27							//'GetAbilityButtonStage'
      &delete2
      &pop
      &pushsdb 28							//'SetState'
      &delete2
      &pop
      &pushsdb 29							//'SetUnitCategory'
      &delete2
      &pop
      &pushsdb 30							//'SetWeaponCategory'
      &delete2
      &pop
      &pushsdb 31							//'SetRank'
      &delete2
      &pop
      &pushsdb 32							//'SetHealth'
      &delete2
      &pop
      &pushsdb 33							//'GetUpgradeIconList'
      &delete2
      &pop
      &pushsdb 34							//'GetPortraitHelpSite'
      &delete2
      &pop
      &pushsdb 35							//'SetLargeBarVisibility'
      &delete2
      &pop
      &pushsdb 36							//'SetAmmo'
      &delete2
      &pop
      &pushsdb 37							//'onUnload'
      &delete2
      &pop
    &end // of function onUnload

    &pushsdbgv 24							//'initialized'
    &not
    &not
    &jnz label6    
    &pushsdb 2							//'unitCategory'
    &pushsdb 38							//'_hide'
    &setVariable
    &pushsdb 5							//'weaponCategory'
    &pushsdb 38							//'_hide'
    &setVariable
    &pushsdb 7							//'rank'
    &pushone
    &setVariable
    &pushsdb 16							//'healthPct'
    &pushbyte 100
    &setVariable
    &pushsdb 21							//'ammoCapacity'
    &pushzerosv
    &pushsdb 22							//'ammoLoad'
    &pushzerosv
    &pushsdb 24							//'initialized'
    &pushtrue
    &setVariable
    &pushsdb 39							//'FSCommand:'
    &pushthisgv
    &toString
    &pushsdb 41							//':OnInitialized'
    &add
    &concat
    &pushsdb 42							//''
    &getURL2
    &pushsdbgv 43							//'extern'
    &pushsdbgm 44							//'InGame'
    &not
    &not
    &jnz label6    
    &gotoLabel '_singleUnit'
    &play
    &pushsdb 45							//'_infantry'
    &pushone
    &dcallfp 29							// SetUnitCategory()
    &pushsdb 46							//'_gun'
    &pushone
    &dcallfp 30							// SetWeaponCategory()
    &pushbyte 70
    &pushbyte 50
    &pushbyte 2
    &dcallfp 47							// SetUnitHealth()
    &pushbyte 5
    &pushzero
    &pushbyte 2
    &dcallfp 36							// SetAmmo()
    &pushsdb 16							//'healthPct'
    &pushbyte 100
    &random
    &setVariable
   label6:
  &end // of frame 0
  
  &importAssets &from 'HelpBox.swf'
    'HelpBoxSite' &as 6
  &end // of importAssets

  &placeMovieClip 6 &as 'portraitHelpSite'
  
    &onClipEvent &construct
      &pushs 'vertAlignment'
      &pushssv 'top'
      &pushs 'horzAlignment'
      &pushssv 'right'
    &end
  &end // of placeMovieClip 6
  
  &importAssets &from 'libHUD.swf'
    'WhiteRectangle' &as 7
  &end // of importAssets
  
  &importAssets &from 'libHUD.swf'
    'LoadMovieStage' &as 8
  &end // of importAssets

  &defineMovieClip 9 // total frames: 1

    &placeMovieClip 7 
    
      &onClipEvent &load
        &pushs ''
        &pushbyte 7
        &pushfalse
        &setProperty
      &end
    &end // of placeMovieClip 7
  &end // of defineMovieClip 9

  &defineMovieClip 10 // total frames: 1

    &frame 0
      &constants 'initialized', 'i', 'this', 'stage', 'helpSite'  
      &pushsdbgv 0							//'initialized'
      &not
      &not
      &jnz label3      
      &pushsdb 1							//'i'
      &pushzero
      &varEquals
     label1:
      &pushsdbgv 1							//'i'
      &pushbyte 6
      &lessThan
      &not
      &jnz label2      
      &pushthisgv
      &pushsdbgv 1							//'i'
      &toString
      &getMember
      &pushsdbgm 3							//'stage'
      &pushsdb 4							//'helpSite'
      &pushthisgv
      &pushsdb 4							//'helpSite'
      &pushsdbgv 1							//'i'
      &toString
      &add
      &getMember
      &setMember
      &pushsdb 1							//'i'
      &pushsdbgv 1							//'i'
      &increment
      &setVariable
      &jmp label1      
     label2:
      &pushsdb 0							//'initialized'
      &pushtrue
      &setVariable
     label3:
      &stop
    &end // of frame 0

    &placeMovieClip 6 &as 'helpSite0'
    
      &onClipEvent &construct
        &pushs 'vertAlignment'
        &pushssv 'bottom'
        &pushs 'horzAlignment'
        &pushssv 'right'
      &end
    &end // of placeMovieClip 6

    &placeMovieClip 6 &as 'helpSite1'
    
      &onClipEvent &construct
        &pushs 'vertAlignment'
        &pushssv 'bottom'
        &pushs 'horzAlignment'
        &pushssv 'right'
      &end
    &end // of placeMovieClip 6

    &placeMovieClip 6 &as 'helpSite2'
    
      &onClipEvent &construct
        &pushs 'vertAlignment'
        &pushssv 'bottom'
        &pushs 'horzAlignment'
        &pushssv 'right'
      &end
    &end // of placeMovieClip 6

    &placeMovieClip 6 &as 'helpSite3'
    
      &onClipEvent &construct
        &pushs 'vertAlignment'
        &pushssv 'bottom'
        &pushs 'horzAlignment'
        &pushssv 'right'
      &end
    &end // of placeMovieClip 6

    &placeMovieClip 6 &as 'helpSite4'
    
      &onClipEvent &construct
        &pushs 'vertAlignment'
        &pushssv 'bottom'
        &pushs 'horzAlignment'
        &pushssv 'right'
      &end
    &end // of placeMovieClip 6

    &placeMovieClip 6 &as 'helpSite5'
    
      &onClipEvent &construct
        &pushs 'vertAlignment'
        &pushssv 'bottom'
        &pushs 'horzAlignment'
        &pushssv 'right'
      &end
    &end // of placeMovieClip 6
  &end // of defineMovieClip 10

  &frame 9
    &stop
  &end // of frame 9

  &defineMovieClip 19 // total frames: 30

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
  &end // of defineMovieClip 19

  &defineMovieClip 22 // total frames: 1
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

  &defineMovieClip 81 // total frames: 41

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
  &end // of defineMovieClip 81

  &defineMovieClip 82 // total frames: 75

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
  &end // of defineMovieClip 82

  &defineMovieClip 89 // total frames: 30

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
  &end // of defineMovieClip 89

  &defineMovieClip 92 // total frames: 1
  &end // of defineMovieClip 92

  &defineMovieClip 95 // total frames: 101

    &frame 0
      &stop
    &end // of frame 0

    &placeMovieClip 92 
    
      &onClipEvent &load
        &pushs ''
        &pushbyte 7
        &pushfalse
        &setProperty
      &end
    &end // of placeMovieClip 92
  &end // of defineMovieClip 95

  &placeMovieClip 95 &as 'healthBar'
  
    &onClipEvent &load
      &constants '_parent', 'healthPct', 'vFrame', 'this', 'gotoAndStop'  
      &pushsdbgv 0							//'_parent'
      &pushsdbgm 1							//'healthPct'
      &pushundef
      &equals
      &not
      &not
      &jnz label1      
      &pushsdb 2							//'vFrame'
      &pushsdbgv 0							//'_parent'
      &pushsdbgm 1							//'healthPct'
      &pushone
      &add
      &varEquals
      &pushsdbgv 2							//'vFrame'
      &pushone
      &pushthisgv
      &dcallmp 4							// gotoAndStop()
     label1:
    &end
  &end // of placeMovieClip 95

  &defineMovieClip 98 // total frames: 1
  &end // of defineMovieClip 98

  &placeMovieClip 98 
  
    &onClipEvent &load
      &pushs 'unitNameText'
      &pushs '$'
      &pushsgv '_parent'
      &toString
      &add
      &pushs ':UnitName&dropshadow'
      &add
      &setVariable
    &end
  &end // of placeMovieClip 98

  &defineButton 99
  
    &on     &idleToOverUp
      &pushs 'FSCommand:'
      &pushsgv '_parent'
      &toString
      &pushs ':OnPortraitRollOver'
      &add
      &concat
      &pushs ''
      &getURL2
    &end
  
    &on     &overUpToIdle
      &pushs 'FSCommand:'
      &pushsgv '_parent'
      &toString
      &pushs ':OnPortraitRollOut'
      &add
      &concat
      &pushs ''
      &getURL2
    &end
  &end // of defineButton 99
  
  &importAssets &from 'libHUD.swf'
    'RenderImage' &as 100
  &end // of importAssets

  &defineMovieClip 101 // total frames: 1

    &placeMovieClip 100 &as 'image'
    
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
        &constants '_imageMap', '_parent', ':Portrait'  
        &pushsdb 0							//'_imageMap'
        &pushsdbgv 1							//'_parent'
        &pushsdbgm 1							//'_parent'
        &toString
        &pushsdb 2							//':Portrait'
        &add
        &setVariable
      &end
    &end // of placeMovieClip 100
  &end // of defineMovieClip 101

  &defineMovieClip 102 // total frames: 1

    &frame 0
      &constants 'currentCapacity', '_x', '_width', 'AmmoPip', 'attachMovie', '_y', 'currentLoad', '_empty', '_filled', 'gotoAndPlay', 'removeMovieClip', 'Math', 'min', 'SetCapacity', 'SetLoad', 'onUnload', 'initialized', '_parent', 'ammoCapacity', 'ammoLoad'  
      &function2 SetCapacity (r:5='ammoCapacity') (r:1='this')
        &push r:5        
        &pushsdbgv 0							//'currentCapacity'
        &greaterThan
        &not
        &jnz label7        
        &pushundef
        &setRegister r:6
        &pop
        &pushsdbgv 0							//'currentCapacity'
        &pushzero
        &greaterThan
        &not
        &jnz label1        
        &push r:1        
        &pushsdbgv 0							//'currentCapacity'
        &pushone
        &subtract
        &toString
        &getMember
        &setRegister r:7
        &pop
        &push r:7        
        &pushsdbgm 1							//'_x'
        &push r:7        
        &pushsdbgm 2							//'_width'
        &add
        &setRegister r:6
        &pop
        &jmp label2        
       label1:
        &pushzero
        &setRegister r:6
        &pop
       label2:
        &pushsdbgv 0							//'currentCapacity'
        &setRegister r:3
        &pop
       label3:
        &push r:3        
        &push r:5        
        &lessThan
        &not
        &jnz label6        
        &push r:3        
        &push r:3        
        &toString
        &pushsdb 3							//'AmmoPip'
        &pushbyte 3
        &push r:1        
        &pushsdb 4							//'attachMovie'
        &callMethod
        &setRegister r:2
        &pop
        &push r:2        
        &pushsdb 1							//'_x'
        &push r:6        
        &setMember
        &push r:2        
        &pushsdb 5							//'_y'
        &pushzero
        &setMember
        &push r:3        
        &pushsdbgv 6							//'currentLoad'
        &lessThan
        &jnz label4        
        &pushsdb 7							//'_empty'
        &jmp label5        
       label4:
        &pushsdb 8							//'_filled'
       label5:
        &pushone
        &push r:2        
        &dcallmp 9							// gotoAndPlay()
        &push r:6        
        &push r:2        
        &pushsdbgm 2							//'_width'
        &add
        &setRegister r:6
        &pop
        &push r:3        
        &increment
        &setRegister r:3
        &pop
        &jmp label3        
       label6:
        &jmp label9        
       label7:
        &push r:5        
        &pushsdbgv 0							//'currentCapacity'
        &lessThan
        &not
        &jnz label9        
        &pushsdbgv 0							//'currentCapacity'
        &setRegister r:3
        &pop
       label8:
        &push r:3        
        &decrement
        &setRegister r:3
        &pop
        &push r:1        
        &push r:3        
        &toString
        &getMember
        &setRegister r:4
        &pop
        &pushzero
        &push r:4        
        &dcallmp 10							// removeMovieClip()
        &push r:3        
        &push r:5        
        &greaterThan
        &jnz label8        
       label9:
        &pushsdb 0							//'currentCapacity'
        &push r:5        
        &setVariable
      &end // of function SetCapacity

      &function2 SetLoad (r:4='ammoLoad') (r:1='this')
        &push r:4        
        &pushsdbgv 6							//'currentLoad'
        &greaterThan
        &not
        &jnz label12        
        &pushsdbgv 6							//'currentLoad'
        &pushsdbgv 0							//'currentCapacity'
        &lessThan
        &not
        &jnz label11        
        &pushsdbgv 0							//'currentCapacity'
        &push r:4        
        &pushbyte 2
        &pushsdbgv 11							//'Math'
        &pushsdb 12							//'min'
        &callMethod
        &setRegister r:5
        &pop
        &pushsdbgv 6							//'currentLoad'
        &setRegister r:2
        &pop
       label10:
        &push r:2        
        &push r:5        
        &lessThan
        &not
        &jnz label11        
        &push r:1        
        &push r:2        
        &toString
        &getMember
        &setRegister r:3
        &pop
        &pushsdb 8							//'_filled'
        &pushone
        &push r:3        
        &dcallmp 9							// gotoAndPlay()
        &push r:2        
        &increment
        &setRegister r:2
        &pop
        &jmp label10        
       label11:
        &jmp label14        
       label12:
        &push r:4        
        &pushsdbgv 6							//'currentLoad'
        &lessThan
        &not
        &jnz label14        
        &push r:4        
        &pushsdbgv 0							//'currentCapacity'
        &lessThan
        &not
        &jnz label14        
        &pushsdbgv 0							//'currentCapacity'
        &pushsdbgv 6							//'currentLoad'
        &pushbyte 2
        &pushsdbgv 11							//'Math'
        &pushsdb 12							//'min'
        &callMethod
        &setRegister r:5
        &pop
        &push r:4        
        &setRegister r:2
        &pop
       label13:
        &push r:2        
        &push r:5        
        &lessThan
        &not
        &jnz label14        
        &push r:1        
        &push r:2        
        &toString
        &getMember
        &setRegister r:3
        &pop
        &pushsdb 7							//'_empty'
        &pushone
        &push r:3        
        &dcallmp 9							// gotoAndPlay()
        &push r:2        
        &increment
        &setRegister r:2
        &pop
        &jmp label13        
       label14:
        &pushsdb 6							//'currentLoad'
        &push r:4        
        &setVariable
      &end // of function SetLoad

      &function onUnload (      )      
        &pushsdb 13							//'SetCapacity'
        &delete2
        &pop
        &pushsdb 14							//'SetLoad'
        &delete2
        &pop
        &pushsdb 15							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 16							//'initialized'
      &not
      &not
      &jnz label17      
      &pushsdb 0							//'currentCapacity'
      &pushzerosv
      &pushsdb 6							//'currentLoad'
      &pushzerosv
      &pushsdbgv 17							//'_parent'
      &pushsdbgm 18							//'ammoCapacity'
      &pushzero
      &equals
      &not
      &not
      &jnz label15      
      &pushsdbgv 17							//'_parent'
      &pushsdbgm 18							//'ammoCapacity'
      &pushone
      &dcallfp 13							// SetCapacity()
     label15:
      &pushsdbgv 17							//'_parent'
      &pushsdbgm 19							//'ammoLoad'
      &pushzero
      &equals
      &not
      &not
      &jnz label16      
      &pushsdbgv 17							//'_parent'
      &pushsdbgm 19							//'ammoLoad'
      &pushone
      &dcallfp 14							// SetLoad()
     label16:
      &pushsdb 16							//'initialized'
      &pushtrue
      &setVariable
     label17:
    &end // of frame 0
  &end // of defineMovieClip 102

  &defineMovieClip 105 // total frames: 1

    &frame 0
      &pushs ''
      &pushbyte 7
      &pushfalse
      &setProperty
    &end // of frame 0
  &end // of defineMovieClip 105

  &defineMovieClip 108 // total frames: 1
  &end // of defineMovieClip 108

  &defineMovieClip 113 // total frames: 30

    &frame 0
      &pushsgv '_parent'
      &pushsgm 'factionLabel'
      &gotoAndPlay    &end // of frame 0

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

  &defineMovieClip 118 // total frames: 30

    &frame 0
      &pushsgv '_parent'
      &pushsgm 'factionLabel'
      &gotoAndPlay    &end // of frame 0

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 118

  &defineMovieClip 123 // total frames: 30

    &frame 0
      &pushsgv '_parent'
      &pushsgm 'factionLabel'
      &gotoAndPlay    &end // of frame 0

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

  &defineMovieClip 124 // total frames: 40

    &frame 0
      &constants 'factionLabel', 'image', 'gotoAndPlay', 'SetFaction', 'onUnload', 'initialized', 'GDI'  
      &function2 SetFaction (r:1='faction') ()
        &pushsdb 0							//'factionLabel'
        &push r:1        
        &setVariable
        &pushsdbgv 0							//'factionLabel'
        &pushone
        &pushsdbgv 1							//'image'
        &dcallmp 2							// gotoAndPlay()
      &end // of function SetFaction

      &function onUnload (      )      
        &pushsdb 3							//'SetFaction'
        &delete2
        &pop
        &pushsdb 4							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 5							//'initialized'
      &not
      &not
      &jnz label2      
      &pushsdbgv 0							//'factionLabel'
      &pushundef
      &equals
      &not
      &jnz label1      
      &pushsdb 0							//'factionLabel'
      &pushsdb 6							//'GDI'
      &setVariable
     label1:
      &pushsdb 5							//'initialized'
      &pushtrue
      &setVariable
     label2:
    &end // of frame 0

    &frame 9
      &stop
    &end // of frame 9

    &placeMovieClip 113 &as 'image'
    
      &onClipEvent &load
        &pushsgv '_parent'
        &pushsgm 'factionLabel'
        &gotoAndPlay      &end
    &end // of placeMovieClip 113

    &frame 19
      &stop
    &end // of frame 19

    &placeMovieClip 118 &as 'image'
    
      &onClipEvent &load
        &pushsgv '_parent'
        &pushsgm 'factionLabel'
        &gotoAndPlay      &end
    &end // of placeMovieClip 118

    &frame 29
      &stop
    &end // of frame 29

    &placeMovieClip 123 &as 'image'
    
      &onClipEvent &load
        &pushsgv '_parent'
        &pushsgm 'factionLabel'
        &gotoAndPlay      &end
    &end // of placeMovieClip 123

    &frame 39
      &stop
    &end // of frame 39
  &end // of defineMovieClip 124

  &placeMovieClip 124 &as 'rankInd'
  
    &onClipEvent &load
      &constants 'labelText', '$', '_parent', ':RankLabel', 'rankFactionLabel', 'factionLabel', 'rank', '_'  
      &pushsdb 0							//'labelText'
      &pushsdb 1							//'$'
      &pushsdbgv 2							//'_parent'
      &toString
      &add
      &pushsdb 3							//':RankLabel'
      &add
      &setVariable
      &pushsdbgv 2							//'_parent'
      &pushsdbgm 4							//'rankFactionLabel'
      &pushundef
      &equals
      &not
      &not
      &jnz label1      
      &pushsdb 5							//'factionLabel'
      &pushsdbgv 2							//'_parent'
      &pushsdbgm 4							//'rankFactionLabel'
      &setVariable
     label1:
      &pushsdbgv 2							//'_parent'
      &pushsdbgm 6							//'rank'
      &pushundef
      &equals
      &not
      &not
      &jnz label2      
      &pushsdb 7							//'_'
      &pushsdbgv 2							//'_parent'
      &pushsdbgm 6							//'rank'
      &toString
      &add
      &gotoAndPlay     label2:
    &end
  &end // of placeMovieClip 124

  &defineButton 125
  
    &on     &idleToOverUp
      &pushs 'FSCommand:'
      &pushsgv '_parent'
      &toString
      &pushs ':OnIconRollOver'
      &add
      &concat
      &pushs ''
      &pushbyte 13
      &getProperty
      &getURL2
    &end
  
    &on     &overUpToIdle
      &pushs 'FSCommand:'
      &pushsgv '_parent'
      &toString
      &pushs ':OnIconRollOut'
      &add
      &concat
      &pushs ''
      &pushbyte 13
      &getProperty
      &getURL2
    &end
  &end // of defineButton 125
  
  &importAssets &from 'libHUD.swf'
    'RenderImageDisabled' &as 126
  &end // of importAssets

  &defineMovieClip 127 // total frames: 20

    &frame 0
      &constants 'initialized', '_parent', 'iconState', '', 'highlighted'  
      &pushsdbgv 0							//'initialized'
      &not
      &not
      &jnz label2      
      &pushsdbgv 1							//'_parent'
      &pushsdbgm 2							//'iconState'
      &pushsdb 3							//''
      &pushbyte 13
      &getProperty
      &toNumber
      &getMember
      &pushsdbgm 4							//'highlighted'
      &not
      &jnz label1      
      &gotoLabel '_on'
      &play
     label1:
      &pushsdb 0							//'initialized'
      &pushtrue
      &setVariable
     label2:
    &end // of frame 0

    &placeMovieClip 126 &as 'offImage'
    
      &onClipEvent &construct
        &pushs '_type'
        &pushssv 'RenderImageDisabled'
        &pushs '_imageMap'
        &pushssv ''
      &end
    
      &onClipEvent &load
        &constants '_imageMap', '_parent', ':Image', '_name'  
        &pushsdb 0							//'_imageMap'
        &pushsdbgv 1							//'_parent'
        &pushsdbgm 1							//'_parent'
        &toString
        &pushsdb 2							//':Image'
        &add
        &pushsdbgv 1							//'_parent'
        &pushsdbgm 3							//'_name'
        &add
        &setVariable
      &end
    &end // of placeMovieClip 126

    &frame 9
      &stop
    &end // of frame 9

    &placeMovieClip 100 &as 'image'
    
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
        &constants '_imageMap', '_parent', ':Image', '_name', 'colorizer', 'this', 'Color', 'imageTint', 'setRGB'  
        &pushsdb 0							//'_imageMap'
        &pushsdbgv 1							//'_parent'
        &pushsdbgm 1							//'_parent'
        &toString
        &pushsdb 2							//':Image'
        &add
        &pushsdbgv 1							//'_parent'
        &pushsdbgm 3							//'_name'
        &add
        &setVariable
        &pushsdb 4							//'colorizer'
        &pushthisgv
        &pushone
        &pushsdb 6							//'Color'
        &new
        &setVariable
        &pushsdbgv 1							//'_parent'
        &pushsdbgm 1							//'_parent'
        &pushsdbgm 7							//'imageTint'
        &pushundef
        &equals
        &not
        &not
        &jnz label1        
        &pushsdbgv 1							//'_parent'
        &pushsdbgm 1							//'_parent'
        &pushsdbgm 7							//'imageTint'
        &pushone
        &pushsdbgv 4							//'colorizer'
        &dcallmp 8							// setRGB()
       label1:
      &end
    &end // of placeMovieClip 100

    &frame 19
      &stop
    &end // of frame 19
  &end // of defineMovieClip 127

  &defineMovieClip 128 // total frames: 30

    &frame 0
      &constants 'iconState', 'length', 'highlighted', 'push', 'pop', '_', '_off', '_on', 'gotoAndPlay', 'imageTint', 'image', 'colorizer', 'setRGB', 'SetIconCount', 'SetIconHighlighted', 'SetIconImageTint', 'onUnload', 'initialized', 'Array', 'FSCommand:', 'this', ':OnInitialized', '', 'extern', 'InGame'  
      &function2 SetIconCount (r:3='countArg') ()
        &push r:3        
        &toNumber
        &setRegister r:1
        &pop
        &push r:1        
        &pushsdbgv 0							//'iconState'
        &pushsdbgm 1							//'length'
        &equals
        &not
        &jnz label1        
        &pushundef
        &return
       label1:
        &pushsdbgv 0							//'iconState'
        &pushsdbgm 1							//'length'
        &push r:1        
        &lessThan
        &not
        &jnz label3        
       label2:
        &pushsdb 2							//'highlighted'
        &pushfalse
        &pushone
        &initObject
        &pushone
        &pushsdbgv 0							//'iconState'
        &dcallmp 3							// push()
        &pushsdbgv 0							//'iconState'
        &pushsdbgm 1							//'length'
        &push r:1        
        &lessThan
        &jnz label2        
        &jmp label4        
       label3:
        &pushsdbgv 0							//'iconState'
        &pushsdbgm 1							//'length'
        &push r:1        
        &greaterThan
        &not
        &jnz label4        
        &pushzero
        &pushsdbgv 0							//'iconState'
        &dcallmp 4							// pop()
        &jmp label3        
       label4:
        &pushsdb 5							//'_'
        &push r:1        
        &toString
        &add
        &gotoAndPlay      &end // of function SetIconCount

      &function2 SetIconHighlighted (r:5='indexArg', r:4='highlightedArg') (r:1='this')
        &push r:5        
        &toNumber
        &setRegister r:2
        &pop
        &push r:4        
        &toNumber
        &pushzero
        &equals
        &not
        &setRegister r:3
        &pop
        &push r:3        
        &pushsdbgv 0							//'iconState'
        &push r:2        
        &getMember
        &pushsdbgm 2							//'highlighted'
        &equals
        &not
        &not
        &jnz label7        
        &push r:3        
        &jnz label5        
        &pushsdb 6							//'_off'
        &jmp label6        
       label5:
        &pushsdb 7							//'_on'
       label6:
        &pushone
        &push r:1        
        &push r:2        
        &toString
        &getMember
        &dcallmp 8							// gotoAndPlay()
        &pushsdbgv 0							//'iconState'
        &push r:2        
        &getMember
        &pushsdb 2							//'highlighted'
        &push r:3        
        &setMember
       label7:
      &end // of function SetIconHighlighted

      &function2 SetIconImageTint (r:5='colorArg') (r:1='this')
        &pushsdb 9							//'imageTint'
        &push r:5        
        &toNumber
        &setVariable
        &pushsdbgv 0							//'iconState'
        &pushsdbgm 1							//'length'
        &setRegister r:4
        &pop
        &pushzero
        &setRegister r:2
        &pop
       label8:
        &push r:2        
        &push r:4        
        &lessThan
        &not
        &jnz label9        
        &push r:1        
        &push r:2        
        &toString
        &getMember
        &setRegister r:3
        &pop
        &pushsdbgv 9							//'imageTint'
        &pushone
        &push r:3        
        &pushsdbgm 10							//'image'
        &pushsdbgm 11							//'colorizer'
        &dcallmp 12							// setRGB()
        &push r:2        
        &increment
        &setRegister r:2
        &pop
        &jmp label8        
       label9:
      &end // of function SetIconImageTint

      &function onUnload (      )      
        &pushsdb 13							//'SetIconCount'
        &delete2
        &pop
        &pushsdb 14							//'SetIconHighlighted'
        &delete2
        &pop
        &pushsdb 15							//'SetIconImageTint'
        &delete2
        &pop
        &pushsdb 16							//'onUnload'
        &delete2
        &pop
      &end // of function onUnload

      &pushsdbgv 17							//'initialized'
      &not
      &not
      &jnz label10      
      &pushsdb 9							//'imageTint'
      &pushlong 16777215
      &setVariable
      &pushsdb 0							//'iconState'
      &pushzero
      &pushsdb 18							//'Array'
      &new
      &setVariable
      &pushsdb 17							//'initialized'
      &pushtrue
      &setVariable
      &pushsdb 19							//'FSCommand:'
      &pushthisgv
      &toString
      &pushsdb 21							//':OnInitialized'
      &add
      &concat
      &pushsdb 22							//''
      &getURL2
      &pushsdbgv 23							//'extern'
      &pushsdbgm 24							//'InGame'
      &not
      &not
      &jnz label10      
      &pushbyte 2
      &pushone
      &dcallfp 13							// SetIconCount()
      &pushtrue
      &pushone
      &pushbyte 2
      &dcallfp 14							// SetIconHighlighted()
     label10:
    &end // of frame 0

    &placeMovieClip 6 &as 'helpSite'
    
      &onClipEvent &construct
        &pushs 'vertAlignment'
        &pushssv 'top'
        &pushs 'horzAlignment'
        &pushssv 'right'
      &end
    &end // of placeMovieClip 6

    &frame 9
      &stop
    &end // of frame 9

    &frame 19
      &stop
    &end // of frame 19

    &frame 29
      &stop
    &end // of frame 29
  &end // of defineMovieClip 128

  &placeMovieClip 128 &as 'upgrades'
  
    &onClipEvent &load
      &pushs 'labelText'
      &pushs '$'
      &pushsgv '_parent'
      &toString
      &add
      &pushs ':UpgradesLabel'
      &add
      &setVariable
    &end
  &end // of placeMovieClip 128

  &frame 19
    &stop
  &end // of frame 19

  &defineMovieClip 131 // total frames: 1
  &end // of defineMovieClip 131

  &placeMovieClip 131 
  
    &onClipEvent &load
      &pushs 'text'
      &pushs '$'
      &pushsgv '_parent'
      &toString
      &add
      &pushs ':UnitQuantity&dropshadow'
      &add
      &setVariable
    &end
  &end // of placeMovieClip 131

  &frame 29
    &stop
  &end // of frame 29

  &defineMovieClip 138 // total frames: 30

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
  &end // of defineMovieClip 138

  &frame 39
    &stop
  &end // of frame 39
&end
