# mkdocs-furigana-plugin

An MkDocs plugin to add furigana to Japanese Kanji text.

## Installation

```
pip3 install https://github.com/ijaureguialzo/mkdocs-furigana-plugin/archive/refs/heads/master.zip
```

## Usage

Write kanji like this:

日【に】本【ほん】語【ご】

Or like this when there is more than one character:

§今日【きょう】

And include this CSS file in your MkDown project:

```css
.furigana-plugin {
    display: inline-flex;
    align-items: center;
    justify-content: end;
    flex-direction: column-reverse;
}

.furigana-plugin > .furigana-plugin-kanji {
    font-size: 100%;
}

.furigana-plugin > .furigana-plugin-furigana {
    font-size: 40%;
}
```

To enable the plugin and the CSS edit the `mkdocs.yml` file:

```yaml
plugins:
  - furigana:
      multiple: "§"
      inicio: "【"
      fin: "】"

extra_css:
  - furigana.css
```
