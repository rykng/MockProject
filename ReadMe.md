# MockProject aka Project M
it's for helping to test my private GateKeeper

## Example of unit test and integration test with Services
# app.facebook - unit test
# app.google - unit test
# services.screening - integration test



``` requirements
pip install pytest
# for making pytest running in parallell
pip install pytest-xdist
```

```
# run unittest
python -m unittest
# run pytest
pytest
#run pytest in parallel
pytest -n 2
```

no need to setup any venv because the code uses all default package from python 3.10

## Reference
[Mocking tutorial](https://realpython.com/lessons/mock-objects/)