import html
import sys
import os
import re
import argparse
from bs4 import BeautifulSoup
from datetime import datetime
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QFileDialog, QProgressBar, QLabel, QMessageBox
)
from PyQt6.QtCore import QThread, pyqtSignal

def post_proc(html: str, debug=False) -> str:
    def dbg(msg):
        if debug:
            print(f"[DEBUG] {msg}")
    dbg("POST PROCESS aka POST-PROC> Starting BeautifulSoup4")
    soup = BeautifulSoup(html, 'html.parser')
    for tag_name in ['span', 'em', 'u', 'del', 'strong']:
        for tag in soup.find_all(tag_name):
            # Si el tag está vacío o solo espacios, lo eliminamos
            if not tag.text.strip():
                tag.decompose()
                dbg("POST-PROC> Tag empty detected by bs4.BeautifulSoup")
                dbg("POST-PROC> [DESCOMPOSING...]")
                dbg(tag.text)
    dbg("POST-PROC> [POST-PROC] Finished BeautifulSoup4")
    dbg("POST-PROC> [POST-PROC] Returning the soup...")
    return str(soup)

def time_now() -> str:
    """Devuelve la hora actual formateada para logs."""
    return datetime.now().strftime('%H:%M:%S~%Y/%m/%d')


def convert_qtf_to_html(qtf_content: str, progress_callback=None, debug=False) -> str:
    def dbg(msg):
        if debug:
            print(f"[DEBUG-QPAD] {msg}")

    """
    Convierte contenido QTF a HTML.
    Si se pasa progress_callback, se actualiza el progreso (0-100).
    """
    origin = "GUI" if progress_callback else "CLI"
    print(f"[QPad-QTF2HTML]: Parsing [Started at> {time_now()} | Origin> {origin}]")

    dbg("Parsing-debug [Started at> {time_now()} | Origin> {origin}]")
    dbg("[DBG ENABLED]")
    lines = [line.strip() for line in qtf_content.splitlines()]
    default_font = None
    default_size = None

    for line in lines:
        if line.startswith('Font='):
            default_font = line.split('=', 1)[1]
        elif line.startswith('Size='):
            default_size = line.split('=', 1)[1]

    html = ['<!DOCTYPE html>', '<html>', '<head>', '<meta charset="utf-8">', '</head>']

    style = []
    if default_font:
        style.append(f"font-family:{default_font};")
    if default_size:
        style.append(f"font-size:{default_size};")
    body_style = " ".join(style)
    html.append(f'<body style="{body_style}">')

    content = '\n'.join(lines)
    body_match = re.search(r"\[Body\](.*?)\[/Body\]", content, re.DOTALL)

    if body_match:
        body = body_match.group(1)
        p_blocks = re.findall(r"\[P(?:\s+align=([^\]]+))?\](.*?)\[/P\]", body, re.DOTALL)
        total = len(p_blocks)

        for idx, (align, block) in enumerate(p_blocks, start=1):
            # Dividir por <def> para separar líneas
            lines = block.split('<def>')
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                if debug:
                    print("[dbg]segment call >> process_block")
                ...
                segment = process_block(line, debug=debug)
                ...
                if segment.strip():
                    p_tag = f'<p style="text-align:{align};">' if align else '<p>'
                    html.append(f"{p_tag}{segment}</p>")
            if progress_callback:
                progress_callback(int(idx / total * 100))

    html.extend(['</body>', '</html>'])

    if progress_callback:
        progress_callback(100)
    print("[QPad-QTF2HTML]: Parsing Done.")

    html_result = '\n'.join(html)

    # Aquí aplicas el post-proceso para eliminar spans vacíos
    html_result = post_proc(html_result, debug=debug)

    if progress_callback:
        progress_callback(100)
    print("[QPad-QTF2HTML]: Post-Parsing Done.")

    return html_result

def process_block(content: str, debug=False) -> str:
    import re, html

    def dbg(msg):
        if debug:
            print(f"[DEBUG] {msg}")

    dbg("[dbg] (qtf-daemon) > DEFINING SEM")
    # Mapeo semántico
    SEM = {'bold':'strong','italic':'em','underline':'u','strikeout':'del'}

    dbg("[dbg] (qtf-daemon) > TOKENIZE")
    # Tokenizamos en texto o tags (<def>, <bold>, </bold>, <font=...>, etc.)
    TOKEN_RE = re.compile(r'(?:<def>)|(?:</?[A-Za-z]+(?:=[^>]+)?>)', re.IGNORECASE)
    parts = TOKEN_RE.split(content)
    tags  = TOKEN_RE.findall(content)
    seq = []
    for txt, tag in zip(parts, tags+['']):
        if txt: seq.append(('text', txt))
        if tag: seq.append(('tag', tag))

    semantic = []               # stack de 'bold','italic',...
    style = {'font':None,'size':None,'color':None}
    span_open = False

    def close_span():
        dbg("[dbg] (qtf-daemon) > Closing span")
        nonlocal span_open
        if span_open:
            span_open = False
            return '</span>'
        return ''

    def open_span():
        dbg("[dbg] (qtf-daemon) > Opening span")
        nonlocal span_open
        css = []
        if style['font']: css.append(f'font-family:{style["font"]};')
        if style['size']: css.append(f'font-size:{style["size"]};')
        if style['color']:css.append(f'color:{style["color"]};')
        if css:
            span_open = True
            dbg("[dbg] (qtf-daemon) > Open span [with CSS]")
            return f'<span style="{" ".join(css)}">'
        return ''

    def open_sem(t):
        dbg("[dbg] (qtf-daemon) > Opening span [with SEM]")
        if t not in semantic:
            semantic.append(t)
            return f'<{SEM[t]}>'
        return ''

    def close_sem(t):
        dbg("[dbg] (qtf-daemon) > Closing span [with SEM]")
        if semantic and semantic[-1]==t:
            semantic.pop()
            return f'</{SEM[t]}>'
        return ''

    out = ''
    first = True

    for kind, val in seq:
        if kind=='text':
            out += html.escape(val)
            first = False
            continue

        tag = val[1:-1].lower()  # quita < y >
        if tag=='def':
            # cerrar semánticos (solo el tope) y span
            if semantic:
                out += close_sem(semantic[-1])
            out += close_span() + '<br/>' + open_span()
            dbg("[dbg] (qtf-daemon) > Closing span [with SEM] [DEF]")
            # reabrir semánticos en orden
            for s in semantic:
                out += f'<{SEM[s]}>'
            continue

        # semántico open
        if tag in SEM:
            out += open_sem(tag)
            dbg("[dbg] (qtf-daemon) > Opening SEM <SEM> [DEF-SEM]")
            continue

        # semántico close
        if tag.startswith('/'):
            dbg("[dbg] (qtf-daemon) > Closing SEM </SEM> [DEF-SEM]")
            inner = tag[1:]
            if inner in SEM:
                out += close_sem(inner)
                dbg("[dbg] (qtf-daemon) > Closing SEM [DEF-SEM]")
            continue

        # visual style
        if '=' in tag:
            dbg("[dbg] (qtf-daemon) > VSSTYLE [DEF-SEM-css]")
            key,val2 = tag.split('=',1)
            key=key.lower()
            if key in style and style[key]!=val2:
                dbg("[dbg] (qtf-daemon) > VSSTYLE [DEF-SEM-css] >> Closing SPAN [DEF]")
                out += close_span()
                style[key]=val2
                dbg("[dbg] (qtf-daemon) > VSSTYLE [DEF-SEM-css] >> Opening SPAN [DEF]")
                out += open_span()
                # reabrir semánticos
                for s in semantic:
                    dbg("[dbg] (qtf-daemon) > VSSTYLE [DEF-SEM-css] >> Reopen SEM [SEM]")
                    out += f'<{SEM[s]}>'
            continue

        # ignorar cualquier otro

    # cierre final
    dbg("[dbg] (qtf-daemon) > END [DEF] >> Closing SPAN [DEF]")
    out += close_span()
    while semantic:
        dbg("[dbg] (qtf-daemon) > END [DEF] >> Closing SEM [SEM]")
        out += close_sem(semantic[-1])

    dbg("[dbg] (qtf-daemon) > RETURN")
    return out

class ParserThread(QThread):
    progress = pyqtSignal(int)
    finished = pyqtSignal(str)

    def __init__(self, input_path: str):
        super().__init__()
        self.input_path = input_path
        self.output_folder = os.path.join(os.getcwd(), 'comp', 'cache')
        os.makedirs(self.output_folder, exist_ok=True)
    def run(self):
        try:
            with open(self.input_path, encoding='utf-8') as f:
                qtf = f.read()
            html = convert_qtf_to_html(qtf, progress_callback=self.progress.emit)
            base = os.path.splitext(os.path.basename(self.input_path))[0]
            output_file = os.path.join(self.output_folder, f'{base}.html')
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(html)
            self.finished.emit(output_file)
        except Exception as e:
            self.finished.emit(f'ERROR: {e}')


class Qtf2HtmlExporter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QTF → HTML Exporter')
        self.resize(400, 200)

        self.layout = QVBoxLayout(self)

        self.label = QLabel('Select a QTF file')
        self.layout.addWidget(self.label)

        self.browse_button = QPushButton('Browse')
        self.browse_button.clicked.connect(self.select_file)
        self.layout.addWidget(self.browse_button)

        self.progress_bar = QProgressBar()
        self.layout.addWidget(self.progress_bar)

        self.thread = None

    def select_file(self):
        path, _ = QFileDialog.getOpenFileName(self, 'Open QTF', '', 'QTF Files (*.qtf)')
        if path:
            self.label.setText(f'Parsing: {os.path.basename(path)}')
            self.browse_button.setEnabled(False)
            self.progress_bar.setValue(0)

            self.thread = ParserThread(path)
            self.thread.progress.connect(self.progress_bar.setValue)
            self.thread.finished.connect(self.on_finished)
            self.thread.start()

    def on_finished(self, output_path: str):
        self.browse_button.setEnabled(True)
        if output_path.startswith('ERROR'):
            QMessageBox.critical(self, 'Error', output_path)
            self.label.setText('Select a QTF file')
        else:
            QMessageBox.information(self, 'Done', f'HTML saved to:\n{output_path}')
            self.label.setText('Select a QTF file')
            self.progress_bar.setValue(100)


def run_cli(cli_args, debug=False):
    with open(cli_args.input, encoding='utf-8') as f:
        qtf = f.read()

    html = convert_qtf_to_html(qtf, debug=debug)
    folder = cli_args.output or os.path.join(os.getcwd(), 'comp', 'cache')
    os.makedirs(folder, exist_ok=True)

    base = os.path.splitext(os.path.basename(cli_args.input))[0]
    output_file = os.path.join(folder, f'{base}.html')


    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)

    print(output_file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='QTF to HTML converter')
    parser.add_argument('-i', '--input', help='QTF input file')
    parser.add_argument('-o', '--output', help='Output folder')
    parser.add_argument('--gui', action='store_true', help='Use GUI mode')
    parser.add_argument('--debug', action='store_true', help='Enable debug output')
    args = parser.parse_args()

    if args.gui or not args.input:
        app = QApplication(sys.argv)
        exporter = Qtf2HtmlExporter()
        exporter.show()
        sys.exit(app.exec())
    else:
        run_cli(args, debug=args.debug)
