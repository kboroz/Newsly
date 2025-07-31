# Newsly

Dieser Code beschreibt einen dynamischen Nachrichtenassistenten, der Nachrichten von Deutschlandfunk nicht nur abruft, sondern auch intelligent verarbeitet. Er bietet dem Benutzer eine prägnante Zusammenfassung und eine interaktive Frage-Antwort-Funktion. Hier ist eine lebendige Zusammenfassung der Funktionsweise und Idee dieses Agents:
Projektstruktur und Einrichtung

    Projektstruktur: Das Projekt besteht aus mehreren Verzeichnissen und Dateien, darunter app.py, config.py, agents/, data/ und utils/. Diese Struktur ermöglicht eine klare Trennung der verschiedenen Funktionen und Aufgaben.
    Einrichtung: Die Einrichtung ist einfach und effektiv: Erstellen von __init__.py-Dateien, Einrichten einer virtuellen Umgebung, Installieren von Abhängigkeiten und Starten des Ollama-Servers. So wird sichergestellt, dass alles reibungslos funktioniert.

Hauptkomponenten

    config.py: Hier werden wichtige Konfigurationsparameter wie API-Token und Modellnamen zentral verwaltet.
    data/news_fetcher.py: Dieser Teil des Codes holt aktiv die neuesten Nachrichten von Deutschlandfunk und bereitet sie für die weitere Verarbeitung auf.
    utils/embeddings.py: Hier wird der abgerufene Text in einen leistungsstarken Vektorenspeicher umgewandelt, der für die spätere Verwendung in der Frage-Antwort-Kette optimiert ist.
    agents/qa_agent.py: Dieser Agent baut eine intelligente Frage-Antwort-Kette auf, die den Vektorenspeicher nutzt, um präzise und schnelle Antworten zu liefern.
    agents/summarizer.py: Dieser Teil fasst den abgerufenen Nachrichtentext prägnant zusammen, sodass der Benutzer schnell einen Überblick erhält.
    utils/text_to_speech.py: Hier wird Text in Audio umgewandelt, um die Antworten nicht nur lesbar, sondern auch hörbar zu machen.
    app.py: Die Hauptanwendung nutzt Streamlit, um eine benutzerfreundliche und interaktive Oberfläche bereitzustellen. Sie ruft Nachrichten ab, zeigt eine Zusammenfassung an und ermöglicht es dem Benutzer, Fragen zu stellen.

Funktionsweise

    Nachrichtenabruf: Die Anwendung ruft proaktiv die neuesten Nachrichten von Deutschlandfunk ab und speichert sie in einer Variable.
    Vektorenspeicher: Der abgerufene Text wird in einen Vektorenspeicher umgewandelt, um eine effiziente Suche und Abfrage zu ermöglichen. Dies sorgt für schnelle und präzise Antworten.
    Zusammenfassung: Der abgerufene Text wird automatisch zusammengefasst und dem Benutzer angezeigt, sodass er schnell den Überblick behält.
    Frage-Antwort-Funktion: Der Benutzer kann Fragen stellen, die von der Frage-Antwort-Kette intelligent beantwortet werden. Die Antwort wird sowohl als Text als auch als Audio ausgegeben, was die Benutzerfreundlichkeit erhöht.

Benutzeroberfläche

Die Benutzeroberfläche wird mit Streamlit erstellt und bietet folgende Funktionen:

    Anzeige einer prägnanten Zusammenfassung der Nachrichten.
    Eingabefeld für Fragen des Benutzers, das zur Interaktion einlädt.
    Anzeige der Antworten und Wiedergabe der Audioausgabe, was die Nutzung noch angenehmer macht.


Hier sind die Linux-Kommandozeilen zum Ausführen des Codes:

cd Downloads/
cd deutschlandfunk_ai_agent/
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install -U langchain-community
ollama pull llama3.2
touch agents/__init__.py config/__init__.py data/__init__.py utils/__init__.py
streamlit run app.py



