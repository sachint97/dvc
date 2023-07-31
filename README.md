```bash
mkdir dvc
```

```bash
cd dvc
```

```bash
conda create --prefix venv python=3.8 -y
```

```bash
git init
```

```bash
touch .gitignore
```

```bash
touch README.md
```

```bash
touch requirements.txt
```

```bash
pip install -r requirements.txt
```


```
dcv init
```

```
dvc repro
```

```
dvc dag
```


```
dvc repro --force stage_03
```