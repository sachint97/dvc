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

```
dvc add <filename>
```

```
git add <filename> && git commit -m "file added"
```

```
mkdir /tmp/dvcstore
```

```
dvc remote add -d myremote /tmp/dvcstore
```

```
dvc push
```

```
https://dvc.org/doc/start/data-management/data-versioning
```