# GPT3 Auditor

Turns out GPT3 is pretty good at finding vulnerabilities (sometimes). 

I made this in a few hours at the Scale AI hackathon. So there isn't a whole lot of syntactic sugar or error handling. For instance, if your code file is too big, I will just skip it. Someone else should maybe figure out how to recursively read long code files or fit it into the context window somehow. That someone is not me, at least not today. 

## Usage

`python main.py --help`

gives you:

```
Usage: main.py [OPTIONS] COMMAND [ARGS]...

  Command scripts.

Options:
  --help  Show this message and exit.

Commands:
  audit       Audit a GitHub repo.
  audit-file  Audit a single file.
```

Then you can:

```
python main.py audit https://github.com/doublehops/sql-injection-attack-example
```
