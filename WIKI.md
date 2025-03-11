# Wiki

## Extracting strings from files for localization

```
pybabel extract -F babel.cfg -o messages.pot .
```

## Creating language specific translation

```
pybabel init -i messages.pot -d flaskr/translations -l pl
```

## Compiling translation file

```
pybabel compile -d flaskr/translations
```

## Updating exisiting translation file

```
pybabel update -i messages.pot -d flaskr/translations
```