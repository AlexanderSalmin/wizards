# Wizard generator

Generate random wizard descriptions from the included data files.

## Usage

```bash
python wizards.py
```

### Options

- `--count N`: generate N wizard descriptions.
- `--seed N`: set a random seed for repeatable output.
- `--files NAMES ELEMENTS ORIGINS`: use custom data files instead of the defaults.

#### Examples

```bash
python wizards.py --count 3
python wizards.py --seed 42
python wizards.py --files wizard_names.txt wizard_elements.txt wizard_from.txt
```
