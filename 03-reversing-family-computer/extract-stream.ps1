Get-Item credentials.txt -stream *
$file = Get-Content credentials.txt -stream 'FILE0' -Encoding Byte -ReadCount 0
Set-Content 'file0.png' -Encoding Byte -Value $file
