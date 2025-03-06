# 📌 Nom de la tâche
$TaskName = "Skype"
#$ExePath = "C:\Users\skedu\AppData\Local\Programs\signal-desktop\Signal.exe"  # Programme dans AppData\Local

$LocalAppData = [System.Environment]::GetFolderPath('LocalApplicationData')

# 📌 Chemin vers l'exécutable Signal.exe
$ExePath = "$LocalAppData\Programs\signal-desktop\Signal.exe"

# 📌 Définir l'action : exécuter le programme
$Action = New-ScheduledTaskAction -Execute $ExePath

# 📌 Déclencheur : Exécuter toutes les 5 minutes (répétition infinie)
$Trigger = New-ScheduledTaskTrigger -Once -At (Get-Date).AddMinutes(1) -RepetitionInterval (New-TimeSpan -Minutes 5) #-RepetitionDuration ([TimeSpan]::MaxValue)


# 📌 Définir l'utilisateur et les permissions sans admin
$Principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive

# 📌 Création de la tâche planifiée
Register-ScheduledTask -TaskName $TaskName -Action $Action -Trigger $Trigger -Principal $Principal
