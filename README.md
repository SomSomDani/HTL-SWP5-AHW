# SWP5AHW
Repository für ein Schulprojekt:
Mit diesem Programm sollen wir dem Leher beweisen, ob man bei "Stein-Schere-Papier-Echse-Spock" am meisten Spock gewählt wird und dabei gewinnt. Das Programm wurde in Python geschrieben und wird über die Console gespielt. Man kann wählen, welche Art von KI man spielen will, bisher wird nur eine random KI benutzt und dessen Daten werden dann auf ein SQLite Datenbank gespeichert und ausgeführt. Diese wird dann zum Flask weitergeleitet.

Spielprinzip:
Der Spieler wählt zwischen den Möglichkeiten aus und diese wird dann gegen die random Angabe von der KI entgegenverglichen und dann wird durch eine Modulo der Winner gesucht und eingetragen in die Statistik sowohl als auch in die Datenbank.
