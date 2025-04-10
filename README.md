## UseCase Template für Anwendungsfall Leistungsdiagnostik

### Name und Identifikationsnummer
- UC 1.03 (Alarm bei zu hoher Herzfrequenz)
  
### Beschreibung
- Steigt die HF über einen bestimmten Wert, wird ein Alarm ausgelöst

### Beteiligte Akteure
- Versuchsleiter, Proband
### Verwendete Anwendungsfälle
- keine verwendeten Anwendungsfälle
  
### Auslöser
-Bei erhöhten Pulsfrequenzen ist das Herz nicht mehr in der Lage ausreichend Blut mit Sauerstoff in den Körperkreislauf zu pumpen. Deshalb kommt es zu Symptomen wie Schwindel, Übelkeit oder Benommenheit. In seltenen Fällen kann eine kurze Ohnmacht auftreten.
### Vorbedingungen
-   Der Patient muss im System sein und der Leistungstest muss funktionieren, ansonsten können die essenziellen Daten nicht abgerufen werden
### Invarianten
-Falls die HF einen bestimmten Wert überschreitet und die Anwendung auslöst, werden die Daten trotzdem gespeichert und analysiert

### Nachbedingungen/Ergebnis
-Test wird abgebrochen und Proban wird, falls nötigt versorgt

### Standartablauf
-Test läuft reibungslos ab und die Anwendung wird nicht ausgeführt

### Alternative Ablaufschritte
-Die Anwendung wird ausgeführt, der Test wird jedoch nicht abgebrochen. Der Test wird hingegen angepasst um die HF wieder in den gewollten Bereich zu lenken

### Hinweise
-Bei Überschreittung des HF-Wertes wird die Anwendung ausgelöst, Proband könnte im schlimmsten Fall negative Körperliche Folgen erleiden

### Änderungsgeschichte
Version_01, Julius Mayr, 17.03.2025
