import re

from mkdocs.config import base, config_options as c
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import Files
from mkdocs.structure.nav import Navigation
from mkdocs.structure.pages import Page
from mkdocs.utils.templates import TemplateContext


class FuriganaPluginConfig(base.Config):
    multiple = c.Type(str, default='§')
    inicio = c.Type(str, default='【')
    fin = c.Type(str, default='】')


class FuriganaPlugin(BasePlugin[FuriganaPluginConfig]):

    def on_page_content(self, html: str, *, page: Page, config: MkDocsConfig, files: Files) -> str:
        html = self.reemplazar_expresiones(html)
        page.title = self.eliminar_caracteres_control(page.title)
        return html

    def on_page_context(self, context: TemplateContext, *, page: Page, config: MkDocsConfig,
                        nav: Navigation) -> TemplateContext:
        for i in page.toc.items:
            self.recorrer_hijos(i)
        return context

    def recorrer_hijos(self, item):
        item.title = self.eliminar_caracteres_control(item.title)
        for i in item.children:
            self.recorrer_hijos(i)

    def reemplazar_expresiones(self, texto: str) -> str:
        reemplazo = (r'<span class="furigana-plugin">'
                     r'<span class="furigana-plugin-kanji">\1</span>'
                     r'<span class="furigana-plugin-furigana">\2</span>'
                     r'</span>')
        return self.aplicar_reemplazo(reemplazo, texto)

    def eliminar_caracteres_control(self, texto: str) -> str:
        reemplazo = r'\1'
        return self.aplicar_reemplazo(reemplazo, texto)

    def aplicar_reemplazo(self, reemplazo, texto):
        # §今日【きょう】
        busqueda = rf'{self.config.multiple}(.+?){self.config.inicio}(.+?){self.config.fin}'
        texto = re.sub(busqueda, reemplazo, texto)

        # 水【すい】曜【よう】日【び】
        busqueda = rf'(.){self.config.inicio}(.+?){self.config.fin}'
        texto = re.sub(busqueda, reemplazo, texto)

        return texto
