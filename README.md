""""""""""""""""""""""""""""""""""""""

Python version - 3.12.5

For virtual environment used pipenv

Trello link -> https://trello.com/invite/63c5092812c85e023c19d512/ATTIa09eb5e1ea49a606bbbf4812c0c0f853B0B1DB86

""""""""""""""""""""""""""""""""""""""

______________________________________
How to deploy and start?

1. pip install pipenv (it is need to do only once)
2. pipenv shell or pipenv run (it is a similar)
3. pipenv install (this command run installing all packs from pipfile)

Hint: that to add new or delete existing pack - pipenv install/uninstall some-pack-name

______________________________________
How to run some *.py file from current environment? 

pipenv run python /path/to/*.py


______________________________________
How to click in Skoda web app?

The list of potential libs:
1. pipenv install PyChromeDevTools            ->   ( https://github.com/marty90/PyChromeDevTools )
2. pipenv install chrome-devtools-protocol    ->   ( https://github.com/HyperionGray/python-chrome-devtools-protocol )

