Private Declare Function SetCurrentDirectoryA Lib _
        "kernel32" (ByVal lpPathName As String) As Long

Public Function ChDirNet(szPath As String) As Boolean
'based on Rob Bovey's code
    Dim lReturn As Long
    lReturn = SetCurrentDirectoryA(szPath)
    ChDirNet = CBool(lReturn <> 0)
End Function

Sub Get_TXT_Files()
'For Excel 2000 and higher
    Dim Fnum As Long
    Dim mysheet As Worksheet
    Dim basebook As Workbook
    Dim TxtFileNames As Variant
    Dim QTable As QueryTable
    Dim SaveDriveDir As String
    Dim ExistFolder As Boolean

    'Save the current dir
    SaveDriveDir = CurDir

    'You can change the start folder if you want for
    'GetOpenFilename,you can use a network or local folder.
    'For example ChDirNet("C:\Users\Ron\test")
    'It now use Excel's Default File Path

    ExistFolder = ChDirNet("D:\add-this")
    If ExistFolder = False Then
        MsgBox "Error changing folder"
        Exit Sub
    End If

    TxtFileNames = Application.GetOpenFilename _
    (filefilter:="TXT Files (*.txt), *.txt", MultiSelect:=True)

    If IsArray(TxtFileNames) Then

        On Error GoTo CleanUp

        With Application
            .ScreenUpdating = False
            .EnableEvents = False
        End With

        'Add workbook with one sheet
        Set basebook = Workbooks.Add(xlWBATWorksheet)

        'Loop through the array with txt files
        For Fnum = LBound(TxtFileNames) To UBound(TxtFileNames)

            'Add a new worksheet for the name of the txt file
            Set mysheet = Worksheets.Add(After:=basebook. _
                                Sheets(basebook.Sheets.Count))
            On Error Resume Next
            mysheet.Name = Right(TxtFileNames(Fnum), Len(TxtFileNames(Fnum)) - _
                                    InStrRev(TxtFileNames(Fnum), "\", , 1))
            On Error GoTo 0

            With ActiveSheet.QueryTables.Add(Connection:= _
                        "TEXT;" & TxtFileNames(Fnum), Destination:=Range("A1"))
                .TextFilePlatform = xlWindows
                .TextFileStartRow = 1

                'This example use xlDelimited
                'See a example for xlFixedWidth below the macro
                .TextFileParseType = xlDelimited

                'Set your Delimiter to true
                .TextFileTabDelimiter = True
                .TextFileSemicolonDelimiter = False
                .TextFileCommaDelimiter = False
                .TextFileSpaceDelimiter = False

                'Set the format for each column if you want (Default = General)
                'For example Array(1, 9, 1) to skip the second column
                .TextFileColumnDataTypes = Array(1, 9, 1)

                'xlGeneralFormat  General          1
                'xlTextFormat     Text             2
                'xlMDYFormat      Month-Day-Year   3
                'xlDMYFormat      Day-Month-Year   4
                'xlYMDFormat      Year-Month-Day   5
                'xlMYDFormat      Month-Year-Day   6
                'xlDYMFormat      Day-Year-Month   7
                'xlYDMFormat      Year-Day-Month   8
                'xlSkipColumn     Skip             9

                ' Get the data from the txt file
                .Refresh BackgroundQuery:=False
            End With
        ActiveSheet.QueryTables(1).Delete
        Next Fnum

        'Delete the first sheet of basebook
        On Error Resume Next
        Application.DisplayAlerts = False
        basebook.Worksheets(1).Delete
        Application.DisplayAlerts = True
        On Error GoTo 0

CleanUp:

        ChDirNet SaveDriveDir

        With Application
            .ScreenUpdating = True
            .EnableEvents = True
        End With
    End If
End Sub