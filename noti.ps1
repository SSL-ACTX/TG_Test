[void] [System.Reflection.Assembly]::LoadWithPartialName("System.Windows.Forms")

$objNotifyIcon = New-Object System.Windows.Forms.NotifyIcon

$objNotifyIcon.Icon = [System.Drawing.SystemIcons]::Information
$objNotifyIcon.BalloonTipIcon = "Warning" 
$objNotifyIcon.BalloonTipText = "Your device is under monitoring." 
$objNotifyIcon.BalloonTipTitle = "ATTENTION!"
$objNotifyIcon.Visible = $True

$objNotifyIcon.ShowBalloonTip(10000)
Start-Sleep 50