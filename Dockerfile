FROM python:3.9.0

ADD src /src

CMD [ "python", "./src/CalculatorTest.py" ]