from docxtpl import DocxTemplate
""" import os
os.makedirs("app/outputs", exist_ok=True) """


def convertir(nombre_doc,plantilla, contexto,):
    template = DocxTemplate(f"app/inputs/{plantilla}.docx")
    context = contexto
    template.render(context)
    template.save(f"app/outputs/{nombre_doc}.docx")

