# Rock-paper-scissors game

The rock-paper-scissors game is a classic hand game played between 2 people. Its style was originated in China and was subsequently imported into Japan.

Here you can find a small version of this game in a console application. The idea is to complete 3 tries in order to get the winner between 2 players.

<p>
<img src="https://globalsymbols.com/uploads/production/image/imagefile/46514/17_46515_89c735d8-75ab-4c92-9e84-0b73c799f87f.png">
</p>

## Setup

First of all, you need to install [Python 3.12](https://www.python.org).

Later, you can create a **virtual environment** and active it in order to install the dependencies only for this project:

```bash
$ python3.12 -m venv venv
$ source venv/bin/activate
```

After that, you must install the dependencies:

```bash
pip install --upgrade -r requirements.txt
```

Now you have an environment to run this application and the automated tests.

### Execution

You can run this application with the following command:

```bash
$ python main.py
```

### Testing

Some unit tests were implemented in order to validate the rock-paper-scissors game models. You can run them and see the coverage report with the following commands:

```bash
$ coverage run -m pytest --verbose
$ coverage report -m
```
