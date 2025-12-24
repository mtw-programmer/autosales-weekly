from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from datetime import datetime

def render_html_report(context: dict, output_html: str):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("report_template.html")

    html_content = template.render(**context)

    with open(output_html, "w", encoding="utf-8") as f:
        f.write(html_content)

def html_to_pdf(input_html: str, output_pdf: str):
    HTML(input_html).write_pdf(output_pdf)
