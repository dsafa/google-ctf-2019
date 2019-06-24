$bytes = [byte[]]::new(264)
$contents = "run" + $bytes
Set-Content input -Encoding byte -Value $contents