# (Microsoft Teams) VTT Transcript to Descript Import Helper

Export a transcript recorded in Microsoft Teams as VTT, run it through this simple program, copy paste its output to
Descript's [Import Transcript][import_trans] feature.

The output format conforms to [Descript's format][output_format]. We let Descript handle syncing.

Unlike Descript's transcription of the mixed stream, Microsoft Teams's transcription is able to properly separate
speakers, likely due to having proper access to separated auto mixes.

Team's built in transcription may not be as good but at least it won't let "yeahs" and "OKs" run into other speaker's
"monologues".

Importing this way also saves you the hassle of having to identify speakers. This is also probably due to Teams having
access to name metadata.

[import_trans]: https://help.descript.com/hc/en-us/articles/360042210632-Import-Transcript
[output_format]: https://help.descript.com/hc/en-us/articles/360042639691