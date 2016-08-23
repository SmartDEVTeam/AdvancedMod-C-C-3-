movie 'E:\Projects\CNC3\Data\APTBUI~1\034A3~1.0-D\pc\Output\MISSIO~2\\MISSIO~1.eaf' &compressed // flash 7, total frames: 1, frame rate: 30 fps, 1024x768 px
  
  &importAssets &from 'ShellContent.swf'
    'Guage_Simple' &as 2
  &end // of importAssets

  &defineMovieClip 7 // total frames: 1

    &frame 0
      &pushs 'vMissionName'
      &pushzero
      &pushsgv '_root'
      &pushsgm 'Campaign'
      &pushs 'GetCurrentMissionName'
      &callMethod
      &varEquals
    &end // of frame 0
  &end // of defineMovieClip 7

  &defineMovieClip 13 // total frames: 1
  &end // of defineMovieClip 13

  &defineMovieClip 18 // total frames: 1
  &end // of defineMovieClip 18

  &defineMovieClip 20 // total frames: 1
  &end // of defineMovieClip 20

  &defineMovieClip 21 // total frames: 1
  &end // of defineMovieClip 21

  &defineMovieClip 24 // total frames: 1
  &end // of defineMovieClip 24

  &defineMovieClip 26 // total frames: 1
  &end // of defineMovieClip 26
  
  &importAssets &from 'ShellButtons.swf'
    'ShellButtons Small' &as 27
  &end // of importAssets

  &placeMovieClip 27 &as 'Cancel'
  
    &onClipEvent &construct
      &pushs 'vStartMode'
      &pushssv ''
    &end
  &end // of placeMovieClip 27

  &placeMovieClip 27 &as 'Play'
  
    &onClipEvent &construct
      &pushs 'vStartMode'
      &pushssv 'Disabled'
    &end
  &end // of placeMovieClip 27
&end
