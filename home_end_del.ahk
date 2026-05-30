#Requires AutoHotkey v2.0

; Ctrl + Win + Home
^#Home:: {
    Send "+{Home}"
    Sleep 10
    Send "{Delete}"
}

; Ctrl + Win + End
^#End:: {
    Send "+{End}"
    Sleep 10
    Send "{Delete}"
}