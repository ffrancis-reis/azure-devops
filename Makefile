hello:
	echo "this is my first make command"
install:
	python.exe -m pip install --upgrade pip &&\
			pip install -r requirements.txt
test:
	python -m pytest -vv test_hello.py
all: hello install