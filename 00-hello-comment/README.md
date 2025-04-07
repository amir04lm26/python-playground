## 1. Create a virtual environment
``` bash
   python3 -m venv venv
```

Activate the environment
``` bash
   source venv/bin/activate
```

## 2. Use it
Once activated, you can install packages with pip and they'll stay within that environment:

``` bash
   pip install some_package
```

## To save your environment:
``` bash
   pip freeze > requirements.txt
```

And to reinstall from a requirements file:
``` bash
    pip install -r requirements.txt
```

## 4. Deactivate
When you're done:

``` bash
   deactivate
```
