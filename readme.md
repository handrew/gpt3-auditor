# GPT3 Auditor

Turns out GPT3 is pretty good at finding vulnerabilities (sometimes). 

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
